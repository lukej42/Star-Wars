#!/usr/bin/env python3
"""Export character hero manifest JSON for batch image generation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from character_hero_prompts import all_character_prompts
from parse_csharp_data import load_characters

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "character_hero_manifest.json"


def main() -> None:
    prompts = all_character_prompts()
    manifest = []
    for entry in load_characters():
        slug = entry["slug"]
        manifest.append(
            {
                "category": "characters",
                "slug": slug,
                "name": entry.get("name", slug),
                "prompt": prompts[slug],
                "output": f"wwwroot/images/characters/{slug}-scene.webp",
            }
        )
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest)} entries to {MANIFEST}")


if __name__ == "__main__":
    main()
