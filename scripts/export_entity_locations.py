#!/usr/bin/env python3
"""Export entity homeworld/location links to wwwroot/data/entity-locations.json."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from cross_link_builder import CrossLinkIndexes
from entity_homeworld_overrides import (
    CATEGORY_OVERRIDES,
    DROID_KEYWORDS,
    DROID_MANUFACTURERS,
    SHIP_KEYWORDS,
)
from parse_csharp_data import all_directory_entries, load_characters

OUTPUT = ROOT / "wwwroot" / "data" / "entity-locations.json"


def resolve_ship(indexes: CrossLinkIndexes, entry: dict[str, str]) -> dict[str, str] | None:
    blob = f"{entry.get('name', '')} {entry.get('class', '')} {entry.get('description', '')} {entry.get('era', '')}".lower()
    for keyword, slug in SHIP_KEYWORDS:
        if keyword in blob:
            planet = indexes._planet_for_name(slug.replace("-", " "))
            if planet:
                return planet
    planets = indexes._match_planets(indexes._norm(blob))
    return planets[0] if planets else None


def resolve_droid(indexes: CrossLinkIndexes, entry: dict[str, str]) -> dict[str, str] | None:
    manufacturer = entry.get("manufacturer", "")
    if manufacturer in DROID_MANUFACTURERS:
        planet = indexes._planet_for_name(DROID_MANUFACTURERS[manufacturer].replace("-", " "))
        if planet:
            return planet
    blob = f"{entry.get('name', '')} {manufacturer} {entry.get('description', '')}".lower()
    for keyword, slug in DROID_KEYWORDS:
        if keyword in blob:
            planet = indexes._planet_for_name(slug.replace("-", " "))
            if planet:
                return planet
    planets = indexes._match_planets(indexes._norm(blob))
    return planets[0] if planets else None


def resolve_person(indexes: CrossLinkIndexes, category: str, entry: dict[str, str]) -> dict[str, str] | None:
    slug = entry["slug"]
    override = CATEGORY_OVERRIDES.get(category, {}).get(slug)
    if override and override != "unknown":
        planet = indexes._planet_for_name(override.replace("-", " "))
        if planet:
            return planet

    homeworld = entry.get("homeworld", "")
    if homeworld:
        for part in re.split(r"[;/,]", homeworld):
            planet = indexes._planet_for_name(part.strip())
            if planet:
                return planet

    profile = indexes.profiles.get(category, {}).get(slug, {})
    text = indexes._norm(
        " ".join(
            [
                entry.get("description", ""),
                entry.get("role", ""),
                entry.get("rank", ""),
                entry.get("title", ""),
                profile.get("overview", ""),
                profile.get("history", ""),
            ]
        )
    )
    planets = indexes._match_planets(text)
    return planets[0] if planets else None


def to_record(planet: dict[str, str]) -> dict[str, str]:
    return {
        "planetName": planet["name"],
        "route": planet["route"],
    }


def main() -> int:
    indexes = CrossLinkIndexes()
    indexes.load()

    records: dict[str, dict[str, str]] = {}

    for category in ("jedi", "sith", "characters", "ships", "droids", "bounty-hunters"):
        items = all_directory_entries().get(category, [])
        if category == "characters":
            items = load_characters()
        for entry in items:
            slug = entry["slug"]
            if category in ("ships",):
                planet = resolve_ship(indexes, entry)
            elif category == "droids":
                planet = resolve_droid(indexes, entry)
            else:
                planet = resolve_person(indexes, category, entry)
            if planet:
                records[f"{category}/{slug}"] = to_record(planet)

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(records, indent=2), encoding="utf-8")
    print(f"Wrote {len(records)} entity location records to {OUTPUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
