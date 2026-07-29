#!/usr/bin/env python3
"""Map directory entities and wars to Galactic History chronicle eras."""

from __future__ import annotations

import re
from typing import Any

from entity_associations import catalogue_text, inference_text, is_generic_profile, _chronicle_inference_text

CHRONICLES: dict[str, dict[str, str]] = {
    "dawn-of-the-jedi": {
        "name": "Dawn of the Jedi",
        "route": "chronicles/galactic-history/dawn-of-the-jedi",
    },
    "old-sith-empire": {
        "name": "Sith Empire",
        "route": "chronicles/galactic-history/old-sith-empire",
    },
    "old-republic": {
        "name": "Old Republic",
        "route": "chronicles/galactic-history/old-republic",
    },
    "high-republic": {
        "name": "High Republic",
        "route": "chronicles/galactic-history/high-republic",
    },
    "fall-of-the-republic": {
        "name": "Fall of the Republic",
        "route": "chronicles/galactic-history/fall-of-the-republic",
    },
    "reign-of-the-empire": {
        "name": "Reign of the Empire",
        "route": "chronicles/galactic-history/reign-of-the-empire",
    },
    "age-of-rebellion": {
        "name": "Age of Rebellion",
        "route": "chronicles/galactic-history/age-of-rebellion",
    },
    "new-republic": {
        "name": "New Republic",
        "route": "chronicles/galactic-history/new-republic",
    },
    "rise-of-the-first-order": {
        "name": "Rise of the First Order",
        "route": "chronicles/galactic-history/rise-of-the-first-order",
    },
    "new-jedi-order": {
        "name": "New Jedi Order",
        "route": "chronicles/galactic-history/new-jedi-order",
    },
}

WAR_TO_CHRONICLE: dict[str, str] = {
    "hundred-year-darkness": "dawn-of-the-jedi",
    "great-sith-war": "old-sith-empire",
    "stark-hyperspace-war": "old-sith-empire",
    "mandalorian-wars": "old-republic",
    "new-sith-wars": "old-republic",
    "great-galactic-war": "old-republic",
    "great-war": "old-republic",
    "clone-wars": "fall-of-the-republic",
    "galactic-civil-war": "age-of-rebellion",
    "cold-war": "rise-of-the-first-order",
}

SITH_ERA: dict[str, list[str]] = {
    "dawn-of-the-jedi": [],
    "old-sith-empire": [
        "ajunta-pall",
        "naga-sadow",
        "ludo-kressh",
        "marka-ragnos",
        "exar-kun",
        "freedon-nadd",
        "tulak-hord",
        "darth-vitiate",
        "ulic-qel-droma",
    ],
    "old-republic": [
        "darth-revan",
        "darth-malak",
        "darth-nihilus",
        "darth-sion",
        "darth-traya",
        "darth-bane",
        "darth-zannah",
        "ulic-qel-droma",
        "darth-malgus",
        "darth-bandon",
    ],
    "fall-of-the-republic": [
        "darth-sidious",
        "darth-tyranus",
        "darth-maul",
        "darth-plagueis",
        "savage-opress",
        "asajj-ventress",
        "pong-krell",
        "barriss-offee",
    ],
    "reign-of-the-empire": [
        "darth-vader",
        "grand-inquisitor",
        "second-sister",
        "fifth-brother",
        "sixth-brother",
        "seventh-sister",
        "eighth-brother",
        "ninth-sister",
    ],
}

JEDI_ERA: dict[str, list[str]] = {
    "dawn-of-the-jedi": [],
    "old-republic": [
        "yoda",
        "bastila-shan",
        "jolee-bindo",
        "meetra-surik",
        "revan",
        "satele-shan",
    ],
    "high-republic": [
        "yaddle",
        "depa-billaba",
    ],
    "fall-of-the-republic": [
        "anakin-skywalker",
        "obi-wan-kenobi",
        "ahsoka-tano",
        "mace-windu",
        "yoda",
        "qui-gon-jinn",
        "kit-fisto",
        "plo-koon",
        "shaak-ti",
        "luminara-unduli",
        "aayla-secura",
        "adi-gallia",
        "agen-kolar",
        "bolla-ropal",
        "ima-gun-di",
        "nahdar-vebb",
        "quinlan-vos",
        "tera-sinube",
        "depa-billaba",
        "ki-adi-mundi",
        "saesee-tiin",
        "eeth-koth",
        "even-piell",
        "oppo-rancisis",
        "coleman-trebor",
        "coleman-kcaj",
        "stass-allie",
        "cin-drallig",
        "jocasta-nu",
        "sifo-dyas",
        "barriss-offee",
        "tiplee",
        "tiplar",
        "petro",
        "katooni",
        "gungi",
        "byph",
        "ganodi",
        "zatt",
        "kelleran-beq",
    ],
    "reign-of-the-empire": [
        "kanan-jarrus",
        "ezra-bridger",
        "cal-kestis",
        "cere-junda",
    ],
    "age-of-rebellion": [
        "luke-skywalker",
        "obi-wan-kenobi",
        "yoda",
    ],
    "new-republic": [
        "luke-skywalker",
    ],
    "new-jedi-order": [
        "luke-skywalker",
        "grogu",
        "kanan-jarrus",
        "ezra-bridger",
    ],
}

