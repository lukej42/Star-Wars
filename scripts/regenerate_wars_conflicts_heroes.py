#!/usr/bin/env python3
"""Remove old Wars & Conflicts heroes and export photorealistic generation manifest."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from wars_conflicts_hero_scenes import battle_prompt, war_prompt

ROOT = Path(__file__).resolve().parents[1]
WARS_IMAGES = ROOT / "wwwroot" / "images" / "wars-conflicts"
MANIFEST = SCRIPTS / "wars_conflicts_hero_manifest.json"
DATA = ROOT / "Data"


def load_wars() -> list[dict[str, str]]:
    text = (DATA / "WarConflictData.cs").read_text(encoding="utf-8")
    items: list[dict[str, str]] = []
    for match in re.finditer(
        r'Name\s*=\s*"([^"]+)".*?Slug\s*=\s*"([^"]+)"',
        text,
        re.DOTALL,
    ):
        name, slug = match.groups()
        filename = f"{slug}-hero.webp"
        items.append(
            {
                "category": "war",
                "slug": slug,
                "name": name,
                "filename": filename,
                "output": str((WARS_IMAGES / filename).relative_to(ROOT)),
                "prompt": war_prompt(name, slug),
            }
        )
    return items


def load_battles() -> list[dict[str, str]]:
    text = (DATA / "BattleData.cs").read_text(encoding="utf-8")
    items: list[dict[str, str]] = []
    for match in re.finditer(
        r'Battle\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)"\)',
        text,
    ):
        war_slug, slug, name, era, _color = match.groups()
        filename = f"{slug}-hero.webp"
        items.append(
            {
                "category": "battle",
                "slug": slug,
                "name": name,
                "war_slug": war_slug,
                "era": era,
                "filename": filename,
                "output": str((WARS_IMAGES / "battles" / filename).relative_to(ROOT)),
                "prompt": battle_prompt(name, slug, era, war_slug),
            }
        )
    return items


def remove_wars_heroes() -> int:
    keep = {"wars-conflicts-directory-hero.webp"}
    removed = 0
    for path in WARS_IMAGES.rglob("*.webp"):
        if path.name in keep:
            continue
        path.unlink()
        removed += 1
    return removed


def export_manifest() -> list[dict[str, str]]:
    items = load_wars() + load_battles()
    MANIFEST.write_text(json.dumps(items, indent=2), encoding="utf-8")
    return items


def main() -> None:
    parser = argparse.ArgumentParser(description="Regenerate Wars & Conflicts hero manifest")
    parser.add_argument("--keep", action="store_true", help="Do not delete existing heroes")
    parser.add_argument("--manifest-only", action="store_true")
    args = parser.parse_args()

    if not args.keep and not args.manifest_only:
        removed = remove_wars_heroes()
        print(f"Removed {removed} existing Wars & Conflicts hero images")

    items = export_manifest()
    wars = sum(1 for i in items if i["category"] == "war")
    battles = sum(1 for i in items if i["category"] == "battle")
    print(f"Manifest: {wars} wars + {battles} battles = {len(items)} entries -> {MANIFEST}")


if __name__ == "__main__":
    main()
