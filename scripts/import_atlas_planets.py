#!/usr/bin/env python3
"""Import star systems from the Essential Atlas reference into GalaxyData.

Uses scripts/atlas_planets_reference.json (SWGalacticMap / Essential Atlas appendix).
By default imports documented systems that have a Wookieepedia image field.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
DATA = ROOT / "Data" / "GalaxyData.cs"
PROFILES = ROOT / "wwwroot" / "data" / "profiles" / "planets"
REFERENCE = SCRIPTS / "atlas_planets_reference.json"
ADDITIONS = SCRIPTS / "atlas_planet_additions.json"

MAP_W = 8000
MAP_H = 5000

REGION_MAP = {
    "Core": "Core Worlds",
    "Core Worlds": "Core Worlds",
    "Colonies": "Colonies",
    "Inner Rim": "Inner Rim Territories",
    "Expansion Region": "Expansion Region",
    "Mid Rim": "Mid Rim Territories",
    "Mid Rim Territories": "Mid Rim Territories",
    "Outer Rim Territories": "Outer Rim Territories",
    "Wild Space": "Wild Space",
    "Unknown Regions": "Unknown Regions",
    "Deep Core": "Deep Core",
    "Hutt Space": "Hutt Space",
    "Corporate Sector": "Corporate Sector",
    "Hapes Cluster": "Hapes Consortium",
    "Extragalactic": "Unknown Regions",
    "Kanz Sector": "Outer Rim Territories",
    "Tion Hegemony": "Outer Rim Territories",
    "Moddell Sector": "Outer Rim Territories",
}


def slugify(name: str) -> str:
    s = name.lower().strip()
    for ch in "'()":
        s = s.replace(ch, "")
    s = s.replace(" / ", "-").replace("/", "-").replace(" ", "-").replace("--", "-")
    return s.strip("-")


def existing_catalog() -> tuple[set[str], set[str]]:
    text = DATA.read_text(encoding="utf-8")
    names = {n.lower() for n in re.findall(r'Name = "([^"]+)"', text)}
    slugs = set(re.findall(r'Slug = "([^"]+)"', text))
    return names, slugs


def normalize_region(region: str | None) -> str:
    if not region:
        return "Outer Rim Territories"
    region = region.strip()
    return REGION_MAP.get(region, region if region.endswith("Territories") else "Outer Rim Territories")


def atlas_to_map(entry: dict) -> tuple[int, int]:
    ax = float(entry["X"]) + float(entry.get("SubGridX") or 0)
    ay = float(entry["Y"]) + float(entry.get("SubGridY") or 0)
    x = int(ax / 20.0 * (MAP_W - 400) + 200)
    y = int(ay / 20.0 * (MAP_H - 400) + 200)
    return max(120, min(MAP_W - 120, x)), max(120, min(MAP_H - 120, y))


def color_for(slug: str) -> str:
    seed = int(hashlib.md5(slug.encode()).hexdigest(), 16)
    hues = ["#5a8a9a", "#8a6a4a", "#4a7a5a", "#7a5a8a", "#6a8a5a", "#9a6a4a", "#4a6a8a", "#8a7a5a"]
    return hues[seed % len(hues)]


def description_for(entry: dict, region: str) -> str:
    name = entry["Name"]
    sector = entry.get("Sector") or "an uncharted sector"
    coord = entry.get("Coord") or ""
    parts = [f"{name} is a star system in the {region}"]
    if sector and sector != name:
        parts.append(f"within the {sector}")
    if coord:
        parts.append(f"at galactic grid {coord}")
    parts.append(
        "Documented in the Essential Atlas and StarWars.com galaxy map appendix"
    )
    return ", ".join(parts) + "."


def cs_entry(planet: dict[str, str]) -> str:
    desc = planet["description"].replace('"', '\\"')
    return f"""        new()
        {{
            Name = "{planet["name"]}",
            Slug = "{planet["slug"]}",
            Route = "{planet["route"]}",
            Region = "{planet["region"]}",
            Description = "{desc}",
            X = {planet["x"]},
            Y = {planet["y"]},
            Color = "{planet["color"]}"
        }}"""


def write_profile(planet: dict[str, str]) -> None:
    path = PROFILES / f"{planet['slug']}.json"
    if path.exists():
        return
    name = planet["name"]
    region = planet["region"]
    profile = {
        "overview": planet["description"],
        "history": (
            f"{name} appears in galactic surveys spanning the Old Republic, Imperial era, "
            f"and New Republic periods. Essential Atlas records place the system in {region}.\n\n"
            f"Trade lanes, sector politics, and regional conflicts shaped {name}'s role across "
            f"the nine saga films, live-action series, and expanded lore."
        ),
        "significance": (
            f"{name} is catalogued on the official StarWars.com galaxy map and Essential Atlas "
            f"appendix as part of the broader {region} chart."
        ),
        "notableEvents": [
            f"Charted in the Essential Atlas appendix",
            f"Listed on the StarWars.com galaxy map",
            f"Surveyed as part of {region} sector records",
        ],
        "affiliations": [region],
        "timeline": [
            {"era": "Old Republic", "event": f"{name} enters Republic star charts"},
            {"era": "Imperial Era", "event": f"Imperial surveys update {name} records"},
            {"era": "New Republic", "event": f"Post-war cartography confirms {name} coordinates"},
        ],
        "gallery": [
            {
                "path": f"/images/planets/{planet['slug']}-hero.webp",
                "caption": f"Cinematic view of {name}",
            }
        ],
    }
    path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def append_to_galaxy_data(planets: list[dict[str, str]]) -> None:
    text = DATA.read_text(encoding="utf-8")
    marker = "    ];"
    if marker not in text:
        raise RuntimeError("Could not find GalaxyData closing marker")
    block = ",\n".join(cs_entry(p) for p in planets)
    text = text.replace(marker, ",\n" + block + "\n" + marker, 1)
    DATA.write_text(text, encoding="utf-8")


def collect_imports(filter_mode: str) -> list[dict[str, str]]:
    if not REFERENCE.is_file():
        raise SystemExit(f"Missing {REFERENCE}. Download the Essential Atlas reference JSON first.")

    ref = json.loads(REFERENCE.read_text(encoding="utf-8"))
    existing_names, existing_slugs = existing_catalog()
    used_slugs = set(existing_slugs)
    planets: list[dict[str, str]] = []

    for entry in ref:
        name = entry["Name"].strip()
        if not name:
            continue
        slug = slugify(name)
        if not slug:
            continue
        if name.lower() in existing_names or slug in existing_slugs:
            continue
        if filter_mode == "image" and not entry.get("Image"):
            continue
        if filter_mode == "all" and not entry.get("Region"):
            continue
        if re.match(r"^\d", name):
            continue
        if len(name) < 2:
            continue

        unique_slug = slug
        suffix = 2
        while unique_slug in used_slugs:
            unique_slug = f"{slug}-{suffix}"
            suffix += 1

        region = normalize_region(entry.get("Region"))
        x, y = atlas_to_map(entry)
        planet = {
            "name": name,
            "slug": unique_slug,
            "route": f"planet/{unique_slug}",
            "region": region,
            "description": description_for(entry, region),
            "x": str(x),
            "y": str(y),
            "color": color_for(unique_slug),
            "atlasCoord": entry.get("Coord", ""),
            "sector": entry.get("Sector", ""),
        }
        planets.append(planet)
        used_slugs.add(unique_slug)
        existing_names.add(name.lower())

    planets.sort(key=lambda p: p["name"].lower())
    return planets


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Import Essential Atlas planets into GalaxyData")
    parser.add_argument(
        "--filter",
        choices=("image", "all"),
        default="image",
        help="Import systems with Wookieepedia images (default) or all atlas systems",
    )
    parser.add_argument("--dry-run", action="store_true", help="Report counts without writing files")
    args = parser.parse_args()

    planets = collect_imports(args.filter)
    print(f"Prepared {len(planets)} atlas systems for import (filter={args.filter})")
    if not planets:
        return
    if args.dry_run:
        for p in planets[:20]:
            print(f"  {p['name']} ({p['slug']}) @ {p['x']},{p['y']} — {p['region']}")
        if len(planets) > 20:
            print(f"  ... and {len(planets) - 20} more")
        return

    append_to_galaxy_data(planets)
    for planet in planets:
        write_profile(planet)
    ADDITIONS.write_text(json.dumps(planets, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Added {len(planets)} planets to GalaxyData and profiles.")
    print(f"Wrote {ADDITIONS}")


if __name__ == "__main__":
    main()
