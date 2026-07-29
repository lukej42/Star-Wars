#!/usr/bin/env python3
"""Curated and rule-based entity → faction/chronicle associations for cross-links."""

from __future__ import annotations

import re
from typing import Any

GENERIC_PROFILE_MARKERS = (
    "In contemporary chronicles",
    "modern galactic politics",
    "the fall of old institutions",
    "galactic institutions fracture",
    "invites new generations to question what duty demands",
)

# Longest phrases first. Each entry: (route, display name, phrases).
FACTION_PHRASES: list[tuple[str, str, tuple[str, ...]]] = [
    ("factions/sith-empire", "Sith Empire", ("reconstituted sith empire", "old sith empire", "sith empire")),
    ("factions/new-republic", "New Republic", ("new republic",)),
    (
        "factions/rebel-alliance",
        "Rebel Alliance",
        ("rebel alliance", "alliance to restore the republic"),
    ),
    ("factions/trade-federation", "Trade Federation", ("trade federation",)),
    ("factions/first-order", "First Order", ("first order",)),
    ("factions/resistance", "Resistance", ("resistance",)),
    (
        "factions/confederacy",
        "Confederacy",
        (
            "confederacy of independent systems",
            "separatist alliance",
            "separatist council",
            "confederacy",
            "separatist",
        ),
    ),
    ("factions/mandalorians", "Mandalorians", ("mandalorian", "mandalorians")),
    ("factions/hutts", "Hutts", ("hutt cartel", "hutt clan", "hutt syndicate", "hutt")),
    ("factions/republic", "Republic", ("galactic republic",)),
    (
        "factions/empire",
        "Empire",
        ("galactic empire", "imperial navy", "imperial army", "imperial era", "stormtrooper corps"),
    ),
]

OLD_SITH_EMPIRE_SLUGS = {
    "ajunta-pall",
    "naga-sadow",
    "ludo-kressh",
    "marka-ragnos",
    "exar-kun",
    "freedon-nadd",
    "tulak-hord",
}

OLD_REPUBLIC_SITH_SLUGS = {
    "darth-revan",
    "darth-malak",
    "darth-nihilus",
    "darth-sion",
    "darth-traya",
    "darth-bane",
    "darth-zannah",
    "ulic-qel-droma",
    "darth-vitiate",
    "darth-malgus",
    "darth-bandon",
}

FALL_REPUBLIC_SITH_FACTIONS: dict[str, list[str]] = {
    "darth-sidious": ["republic", "confederacy", "empire", "trade-federation"],
    "darth-tyranus": ["confederacy"],
    "darth-maul": ["confederacy"],
    "darth-plagueis": ["republic"],
    "savage-opress": ["confederacy"],
    "asajj-ventress": ["confederacy"],
    "barriss-offee": ["republic"],
    "pong-krell": ["republic"],
}

REIGN_EMPIRE_SITH_SLUGS = {
    "darth-vader",
    "grand-inquisitor",
    "second-sister",
    "fifth-brother",
    "sixth-brother",
    "seventh-sister",
    "eighth-brother",
    "ninth-sister",
}

ENTITY_FACTION_OVERRIDES: dict[tuple[str, str], list[str]] = {
    ("characters", "palpatine"): ["republic", "confederacy", "empire"],
    ("characters", "darth-vader"): ["empire"],
    ("characters", "anakin-skywalker"): ["republic", "empire"],
    ("characters", "luke-skywalker"): ["rebel-alliance", "new-republic"],
    ("characters", "leia-organa"): ["rebel-alliance", "new-republic"],
    ("characters", "han-solo"): ["rebel-alliance", "new-republic"],
    ("characters", "chewbacca"): ["rebel-alliance", "new-republic"],
    ("characters", "mon-mothma"): ["republic", "rebel-alliance", "new-republic"],
    ("characters", "general-grievous"): ["confederacy"],
    ("characters", "count-dooku"): ["confederacy"],
    ("characters", "finn"): ["resistance", "first-order"],
    ("characters", "rey"): ["resistance"],
    ("characters", "poe-dameron"): ["resistance", "new-republic"],
    ("characters", "kylo-ren"): ["first-order"],
    ("characters", "general-hux"): ["first-order"],
    ("characters", "captain-phasma"): ["first-order"],
    ("characters", "mace-windu"): ["republic"],
    ("characters", "obi-wan-kenobi"): ["republic", "rebel-alliance"],
    ("characters", "padme-amidala"): ["republic"],
    ("characters", "bail-organa"): ["republic", "rebel-alliance"],
    ("characters", "jar-jar-binks"): ["republic"],
    ("characters", "grand-moff-tarkin"): ["empire"],
    ("characters", "wilhuff-tarkin"): ["empire"],
    ("characters", "hk-47"): ["sith-empire"],
    ("bounty-hunters", "jango-fett"): ["confederacy"],
    ("bounty-hunters", "cad-bane"): ["confederacy"],
    ("bounty-hunters", "asajj-ventress"): ["confederacy"],
    ("bounty-hunters", "boba-fett"): ["empire"],
    ("bounty-hunters", "ig-88"): ["empire"],
    ("droids", "r2-d2"): ["republic", "rebel-alliance"],
    ("characters", "c-3po"): ["republic", "rebel-alliance"],
    ("characters", "boba-fett"): ["empire"],
    ("droids", "hk-47"): ["sith-empire"],
    ("droids", "bb-8"): ["resistance"],
}


def _norm(value: str) -> str:
    value = value.lower()
    value = re.sub(r"'s\b", "", value)
    value = value.replace("'", "").replace("'", "")
    value = value.replace("-", " ")
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def is_generic_profile(profile: dict[str, Any]) -> bool:
    history = profile.get("history", "")
    if not history:
        return False
    return any(marker in history for marker in GENERIC_PROFILE_MARKERS)


