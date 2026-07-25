#!/usr/bin/env python3
"""Generate Droid C# data, profile JSON, and PNG hero paths."""

from __future__ import annotations

import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DROID_CS = ROOT / "Data" / "DroidData.cs"
DROID_IMAGES = ROOT / "wwwroot" / "images" / "droids"
DROID_PROFILES = ROOT / "wwwroot" / "data" / "profiles" / "droids"
SCRIPTS = Path(__file__).resolve().parent

import sys
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))


def cs_escape(value: str) -> str:
    return value.replace("\\", "\\\\").replace('"', '\\"')


def slugify(name: str) -> str:
    s = name.lower().replace("'", "")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return s


def join_sentences(*parts: str) -> str:
    return " ".join(p.strip() for p in parts if p and p.strip())


def join_paragraphs(*parts: str) -> str:
    return "\n\n".join(p.strip() for p in parts if p and p.strip())


def _tl(*pairs: tuple[str, str]) -> list[tuple[str, str]]:
    return list(pairs)


def _ev(*items: str) -> list[str]:
    return list(items)


def _aff(*items: str) -> list[str]:
    return list(items)


def build_droid_lore(
    name: str,
    droid_type: str,
    manufacturer: str,
    *,
    origin_detail: str,
    ancient_detail: str,
    modern_detail: str,
    conflict_detail: str,
    design_detail: str,
    ethics_detail: str,
    impact_detail: str,
    events: list[str],
    affiliations: list[str],
    timeline: list[tuple[str, str]],
) -> dict:
    origins = join_sentences(
        f"{name} belongs to the {droid_type.lower()} class manufactured by {manufacturer}, one of the most recognizable automaton designs documented across galactic history.",
        origin_detail,
        f"Factory logs, maintenance manuals, and holodrama archives all treat {name} as more than a serial number—a unit whose choices and failures moved empires.",
        f"Sources spanning all nine saga films, animated series, Knights of the Old Republic, Knights of the Old Republic II, The Old Republic, and the ancient Sith Empire reference this design lineage.",
    )
    ancient = join_sentences(
        f"Early prototypes and predecessor chassis from the Old Republic era established the engineering tradition that produced {name}.",
        ancient_detail,
        f"Sith Empire war factories and Rakatan salvage teams occasionally copied {manufacturer} subsystems without license, spreading the design language across millennia.",
        f"Jedi Archives contain maintenance notes on droid ethics and {droid_type.lower()} behavior long before the Clone Wars industrialized droid warfare.",
    )
    modern = join_sentences(
        f"In the modern era, {name} units appear in fleet hangars, palace courts, rebel safe houses, and Separatist foundries with equal frequency.",
        modern_detail,
        f"Mandalorian-era bounty postings and Resistance repair bays still stock spare parts compatible with {manufacturer} frames.",
        f"Historians studying the Sequel Era treat surviving {name} memory cores as primary sources on earlier conflicts.",
    )
    conflicts = join_sentences(
        f"{name} and similar units were deployed in the galaxy's bloodiest campaigns—sometimes as soldiers, sometimes as medics, pilots, or saboteurs.",
        conflict_detail,
        f"KOTOR-era battlefields and TOR-era fleet actions show earlier generations of {droid_type.lower()} units performing comparable roles under different banners.",
        f"Rebel and Imperial manuals both include tactical appendices on neutralizing or reprogramming {manufacturer} automata.",
    )
    design = join_sentences(
        f"Engineering analysis of {name} highlights why {droid_type.lower()} designs succeed: modular parts, clear firmware roles, and production lines scaled to wartime demand.",
        design_detail,
        f"Technicians praise {manufacturer} documentation; slicers praise its predictable security flaws—both keep {name} relevant in scrap yards centuries later.",
        f"New Republic certification boards still debate which {droid_type.lower()} subroutines require sentience review under the Galactic Rights Charter.",
    )
    ethics = join_sentences(
        f"Droid rights activists cite {name} when arguing that personality matrices, memory wipes, and restraining bolts can be torture or enslavement.",
        ethics_detail,
        f"C-3PO's testimony before Bail Organa and L3-37's Kessel uprising belong to the same moral conversation as {name}'s service record.",
        f"Whether {name} is property or person remains unsettled law on a hundred worlds.",
    )
    impact = join_sentences(
        f"The galactic impact of {name} exceeds production statistics: this unit type altered battles, treaties, and cultural memory.",
        impact_detail,
        f"Without units like {name}, key missions—from Death Star data recovery to Separatist invasions—would have unfolded differently or failed entirely.",
        f"Museums on Coruscant, Mandalore, and Nar Shaddaa display {manufacturer} chassis as icons of industrial civilization and its costs.",
    )
    return {
        "origins": origins,
        "ancient": ancient,
        "modern": modern,
        "conflicts": conflicts,
        "design": design,
        "ethics": ethics,
        "impact": impact,
        "events": events,
        "affiliations": affiliations,
        "timeline": [{"era": era, "event": event} for era, event in timeline],
    }


