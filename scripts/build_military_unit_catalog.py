#!/usr/bin/env python3
"""Generate Data/MilitaryUnitCatalog.cs from military_unit_catalog_data.py."""

from __future__ import annotations

import sys
from collections import Counter, defaultdict
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent
OUTPUT = ROOT / "Data" / "MilitaryUnitCatalog.cs"

if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from military_unit_catalog_data import UNITS  # noqa: E402


def cs_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def format_unit(unit: tuple) -> str:
    (
        faction_slug,
        branch,
        slug,
        name,
        unit_type,
        navy_class,
        description,
        color,
        related,
    ) = unit
    branch_expr = (
        "MilitaryUnitBranch.Army" if branch == "army" else "MilitaryUnitBranch.Navy"
    )
    navy_expr = "null" if navy_class is None else f'"{cs_escape(navy_class)}"'
    related_args = ", ".join(f'"{cs_escape(r)}"' for r in related)
    related_suffix = f", {related_args}" if related else ""
    return (
        f'        Unit("{cs_escape(faction_slug)}", {branch_expr}, '
        f'"{cs_escape(slug)}", "{cs_escape(name)}", "{cs_escape(unit_type)}", '
        f"{navy_expr}, "
        f'"{cs_escape(description)}", "{cs_escape(color)}"{related_suffix}),'
    )


def write_catalog(units: list[tuple]) -> None:
    lines = [
        "using StarWars.Models;",
        "",
        "namespace StarWars.Data;",
        "",
        "public static partial class MilitaryUnitData",
        "{",
        "    public static IReadOnlyList<MilitaryUnit> Units { get; } =",
        "    [",
    ]

    current_faction: str | None = None
    for unit in units:
        faction_slug = unit[0]
        if faction_slug != current_faction:
            if current_faction is not None:
                lines.append("")
            label = faction_slug.replace("-", " ").title()
            lines.append(f"        // {label}")
            current_faction = faction_slug
        lines.append(format_unit(unit))

    lines.extend(
        [
            "    ];",
            "",
            "    private static MilitaryUnit Unit(",
            "        string factionSlug,",
            "        MilitaryUnitBranch branch,",
            "        string slug,",
            "        string name,",
            "        string unitType,",
            "        string? navyClass,",
            "        string description,",
            "        string color,",
            "        params string[] related) =>",
            "        new()",
            "        {",
            "            FactionSlug = factionSlug,",
            "            Branch = branch,",
            "            Slug = slug,",
            "            Name = name,",
            "            UnitType = unitType,",
            "            NavyClass = navyClass,",
            "            Description = description,",
            "            Color = color,",
            "            RelatedUnitSlugs = related,",
            "        };",
            "}",
            "",
        ]
    )
    OUTPUT.write_text("\n".join(lines))


def print_stats(units: list[tuple]) -> None:
    by_faction: dict[str, Counter[str]] = defaultdict(Counter)
    for faction_slug, branch, *_rest in units:
        by_faction[faction_slug][branch] += 1
        by_faction[faction_slug]["total"] += 1

    print(f"Generated {OUTPUT}")
    print(f"Total units: {len(units)}")
    print()
    for faction_slug in sorted(by_faction):
        counts = by_faction[faction_slug]
        print(
            f"{faction_slug}: total={counts['total']}, "
            f"army={counts['army']}, navy={counts['navy']}"
        )


def main() -> None:
    write_catalog(UNITS)
    print_stats(UNITS)


if __name__ == "__main__":
    main()
