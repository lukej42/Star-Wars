#!/usr/bin/env python3
"""Export regen batches containing ONLY planets below cinematic quality threshold."""

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


def needs_hero_regeneration(entry: dict[str, str]) -> bool:
    path = ROOT / "wwwroot" / "images" / "planets" / f"{entry['slug']}-hero.webp"
    return not path.is_file() or path.stat().st_size < MIN_CINEMATIC_BYTES


def write_pending_batches(prefix: str, items: list[dict], label: str) -> int:
    if not items:
        # remove stale batch files
        for old in SCRIPTS.glob(f"{prefix}_pending_batch_*.json"):
            old.unlink()
        print(f"{label}: 0 pending — no batches written")
        return 0
    count = math.ceil(len(items) / BATCH_SIZE)
    for old in SCRIPTS.glob(f"{prefix}_pending_batch_*.json"):
        old.unlink()
    for i in range(count):
        chunk = items[i * BATCH_SIZE : (i + 1) * BATCH_SIZE]
        path = SCRIPTS / f"{prefix}_pending_batch_{i + 1}.json"
        path.write_text(json.dumps(chunk, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    manifest = SCRIPTS / f"{prefix}_pending_manifest.json"
    manifest.write_text(json.dumps(items, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"{label}: {len(items)} pending → {count} batches")
    return count


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

    hero_items.sort(key=lambda e: e["name"].lower())
    space_items.sort(key=lambda e: e["name"].lower())
    write_pending_batches("planet_hero", hero_items, "Hero")
    write_pending_batches("planet_space", space_items, "Space")


if __name__ == "__main__":
    main()
