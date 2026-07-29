#!/usr/bin/env python3
"""Generate wwwroot/data/profiles/chronicles/*.json from chronicle_profile_data."""

from __future__ import annotations

import json
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from chronicle_profile_data import get_chronicle_profiles

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "wwwroot" / "data" / "profiles" / "chronicles"


def main() -> None:
    profiles = get_chronicle_profiles()
    OUTPUT.mkdir(parents=True, exist_ok=True)
    for slug, profile in profiles.items():
        path = OUTPUT / f"{slug}.json"
        path.write_text(json.dumps(profile, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote {path.relative_to(ROOT)}")
    print(f"Generated {len(profiles)} chronicle profiles")


if __name__ == "__main__":
    main()
