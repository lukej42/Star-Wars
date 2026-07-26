#!/usr/bin/env python3
"""Install Wars & Conflicts hero images from Cursor assets into wwwroot."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[1]
MANIFEST = SCRIPTS / "wars_conflicts_hero_manifest.json"
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)
LOCAL_ASSETS = ROOT / "assets" / "wars-conflicts"


def copy_webp(source: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.is_file() and source.stat().st_size <= dest.stat().st_size:
        return
    if source.suffix.lower() == ".webp":
        shutil.copy2(source, dest)
        return
    from PIL import Image

    Image.open(source).convert("RGB").save(dest, format="WEBP", quality=90, method=6)


def asset_name(item: dict[str, str]) -> str:
    if item["category"] == "battle":
        return f"battles-{item['slug']}-hero.webp"
    return f"wars-{item['slug']}-hero.webp"


def find_source(item: dict[str, str], source_dir: Path | None) -> Path | None:
    dirs = [source_dir] if source_dir else []
    dirs.extend([LOCAL_ASSETS, CURSOR_ASSETS])
    names = [
        item["filename"],
        asset_name(item),
        item["filename"].replace(".webp", ".png"),
    ]
    for base in dirs:
        if base is None or not base.is_dir():
            continue
        for name in names:
            candidate = base / name
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
        src = find_source(item, source_dir)
        if src is None:
            missing.append(item)
            continue
        copy_webp(src, dest)
        installed += 1
    return installed, missing


def main() -> None:
    parser = argparse.ArgumentParser(description="Install Wars & Conflicts hero images")
    parser.add_argument("--source", type=Path)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--verify", action="store_true")
    args = parser.parse_args()

    items: list[dict[str, str]] = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.verify:
        missing = [item for item in items if not (ROOT / item["output"]).is_file()]
        present = len(items) - len(missing)
        print(f"Wars & Conflicts heroes: {present}/{len(items)} present")
        if missing:
            for item in missing:
                print(f"  {item['filename']}")
        raise SystemExit(1 if missing else 0)

    installed, missing = install(args.source, args.force)
    print(f"Installed {installed} Wars & Conflicts hero images")
    if missing:
        print(f"Still missing {len(missing)} heroes")
    raise SystemExit(0 if not missing else 1)


if __name__ == "__main__":
    main()
