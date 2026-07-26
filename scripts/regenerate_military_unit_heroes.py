#!/usr/bin/env python3
"""Remove procedural military heroes; copy ship scenes for navy; export army manifest."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from military_navy_ship_map import (
    FACTION_NAVY_BRANCH_SHIP,
    NAVY_SHIP_MAP,
    army_prompt,
    branch_prompt,
    navy_fallback_prompt,
)
from military_unit_catalog_loader import MilitaryUnitEntry, branch_listing_entries, load_faction_slugs, load_military_units

ROOT = Path(__file__).resolve().parents[1]
MILITARY_IMAGES = ROOT / "wwwroot" / "images" / "military-units"
SHIPS = ROOT / "wwwroot" / "images" / "ships"
CURSOR_ASSETS = (
    Path.home()
    / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
)
MANIFEST = SCRIPTS / "military_army_hero_manifest.json"
FACTIONS_FILE = ROOT / "Data" / "MilitaryUnitData.cs"


def faction_names() -> dict[str, str]:
    import re

    text = FACTIONS_FILE.read_text(encoding="utf-8")
    pairs = re.findall(r'Name = "([^"]+)".*?Slug = "([^"]+)"', text, re.DOTALL)
    return {slug: name for name, slug in pairs}


def expected_hero_filenames(units: list[MilitaryUnitEntry]) -> set[str]:
    names = {entry.hero_filename for entry in units}
    for slug in load_faction_slugs():
        names.add(f"{slug}-army-hero.webp")
        names.add(f"{slug}-navy-hero.webp")
    return names


def remove_unit_heroes(units: list[MilitaryUnitEntry]) -> int:
    removed = 0
    keep = {"military-units-directory-hero.webp"}
    expected = expected_hero_filenames(units)
    faction_prefixes = tuple(f"{slug}-" for slug in load_faction_slugs())
    for path in MILITARY_IMAGES.glob("*.webp"):
        if path.name in keep:
            continue
        is_current = path.name in expected
        is_legacy_military = path.name.startswith(faction_prefixes) and path.name.endswith("-hero.webp")
        if is_current or is_legacy_military or "-army-" in path.name or "-navy-" in path.name:
            if path.name in keep:
                continue
            path.unlink()
            removed += 1
    return removed


def regenerate_navy_branch_heroes() -> int:
    copied = 0
    for slug, ship_stem in FACTION_NAVY_BRANCH_SHIP.items():
        ship_path = SHIPS / f"{ship_stem}-scene.webp"
        dest = MILITARY_IMAGES / f"{slug}-navy-hero.webp"
        if not ship_path.is_file():
            continue
        copy_webp(ship_path, dest)
        copied += 1
    return copied


def copy_webp(source: Path, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() == ".webp":
        shutil.copy2(source, dest)
        return
    from PIL import Image

    Image.open(source).convert("RGB").save(dest, format="WEBP", quality=90, method=6)


def install_from_assets(filename: str, dest: Path) -> bool:
    for base in (CURSOR_ASSETS, ROOT / "assets" / "military-units"):
        for candidate in (base / filename, base / filename.replace(".webp", ".png")):
            if candidate.is_file():
                copy_webp(candidate, dest)
                return True
    return False


def regenerate_navy(units: list[MilitaryUnitEntry]) -> tuple[int, int, list[MilitaryUnitEntry]]:
    copied = 0
    missing: list[MilitaryUnitEntry] = []
    for entry in units:
        if entry.branch != "Navy":
            continue
        dest = entry.output_path
        ship_slug = NAVY_SHIP_MAP.get(entry.slug)
        if ship_slug:
            ship_path = SHIPS / f"{ship_slug}-scene.webp"
            if ship_path.is_file():
                copy_webp(ship_path, dest)
                copied += 1
                continue
        missing.append(entry)
    return copied, len([u for u in units if u.branch == "Navy"]), missing


def export_army_manifest(units: list[MilitaryUnitEntry]) -> None:
    names = faction_names()
    items: list[dict[str, str]] = []
    for entry in units:
        if entry.branch != "Army":
            continue
        items.append(
            {
                "filename": entry.hero_filename,
                "output": str(entry.output_path.relative_to(ROOT)),
                "prompt": army_prompt(entry.name, entry.unit_type, entry.description),
            }
        )
    for slug in load_faction_slugs():
        for branch in ("army", "navy"):
            filename = f"{slug}-{branch}-hero.webp"
            output = MILITARY_IMAGES / filename
            fname = names.get(slug, slug.replace("-", " ").title())
            items.append(
                {
                    "filename": filename,
                    "output": str(output.relative_to(ROOT)),
                    "prompt": branch_prompt(fname, branch),
                }
            )
    MANIFEST.write_text(json.dumps(items, indent=2), encoding="utf-8")


def install_army_from_assets(units: list[MilitaryUnitEntry]) -> int:
    installed = 0
    for entry in units:
        if entry.branch != "Army":
            continue
        if entry.output_path.is_file():
            continue
        if install_from_assets(entry.hero_filename, entry.output_path):
            installed += 1
    for slug in load_faction_slugs():
        for branch in ("army", "navy"):
            dest = MILITARY_IMAGES / f"{slug}-{branch}-hero.webp"
            if dest.is_file():
                continue
            if install_from_assets(dest.name, dest):
                installed += 1
    return installed


def write_navy_missing_manifest(missing: list[MilitaryUnitEntry]) -> None:
    path = SCRIPTS / "military_navy_missing_manifest.json"
    items = [
        {
            "filename": entry.hero_filename,
            "output": str(entry.output_path.relative_to(ROOT)),
            "prompt": navy_fallback_prompt(entry.name, entry.unit_type, entry.description),
        }
        for entry in missing
    ]
    path.write_text(json.dumps(items, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate military unit hero images")
    parser.add_argument("--keep", action="store_true", help="Do not delete existing heroes")
    parser.add_argument("--navy-only", action="store_true")
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()

    units = load_military_units()
    if not args.keep and not args.manifest_only:
        removed = remove_unit_heroes(units)
        print(f"Removed {removed} existing military unit hero images")

    if args.manifest_only:
        export_army_manifest(units)
        print(f"Wrote army manifest with {len(json.loads(MANIFEST.read_text()))} entries to {MANIFEST}")
        return

    copied, navy_total, missing = regenerate_navy(units)
    branch_navy = regenerate_navy_branch_heroes()
    print(f"Navy: copied {copied}/{navy_total} unit heroes from ships directory")
    print(f"Navy branch listings: copied {branch_navy}/{len(FACTION_NAVY_BRANCH_SHIP)} heroes from ships directory")
    if missing:
        write_navy_missing_manifest(missing)
        print(f"Navy missing ship match: {len(missing)} (see military_navy_missing_manifest.json)")

    export_army_manifest(units)
    army_count = sum(1 for u in units if u.branch == "Army")
    print(f"Army manifest: {army_count} units + {len(load_faction_slugs()) * 2} branch listings -> {MANIFEST}")

    if not args.navy_only:
        installed = install_army_from_assets(units)
        if installed:
            print(f"Installed {installed} army heroes from Cursor assets")


if __name__ == "__main__":
    main()
