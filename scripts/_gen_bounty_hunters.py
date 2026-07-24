#!/usr/bin/env python3
"""One-shot generator for bounty_hunter_catalog_data.py"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from textwrap import indent

OUT = Path(__file__).resolve().parent / "bounty_hunter_catalog_data.py"
SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from build_bh_hunters import HUNTERS  # noqa: E402


def slugify(name: str) -> str:
    s = name.lower().replace("'", "")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")


def lore_block(d: dict) -> str:
    lines = [
        f'"origin_detail": {d["origin_detail"]!r},',
        f'"ancient_detail": {d["ancient_detail"]!r},',
        f'"modern_detail": {d["modern_detail"]!r},',
        f'"conflict_detail": {d["conflict_detail"]!r},',
        f'"methods_detail": {d["methods_detail"]!r},',
        f'"reputation_detail": {d["reputation_detail"]!r},',
        f'"impact_detail": {d["impact_detail"]!r},',
        f'"events": _ev({", ".join(repr(e) for e in d["events"])}),',
        f'"affiliations": _aff({", ".join(repr(a) for a in d["affiliations"])}),',
        f'"timeline": _tl({", ".join(f"({repr(e[0])}, {repr(e[1])})" for e in d["timeline"])}),',
    ]
    return "{\n" + indent("\n".join(lines), " " * 12) + "\n        }"


def entry(name, specialty, homeworld, description, color, sources, silhouette, lore: dict) -> str:
    return f"""    bp({name!r}, {specialty!r}, {homeworld!r},
       {description!r},
       {color!r}, {sources!r}, {silhouette!r},
       {lore_block(lore)}),"""


EXEC_HEADER = '''#!/usr/bin/env python3
"""Bounty hunter catalog entries for generate_bounty_hunter_catalog.py."""

from __future__ import annotations

from pathlib import Path

_catalog_path = Path(__file__).resolve().parent / "generate_bounty_hunter_catalog.py"
_code = _catalog_path.read_text()
_ns: dict = {"__file__": str(_catalog_path), "__name__": "_catalog_helpers"}
exec(compile(_code.split("def main()")[0], str(_catalog_path), "exec"), _ns)
bp = _ns["bp"]
_ev = _ns["_ev"]
_aff = _ns["_aff"]
_tl = _ns["_tl"]

BOUNTY_HUNTERS: list[dict] = [
'''


def main() -> None:
    seen: set[str] = set()
    for hunter in HUNTERS:
        slug = slugify(hunter[0])
        if slug in seen:
            raise SystemExit(f"Duplicate slug: {slug} for {hunter[0]}")
        seen.add(slug)
    if len(HUNTERS) < 65:
        raise SystemExit(f"Only {len(HUNTERS)} hunters")

    body = "\n".join(entry(*h) for h in HUNTERS)
    OUT.write_text(EXEC_HEADER + body + "\n]\n")
    print(f"Wrote {len(HUNTERS)} hunters to {OUT}")
    print(f"Unique slugs: {len(seen)}")


if __name__ == "__main__":
    main()