ENTITY_OVERRIDES: dict[tuple[str, str], list[str]] = {
    ("characters", "rey"): ["rise-of-the-first-order", "new-jedi-order"],
    ("characters", "finn"): ["rise-of-the-first-order", "new-jedi-order"],
    ("characters", "poe-dameron"): ["rise-of-the-first-order", "new-jedi-order"],
    ("characters", "han-solo"): ["age-of-rebellion", "new-republic"],
    ("characters", "leia-organa"): ["age-of-rebellion", "new-republic", "new-jedi-order"],
    ("characters", "chewbacca"): ["age-of-rebellion", "new-republic"],
    ("characters", "luke-skywalker"): ["age-of-rebellion", "new-republic", "new-jedi-order"],
    ("characters", "darth-vader"): ["fall-of-the-republic", "reign-of-the-empire", "age-of-rebellion"],
    ("sith", "darth-sidious"): ["fall-of-the-republic", "reign-of-the-empire", "rise-of-the-first-order"],
    ("sith", "darth-vader"): ["fall-of-the-republic", "reign-of-the-empire", "age-of-rebellion"],
    ("sith", "darth-revan"): ["old-republic"],
    ("sith", "darth-malgus"): ["old-republic"],
    ("sith", "darth-vitiate"): ["old-sith-empire"],
    ("jedi", "bastila-shan"): ["old-republic"],
    ("jedi", "jolee-bindo"): ["old-republic"],
    ("jedi", "meetra-surik"): ["old-republic"],
    ("jedi", "revan"): ["old-republic"],
    ("jedi", "satele-shan"): ["old-republic"],
    ("characters", "palpatine"): ["fall-of-the-republic", "reign-of-the-empire", "rise-of-the-first-order"],
    ("characters", "grand-moff-tarkin"): ["reign-of-the-empire", "age-of-rebellion"],
    ("characters", "mon-mothma"): ["fall-of-the-republic", "age-of-rebellion", "new-republic"],
    ("characters", "general-grievous"): ["fall-of-the-republic"],
    ("characters", "hk-47"): ["old-republic"],
    ("characters", "maz-kanata"): ["new-republic", "rise-of-the-first-order"],
    ("characters", "din-djarin"): ["new-republic", "new-jedi-order"],
    ("characters", "grogu"): ["new-jedi-order"],
    ("characters", "shmi-skywalker"): ["fall-of-the-republic"],
    ("characters", "c-3po"): ["fall-of-the-republic", "age-of-rebellion", "new-jedi-order"],
    ("bounty-hunters", "din-djarin"): ["new-republic", "new-jedi-order"],
    ("bounty-hunters", "boba-fett"): ["age-of-rebellion", "new-republic", "rise-of-the-first-order"],
    ("bounty-hunters", "jango-fett"): ["fall-of-the-republic"],
    ("bounty-hunters", "cad-bane"): ["fall-of-the-republic", "reign-of-the-empire"],
    ("bounty-hunters", "asajj-ventress"): ["fall-of-the-republic"],
    ("droids", "r2-d2"): ["fall-of-the-republic", "age-of-rebellion", "new-jedi-order"],
    ("droids", "c-3po"): ["fall-of-the-republic", "age-of-rebellion", "new-jedi-order"],
    ("droids", "bb-8"): ["rise-of-the-first-order", "new-jedi-order"],
    ("droids", "hk-47"): ["old-republic"],
    ("droids", "bd-1"): ["reign-of-the-empire", "new-jedi-order"],
    ("droids", "k-2so"): ["reign-of-the-empire", "age-of-rebellion"],
}

