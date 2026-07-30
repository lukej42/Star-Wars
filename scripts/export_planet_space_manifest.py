#!/usr/bin/env python3
"""Build photorealistic space-view prompts and export manifest for missing backgrounds."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from parse_csharp_data import load_planets
from planet_hero_prompts import PLANET_OVERRIDES, _trim_description

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = SCRIPTS / "planet_space_manifest.json"
OUT = ROOT / "wwwroot" / "images" / "planets"
MIN_CINEMATIC_BYTES = 500_000

STYLE = (
    "Cinematic photorealistic planet viewed from space, wide orbital perspective, "
    "curved planetary horizon filling the lower third of the frame, thin glowing "
    "atmospheric rim light, deep black starfield with scattered white stars, "
    "highly detailed Star Wars sci-fi space art, dramatic rim lighting, IMAX quality. "
    "No text, no labels, no watermarks"
)

VISUALS: dict[str, str] = {
    "ahch-to": "stormy deep blue ocean world with rocky islands and heavy cloud cover",
    "ajan-kloss": "lush green jungle moon with thick cloud bands",
    "alderaan": "peaceful blue-green world with snow-capped mountains, valleys and lakes",
    "ashas-ree": "dark crimson wasteland world with ruined temples and purple haze",
    "atollon": "tan desert planet with coral-colored mesas and canyons",
    "bracca": "grey industrial junkyard world covered in starship graveyards",
    "cantonica": "golden desert planet with glittering resort cities on the surface",
    "carida": "grey militarized world with academy complexes and rugged terrain",
    "cato-neimoidia": "misty amber world with bridge cities above fungal swamps",
    "christophsis": "green crystalline mesas and turquoise canyons",
    "crait": "white salt flats and red mineral dust on a barren world",
    "d-qar": "green temperate world with oceans and continents",
    "dagobah": "murky green swamp planet shrouded in thick mist and clouds",
    "daiyu": "industrial city-planet with dense urban sprawl and smog",
    "dathomir": "red sky jungle world with crimson clouds and dark forests",
    "dromund-kaas": "storm-wracked dark green jungle world with lightning-lit clouds",
    "endor": "green forest moon with patchwork canopy visible from orbit",
    "exegol": "pitch black rocky world in eternal darkness with faint red lightning",
    "felucia": "vibrant magenta and green jungle with giant fungal towers",
    "ferrix": "rust-brown industrial world with salvage yards and factories",
    "florrum": "sulfurous yellow desert canyons and pirate outposts",
    "geonosis": "red rock desert with rings of droid factory spires",
    "ilum": "pale blue-white ice planet with crystalline glints",
    "jabiim": "rain-soaked muddy brown battlefield world under grey clouds",
    "jakku": "tan desert world littered with starship wreckage scars",
    "jedha": "cold desert moon with tan dunes and ancient temple spires",
    "kamino": "entirely ocean-covered blue world with storm systems",
    "kashyyyk": "deep green jungle planet with endless wroshyr tree canopy",
    "kef-bir": "blue ocean moon with Death Star wreckage visible in water",
    "kijimi": "snow-covered grey world with mining city lights",
    "koboh": "green mesas and wetlands on a frontier world",
    "lothal": "savannah grasslands with purple hints and scattered settlements",
    "malachor": "charred grey Sith wasteland with petrified battlefield scars",
    "malachor-v": "shattered grey-brown dead world with fractured crust",
    "manaan": "deep blue ocean planet with scattered white clouds",
    "mandalore": "white domed cities on a war-scarred brown-orange world",
    "mon-cala": "blue ocean world with floating city structures",
    "mygeeto": "icy world with crystalline spires and blue glaciers",
    "nar-shaddaa": "vertical ecumenopolis moon glowing with neon city lights",
    "nathema": "lifeless grey dead world with no atmosphere glow",
    "nevarro": "volcanic world with lava rivers and frontier towns",
    "onderon": "jungle world with a walled capital city visible",
    "pasaana": "orange desert festival world with sweeping dunes",
    "peridea": "dead grey extragalactic world with withered forests",
    "polis-massa": "grey asteroid archipelago in space instead of a full planet",
    "rakata-prime": "overgrown jungle ruins on a dark green world",
    "raxus": "temperate green world with elegant Separatist palaces",
    "rishi": "tropical blue-green moon with white beaches",
    "ryloth": "tidally locked world with scorched brown dayside and dark nightside",
    "serenno": "elegant purple-grey aristocratic world with great estates",
    "takodana": "green lake world with Maz Kanata castle beside water",
    "taris": "ruined ecumenopolis planet with broken city rings",
    "telos": "partially restored blue world with orbital station ring",
    "tython": "mystical green valley world with ancient temple peaks",
    "umbara": "perpetually dark purple world with bioluminescent fungi",
    "utapau": "tan sinkhole world with wind-carved desert cities in craters",
    "yavin-4": "jungle moon with dense green canopy orbiting a red gas giant in background",
    "ziost": "frozen pale blue Sith world covered in ice and snow",
    "agamar": "green-brown temperate world with cloud bands and scattered surface settlements",
    "denova": "lush blue-green jungle world with white cloud swirls and mountainous terrain",
    "bardotta": "purple-grey Colonies world with temple districts visible through thin clouds",
    "denon": "urbanized Inner Rim world glowing with city lights on the nightside",
    "kiros": "pale marble-white world with elegant domed cities and green continental patches",
    "lotho-minor": "sickly yellow-brown toxic industrial world with smog and acid haze",
    "ringo-vinda": "large orbital ring habitat structure against starfield with planet below",
}


def space_features(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in VISUALS:
        return VISUALS[slug]
    if slug in PLANET_OVERRIDES:
        return PLANET_OVERRIDES[slug]
    name = entry.get("name", slug)
    region = entry.get("region", "the galaxy")
    desc = _trim_description(entry.get("description", ""), 200)
    if desc:
        return f"{name} in the {region}, {desc}"
    return f"{name}, a distinctive {region} world with unique coloration and terrain visible from orbit"


def space_prompt(entry: dict[str, str]) -> str:
    features = space_features(entry)
    return f"{STYLE}. {features}."


def needs_regeneration(entry: dict[str, str]) -> bool:
    custom = entry.get("imagePath", "")
    if custom:
        path = ROOT / "wwwroot" / custom.lstrip("/")
    else:
        path = OUT / f"{entry['slug']}-space.webp"
    return not path.is_file() or path.stat().st_size < MIN_CINEMATIC_BYTES


def main() -> None:
    manifest = []
    for entry in load_planets():
        if not needs_regeneration(entry):
            continue
        slug = entry["slug"]
        manifest.append(
            {
                "slug": slug,
                "name": entry.get("name", slug),
                "prompt": space_prompt(entry),
                "output": f"wwwroot/images/planets/{slug}-space.webp",
            }
        )
    MANIFEST.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Wrote {len(manifest)} entries to {MANIFEST}")


if __name__ == "__main__":
    main()
