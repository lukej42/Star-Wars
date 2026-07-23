#!/usr/bin/env python3
"""Build photorealistic space-view prompts for planet hero images."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data" / "GalaxyData.cs"

STYLE = (
    "Cinematic photorealistic planet viewed from space, wide orbital perspective, "
    "curved planetary horizon, thin glowing atmospheric rim, deep black starfield "
    "with scattered white stars, highly detailed sci-fi space art, no text, no labels"
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
}


def parse_planets() -> list[dict]:
    text = DATA.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        image = re.search(r'ImagePath = "(.*?)"', block)
        if name and slug and not image:
            slug_val = slug.group(1)
            entries.append(
                {
                    "slug": slug_val,
                    "name": name.group(1),
                    "prompt": f"{STYLE}. Surface features: {VISUALS.get(slug_val, desc.group(1) if desc else 'alien world')}.",
                }
            )
    return entries


def main() -> None:
    for entry in parse_planets():
        print(f"{entry['slug']}|{entry['prompt']}")


if __name__ == "__main__":
    main()
