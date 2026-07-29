#!/usr/bin/env python3
"""Generate placeholder government profile JSON files."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import parse_blocks

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "GovernmentData.cs"
OUTPUT = ROOT / "wwwroot" / "data" / "profiles" / "governments"
IMAGES = ROOT / "wwwroot" / "images" / "governments"


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    IMAGES.mkdir(parents=True, exist_ok=True)

    entries = parse_blocks(DATA.read_text(encoding="utf-8"))
    for entry in entries:
        slug = entry["Slug"]
        name = entry["Name"]
        description = entry["Description"]
        era = entry.get("Era", "Galactic history")
        profile = {
            "overview": description,
            "history": (
                f"{name} governed galactic affairs during the {era}. "
                "Detailed chronicles, succession rules, and institutional structure will be expanded in a future update."
            ),
            "significance": (
                f"{name} shaped the political identity of its era and remains a reference point when "
                "historians compare later governments across the Star Wars timeline."
            ),
            "notableEvents": [
                f"{name} established as a governing authority in galactic records",
                "Institutional powers and succession rules documented across chronicle eras",
            ],
            "affiliations": [name, era],
            "timeline": [
                {"era": era, "event": f"{name} enters the historical record"},
            ],
            "gallery": [
                {
                    "path": f"/images/governments/{slug}-scene.webp",
                    "caption": f"Cinematic illustration — {name}",
                }
            ],
        }
        (OUTPUT / f"{slug}.json").write_text(
            json.dumps(profile, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        print(f"Wrote governments/{slug}.json")

    print(f"Generated {len(entries)} government profiles")


if __name__ == "__main__":
    main()
