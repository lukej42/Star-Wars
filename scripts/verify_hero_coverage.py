#!/usr/bin/env python3
"""Verify cinematic hero PNG coverage for directory entries."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import all_directory_entries

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images"


def main() -> None:
    entries = all_directory_entries()
    total = 0
    missing_total = 0
    for category, items in entries.items():
        missing = []
        for entry in items:
            slug = entry["slug"]
            scene = IMAGES / category / f"{slug}-scene.png"
            if not scene.is_file():
                missing.append(slug)
        total += len(items)
        missing_total += len(missing)
        status = "OK" if not missing else f"MISSING {len(missing)}"
        print(f"{category}: {len(items) - len(missing)}/{len(items)} {status}")
        if missing and len(missing) <= 6:
            print(f"  {', '.join(missing)}")
        elif missing:
            print(f"  {', '.join(missing[:6])}…")
    print(f"\nTotal coverage: {total - missing_total}/{total}")
    sys.exit(0 if missing_total == 0 else 1)


if __name__ == "__main__":
    main()
