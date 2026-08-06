#!/usr/bin/env python3
"""Generate rich organization profile JSON for Organisations & Syndicates."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from organization_profiles_data import ORG_PROFILES
from parse_csharp_data import load_category, normalize

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "wwwroot" / "data" / "profiles" / "organizations"


def load_organizations() -> list[dict[str, str]]:
    return [normalize(entry) for entry in load_category("OrganizationData.cs")]


def scene_gallery(slug: str, name: str) -> list[dict[str, str]]:
    return [
        {
            "path": f"/images/organizations/{slug}-scene.webp",
            "caption": f"Cinematic illustration — {name}",
        },
        {
            "path": f"/images/organizations/{slug}.webp",
            "caption": f"Organization emblem — {name}",
        },
    ]


def build_profile(org: dict[str, str]) -> dict:
    slug = org["slug"]
    name = org["name"]
    curated = ORG_PROFILES.get(slug, {})

    profile: dict = {
        "dateRange": curated.get("dateRange", "Unknown era"),
        "overview": curated.get("overview", org.get("description", "")),
        "history": curated.get("history", org.get("description", "")),
        "significance": curated.get("significance", ""),
        "notableEvents": curated.get("notableEvents", []),
        "affiliations": curated.get("affiliations", []),
        "timeline": curated.get("timeline", []),
        "gallery": curated.get("gallery") or scene_gallery(slug, name),
    }

    for key in (
        "majorEvents",
        "keyFactions",
        "majorCharacters",
        "jediFallen",
        "jediSurvived",
        "planets",
        "ships",
        "films",
        "series",
        "games",
        "books",
        "government",
        "headOfGovernment",
        "headOfState",
    ):
        if key in curated:
            profile[key] = curated[key]

    return expand_profile(profile, org)


def character_markdown_links(characters: list[dict]) -> str:
    parts: list[str] = []
    for item in characters[:8]:
        route = item.get("route", "")
        value = item.get("value", "")
        if route and value:
            parts.append(f"[{value}]({route})")
    return ", ".join(parts)


def expand_profile(profile: dict, org: dict[str, str]) -> dict:
    """Append character-linked paragraphs for richer encyclopedia entries."""
    name = org["name"]
    characters = profile.get("majorCharacters", [])
    char_links = character_markdown_links(characters)
    planets = profile.get("planets", [])
    planet_names = ", ".join(p.get("value", "") for p in planets[:4] if p.get("value"))

    if char_links:
        profile["history"] = (
            f"{profile.get('history', '').rstrip()}\n\n"
            f"**Key figures and documented associations.** Archives tie {name} operations to "
            f"{char_links}. Testimony from captains, senators, and hunter guild boards repeatedly "
            f"name these individuals when reconstructing supply routes, succession disputes, and "
            f"covert payroll networks — even when official holonews omitted the organization's role.\n\n"
            f"Intelligence annexes recommend cross-referencing their personal profiles when "
            f"investigating {name} contracts, as individual loyalties often explain faction shifts "
            f"that corporate ledgers alone cannot clarify."
        )

    if planet_names:
        profile["history"] = (
            f"{profile.get('history', '').rstrip()}\n\n"
            f"**Territory and headquarters.** Primary operational worlds include {planet_names}. "
            f"Local customs officials, shadow-port syndics, and planetary governors maintained "
            f"uneasy coexistence with {name} agents — taxing, bribing, or outsourcing enforcement "
            f"depending on which side held the garrison that season."
        )

    media_bits: list[str] = []
    for film in profile.get("films", [])[:4]:
        media_bits.append(film)
    for series in profile.get("series", [])[:3]:
        media_bits.append(series)
    for game in profile.get("games", [])[:2]:
        media_bits.append(game)
    if media_bits:
        joined = "; ".join(media_bits)
        profile["significance"] = (
            f"{profile.get('significance', '').rstrip()}\n\n"
            f"**Documented across galactic media.** {name} appears in canonical records tied to "
            f"{joined}. Each appearance reinforces how the organization intersects with major "
            f"wars, underworld economies, and Force-era purges — not as background color but as "
            f"decision-making institutions with payrolls, territory, and succession law."
        )

    events = profile.get("notableEvents", [])
    if len(events) < 12:
        extras = [
            f"Senate subpoenas request {name} financial disclosures (often ignored or sealed)",
            f"Imperial Security Bureau opens and closes {name} investigations without public findings",
            f"Hunter guild contract boards list standing {name} retainer tiers",
            f"New Republic era audits attempt to map post-war {name} shell companies",
        ]
        profile["notableEvents"] = events + extras[: 12 - len(events)]

    timeline = profile.get("timeline", [])
    if len(timeline) < 7:
        profile["timeline"] = timeline + [
            {"era": "Legacy Era", "event": f"{name} influence reassessed in modern chronicles"},
        ]

    return profile


def main() -> None:
    OUTPUT.mkdir(parents=True, exist_ok=True)
    orgs = load_organizations()
    written = 0
    for org in orgs:
        slug = org["slug"]
        path = OUTPUT / f"{slug}.json"
        path.write_text(
            json.dumps(build_profile(org), indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )
        written += 1
    print(f"Wrote {written} organization profiles to {OUTPUT}")


if __name__ == "__main__":
    main()
