#!/usr/bin/env python3
"""Install planet cinematic hero PNGs from Cursor assets into wwwroot."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_planets

ROOT = Path(__file__).resolve().parents[1]
PLANET_IMAGES = ROOT / "wwwroot" / "images" / "planets"
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"


def install_slug(slug: str, source_dir: Path) -> bool:
    src = source_dir / f"{slug}.png"
    if not src.is_file():
        return False
    PLANET_IMAGES.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, PLANET_IMAGES / f"{slug}-hero.png")
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Install planet hero PNGs")
    parser.add_argument("source", nargs="?", default=str(DEFAULT_ASSETS))
    args = parser.parse_args()
    source = Path(args.source)
    entries = load_planets()
    installed = 0
    missing = []
    for entry in entries:
        slug = entry["slug"]
        if install_slug(slug, source):
            installed += 1
        else:
            missing.append(slug)
    print(f"Installed {installed}/{len(entries)} planet hero PNGs from {source}")
    if missing:
        preview = ", ".join(missing[:10])
        suffix = "…" if len(missing) > 10 else ""
        print(f"Missing ({len(missing)}): {preview}{suffix}")


if __name__ == "__main__":
    main()