PLANET_CHRONICLES: dict[str, list[str]] = {
    "tython": ["dawn-of-the-jedi"],
    "korriban": ["dawn-of-the-jedi", "old-sith-empire", "old-republic"],
    "ossus": ["dawn-of-the-jedi", "old-sith-empire"],
    "ziost": ["old-sith-empire", "old-republic"],
    "rakata-prime": ["dawn-of-the-jedi"],
    "dromund-kaas": ["old-sith-empire", "old-republic"],
    "taris": ["old-republic"],
    "telos": ["old-republic"],
    "malachor-v": ["old-republic"],
    "dxun": ["old-republic"],
    "ruusan": ["old-republic"],
    "manaan": ["old-republic"],
    "coruscant": [
        "old-republic",
        "high-republic",
        "fall-of-the-republic",
        "reign-of-the-empire",
        "new-republic",
    ],
    "naboo": ["high-republic", "fall-of-the-republic"],
    "geonosis": ["fall-of-the-republic"],
    "mustafar": ["fall-of-the-republic", "reign-of-the-empire"],
    "kashyyyk": ["fall-of-the-republic", "reign-of-the-empire"],
    "utapau": ["fall-of-the-republic"],
    "lothal": ["reign-of-the-empire"],
    "malachor": ["reign-of-the-empire"],
    "ilum": ["reign-of-the-empire", "rise-of-the-first-order"],
    "jedha": ["reign-of-the-empire", "age-of-rebellion"],
    "yavin-4": ["age-of-rebellion"],
    "hoth": ["age-of-rebellion"],
    "endor": ["age-of-rebellion"],
    "bespin": ["age-of-rebellion"],
    "scarif": ["age-of-rebellion"],
    "dagobah": ["age-of-rebellion", "new-jedi-order"],
    "jakku": ["new-republic"],
    "hosnian-prime": ["new-republic", "rise-of-the-first-order"],
    "takodana": ["new-republic", "rise-of-the-first-order"],
    "ahch-to": ["new-republic", "new-jedi-order"],
    "starkiller-base": ["rise-of-the-first-order"],
    "crait": ["rise-of-the-first-order"],
    "exegol": ["rise-of-the-first-order", "new-jedi-order"],
    "d-qar": ["rise-of-the-first-order"],
    "tatooine": [
        "fall-of-the-republic",
        "reign-of-the-empire",
        "age-of-rebellion",
        "new-jedi-order",
    ],
}

TEXT_ERA_RULES: list[tuple[str, str]] = [
    ("je'daii", "dawn-of-the-jedi"),
    ("jedaii", "dawn-of-the-jedi"),
    ("tho yor", "dawn-of-the-jedi"),
    ("hundred-year darkness", "dawn-of-the-jedi"),
    ("naga sadow", "old-sith-empire"),
    ("exar kun", "old-sith-empire"),
    ("great hyperspace war", "old-sith-empire"),
    ("marka ragnos", "old-sith-empire"),
    ("kotor", "old-republic"),
    ("knights of the old republic", "old-republic"),
    ("old republic mmo", "old-republic"),
    ("the old republic", "old-republic"),
    ("great galactic war", "old-republic"),
    ("sacking of coruscant", "old-republic"),
    ("mandalorian wars", "old-republic"),
    ("jedi civil war", "old-republic"),
    ("darth revan", "old-republic"),
    ("darth malgus", "old-republic"),
    ("ruusan", "old-republic"),
    ("darth bane", "old-republic"),
    ("rule of two", "old-republic"),
    ("high republic", "high-republic"),
    ("starlight beacon", "high-republic"),
    ("nihil", "high-republic"),
    ("clone wars", "fall-of-the-republic"),
    ("order 66", "fall-of-the-republic"),
    ("separatist", "fall-of-the-republic"),
    ("prequel", "fall-of-the-republic"),
    ("galactic empire", "reign-of-the-empire"),
    ("imperial era", "reign-of-the-empire"),
    ("inquisitor", "reign-of-the-empire"),
    ("death star", "reign-of-the-empire"),
    ("rebel alliance", "age-of-rebellion"),
    ("galactic civil war", "age-of-rebellion"),
    ("original trilogy", "age-of-rebellion"),
    ("battle of yavin", "age-of-rebellion"),
    ("battle of hoth", "age-of-rebellion"),
    ("battle of endor", "age-of-rebellion"),
    ("new republic", "new-republic"),
    ("aftermath", "new-republic"),
    ("the mandalorian", "new-republic"),
    ("mandalorian civil war", "new-republic"),
    ("first order", "rise-of-the-first-order"),
    ("resistance", "rise-of-the-first-order"),
    ("starkiller base", "rise-of-the-first-order"),
    ("sequel trilogy", "rise-of-the-first-order"),
    ("luke's academy", "new-jedi-order"),
    ("new jedi order era", "new-jedi-order"),
]

SHIP_ERA_RULES: list[tuple[str, str]] = [
    ("old republic", "old-republic"),
    ("sith empire", "old-sith-empire"),
    ("clone wars", "fall-of-the-republic"),
    ("imperial era", "reign-of-the-empire"),
    ("galactic civil war", "age-of-rebellion"),
    ("first order", "rise-of-the-first-order"),
    ("resistance", "rise-of-the-first-order"),
    ("high republic", "high-republic"),
]

