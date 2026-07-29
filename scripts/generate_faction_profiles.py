#!/usr/bin/env python3
"""Write faction profile JSON files from catalogue data and enrichments."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from faction_profile_enrichments import FACTION_GOVERNANCE, FACTION_PROFILES
from parse_csharp_data import load_factions

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "wwwroot" / "data" / "profiles" / "factions"


def gallery_for(slug: str) -> list[dict[str, str]]:
    return [
        {
            "path": f"/images/factions/{slug}-scene.webp",
            "caption": f"Cinematic illustration — faction banner",
        },
        {
            "path": f"/images/factions/{slug}.svg",
            "caption": f"Faction emblem",
        },
    ]


def build_profile(entry: dict[str, str]) -> dict:
    slug = entry["slug"]
    enriched = FACTION_PROFILES.get(slug, {})
    governance = FACTION_GOVERNANCE.get(slug, {})
    profile = {
        "overview": enriched.get("overview", entry.get("description", "")),
        "history": enriched.get("history", ""),
        "significance": enriched.get("significance", ""),
        "notableEvents": enriched.get("notableEvents", []),
        "affiliations": enriched.get("affiliations", []),
        "timeline": enriched.get("timeline", []),
        "gallery": gallery_for(slug),
    }
    if "headOfGovernment" in governance:
        profile["headOfGovernment"] = governance["headOfGovernment"]
    if "headOfState" in governance:
        profile["headOfState"] = governance["headOfState"]
    return profile


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    factions = load_factions()
    for entry in factions:
        slug = entry["slug"]
        path = OUT / f"{slug}.json"
        path.write_text(
            json.dumps(build_profile(entry), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(f"Wrote {len(factions)} faction profiles to {OUT}")


if __name__ == "__main__":
    main()
