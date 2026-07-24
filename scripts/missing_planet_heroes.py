#!/usr/bin/env python3
"""List planets missing cinematic hero PNGs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_planets
from planet_hero_prompts import planet_prompt

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images" / "planets"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    missing_entries = []
    for entry in load_planets():
        slug = entry["slug"]
        if not (IMAGES / f"{slug}-hero.png").is_file():
            missing_entries.append(entry)
    if args.json:
        out = [
            {
                "category": "planets",
                "slug": e["slug"],
                "name": e.get("name", e["slug"]),
                "prompt": planet_prompt(e),
                "output": f"wwwroot/images/planets/{e['slug']}-hero.png",
            }
            for e in missing_entries
        ]
        json.dump(out, sys.stdout, indent=2)
    else:
        for e in missing_entries:
            print(e["slug"])


if __name__ == "__main__":
    main()
