#!/usr/bin/env python3
"""Install species hero PNGs from assets into wwwroot."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"


def install_slugs(slugs: list[str], source: Path) -> tuple[int, list[str]]:
    dest = ROOT / "wwwroot" / "images" / "species"
    dest.mkdir(parents=True, exist_ok=True)
    installed = 0
    missing: list[str] = []
    for slug in slugs:
        src = source / f"{slug}.png"
        if not src.is_file():
            missing.append(slug)
            continue
        shutil.copy2(src, dest / f"{slug}.png")
        shutil.copy2(src, dest / f"{slug}-scene.png")
        installed += 1
    return installed, missing


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("slugs", nargs="+", help="Species slugs to install")
    parser.add_argument("--source", default=str(DEFAULT_ASSETS))
    args = parser.parse_args()
    installed, missing = install_slugs(args.slugs, Path(args.source))
    print(f"installed {installed}/{len(args.slugs)}")
    if missing:
        print("missing:", ", ".join(missing), file=sys.stderr)


if __name__ == "__main__":
    main()
