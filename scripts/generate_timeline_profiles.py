#!/usr/bin/env python3
"""Write timeline profile JSON files from catalogue data and enrichments."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_timelines
from timeline_profile_enrichments import TIMELINE_PROFILES

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "wwwroot" / "data" / "profiles" / "timelines"


def gallery_for(slug: str) -> list[dict[str, str]]:
    return [
        {
            "path": f"/images/timelines/{slug}-scene.png",
            "caption": f"Cinematic illustration — {slug.replace('-', ' ').title()}",
        }
    ]


def build_profile(entry: dict[str, str]) -> dict:
    slug = entry["slug"]
    enriched = TIMELINE_PROFILES.get(slug, {})
    return {
        "overview": enriched.get("overview", entry.get("description", "")),
        "history": enriched.get("history", ""),
        "significance": enriched.get("significance", ""),
        "notableEvents": enriched.get("notableEvents", []),
        "affiliations": enriched.get("affiliations", []),
        "timeline": enriched.get("timeline", []),
        "gallery": gallery_for(slug),
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    entries = load_timelines()
    for entry in entries:
        slug = entry["slug"]
        path = OUT / f"{slug}.json"
        path.write_text(
            json.dumps(build_profile(entry), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
    print(f"Wrote {len(entries)} timeline profiles to {OUT}")


if __name__ == "__main__":
    main()
