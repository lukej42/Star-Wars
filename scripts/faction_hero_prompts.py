#!/usr/bin/env python3
"""Cinematic hero-banner prompts for Factions Directory entries."""

from __future__ import annotations

from parse_csharp_data import load_factions

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks, no readable lettering."
)

FACTION_OVERRIDES: dict[str, str] = {
    "republic": (
        "Panoramic view of the Galactic Senate rotunda on Coruscant with golden city-spires, "
        "diplomatic starships in traffic lanes, and soft blue dawn light over the capital world"
    ),
    "confederacy": (
        "Separatist droid factory complex on a red desert industrial world with hexagonal hangar "
        "structures, assembly lines of battle droids, and teal energy glow from foundry furnaces"
    ),
    "empire": (
        "Imperial Star Destroyer fleet in formation over a grey city-world skyline with TIE fighters "
        "patrolling and searchlights sweeping through industrial smog at twilight"
    ),
    "rebel-alliance": (
        "Hidden rebel base hangar carved into an asteroid or jungle moon with X-wings and Y-wings "
        "preparing for launch, orange flight suits, and warm lamp light on worn metal walls"
    ),
    "new-republic": (
        "Restored senate plaza on a peaceful green world with Chandrila-style architecture, "
        "celebratory banners in soft gold, and civilian crowds beneath a calm sky"
    ),
    "hutts": (
        "Opulent Hutt crime palace courtyard on a desert world with twin suns, smuggler skiffs, "
        "alien guards, spice bazaar stalls, and distant sail barge silhouettes"
    ),
    "sith-empire": (
        "Ancient Sith temple valley on a crimson Korriban world with lightning storms, "
        "obsidian obelisks, and dark side energy crackling over tombs and sand cliffs"
    ),
    "first-order": (
        "Snow-covered First Order military base with rows of white-armored troopers, red banner "
        "poles, and a massive dark superweapon trench carved into frozen mountains"
    ),
    "resistance": (
        "Resistance command center inside a rugged hangar with orange insignia panels, "
        "starfighters under repair, holo tactical maps, and a violet nebula visible through blast doors"
    ),
    "mandalorians": (
        "Mandalore domed capital city with beskar forges glowing orange, warrior clans on "
        "overlook platforms, and starfighters above a scarred but proud metropolitan skyline"
    ),
    "trade-federation": (
        "Massive circular Lucrehulk battleship hovering over a lush blue-green world with "
        "smaller Federation sphere ships, trade cargo tethers, and Neimoidian bridge silhouettes"
    ),
}

DIRECTORY_HERO_PROMPT = (
    "Panoramic cinematic collage of galactic political power — senate spires, imperial fleets, "
    "rebel hangars, and ancient temples — viewed from a high orbital balcony at golden hour "
    "with starships passing below. "
    + STYLE_SUFFIX
)


def faction_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    scene = FACTION_OVERRIDES.get(
        slug,
        f"Epic cinematic establishing shot representing {entry.get('name', 'a galactic faction')}, "
        f"{entry.get('government', 'a major power')}. "
        f"Environment reflects {entry.get('era', 'galactic history')}",
    )
    return f"{scene}. {STYLE_SUFFIX}"


def all_faction_prompts() -> dict[str, str]:
    return {e["slug"]: faction_prompt(e) for e in load_factions()}


if __name__ == "__main__":
    prompts = all_faction_prompts()
    print(f"Generated {len(prompts)} faction hero prompts")
