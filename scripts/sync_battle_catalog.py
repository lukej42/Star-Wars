#!/usr/bin/env python3
"""Merge battle_catalog_additions into BattleData, planets, hero scenes, and cross-link maps."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
DATA = ROOT / "Data"
BATTLE_DATA = DATA / "BattleData.cs"
PLANET_DATA = DATA / "BattlePlanetData.cs"
SCENES = SCRIPTS / "wars_conflicts_hero_scenes.py"
CROSS_LINK = SCRIPTS / "cross_link_builder.py"

sys.path.insert(0, str(SCRIPTS))
from battle_catalog_additions import NEW_BATTLES

BATTLE_CALL = re.compile(
    r'Battle\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)"\)',
)


def parse_existing_battles() -> list[dict]:
    text = BATTLE_DATA.read_text(encoding="utf-8")
    battles = []
    for war, slug, name, era, color in BATTLE_CALL.findall(text):
        battles.append(
            {
                "war_slug": war,
                "slug": slug,
                "name": name,
                "era": era,
                "color": color,
                "planet": "",
                "scene": "",
                "archives": [],
            }
        )
    return battles


def parse_existing_planets() -> dict[str, str]:
    text = PLANET_DATA.read_text(encoding="utf-8")
    return dict(re.findall(r'\["([^"]+)"\]\s*=\s*"([^"]+)"', text))


def merge_battles() -> list[dict]:
    by_slug = {b["slug"]: b for b in parse_existing_battles()}
    additions_by_slug = {entry["slug"]: entry for entry in NEW_BATTLES}
    for entry in NEW_BATTLES:
        by_slug[entry["slug"]] = {**by_slug.get(entry["slug"], {}), **entry}
    war_order = [
        "clone-wars",
        "galactic-civil-war",
        "mandalorian-wars",
        "great-sith-war",
        "great-galactic-war",
        "stark-hyperspace-war",
        "hundred-year-darkness",
        "new-sith-wars",
        "cold-war",
        "great-war",
    ]
    battles = list(by_slug.values())
    battles.sort(key=lambda b: (war_order.index(b["war_slug"]), b["name"]))
    return battles


def war_comment(war_slug: str) -> str:
    labels = {
        "clone-wars": "Clone Wars",
        "galactic-civil-war": "Galactic Civil War",
        "mandalorian-wars": "Mandalorian Wars",
        "great-sith-war": "Great Sith War",
        "great-galactic-war": "Great Galactic War",
        "stark-hyperspace-war": "Stark Hyperspace War",
        "hundred-year-darkness": "Hundred-Year Darkness",
        "new-sith-wars": "New Sith Wars",
        "cold-war": "Cold War (First Order)",
        "great-war": "Great War (SWTOR)",
    }
    return labels.get(war_slug, war_slug)


def write_battle_data(battles: list[dict]) -> None:
    lines = [
        "using StarWars.Models;",
        "",
        "namespace StarWars.Data;",
        "",
        "public static class BattleData",
        "{",
        "    public static IReadOnlyList<FamousBattle> Battles { get; } =",
        "    [",
    ]
    current_war = None
    for battle in battles:
        if battle["war_slug"] != current_war:
            current_war = battle["war_slug"]
            lines.append("")
            lines.append(f"        // {war_comment(current_war)}")
        lines.append(
            f'        Battle("{battle["war_slug"]}", "{battle["slug"]}", '
            f'"{battle["name"]}", "{battle["era"]}", "{battle["color"]}"),'
        )
    lines.extend(
        [
            "    ];",
            "",
            "    public static FamousBattle? GetBySlug(string slug) =>",
            "        Battles.FirstOrDefault(battle => battle.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));",
            "",
            "    public static IReadOnlyList<FamousBattle> GetByWar(string warSlug) =>",
            "        Battles.Where(battle => battle.WarSlug.Equals(warSlug, StringComparison.OrdinalIgnoreCase))",
            "            .OrderBy(battle => battle.Name)",
            "            .ToList();",
            "",
            "    public static IReadOnlyList<FamousBattle> All() => Battles;",
            "",
            "    private static FamousBattle Battle(string warSlug, string slug, string name, string era, string color) =>",
            "        new()",
            "        {",
            "            WarSlug = warSlug,",
            "            Slug = slug,",
            "            Name = name,",
            "            Route = $\"wars-conflicts/battles/{slug}\",",
            "            Era = era,",
            "            Color = color",
            "        };",
            "}",
            "",
        ]
    )
    BATTLE_DATA.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(battles)} battles to {BATTLE_DATA.relative_to(ROOT)}")


def write_planet_data(battles: list[dict], existing: dict[str, str]) -> None:
    planets = dict(existing)
    for battle in battles:
        if battle.get("planet") and battle["slug"] not in planets:
            planets[battle["slug"]] = battle["planet"]
    if "jedi-purge" not in planets:
        planets["jedi-purge"] = "Coruscant"

    lines = [
        "using StarWars.Models;",
        "using StarWars.Services;",
        "",
        "namespace StarWars.Data;",
        "",
        "public static class BattlePlanetData",
        "{",
        "    private static readonly Dictionary<string, string> BattlePlanets = new(StringComparer.OrdinalIgnoreCase)",
        "    {",
    ]
    for slug in sorted(planets.keys()):
        lines.append(f'        ["{slug}"] = "{planets[slug]}",')
    lines.extend(
        [
            "    };",
            "",
            "    public static ProfileLinkItem? GetLink(string battleSlug) =>",
            "        BattlePlanets.TryGetValue(battleSlug, out var planetName)",
            "            ? PlanetLinks.FromName(planetName)",
            "            : null;",
            "}",
            "",
        ]
    )
    PLANET_DATA.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {len(planets)} battle planet mappings")


def sync_battle_scenes(battles: list[dict]) -> None:
    text = SCENES.read_text(encoding="utf-8")
    start = text.index("BATTLE_SCENES: dict[str, str] = {")
    end = text.index("\n}\n\n\ndef war_prompt", start)

    existing_scenes: dict[str, str] = {}
    block = text[start:end]
    for match in re.finditer(r'"([^"]+)":\s*\(\s*"((?:[^"\\]|\\.)*)"\s*\)', block, re.DOTALL):
        slug = match.group(1)
        scene = match.group(2).replace("\n        ", " ").strip()
        existing_scenes[slug] = scene

    slug_to_war = {b["slug"]: b["war_slug"] for b in battles}
    slug_to_name = {b["slug"]: b["name"] for b in battles}
    slug_to_era = {b["slug"]: b["era"] for b in battles}
    for battle in battles:
        if battle.get("scene"):
            existing_scenes[battle["slug"]] = battle["scene"]
        elif battle["slug"] not in existing_scenes:
            war_name = war_comment(battle["war_slug"])
            planet = battle.get("planet") or "the battlefield"
            existing_scenes[battle["slug"]] = (
                f"Cinematic {battle['name']} ({battle['era']}) on {planet}: armies, starfighters, "
                f"and environmental details unique to this {war_name} engagement"
            )

    lines = ["BATTLE_SCENES: dict[str, str] = {"]
    current_war = None
    for slug in sorted(existing_scenes.keys(), key=lambda s: (slug_to_war.get(s, "zzz"), slug_to_name.get(s, s))):
        war = slug_to_war.get(slug, "")
        if war and war != current_war:
            current_war = war
            lines.append(f"    # {war_comment(war)}")
        lines.append(f'    "{slug}": (')
        lines.append(f'        "{existing_scenes[slug]}"')
        lines.append("    ),")
    lines.append("}")
    new_text = text[:start] + "\n".join(lines) + text[end + len("\n}") :]
    SCENES.write_text(new_text, encoding="utf-8")
    print(f"Synced {len(existing_scenes)} battle hero scenes")


def sync_battle_planets_cross_link(planets: dict[str, str]) -> None:
    text = CROSS_LINK.read_text(encoding="utf-8")
    start = text.index("BATTLE_PLANETS: dict[str, str] = {")
    end = text.index("\n}\n", start)
    lines = ["BATTLE_PLANETS: dict[str, str] = {"]
    for slug in sorted(planets.keys()):
        lines.append(f'    "{slug}": "{planets[slug]}",')
    lines.append("}")
    new_block = "\n".join(lines)
    CROSS_LINK.write_text(text[:start] + new_block + text[end + len("\n}\n") :], encoding="utf-8")
    print(f"Synced BATTLE_PLANETS in cross_link_builder.py ({len(planets)} entries)")


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--upload",
        action="store_true",
        help="Upload wwwroot/images to Azure Blob Storage after sync",
    )
    args = parser.parse_args()

    battles = merge_battles()
    existing_planets = parse_existing_planets()
    write_battle_data(battles)
    planets = dict(existing_planets)
    for battle in battles:
        if battle.get("planet"):
            planets[battle["slug"]] = battle["planet"]
    if "jedi-purge" not in planets:
        planets["jedi-purge"] = "Coruscant"
    write_planet_data(battles, existing_planets)
    sync_battle_scenes(battles)
    sync_battle_planets_cross_link(planets)

    if args.upload:
        import subprocess

        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "upload_images_to_azure.py")],
            check=False,
        )
        if result.returncode != 0:
            raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