MAX_CHRONICLE_LINKS = 8


def _norm(value: str) -> str:
    value = value.lower()
    value = re.sub(r"'s\b", "", value)
    value = value.replace("'", "").replace("'", "")
    value = value.replace("-", " ")
    value = re.sub(r"[^a-z0-9\s]", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def _build_chronicle_era_index(era_map: dict[str, list[str]]) -> dict[str, list[str]]:
    index: dict[str, list[str]] = {}
    for era, slugs in era_map.items():
        for slug in slugs:
            index.setdefault(slug, [])
            if era not in index[slug]:
                index[slug].append(era)
    return index


SITH_CHRONICLE_ERAS = _build_chronicle_era_index(SITH_ERA)
JEDI_CHRONICLE_ERAS = _build_chronicle_era_index(JEDI_ERA)


def _match_text_eras(text: str) -> list[str]:
    matched: list[str] = []
    seen: set[str] = set()
    for phrase, era in sorted(TEXT_ERA_RULES, key=lambda item: -len(item[0])):
        if phrase in text and era not in seen:
            matched.append(era)
            seen.add(era)
    return matched


def _match_ship_era(era_text: str) -> list[str]:
    text = _norm(era_text)
    matched: list[str] = []
    seen: set[str] = set()
    for phrase, era in SHIP_ERA_RULES:
        if phrase in text and era not in seen:
            matched.append(era)
            seen.add(era)
    if "rebellion" in text and "galactic civil war" not in text:
        if "age-of-rebellion" not in seen:
            matched.append("age-of-rebellion")
    return matched


def _slug_eras(category: str, slug: str) -> list[str]:
    if category == "sith":
        return list(SITH_CHRONICLE_ERAS.get(slug, []))
    if category == "jedi":
        return list(JEDI_CHRONICLE_ERAS.get(slug, []))
    return []


def match_chronicle_slugs(
    category: str,
    slug: str,
    entry: dict[str, str],
    profile: dict[str, Any],
    *,
    war_slugs: list[str] | None = None,
    ship_era: str = "",
) -> list[str]:
    """Return chronicle era slugs for a directory entity, ordered by relevance."""
    war_slugs = war_slugs or []
    results: list[str] = []
    seen: set[str] = set()

    def add(era_slug: str) -> None:
        if era_slug and era_slug not in seen and era_slug in CHRONICLES:
            results.append(era_slug)
            seen.add(era_slug)

    override = ENTITY_OVERRIDES.get((category, slug))
    if override:
        for era_slug in override:
            add(era_slug)
        return results[:MAX_CHRONICLE_LINKS]

    slug_eras = _slug_eras(category, slug)
    for era_slug in slug_eras:
        add(era_slug)

    if category == "planets":
        for era_slug in PLANET_CHRONICLES.get(slug, []):
            add(era_slug)

    for war_slug in war_slugs:
        add(WAR_TO_CHRONICLE.get(war_slug, ""))

    if category in {"sith", "jedi"} and slug_eras:
        if ship_era:
            for era_slug in _match_ship_era(ship_era):
                add(era_slug)
        return results[:MAX_CHRONICLE_LINKS]

    text = _chronicle_inference_text(profile, entry)
    for era_slug in _match_text_eras(text):
        add(era_slug)

    if ship_era:
        for era_slug in _match_ship_era(ship_era):
            add(era_slug)

    return results[:MAX_CHRONICLE_LINKS]


def chronicle_links_for_war(war_slug: str) -> list[tuple[str, str, str]]:
    era_slug = WAR_TO_CHRONICLE.get(war_slug)
    if not era_slug:
        return []
    era = CHRONICLES[era_slug]
    return [("Chronicle", era["name"], era["route"])]


def add_chronicle_links(
    builder: Any,
    links: list[dict[str, str]],
    seen: set[str],
    category: str,
    slug: str,
    entry: dict[str, str],
    profile: dict[str, Any],
    *,
    war_slugs: list[str] | None = None,
    ship_era: str = "",
) -> None:
    for era_slug in match_chronicle_slugs(
        category,
        slug,
        entry,
        profile,
        war_slugs=war_slugs,
        ship_era=ship_era,
    ):
        era = CHRONICLES[era_slug]
        builder.add_link(links, seen, "Chronicle", era["name"], era["route"])


def finalize_links(links: list[dict[str, str]], max_archive: int = 24) -> list[dict[str, str]]:
    archive = [link for link in links if link["label"] != "Chronicle"][:max_archive]
    chronicle = [link for link in links if link["label"] == "Chronicle"][:MAX_CHRONICLE_LINKS]
    return archive + chronicle
