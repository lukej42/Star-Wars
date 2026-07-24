#!/usr/bin/env python3
"""List directory entries missing cinematic hero PNGs."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import all_directory_entries

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", required=True)
    parser.add_argument("--json", action="store_true", help="Output manifest-style JSON with prompts")
    args = parser.parse_args()

    entries = all_directory_entries()[args.category]
    missing = []
    for entry in entries:
        slug = entry["slug"]
        scene = IMAGES / args.category / f"{slug}-scene.png"
        if not scene.is_file():
            missing.append(entry)

    if args.json:
        from directory_hero_prompts import prompt_for

        out = [
            {
                "category": args.category,
                "slug": e["slug"],
                "name": e.get("name", e["slug"]),
                "prompt": prompt_for(args.category, e),
            }
            for e in missing
        ]
        json.dump(out, sys.stdout, indent=2)
    else:
        for e in missing:
            print(e["slug"])


if __name__ == "__main__":
    main()
