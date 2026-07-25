#!/usr/bin/env python3
"""Export planet hero manifest JSON for batch image generation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_planets
from planet_hero_prompts import planet_prompt

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "planet_hero_manifest.json"


def main() -> None:
    manifest = []
    for entry in load_planets():
        slug = entry["slug"]
        manifest.append(
            {
                "category": "planets",
                "slug": slug,
                "name": entry.get("name", slug),
                "prompt": planet_prompt(entry),
                "output": f"wwwroot/images/planets/{slug}-hero.webp",
            }
        )
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest)} entries to {MANIFEST}")


if __name__ == "__main__":
    main()
