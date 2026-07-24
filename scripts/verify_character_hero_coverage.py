#!/usr/bin/env python3
"""Verify cinematic hero PNG coverage for character directory entries."""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_characters

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images" / "characters"


def main() -> None:
    entries = load_characters()
    missing = [e["slug"] for e in entries if not (IMAGES / f"{e['slug']}-scene.png").is_file()]
    print(f"characters: {len(entries) - len(missing)}/{len(entries)} OK")
    if missing:
        print(f"Missing ({len(missing)}): {', '.join(missing[:8])}{'…' if len(missing) > 8 else ''}")
    sys.exit(0 if not missing else 1)


if __name__ == "__main__":
    main()
