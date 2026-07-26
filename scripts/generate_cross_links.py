#!/usr/bin/env python3
"""Generate cross-links.json Related Archives for all directory pages."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from cross_link_builder import build_cross_link_entries

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "wwwroot" / "data" / "cross-links.json"


def main() -> None:
    entries = build_cross_link_entries()
    OUTPUT.write_text(json.dumps(entries, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    categories: dict[str, int] = {}
    with_links = 0
    for entry in entries:
        categories[entry["category"]] = categories.get(entry["category"], 0) + 1
        if entry["links"]:
            with_links += 1
    print(f"Wrote {len(entries)} cross-link entries to {OUTPUT}")
    print(f"Entries with links: {with_links}/{len(entries)}")
    for category in sorted(categories):
        print(f"  {category}: {categories[category]}")


if __name__ == "__main__":
    main()
