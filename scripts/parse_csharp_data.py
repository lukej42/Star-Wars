#!/usr/bin/env python3
"""Parse Star Wars directory entries from C# Data/*.cs files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"

STRING_FIELD = re.compile(r'(\w+) = "(.*?)"')
SIDE_FIELD = re.compile(r"Side = ForceSide\.(\w+)")


def parse_blocks(text: str) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        entry: dict[str, str] = {}
        for match in STRING_FIELD.finditer(block):
            key = match.group(1)
            value = match.group(2).replace('\\"', '"')
            entry[key] = value
        side = SIDE_FIELD.search(block)
        if side:
            entry["Side"] = side.group(1).lower()
        if "Slug" in entry:
            entries.append(entry)
    return entries


def load_category(filename: str) -> list[dict[str, str]]:
    path = DATA / filename
    return parse_blocks(path.read_text(encoding="utf-8"))


def normalize(entry: dict[str, str]) -> dict[str, str]:
    out = {k[0].lower() + k[1:]: v for k, v in entry.items()}
    return out


def all_directory_entries() -> dict[str, list[dict[str, str]]]:
    return {
        "jedi": [normalize(e) for e in load_category("JediData.cs")],
        "sith": [normalize(e) for e in load_category("SithData.cs")],
        "ships": [normalize(e) for e in load_category("ShipData.cs")],
        "species": [normalize(e) for e in load_category("SpeciesData.cs")],
        "bounty-hunters": [normalize(e) for e in load_category("BountyHunterData.cs")],
        "settlements": [normalize(e) for e in load_category("SettlementData.cs")],
        "force-powers": [normalize(e) for e in load_category("ForcePowerData.cs")],
    }


def load_planets() -> list[dict[str, str]]:
    return [normalize(e) for e in load_category("GalaxyData.cs")]


def load_characters() -> list[dict[str, str]]:
    return [normalize(e) for e in load_category("CharacterData.cs")]


def load_factions() -> list[dict[str, str]]:
    return [normalize(e) for e in load_category("FactionData.cs")]


if __name__ == "__main__":
    entries = all_directory_entries()
    for cat, items in entries.items():
        print(f"{cat}: {len(items)}")
