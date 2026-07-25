#!/usr/bin/env python3
"""Export hero prompt manifest JSON for batch image generation."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from directory_hero_prompts import all_prompts
from parse_csharp_data import all_directory_entries

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "hero_manifest.json"


def main() -> None:
    prompts = all_prompts()
    entries = all_directory_entries()
    manifest: list[dict] = []
    for category, items in entries.items():
        for entry in items:
            slug = entry["slug"]
            manifest.append(
                {
                    "category": category,
                    "slug": slug,
                    "name": entry.get("name", slug),
                    "prompt": prompts[category][slug],
                    "output": f"wwwroot/images/{category}/{slug}.webp",
                }
            )
    MANIFEST.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print(f"Wrote {len(manifest)} entries to {MANIFEST}")


if __name__ == "__main__":
    main()
