#!/usr/bin/env python3
"""Cinematic hero-banner prompts for Planet Directory entries."""

from __future__ import annotations

from parse_csharp_data import load_planets

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks."
)

PLANET_OVERRIDES: dict[str, str] = {
    "tatooine": "Twin suns over endless golden sand dunes with moisture vaporators and distant domed homesteads",
    "naboo": "Verdant Naboo rolling hills with Theed golden domes and waterfalls beside a turquoise lake",
    "coruscant": "Layered ecumenopolis skyline from upper atmosphere with traffic lanes and Senate district glow",
    "hoth": "Frozen white tundra with ice caves and distant AT-AT walker silhouettes under aurora sky",
    "mustafar": "Volcanic lava rivers and obsidian cliffs with molten falls and ash-choked red sky",
    "dagobah": "Misty swamp forest with twisted roots, hanging moss, and murky green bog water",
    "bespin": "Cloud City floating platforms in orange tibanna cloud sea with sunset horizon",
    "alderaan": "Peaceful snow-capped mountains and verdant valleys under soft blue skies before destruction",
    "endor": "Giant wroshyr trees with forest moon canopy and Ewok village rope bridges at golden hour",
    "yavin-4": "Massassi temple stone pyramids emerging from dense jungle with rebel base launch activity",
    "kamino": "Stilt cities above storm-wracked ocean with cloning facility spires and landing platforms",
    "geonosis": "Red rock droid factory spires and arena colosseum on arid desert planet horizon",
    "utapau": "Sinkhole city tiers inside vast sandstone cavern with windmill platforms and mist",
    "felucia": "Bioluminescent fungal jungle with pink and purple giant mushrooms and misty wetlands",
    "mandalore": "White domed cities on war-scarred red planet surface with beskar foundry smoke",
    "dathomir": "Red misty nightsister swamps with stone fortress and twisted dead trees",
    "korriban": "Valley of Dark Lords with ancient Sith tombs carved into orange desert cliffs",
    "moraband": "Sith homeworld barren red wastes with monolith tombs and lightning-charged sky",
    "exegol": "Dark storm planet with Sith cult citadel spires and forked lightning over black rock",
    "jakku": "Scavenger camps among crashed Star Destroyer wrecks half-buried in desert sand",
    "scarif": "Tropical palm coastline with Imperial Citadel tower and turquoise shielded bay",
    "jedha": "Desert moon holy city with kyber crystal spires and Imperial occupation shadows",
    "crait": "White salt flats with red mineral dust trails and abandoned rebel base entrance",
    "ahch-to": "Storm-lashed ocean islands with ancient stone Jedi temple steps and crashing waves",
    "lothal": "Grass plains with Imperial factory smokestacks and Ghost starship silhouette at sunset",
    "dantooine": "Rolling grassland rebel base with sensor arrays under peaceful blue sky",
    "kashyyyk": "Wroshyr tree canopy layers with rope bridges and mist over deep jungle rivers",
    "mon-cala": "Underwater Mon Calamari coral city with bioluminescent domes and bubble fields",
    "rishi": "Rishi moon tropical island with clone listening post on foggy volcanic peak",
    "christophsis": "Crystal hex-wall battlefield city with blue kyber-like mineral formations",
    "saleucami": "Mosaic grassland with clone trooper medic camp and lavender twilight sky",
    "mortis": "Surreal Force nexus world with floating monoliths and purple-green aurora sky",
    "bracca": "Scrapyard planet of stacked starship hulls with crane silhouettes in orange haze",
    "cantonica": "Canto Bight casino resort strip on desert coast with neon and luxury speeders",
    "pasaana": "Rolling orange desert festival dunes with giant worm tracks and spice caravan",
    "kijimi": "Snow-covered alpine town with narrow alleys and warm window glow under aurora",
    "sullust": "Volcanic industrial world with lava vents and factory complexes glowing at night",
    "mygeeto": "Crystalline ice-covered banking colony with laser-scarred bridge platforms",
    "serenno": "Cliffside aristocratic estate on misty green world with elegant manor spires",
    "ossus": "Jedi library world with ancient trees and ruined temple archives in golden light",
    "dxun": "Jungle moon orbiting red Onderon with mandalorian camp and beast-rider cliffs",
    "ziost": "Frozen Sith world with ice-covered city ruins and pale aurora over glaciers",
    "manaan": "Ocean world Kolto harvesting station with underwater glass domes and reefs",
    "taris": "Multi-level urban sprawl under perpetual rain with neon lower levels and rakghoul haze",
    "telos": "Restoration project world with Ithorian herdship over recovering green valleys",
    "malachor": "Dark side corrupted world with petrified Sith battlefield and crimson storm clouds",
    "malachor-v": "Petrifed Sith battlefield with obsidian surface and Trayus academy ruins under red sky",
    "ryloth": "Twi'lek homeworld showing day side desert and night side underground resistance caverns",
    "rodia": "Jungle swamps with humid green canopy and hunter clan village platforms",
    "concordia": "Mandalore moon with beskar mines and white dome settlements in red dust",
    "carida": "Imperial academy world with military training grounds and orbital shipyards visible",
}


def _trim_description(desc: str, max_len: int = 180) -> str:
    text = desc.strip()
    if len(text) > max_len:
        text = text[:max_len].rsplit(" ", 1)[0] + "…"
    return text


def planet_prompt(entry: dict[str, str]) -> str:
    slug = entry["slug"]
    if slug in PLANET_OVERRIDES:
        scene = PLANET_OVERRIDES[slug]
    else:
        name = entry.get("name", "alien world")
        region = entry.get("region", "the galaxy")
        desc = _trim_description(entry.get("description", ""))
        scene = (
            f"Cinematic planetary landscape of {name} in the {region}, {desc}. "
            f"Dramatic surface vista with distinctive terrain, atmosphere, and sci-fi scale"
        )
    return f"{scene}. {STYLE_SUFFIX}"


def all_planet_prompts() -> dict[str, str]:
    return {e["slug"]: planet_prompt(e) for e in load_planets()}


if __name__ == "__main__":
    prompts = all_planet_prompts()
    print(f"Generated {len(prompts)} planet hero prompts")
