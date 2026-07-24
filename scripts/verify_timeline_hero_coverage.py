#!/usr/bin/env python3
"""Verify cinematic hero PNG coverage for timeline entries."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_timelines

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images" / "timelines"


def main() -> None:
    entries = load_timelines()
    missing = []
    for entry in entries:
        slug = entry["slug"]
        scene = IMAGES / f"{slug}-scene.png"
        if not scene.is_file():
            missing.append(slug)
    ok = len(entries) - len(missing)
    print(f"timelines: {ok}/{len(entries)} OK")
    if missing:
        print("Missing:", ", ".join(missing))
        sys.exit(1)


if __name__ == "__main__":
    main()
