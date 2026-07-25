#!/usr/bin/env python3
"""Verify cinematic hero PNG coverage for planet directory entries."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_planets

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images" / "planets"


def main() -> None:
    entries = load_planets()
    missing = []
    for entry in entries:
        slug = entry["slug"]
        hero = IMAGES / f"{slug}-hero.webp"
        if not hero.is_file():
            missing.append(slug)
    print(f"planets: {len(entries) - len(missing)}/{len(entries)} OK")
    if missing:
        print(f"Missing ({len(missing)}): {', '.join(missing[:8])}{'…' if len(missing) > 8 else ''}")
    sys.exit(0 if not missing else 1)


if __name__ == "__main__":
    main()
