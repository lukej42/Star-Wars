#!/usr/bin/env python3
"""Print hero manifest slice for batch image generation."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "scripts" / "hero_manifest.json"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", help="Filter by category")
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--slugs-only", action="store_true")
    args = parser.parse_args()

    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    if args.category:
        items = [i for i in items if i["category"] == args.category]
    if args.offset:
        items = items[args.offset :]
    if args.limit:
        items = items[: args.limit]

    if args.slugs_only:
        for item in items:
            print(item["slug"])
    else:
        json.dump(items, sys.stdout, indent=2)


if __name__ == "__main__":
    main()