def dp(
    name: str,
    droid_type: str,
    manufacturer: str,
    description: str,
    color: str,
    sources: str,
    silhouette: str,
    lore_kwargs: dict,
) -> dict:
    slug = slugify(name)
    lore = build_droid_lore(name, droid_type, manufacturer, **lore_kwargs)
    return {
        "name": name,
        "slug": slug,
        "droid_type": droid_type,
        "manufacturer": manufacturer,
        "description": description,
        "color": color,
        "sources": sources,
        "silhouette": silhouette,
        "lore": lore,
    }


def build_droid_profile(entry: dict) -> dict:
    lore = entry["lore"]
    overview = join_sentences(
        f"{entry['name']} is a {entry['droid_type'].lower()} built by {entry['manufacturer']}, documented across {entry['sources']}.",
        entry["description"],
    )
    history = join_paragraphs(lore["origins"], lore["ancient"], lore["modern"], lore["conflicts"])
    significance = join_paragraphs(lore["design"], lore["ethics"], lore["impact"])
    return {
        "overview": overview,
        "history": history,
        "significance": significance,
        "notableEvents": lore["events"],
        "affiliations": lore["affiliations"],
        "timeline": lore["timeline"],
        "gallery": [
            {"path": f"/images/droids/{entry['slug']}-scene.webp", "caption": f"Cinematic illustration — {entry['name']}"},
        ],
    }


def write_droid_cs(entries: list[dict]) -> None:
    lines = [
        "using StarWars.Models;",
        "",
        "namespace StarWars.Data;",
        "",
        "public static class DroidData",
        "{",
        "    public static IReadOnlyList<Droid> Droids { get; } =",
        "    [",
    ]
    for e in entries:
        lines.extend([
            "        new()",
            "        {",
            f'            Name = "{cs_escape(e["name"])}",',
            f'            Slug = "{cs_escape(e["slug"])}",',
            f'            Route = "droids/{cs_escape(e["slug"])}",',
            f'            DroidType = "{cs_escape(e["droid_type"])}",',
            f'            Manufacturer = "{cs_escape(e["manufacturer"])}",',
            f'            Description = "{cs_escape(e["description"])}",',
            f'            Color = "{cs_escape(e["color"])}",',
            f'            Sources = "{cs_escape(e["sources"])}",',
            "        },",
        ])
    lines.extend([
        "    ];",
        "",
        "    public static Droid? GetBySlug(string slug) =>",
        "        Droids.FirstOrDefault(d => d.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));",
        "}",
        "",
    ])
    DROID_CS.write_text("\n".join(lines))


def main() -> None:
    from droid_catalog_data import DROIDS

    DROID_PROFILES.mkdir(parents=True, exist_ok=True)

    write_droid_cs(DROIDS)

    for entry in DROIDS:
        slug = entry["slug"]
        (DROID_PROFILES / f"{slug}.json").write_text(
            json.dumps(build_droid_profile(entry), indent=2, ensure_ascii=False) + "\n"
        )

    print(f"Generated {len(DROIDS)} droid profiles and DroidData.cs")
    print("  Install cinematic PNG heroes: python3 scripts/install_droid_heroes.py")


if __name__ == "__main__":
    main()
