#!/usr/bin/env python3
"""Copy a generated hero PNG to assets and wwwroot (portrait + scene)."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"


def copy_hero(category: str, slug: str, source: Path) -> bool:
    if not source.is_file():
        return False
    assets = DEFAULT_ASSETS / f"{slug}.webp"
    assets.parent.mkdir(parents=True, exist_ok=True)
    if source.resolve() != assets.resolve():
        shutil.copy2(source, assets)

    image_dir = ROOT / "wwwroot" / "images" / category
    image_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, image_dir / f"{slug}.webp")
    shutil.copy2(source, image_dir / f"{slug}-scene.webp")
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("category")
    parser.add_argument("slug")
    parser.add_argument("source", nargs="?", help="Source PNG path (defaults to assets/{slug}.webp)")
    args = parser.parse_args()
    source = Path(args.source) if args.source else DEFAULT_ASSETS / f"{args.slug}.webp"
    ok = copy_hero(args.category, args.slug, source)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
