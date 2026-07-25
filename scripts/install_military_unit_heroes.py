#!/usr/bin/env python3
"""Install military unit hero images into wwwroot and verify coverage."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from military_unit_hero_prompts import hero_filename, load_military_units

ROOT = Path(__file__).resolve().parents[1]
IMAGES = ROOT / "wwwroot" / "images" / "military-units"
ASSETS = ROOT / "assets" / "military-units"
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)


def install_from(source_dir: Path) -> tuple[int, int]:
    installed = 0
    units = load_military_units()
    IMAGES.mkdir(parents=True, exist_ok=True)

    for entry in units:
        filename = hero_filename(entry)
        candidates = [
            source_dir / filename,
            source_dir / filename.replace(".webp", ".png"),
            ASSETS / filename,
            ASSETS / filename.replace(".webp", ".png"),
            CURSOR_ASSETS / filename,
            CURSOR_ASSETS / filename.replace(".webp", ".png"),
        ]
        src = next((path for path in candidates if path.is_file()), None)
        if src is None:
            continue
        dest = IMAGES / filename
        if src.suffix.lower() == ".webp":
            shutil.copy2(src, dest)
        else:
            from PIL import Image

            Image.open(src).convert("RGB").save(dest, format="WEBP", quality=88, method=6)
        installed += 1

    return installed, len(units)


def verify() -> int:
    missing = []
    for entry in load_military_units():
        path = IMAGES / hero_filename(entry)
        if not path.is_file():
            missing.append(path.name)

    total = len(load_military_units())
    present = total - len(missing)
    print(f"military-units: {present}/{total} hero webp coverage")
    if missing:
        print("Missing:")
        for name in missing:
            print(f"  {name}")
        return 1
    return 0


def main() -> None:
    parser = argparse.ArgumentParser(description="Install or verify military unit hero webp assets")
    parser.add_argument(
        "--source",
        type=Path,
        help="Directory containing generated hero images (defaults to assets/military-units)",
    )
    parser.add_argument("--verify", action="store_true", help="Only verify coverage")
    args = parser.parse_args()

    if args.verify:
        raise SystemExit(verify())

    source = args.source or ASSETS
    if not source.is_dir():
        print(f"Source directory not found: {source}", file=sys.stderr)
        raise SystemExit(1)

    installed, total = install_from(source)
    print(f"Installed {installed}/{total} military unit hero images from {source}")
    raise SystemExit(verify())


if __name__ == "__main__":
    main()