def catalogue_text(entry: dict[str, str]) -> str:
    parts = [
        entry.get("name", ""),
        entry.get("description", ""),
        entry.get("role", ""),
        entry.get("title", ""),
        entry.get("rank", ""),
        entry.get("specialty", ""),
        entry.get("class", ""),
        entry.get("era", ""),
        entry.get("manufacturer", ""),
        entry.get("model", ""),
    ]
    return _norm(" ".join(str(part) for part in parts if part))


def inference_text(profile: dict[str, Any], entry: dict[str, str] | None = None) -> str:
    """Text safe for faction/chronicle inference — skips auto-generated boilerplate."""
    if entry and is_generic_profile(profile):
        return catalogue_text(entry)

    chunks = [
        profile.get("overview", ""),
        profile.get("history", ""),
        profile.get("significance", ""),
        " ".join(profile.get("notableEvents", [])),
        " ".join(profile.get("affiliations", [])),
    ]
    if entry:
        chunks.extend(
            [
                entry.get("description", ""),
                entry.get("role", ""),
                entry.get("rank", ""),
                entry.get("title", ""),
                entry.get("specialty", ""),
                entry.get("homeworld", ""),
                entry.get("class", ""),
                entry.get("era", ""),
            ]
        )
    return _norm(" ".join(str(chunk) for chunk in chunks if chunk))


def _contains_phrase(text: str, phrase: str) -> bool:
    if not phrase:
        return False
    padded = f" {text} "
    needle = f" {phrase} "
    return needle in padded


def _chronicle_inference_text(profile: dict[str, Any], entry: dict[str, str]) -> str:
    if is_generic_profile(profile):
        return catalogue_text(entry)
    parts = [
        entry.get("description", ""),
        entry.get("role", ""),
        entry.get("title", ""),
        profile.get("overview", ""),
        profile.get("history", ""),
        profile.get("significance", ""),
        " ".join(profile.get("affiliations", [])),
    ]
    return _norm(" ".join(str(part) for part in parts if part))


def match_factions_in_text(text: str) -> list[tuple[str, str, str]]:
    """Return (route, name, label) faction links found in text using phrase matching."""
    if not text:
        return []

    found: list[tuple[str, str, str]] = []
    seen_routes: set[str] = set()

    for route, name, phrases in sorted(FACTION_PHRASES, key=lambda item: -max(len(p) for p in item[2])):
        if route in seen_routes:
            continue
        for phrase in phrases:
            if not _contains_phrase(text, phrase):
                continue
            if route == "factions/empire" and _contains_phrase(text, "sith empire"):
                continue
            if route == "factions/republic" and _contains_phrase(text, "new republic"):
                continue
            found.append(("Faction", name, route))
            seen_routes.add(route)
            break

    return found


def _sith_faction_slugs(slug: str) -> list[str]:
    if slug in REIGN_EMPIRE_SITH_SLUGS:
        return ["empire"]
    if slug in FALL_REPUBLIC_SITH_FACTIONS:
        return FALL_REPUBLIC_SITH_FACTIONS[slug]
    if slug in OLD_SITH_EMPIRE_SLUGS or slug in OLD_REPUBLIC_SITH_SLUGS:
        return ["sith-empire"]
    return []


def _jedi_faction_slugs(slug: str, chronicle_eras: list[str]) -> list[str]:
    if slug in {"kanan-jarrus", "ezra-bridger", "cal-kestis", "cere-junda", "sabine-wren"}:
        return ["rebel-alliance"]
    if slug in {"luke-skywalker", "obi-wan-kenobi"} and "age-of-rebellion" in chronicle_eras:
        return ["rebel-alliance"]
    if any(era in chronicle_eras for era in ("fall-of-the-republic", "high-republic", "old-republic")):
        return ["republic"]
    return []


def _build_faction_links(faction_slugs: list[str]) -> list[tuple[str, str, str]]:
    slug_to_name = {
        "republic": "Republic",
        "empire": "Empire",
        "new-republic": "New Republic",
        "rebel-alliance": "Rebel Alliance",
        "confederacy": "Confederacy",
        "sith-empire": "Sith Empire",
        "first-order": "First Order",
        "resistance": "Resistance",
        "mandalorians": "Mandalorians",
        "hutts": "Hutts",
        "trade-federation": "Trade Federation",
    }
    results: list[tuple[str, str, str]] = []
    seen: set[str] = set()
    for faction_slug in faction_slugs:
        route = f"factions/{faction_slug}"
        if route in seen:
            continue
        name = slug_to_name.get(faction_slug, faction_slug.replace("-", " ").title())
        results.append(("Faction", name, route))
        seen.add(route)
    return results


def factions_for_entity(
    category: str,
    slug: str,
    entry: dict[str, str],
    profile: dict[str, Any],
    *,
    chronicle_eras: list[str] | None = None,
) -> list[tuple[str, str, str]]:
    """Return curated faction links for an entity."""
    chronicle_eras = chronicle_eras or []
    override = ENTITY_FACTION_OVERRIDES.get((category, slug))
    if override is not None:
        return _build_faction_links(override)

    if category == "sith":
        faction_slugs = _sith_faction_slugs(slug)
        if faction_slugs:
            return _build_faction_links(faction_slugs)

    if category == "jedi":
        faction_slugs = _jedi_faction_slugs(slug, chronicle_eras)
        if faction_slugs:
            return _build_faction_links(faction_slugs)

    text = catalogue_text(entry)
    return match_factions_in_text(text)
