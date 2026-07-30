#!/usr/bin/env python3
"""Export hero and space regen manifests split into batch JSON files."""

from __future__ import annotations

import json
import math
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from export_planet_space_manifest import needs_regeneration as needs_space_regen, space_prompt
from parse_csharp_data import load_planets
from planet_hero_prompts import planet_prompt

MIN_CINEMATIC_BYTES = 500_000
BATCH_SIZE = 40
HERO_MANIFEST = SCRIPTS / "planet_hero_regen_manifest.json"
SPACE_MANIFEST = SCRIPTS / "planet_space_regen_manifest.json"


def needs_hero_regeneration(entry: dict[str, str]) -> bool:
    path = ROOT / "wwwroot" / "images" / "planets" / f"{entry['slug']}-hero.webp"
    return not path.is_file() or path.stat().st_size < MIN_CINEMATIC_BYTES


def write_batches(prefix: str, items: list[dict]) -> int:
    batch_count = max(1, math.ceil(len(items) / BATCH_SIZE)) if items else 0
    for i in range(batch_count):
        chunk = items[i * BATCH_SIZE : (i + 1) * BATCH_SIZE]
        path = SCRIPTS / f"{prefix}_regen_batch_{i + 1}.json"
        path.write_text(json.dumps(chunk, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return batch_count


def main() -> None:
    hero_items = []
    space_items = []
    for entry in load_planets():
        slug = entry["slug"]
        if needs_hero_regeneration(entry):
            hero_items.append(
                {
                    "slug": slug,
                    "name": entry.get("name", slug),
                    "prompt": planet_prompt(entry),
                    "output": f"wwwroot/images/planets/{slug}-hero.webp",
                }
            )
        if needs_space_regen(entry):
            space_items.append(
                {
                    "slug": slug,
                    "name": entry.get("name", slug),
                    "prompt": space_prompt(entry),
                    "output": f"wwwroot/images/planets/{slug}-space.webp",
                }
            )

    HERO_MANIFEST.write_text(json.dumps(hero_items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    SPACE_MANIFEST.write_text(json.dumps(space_items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    hero_batches = write_batches("planet_hero", hero_items)
    space_batches = write_batches("planet_space", space_items)
    print(f"Hero regen: {len(hero_items)} entries in {hero_batches} batches")
    print(f"Space regen: {len(space_items)} entries in {space_batches} batches")


if __name__ == "__main__":
    main()
