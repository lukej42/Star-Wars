#!/usr/bin/env python3
"""Install chronicle cinematic hero webp assets into wwwroot."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_category

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"


def chronicle_slugs() -> list[str]:
    entries = load_category("ChroniclesData.cs")
    return [entry["Slug"] for entry in entries]


def install_slug(slug: str, source_dir: Path) -> bool:
    src = source_dir / f"{slug}-scene.webp"
    if not src.is_file():
        src = source_dir / f"{slug}.webp"
    if not src.is_file():
        return False
    image_dir = ROOT / "wwwroot" / "images" / "chronicles"
    image_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, image_dir / f"{slug}-scene.webp")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", nargs="?", default=str(DEFAULT_ASSETS))
    args = parser.parse_args()
    source = Path(args.source)
    slugs = chronicle_slugs()
    installed = 0
    missing = []
    for slug in slugs:
        if install_slug(slug, source):
            installed += 1
        else:
            missing.append(slug)
    print(f"Installed {installed}/{len(slugs)} chronicle hero webp files from {source}")
    if missing:
        preview = ", ".join(missing[:10])
        suffix = "…" if len(missing) > 10 else ""
        print(f"Missing ({len(missing)}): {preview}{suffix}")


if __name__ == "__main__":
    main()
