#!/usr/bin/env python3
"""Load military units from generated catalog for hero image workflows."""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "Data" / "MilitaryUnitCatalog.cs"
FACTIONS_FILE = ROOT / "Data" / "MilitaryUnitData.cs"

UNIT_CALL = re.compile(
    r'Unit\("([^"]+)", MilitaryUnitBranch\.(Army|Navy), "([^"]+)", "([^"]+)", "([^"]+)", (null|"[^"]+"), "([^"]+)", "([^"]+)"(?:, ([^)]+))?\)',
)


@dataclass(frozen=True)
class MilitaryUnitEntry:
    faction_slug: str
    branch: str
    slug: str
    name: str
    unit_type: str
    navy_class: str | None
    description: str
    color: str

    @property
    def hero_filename(self) -> str:
        return f"{self.faction_slug}-{self.branch.lower()}-{self.slug}-hero.webp"

    @property
    def output_path(self) -> Path:
        return ROOT / "wwwroot" / "images" / "military-units" / self.hero_filename


def load_military_units() -> list[MilitaryUnitEntry]:
    text = CATALOG.read_text(encoding="utf-8")
    entries: list[MilitaryUnitEntry] = []
    for match in UNIT_CALL.finditer(text):
        faction, branch, slug, name, unit_type, navy_raw, description, color, _related = match.groups()
        navy_class = None if navy_raw == "null" else navy_raw.strip('"')
        entries.append(
            MilitaryUnitEntry(
                faction_slug=faction,
                branch=branch,
                slug=slug,
                name=name,
                unit_type=unit_type,
                navy_class=navy_class,
                description=description,
                color=color,
            )
        )
    return entries


def load_faction_slugs() -> list[str]:
    text = FACTIONS_FILE.read_text(encoding="utf-8")
    return re.findall(r'Slug = "([^"]+)"', text.split("Factions { get; }")[1].split("];")[0])


def branch_listing_entries() -> list[tuple[str, str, Path]]:
    items: list[tuple[str, str, Path]] = []
    base = ROOT / "wwwroot" / "images" / "military-units"
    for slug in load_faction_slugs():
        items.append((slug, "army", base / f"{slug}-army-hero.webp"))
        items.append((slug, "navy", base / f"{slug}-navy-hero.webp"))
    return items
