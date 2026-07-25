#!/usr/bin/env python3
"""Generate Character C# data and detailed profile JSON."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CHARACTER_CS = ROOT / "Data" / "CharacterData.cs"
CHARACTER_IMAGES = ROOT / "wwwroot" / "images" / "characters"
CHARACTER_PROFILES = ROOT / "wwwroot" / "data" / "profiles" / "characters"
SCRIPTS = Path(__file__).resolve().parent

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from character_catalog_additions import ADDITIONAL_CHARACTERS
from character_profile_enrichments import CHARACTER_ENRICHMENTS
from generate_directory_profiles import generic_character_profile, parse_members

ERAS = [
    "Ancient Era",
    "Old Republic",
    "High Republic",
    "Clone Wars",
    "Imperial Era",
    "Galactic Civil War",
    "New Republic",
    "First Order",
]


def cs_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def merge_profile(entry: dict) -> dict:
    base = generic_character_profile(
        {
            "name": entry["name"],
            "slug": entry["slug"],
            "role": entry["role"],
            "desc": entry["description"],
            "color": entry["color"],
        }
    )
    enriched = CHARACTER_ENRICHMENTS.get(entry["slug"], {})
    for key, value in enriched.items():
        if value:
            base[key] = value
    base["gallery"] = [
        {
            "path": f"/images/characters/{entry['slug']}-scene.webp",
            "caption": f"Cinematic illustration — {entry['name']}",
        },
    ]
    return base


def load_existing() -> list[dict]:
    entries = parse_members(CHARACTER_CS, "Role")
    return [
        {
            "name": e["name"],
            "slug": e["slug"],
            "role": e["role"],
            "description": e["desc"],
            "color": e["color"],
        }
        for e in entries
    ]


def write_character_cs(entries: list[dict]) -> None:
    lines = [
        "using StarWars.Models;",
        "",
        "namespace StarWars.Data;",
        "",
        "public static class CharacterData",
        "{",
        "    public static IReadOnlyList<Character> Characters { get; } =",
        "    [",
    ]
    for e in entries:
        lines.extend([
            "        new()",
            "        {",
            f'            Name = "{cs_escape(e["name"])}",',
            f'            Slug = "{cs_escape(e["slug"])}",',
            f'            Route = "characters/{cs_escape(e["slug"])}",',
            f'            Role = "{cs_escape(e["role"])}",',
            f'            Description = "{cs_escape(e["description"])}",',
            f'            Color = "{cs_escape(e["color"])}",',
            "        },",
        ])
    lines.extend([
        "    ];",
        "",
        "    public static Character? GetBySlug(string slug) =>",
        "        Characters.FirstOrDefault(c => c.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));",
        "}",
        "",
    ])
    CHARACTER_CS.write_text("\n".join(lines))


def main() -> None:
    seen: set[str] = set()
    all_chars: list[dict] = []
    for entry in load_existing() + ADDITIONAL_CHARACTERS:
        if entry["slug"] in seen:
            continue
        seen.add(entry["slug"])
        all_chars.append(entry)

    all_chars.sort(key=lambda e: e["name"].lower())
    CHARACTER_PROFILES.mkdir(parents=True, exist_ok=True)
    write_character_cs(all_chars)

    for entry in all_chars:
        profile = merge_profile(entry)
        (CHARACTER_PROFILES / f"{entry['slug']}.json").write_text(
            json.dumps(profile, indent=2, ensure_ascii=False) + "\n"
        )

    print(f"Generated {len(all_chars)} characters")
    print("  CharacterData.cs")
    print(f"  Character profiles: {len(all_chars)}")


if __name__ == "__main__":
    main()
