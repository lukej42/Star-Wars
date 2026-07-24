#!/usr/bin/env python3
"""Copy generated droid hero PNGs from Cursor assets into wwwroot."""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DROID_IMAGES = ROOT / "wwwroot" / "images" / "droids"
ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from droid_catalog_data import DROIDS


def install_slug(slug: str, source_dir: Path) -> bool:
    src = source_dir / f"{slug}.png"
    if not src.is_file():
        return False
    DROID_IMAGES.mkdir(parents=True, exist_ok=True)
    portrait = DROID_IMAGES / f"{slug}.png"
    scene = DROID_IMAGES / f"{slug}-scene.png"
    shutil.copy2(src, portrait)
    shutil.copy2(src, scene)
    return True


def main() -> None:
    source = ASSETS
    if len(sys.argv) > 1:
        source = Path(sys.argv[1])
    installed = 0
    missing = []
    for entry in DROIDS:
        slug = entry["slug"]
        if install_slug(slug, source):
            installed += 1
        else:
            missing.append(slug)
    print(f"Installed {installed}/{len(DROIDS)} droid hero PNGs from {source}")
    if missing:
        print(f"Missing ({len(missing)}): {', '.join(missing[:12])}{'...' if len(missing) > 12 else ''}")


if __name__ == "__main__":
    main()
