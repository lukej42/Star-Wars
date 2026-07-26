#!/usr/bin/env python3
"""Cinematic hero prompts for The Force and Wars & Conflicts pages."""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"

from wars_conflicts_hero_scenes import battle_prompt, war_prompt

STYLE_SUFFIX = (
    "Photorealistic cinematic Star Wars live-action film still hero banner, 1536x1024, 16:9. "
    "Hyper-realistic practical effects quality matching all nine saga films, Clone Wars, Rebels, "
    "The Mandalorian, Knights of the Old Republic, and Old Sith Empire visuals. "
    "Film grain, dramatic rim lighting, IMAX composition. "
    "No text, no logos, no watermarks, no readable lettering."
)

FORCE_SCENES: dict[str, str] = {
    "conflict-between-light-and-dark-side": (
        "Split cosmic vista with serene blue light-side energy on one half and crimson dark-side "
        "lightning on the other, two hooded Force wielders facing across a misty temple divide"
    ),
    "lightsaber-forms": (
        "Seven distinct lightsaber blade colors arcing through an ancient Jedi training chamber "
        "with holographic combat stances and stone pillars"
    ),
    "kyber-crystals": (
        "Glowing kyber crystals in blue, green, and bleeding red emerging from a sacred cavern "
        "with refracted light beams and temple carvings"
    ),
    "force-creatures": (
        "Convor owls, loth-wolves, and purrgil whales drifting through a mystical Force nexus "
        "above a purple nebula and ancient world"
    ),
    "jedi-code": (
        "A serene light-side Jedi meditating in robes on a cliff at dawn, an ancient holocron "
        "book floating in the air before them surrounded by a soft blue Force aura and distant stars"
    ),
    "sith-code": (
        "A hooded dark-side adept meditating in a Sith shrine, an ancient tome floating in the air "
        "before them wreathed in a crimson Force aura, obsidian pillars and red lightning mist"
    ),
    "force-philosophy": (
        "Jedi and Sith holocrons floating in a starlit archive chamber with golden and violet "
        "energy streams weaving between ancient manuscripts"
    ),
    "ancient-force-orders": (
        "Ruins of Je'daii, Dai Bendu, and Guardians of the Whills temples on forgotten worlds "
        "connected by luminous Force ley lines across space"
    ),
}

FORM_SCENES: dict[str, str] = {
    "shii-cho": "Jedi training in Form I with wide sweeping lightsaber arcs against multiple training remotes in a sunlit courtyard",
    "makashi": "Elegant Form II duel between two lightsaber wielders on a Naboo plaza with precise footwork and formal posture",
    "soresu": "Form III defensive stance deflecting a barrage of blaster bolts behind a tight lightsaber guard in a bunker corridor",
    "ataru": "Acrobatic Form IV practitioner leaping between temple pillars with a green lightsaber trail in moonlight",
    "shien-djem-so": "Form V warrior redirecting blaster fire then delivering a powerful counter-strike on a volcanic battlefield",
    "niman": "Form VI balanced duelist blending lightsaber strikes with Force push in a diplomatic embassy hall",
    "juyo-vaapad": "Ferocious Form VII whirlwind of purple and red lightsaber energy in a storm-lashed arena",
}


@dataclass(frozen=True)
class HeroEntry:
    category: str
    slug: str
    name: str
    color: str
    output: Path
    prompt: str


def _parse_force_topics() -> list[HeroEntry]:
    text = (DATA / "TheForceTopicData.cs").read_text(encoding="utf-8")
    entries: list[HeroEntry] = []
    conflict = re.search(
        r'ConflictBetweenLightAndDark\s*=\s*new\(\)\s*\{.*?Slug\s*=\s*"([^"]+)".*?Name\s*=\s*"([^"]+)".*?Color\s*=\s*"([^"]+)"',
        text,
        re.DOTALL,
    )
    if conflict:
        slug, name, color = conflict.groups()
        entries.append(_force_entry(slug, name, color))
    for match in re.finditer(
        r'Name\s*=\s*"([^"]+)".*?Slug\s*=\s*"([^"]+)".*?Color\s*=\s*"([^"]+)"',
        text.split("Topics { get; }")[1] if "Topics { get; }" in text else text,
        re.DOTALL,
    ):
        name, slug, color = match.groups()
        if slug == "lightsaber-forms":
            entries.append(_force_entry(slug, name, color))
            continue
        entries.append(_force_entry(slug, name, color))
    return entries


def _force_entry(slug: str, name: str, color: str) -> HeroEntry:
    scene = FORCE_SCENES.get(
        slug,
        f"Cinematic establishing shot representing {name} in the Star Wars galaxy",
    )
    return HeroEntry(
        category="the-force",
        slug=slug,
        name=name,
        color=color,
        output=ROOT / "wwwroot" / "images" / "the-force" / f"{slug}-hero.webp",
        prompt=f"{scene}. {STYLE_SUFFIX}",
    )


def _parse_lightsaber_forms() -> list[HeroEntry]:
    text = (DATA / "LightsaberFormData.cs").read_text(encoding="utf-8")
    entries: list[HeroEntry] = []
    for match in re.finditer(
        r'Name\s*=\s*"([^"]+)".*?Slug\s*=\s*"([^"]+)".*?Color\s*=\s*"([^"]+)"',
        text,
        re.DOTALL,
    ):
        name, slug, color = match.groups()
        scene = FORM_SCENES.get(slug, f"Cinematic lightsaber duel illustrating {name}")
        entries.append(
            HeroEntry(
                category="lightsaber-form",
                slug=slug,
                name=name,
                color=color,
                output=ROOT / "wwwroot" / "images" / "the-force" / "lightsaber-forms" / f"{slug}-hero.webp",
                prompt=f"{scene}. {STYLE_SUFFIX}",
            )
        )
    return entries


def _parse_wars() -> list[HeroEntry]:
    text = (DATA / "WarConflictData.cs").read_text(encoding="utf-8")
    entries: list[HeroEntry] = []
    for match in re.finditer(
        r'Name\s*=\s*"([^"]+)".*?Slug\s*=\s*"([^"]+)".*?Color\s*=\s*"([^"]+)"',
        text,
        re.DOTALL,
    ):
        name, slug, color = match.groups()
        entries.append(
            HeroEntry(
                category="war",
                slug=slug,
                name=name,
                color=color,
                output=ROOT / "wwwroot" / "images" / "wars-conflicts" / f"{slug}-hero.webp",
                prompt=war_prompt(name, slug),
            )
        )
    return entries


def _parse_battles() -> list[HeroEntry]:
    text = (DATA / "BattleData.cs").read_text(encoding="utf-8")
    entries: list[HeroEntry] = []
    for match in re.finditer(
        r'Battle\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)"\)',
        text,
    ):
        war_slug, slug, name, era, color = match.groups()
        entries.append(
            HeroEntry(
                category="battle",
                slug=slug,
                name=name,
                color=color,
                output=ROOT / "wwwroot" / "images" / "wars-conflicts" / "battles" / f"{slug}-hero.webp",
                prompt=battle_prompt(name, slug, era, war_slug),
            )
        )
    return entries


def all_hero_entries() -> list[HeroEntry]:
    return _parse_force_topics() + _parse_lightsaber_forms() + _parse_wars() + _parse_battles()


if __name__ == "__main__":
    entries = all_hero_entries()
    print(f"Force/Wars hero entries: {len(entries)}")
