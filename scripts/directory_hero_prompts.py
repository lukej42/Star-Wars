#!/usr/bin/env python3
"""Cinematic hero-banner prompts for directory entries (Jedi, Sith, Ships, etc.)."""

from __future__ import annotations

import re

from hero_prompt_overrides import OVERRIDES
from parse_csharp_data import all_directory_entries

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks."
)

# Strip long proper-name chains from descriptions for safer generation prompts
NAME_PATTERNS = [
    r"Obi-Wan Kenobi",
    r"Anakin Skywalker",
    r"Luke Skywalker",
    r"Darth Vader",
    r"Emperor Palpatine",
    r"General Grievous",
    r"Mace Windu",
    r"Yoda",
]


def _trim_description(desc: str, max_len: int = 180) -> str:
    text = desc.strip()
    if len(text) > max_len:
        cut = text[:max_len].rsplit(" ", 1)[0]
        text = cut + "…"
    return text


def _jedi_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["jedi"]:
        return OVERRIDES["jedi"][slug]
    rank = entry.get("rank", "Jedi")
    desc = _trim_description(entry.get("description", ""))
    return (
        f"A {rank} in flowing Jedi robes with glowing blue or green lightsaber, "
        f"{desc}. Ancient temple pillars or Clone Wars battlefield backdrop, heroic cinematic framing"
    )


def _sith_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["sith"]:
        return OVERRIDES["sith"][slug]
    title = entry.get("title", "Sith Lord")
    desc = _trim_description(entry.get("description", ""))
    return (
        f"A {title} in dark robes with crimson lightsaber and subtle dark side aura, "
        f"{desc}. Sith temple, throne room, or volcanic battlefield with ominous red-black lighting"
    )


def _ship_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["ships"]:
        return OVERRIDES["ships"][slug]
    name = entry.get("name", "starship")
    ship_class = entry.get("class", "vessel")
    era = entry.get("era", "")
    desc = _trim_description(entry.get("description", ""))
    return (
        f"Cinematic profile of the {name}, a {ship_class}, {desc}. "
        f"{'Era: ' + era + '. ' if era else ''}"
        f"In deep space combat deployment or hangar bay with engine glow and starfield depth"
    )


def _species_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["species"]:
        return OVERRIDES["species"][slug]
    name = entry.get("name", "alien species")
    homeworld = entry.get("homeworld", "a distant world")
    classification = entry.get("classification", "sentient species")
    desc = _trim_description(entry.get("description", ""))
    return (
        f"Group portrait of {name} beings, a {classification} from {homeworld}, {desc}. "
        f"Homeworld environment with native architecture or landscape, warm cinematic lighting"
    )


def _bounty_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["bounty-hunters"]:
        return OVERRIDES["bounty-hunters"][slug]
    specialty = entry.get("specialty", "bounty hunter")
    homeworld = entry.get("homeworld", "the Outer Rim")
    desc = _trim_description(entry.get("description", ""))
    return (
        f"A dangerous {specialty} bounty hunter from {homeworld}, armored silhouette with weapons, "
        f"{desc}. Smoky cantina, docking bay, or desert outpost with wanted holo screens"
    )


def _settlement_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["settlements"]:
        return OVERRIDES["settlements"][slug]
    name = entry.get("name", "settlement")
    planet = entry.get("planet", "a planet")
    stype = entry.get("settlementType", "city")
    desc = _trim_description(entry.get("description", ""))
    return (
        f"Aerial cinematic view of {name}, a {stype} on {planet}, {desc}. "
        f"Busy streets, landing platforms, and distinctive local architecture under dramatic sky"
    )


def _force_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in OVERRIDES["force-powers"]:
        return OVERRIDES["force-powers"][slug]
    name = entry.get("name", "Force ability")
    category = entry.get("category", "Force technique")
    side = entry.get("side", "light")
    desc = _trim_description(entry.get("description", ""))
    palette = (
        "golden and azure light side energy"
        if side == "light"
        else "crimson and violet dark side energy"
    )
    return (
        f"Cinematic visualization of {name}, a {category} Force power, {desc}. "
        f"Swirling {palette}, dramatic figure silhouette, abstract Force distortion effects"
    )


BUILDERS = {
    "jedi": _jedi_prompt,
    "sith": _sith_prompt,
    "ships": _ship_prompt,
    "species": _species_prompt,
    "bounty-hunters": _bounty_prompt,
    "settlements": _settlement_prompt,
    "force-powers": _force_prompt,
}


def prompt_for(category: str, entry: dict[str, str]) -> str:
    builder = BUILDERS[category]
    scene = builder(entry)
    return f"{scene}. {STYLE_SUFFIX}"


def all_prompts() -> dict[str, dict[str, str]]:
    entries = all_directory_entries()
    return {
        category: {e["slug"]: prompt_for(category, e) for e in items}
        for category, items in entries.items()
    }


def main() -> None:
    prompts = all_prompts()
    total = sum(len(v) for v in prompts.values())
    overrides = sum(
        1
        for cat, items in prompts.items()
        for slug in items
        if slug in OVERRIDES.get(cat, {})
    )
    print(f"Generated {total} hero prompts ({overrides} hand-crafted overrides)")
    for cat, items in prompts.items():
        print(f"  {cat}: {len(items)}")


if __name__ == "__main__":
    main()
