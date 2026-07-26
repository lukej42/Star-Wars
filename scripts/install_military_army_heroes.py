#!/usr/bin/env python3
"""Install army military unit hero images from Cursor assets into wwwroot."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[1]
MANIFEST = SCRIPTS / "military_army_hero_manifest.json"
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)
LOCAL_ASSETS = ROOT / "assets" / "military-units"


def copy_webp(source: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file() and source.stat().st_size <= dest.stat().st_size:
        return
    if source.suffix.lower() == ".webp":
        shutil.copy2(source, dest)
        return
    from PIL import Image

    Image.open(source).convert("RGB").save(dest, format="WEBP", quality=90, method=6)


def find_source(filename: str, source_dir: Path | None) -> Path | None:
    dirs = [source_dir] if source_dir else []
    dirs.extend([LOCAL_ASSETS, CURSOR_ASSETS])
    stem = filename.replace(".webp", "")
    for base in dirs:
        if base is None or not base.is_dir():
            continue
        for candidate in (
            base / filename,
            base / f"{stem}.png",
            base / filename.replace(".webp", ".png"),
        ):
            if candidate.is_file():
                return candidate
    return None


def install(source_dir: Path | None, force: bool) -> tuple[int, list[dict[str, str]]]:
    items: list[dict[str, str]] = json.loads(MANIFEST.read_text(encoding="utf-8"))
    installed = 0
    missing: list[dict[str, str]] = []
    for item in items:
        dest = ROOT / item["output"]
        if dest.is_file() and not force:
            continue
        src = find_source(item["filename"], source_dir)
        if src is None:
            missing.append(item)
            continue
        copy_webp(src, dest)
        installed += 1
    return installed, missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Install army military hero images from generated assets")
    parser.add_argument("--source", type=Path, help="Directory containing generated hero images")
    parser.add_argument("--force", action="store_true", help="Overwrite existing heroes")
    parser.add_argument("--verify", action="store_true", help="Only report missing heroes")
    args = parser.parse_args()

    items: list[dict[str, str]] = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.verify:
        missing = [item for item in items if not (ROOT / item["output"]).is_file()]
        present = len(items) - len(missing)
        print(f"Army heroes: {present}/{len(items)} present")
        if missing:
            print("Missing:")
            for item in missing:
                print(f"  {item['filename']}")
        raise SystemExit(1 if missing else 0)

    installed, missing = install(args.source, args.force)
    print(f"Installed {installed} army hero images")
    if missing:
        print(f"Still missing {len(missing)} heroes (generate via manifest prompts)")
    raise SystemExit(0 if not missing else 1)


if __name__ == "__main__":
    main()
