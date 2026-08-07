#!/usr/bin/env python3
"""Generate battle profile JSON for all battles except hand-authored jedi-purge."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
DATA = ROOT / "Data"
OUTPUT = ROOT / "wwwroot" / "data" / "profiles" / "battles"
sys.path.insert(0, str(SCRIPTS))

from battle_catalog_additions import NEW_BATTLES
from battle_related_archives import BATTLE_OVERRIDES, WAR_ARCHIVES

BATTLE_CALL = re.compile(
    r'Battle\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)"\)',
)
PLANET_CALL = re.compile(r'\["([^"]+)"\]\s*=\s*"([^"]+)"')

WAR_LABELS = {
    "clone-wars": "Clone Wars",
    "galactic-civil-war": "Galactic Civil War",
    "mandalorian-wars": "Mandalorian Wars",
    "great-sith-war": "Great Sith War",
    "great-galactic-war": "Great Galactic War",
    "stark-hyperspace-war": "Stark Hyperspace War",
    "hundred-year-darkness": "Hundred-Year Darkness",
    "new-sith-wars": "New Sith Wars",
    "cold-war": "Cold War",
    "great-war": "Great War (SWTOR)",
}

PLANET_ROUTES = {
    "Coruscant": "coruscant",
    "Hoth": "hoth",
    "Tatooine": "tatooine",
    "Naboo": "naboo",
    "Yavin 4": "planet/yavin-4",
    "Endor": "planet/endor",
    "Jakku": "planet/jakku",
    "Dantooine": "dantooine",
    "Korriban": "korriban",
    "Bespin": "bespin",
    "Scarif": "planet/scarif",
    "D'Qar": "planet/d-qar",
    "Starkiller Base": "planet/starkiller-base",
    "Hosnian Prime": "planet/hosnian-prime",
    "Kemplex IX": "planet/kemplex-ix",
    "Telos IV": "planet/telos-iv",
    "Malachor V": "planet/malachor-v",
}

WAR_MEDIA = {
    "clone-wars": {
        "films": ["Star Wars: Episode II — Attack of the Clones", "Star Wars: Episode III — Revenge of the Sith"],
        "series": ["Star Wars: The Clone Wars", "Star Wars: The Bad Batch"],
        "games": ["Star Wars Battlefront II (2017)", "Star Wars: Republic Commando"],
    },
    "galactic-civil-war": {
        "films": [
            "Star Wars: Episode IV — A New Hope",
            "Star Wars: Episode V — The Empire Strikes Back",
            "Star Wars: Episode VI — Return of the Jedi",
            "Rogue One: A Star Wars Story",
            "Solo: A Star Wars Story",
        ],
        "series": ["Star Wars Rebels", "Star Wars: Andor"],
        "games": ["Star Wars Battlefront (2015)", "Star Wars: Squadrons"],
    },
    "mandalorian-wars": {
        "games": ["Star Wars: Knights of the Old Republic", "Star Wars: Knights of the Old Republic II"],
        "books": ["Star Wars: Knights of the Old Republic (comics)"],
    },
    "great-sith-war": {
        "series": ["Star Wars: Tales of the Jedi"],
        "games": ["Star Wars: Knights of the Old Republic"],
        "books": ["Tales of the Jedi (Dark Horse Comics)"],
    },
    "great-galactic-war": {
        "games": ["Star Wars: The Old Republic"],
        "books": ["The Old Republic novel series"],
    },
    "stark-hyperspace-war": {
        "books": ["Star Wars: Republic — Stark Hyperspace War (comics)"],
    },
    "hundred-year-darkness": {
        "books": ["Star Wars: Tales of the Jedi — The Golden Age of the Sith"],
    },
    "new-sith-wars": {
        "books": ["Star Wars: Darth Bane trilogy", "Jedi vs. Sith (comics)"],
    },
    "cold-war": {
        "films": [
            "Star Wars: Episode VII — The Force Awakens",
            "Star Wars: Episode VIII — The Last Jedi",
            "Star Wars: Episode IX — The Rise of Skywalker",
        ],
        "series": ["Star Wars Resistance", "Star Wars: The Mandalorian"],
    },
    "great-war": {
        "games": ["Star Wars: The Old Republic"],
    },
}

additions_by_slug = {entry["slug"]: entry for entry in NEW_BATTLES}


def parse_battles() -> list[dict]:
    text = (DATA / "BattleData.cs").read_text(encoding="utf-8")
    planets = dict(PLANET_CALL.findall((DATA / "BattlePlanetData.cs").read_text(encoding="utf-8")))
    battles = []
    for war, slug, name, era, color in BATTLE_CALL.findall(text):
        battles.append(
            {
                "war_slug": war,
                "slug": slug,
                "name": name,
                "era": era,
                "color": color,
                "planet": planets.get(slug, additions_by_slug.get(slug, {}).get("planet", "")),
                "scene": additions_by_slug.get(slug, {}).get("scene", ""),
            }
        )
    return battles


def link_item(label: str, value: str, route: str) -> dict:
    return {"label": label, "value": value, "route": route}


def planet_route(name: str) -> str:
    if name in PLANET_ROUTES:
        return PLANET_ROUTES[name]
    return f"planet/{name.lower().replace(' ', '-').replace(chr(39), '')}"


def profile_for_battle(battle: dict) -> dict:
    war = battle["war_slug"]
    war_name = WAR_LABELS.get(war, war.replace("-", " ").title())
    planet = battle.get("planet") or "the galaxy"
    scene = battle.get("scene") or f"a decisive engagement of the {war_name}"
    media = WAR_MEDIA.get(war, {})

    archives = list(BATTLE_OVERRIDES.get(battle["slug"], []))
    for item in WAR_ARCHIVES.get(war, []):
        if item not in archives:
            archives.append(item)

    planets = []
    if battle.get("planet"):
        planets.append(link_item("Planet", battle["planet"], planet_route(battle["planet"])))

    key_factions = []
    major_characters = []
    major_events = []
    for label, value, route in archives:
        if label in {"Faction", "Organization"}:
            key_factions.append(link_item(label, value, route))
        elif label in {"Character", "Jedi", "Sith", "Species"}:
            major_characters.append(link_item(label, value, route))
        elif label == "Battle":
            major_events.append({"text": value, "route": route})

    overview = (
        f"The **{battle['name']}** ({battle['era']}) was a pivotal engagement of the **{war_name}**, "
        f"fought on or above **{planet}**. {scene.capitalize()}.\n\n"
        f"Archives record this battle across saga films, animated series, Knights of the Old Republic, "
        f"Old Sith Empire chronicles, and expanded universe sources — anchoring the {war_name} in "
        f"both cinematic canon and deep galactic history."
    )
    history = (
        f"Military historians of the New Republic classify the {battle['name']} within the broader "
        f"**{war_name}** campaign. Front-line reports describe {scene.lower()}.\n\n"
        f"Commanders on both sides leveraged local terrain, orbital support, and Force-sensitive "
        f"operatives where available. The engagement's outcome shifted regional control and fed "
        f"into later battles documented across the same war.\n\n"
        f"For chronology enthusiasts, **{battle['era']}** places this conflict in the galactic timeline "
        f"alongside other famous battles of the {war_name}."
    )
    significance = (
        f"The {battle['name']} illustrates how the {war_name} reshaped the galaxy — through combined "
        f"arms warfare, political betrayal, and the eternal struggle between light and dark. "
        f"Its legacy persists in memorials, veteran accounts, and holodramas spanning nine saga films "
        f"and decades of tie-in fiction."
    )

    return {
        "dateRange": battle["era"],
        "overview": overview,
        "history": history,
        "significance": significance,
        "notableEvents": [
            f"{battle['name']} opens on {planet}",
            f"Forces of the {war_name} clash in a decisive engagement",
            "Orbital and ground elements coordinate combined assault",
            "Aftermath reshapes the regional front of the war",
        ],
        "keyFactions": key_factions[:6],
        "majorCharacters": major_characters[:8],
        "majorEvents": major_events[:6],
        "planets": planets[:4],
        "affiliations": [war_name, planet if planet != "the galaxy" else "Galactic conflict"],
        "timeline": [
            {"era": battle["era"], "event": f"{battle['name']} begins"},
            {"era": battle["era"], "event": f"Aftermath of {battle['name']} recorded in New Republic archives"},
        ],
        "films": media.get("films", []),
        "series": media.get("series", []),
        "games": media.get("games", []),
        "books": media.get("books", []),
    }


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    written = 0
    skipped = 0
    for battle in parse_battles():
        if battle["slug"] == "jedi-purge":
            skipped += 1
            continue
        path = OUTPUT / f"{battle['slug']}.json"
        path.write_text(json.dumps(profile_for_battle(battle), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        written += 1
    print(f"Wrote {written} battle profiles ({skipped} skipped hand-authored)")


if __name__ == "__main__":
    main()
