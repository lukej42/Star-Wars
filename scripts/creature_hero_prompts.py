#!/usr/bin/env python3
"""Cinematic hero-banner prompts for Creatures & Fauna directory entries."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks."
)

STRING_FIELD = re.compile(r'(\w+) = "(.*?)"')

OVERRIDES: dict[str, str] = {
    "rancor": "Massive jungle carnivore rearing in a shadowy Hutt palace pit arena with bone-strewn sand and torchlight",
    "wampa": "White-furred ice predator emerging from a snow cave on a frozen tundra under aurora sky",
    "sarlacc": "Immense desert pit creature with tentacles ringing the Great Pit of Carkoon beneath twin suns",
    "krayt-dragon": "Colossal sand dragon skeleton ridge and pearl glint across the Dune Sea at golden hour",
    "purrgil": "Bioluminescent space whales swimming through a violet hyperspace nebula with star trails",
    "tauntaun": "Shaggy ice steed on Hoth ridge with rebel patrol silhouettes and blowing snow",
    "bantha": "Twin-horned desert herd beast at a Tatooine moisture farm with sand dunes and domed homestead",
    "nexu": "Spined arena predator leaping between Geonosis rock pillars in crimson dust storm",
    "sarlacc": "Great desert pit with grasping tentacles and distant sail barge over orange canyon",
    "exogorth": "Giant space slug wrapped around a silent asteroid in deep starfield with freighter scale reference",
    "zillo-beast": "Armored colossus rampaging through Coruscant cityscape with green scales and lightning sky",
    "mudhorn": "Shaggy rhino-like beast on misty Arvala-7 ridge with ugnaught camp embers",
    "loth-wolf": "Mystic giant wolf on Lothal grasslands with aurora mist and temple monoliths",
    "loth-cat": "Striped feline hunter stalking Lothal tall grass at sunset with wind-swept plains",
    "porg": "Fluffy seabird colony on rocky Ahch-To cliff with crashing ocean spray and Jedi ruins",
    "convor": "Owl-like convor perched on ancient temple stone with green Force mist",
    "blurrg": "Two-legged Ryloth riding beast at a rebel camp with dusty red twilight",
    "reek": "Armored bull-like arena beast charging across Geonosis sand with petranaki ring walls",
    "acklay": "Three-eyed crustacean predator in a humid industrial arena with green fog and metal grating",
    "dewback": "Reptilian desert mount at an Imperial garrison checkpoint with heat shimmer",
    "rathtar": "Mass of writhing tentacles aboard a freighter corridor with emergency red lighting",
    "mynock": "Winged silicon parasites swarming an asteroid cave mouth with ship hull cables",
    "krykna": "Six-legged spider creatures on Atollon salt flats beneath twin moons and rebel base lights",
    "varactyl": "Colorful reptavian mount on Utapau sinkhole ledges with windmill platforms",
    "fyrnock": "Bioluminescent canyon predators swarming a cliffside outpost at night",
    "sando-aqua-monster": "Enormous underwater leviathan breaching Naboo ocean surface near Gungan ruins",
    "opee-sea-killer": "Abyssal fish predator rising from Naboo teal depths with coral spires",
    "aiwha": "Giant flying cetaceans gliding over Kamino storm ocean and stilt cities",
    "bogling": "Small swamp critters in Dagobah mist with gnarled roots and glowing bog water",
    "steelpecker": "Mechanical-beaked scavenger birds on a junkyard world among rusted starship hulls",
    "dark-side-spiders": "Shadow arachnids crawling through Malachor Sith temple ruins with green holocron glow",
    "charhound": "Molten volcanic hound on Mustafar obsidian ridge with lava rivers",
    "roggwart": "Horned swamp beast lunging from murky water with gnarled mangrove roots",
    "gundark": "Massive four-armed jungle ape in misty canopy with broken clone armor",
    "wyyyschokk": "Giant Kashyyyk web spider among wroshyr branches and hanging moss",
    "vulptex": "Crystal fox made of salt shards on Crait white flats with red mineral dust trails",
    "ice-spider": "Frozen arachnid on snow-covered mountain pass with imperial probe droid wreckage",
    "dianoga": "One-eyed trash compactor creature in oily darkness with metal walls",
    "gundark": "Towering jungle primate in rain-soaked battle ruins",
    "giant-fly": "Oversized insect swarm over Dathomir mist with red moon",
    "kowakian-monkey-lizard": "Small cackling reptile on a pirate skiff rail over turquoise sea",
    "eopie": "Desert pack beast on Tatooine trade route with twin sun haze",
    "ronto": "Large desert transport beast crossing a frontier settlement street",
    "jerba": "Horned Tatooine herd animal at a moisture vaporator line",
    "happabore": "Muddy pig-like beast at a Jakku scavenger camp among wreckage",
    "bor-gullet": "Mind-probing cephalopod in a shadowy crime fortress tank with cyan lighting",
    "cliff-worm": "Segmented desert worm bursting from a canyon shelf with sand spray",
    "giant-sea-eel": "Serpentine ocean predator in Naboo underwater grotto with sunbeams",
    "energy-spider": "Crystalline arachnid on a kyber-rich asteroid with violet refraction",
    "giant-amphibian": "Toad-like predator in swamp bayou with hanging vines",
    "creatures-directory-hero": "Collage atmosphere of iconic alien fauna silhouettes beneath twin moons on a frontier world with diverse habitats",
}


def parse_creatures() -> list[dict[str, str]]:
    text = (DATA / "CreatureData.cs").read_text(encoding="utf-8")
    entries: list[dict[str, str]] = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        entry: dict[str, str] = {}
        for match in STRING_FIELD.finditer(block):
            entry[match.group(1)] = match.group(2)
        if "Slug" in entry:
            entries.append(entry)
    return entries


def build_prompt(creature: dict[str, str]) -> str:
    slug = creature["Slug"]
    if slug in OVERRIDES:
        scene = OVERRIDES[slug]
    else:
        habitat = creature.get("Habitat", "alien world")
        homeworld = creature.get("Homeworld", "frontier planet")
        desc = creature.get("Description", "alien creature")
        if len(desc) > 160:
            desc = desc[:160].rsplit(" ", 1)[0] + "…"
        scene = f"{desc}. Habitat: {habitat} on {homeworld}"
    return f"{scene}. {STYLE_SUFFIX}"


def main() -> None:
    for creature in parse_creatures():
        print(f"{creature['Slug']}\t{build_prompt(creature)}")


if __name__ == "__main__":
    main()
