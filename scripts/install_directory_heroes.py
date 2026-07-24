#!/usr/bin/env python3
"""Copy generated directory hero PNGs from Cursor assets into wwwroot."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import all_directory_entries

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"


def install_slug(image_dir: Path, slug: str, source_dir: Path) -> bool:
    src = source_dir / f"{slug}.png"
    if not src.is_file():
        return False
    image_dir.mkdir(parents=True, exist_ok=True)
    portrait = image_dir / f"{slug}.png"
    scene = image_dir / f"{slug}-scene.png"
    shutil.copy2(src, portrait)
    shutil.copy2(src, scene)
    return True


def install_category(category: str, slugs: list[str], source: Path) -> tuple[int, list[str]]:
    image_dir = ROOT / "wwwroot" / "images" / category
    installed = 0
    missing: list[str] = []
    for slug in slugs:
        if install_slug(image_dir, slug, source):
            installed += 1
        else:
            missing.append(slug)
    return installed, missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Install directory hero PNGs")
    parser.add_argument("source", nargs="?", default=str(DEFAULT_ASSETS), help="Source assets directory")
    parser.add_argument(
        "--category",
        action="append",
        help="Limit to category (jedi, sith, ships, species, bounty-hunters, settlements, force-powers)",
    )
    args = parser.parse_args()
    source = Path(args.source)
    entries = all_directory_entries()

    categories = args.category or list(entries.keys())
    total_installed = 0
    total_expected = 0
    all_missing: dict[str, list[str]] = {}

    for category in categories:
        if category not in entries:
            print(f"Unknown category: {category}", file=sys.stderr)
            continue
        slugs = [e["slug"] for e in entries[category]]
        total_expected += len(slugs)
        installed, missing = install_category(category, slugs, source)
        total_installed += installed
        if missing:
            all_missing[category] = missing
        print(f"{category}: {installed}/{len(slugs)} installed")

    print(f"\nTotal: {total_installed}/{total_expected} hero PNGs from {source}")
    for category, missing in all_missing.items():
        preview = ", ".join(missing[:8])
        suffix = "…" if len(missing) > 8 else ""
        print(f"  Missing {category} ({len(missing)}): {preview}{suffix}")


if __name__ == "__main__":
    main()
