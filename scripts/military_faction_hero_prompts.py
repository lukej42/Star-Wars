#!/usr/bin/env python3
"""Cinematic hero-banner prompts for military faction overview pages."""

from __future__ import annotations

STYLE_PREFIX = (
    "Photorealistic cinematic science-fiction live-action film still hero banner, 1536x1024, 16:9. "
    "Hyper-realistic practical effects quality matching premium space opera films. "
    "Film grain, dramatic rim lighting, IMAX composition. "
)

STYLE_SUFFIX = " No text, no logos, no watermarks, no readable lettering."

FACTION_SCENES: dict[str, str] = {
    "confederacy-of-independent-systems": (
        "Epic invasion formation on a lush green planet: endless ranks of silver skeletal battle droids "
        "with elongated heads marching in perfect columns across rolling plains, Multi-Troop Transports "
        "and armored droid carriers behind them, STAP repulsor scouts overhead, Trade Federation landing "
        "craft on the horizon at golden hour — evoking the opening ground war of Episode I"
    ),
    "galactic-empire": (
        "A vast army of white-armored imperial legionnaires filling a colossal star destroyer hangar bay "
        "and deployment ramp, thousands of identical helmets and blaster rifles in rigid formation, "
        "searchlights cutting through industrial haze, TIE fighters suspended above, grey and black "
        "Imperial architecture at twilight"
    ),
    "galactic-republic": (
        "Endless columns of white-armored clone soldiers in Phase II kit advancing across a red dust "
        "Geonosis battlefield, LAAT/i gunships screaming overhead, AT-TE walkers in the distance, "
        "explosions and tracer fire, Jedi commanders leading the charge at dramatic sunset"
    ),
    "first-order": (
        "Massed First Order legionnaires in stark white armor with black pauldrons standing at attention "
        "on the snow-covered surface of a weaponized ice planet, red banner cloth snapping in arctic wind, "
        "Atmospheric Assault Transports and TIE echelons in a crimson-streaked sky"
    ),
    "rebel-alliance": (
        "A diverse rebel army gathered on a hidden jungle base clearing: humans, aliens, and pilots in "
        "orange flight suits mixing with infantry in field gear, X-wing fighters parked among tents, "
        "Yavin-style temple spires visible through mist at dawn"
    ),
    "resistance": (
        "Resistance soldiers in brown and black tactical gear dug into trenches on a white salt-crystal "
        "plain streaked with red mineral dust, ski speeders and artillery emplacements, MC85 cruiser "
        "silhouette in a violet sky above a desperate last stand"
    ),
    "new-republic": (
        "New Republic defense legionnaires in blue-trimmed peacekeeping armor mustering in a gleaming "
        "senate district plaza, mixed species volunteers, Aurebesh-free banners of unity, Hosnian-style "
        "architecture and starfighters on ceremonial flyover in soft morning light"
    ),
    "mandalorian": (
        "A wall of Mandalorian warriors in full beskar armor with distinct clan color schemes, "
        "T-visors gleaming, jetpacks and rifles ready on a rocky desert ridge, ancient clan banners "
        "and parked starfighters behind them at dramatic sunset"
    ),
    "sith-empire": (
        "Sith Imperial army in crimson and gunmetal armor advancing beneath lightning over a dark "
        "metropolis, Harrower-class dreadnought silhouettes in a blood-red sky, ancient Sith banners "
        "and war droids flanking the columns — Knights of the Old Republic era aesthetic"
    ),
    "old-republic": (
        "Old Republic troopers in blue and silver armor deploying from a hammerhead cruiser landing zone "
        "on a contested urban world, Aurek starfighters overhead, Jedi and Republic officers coordinating "
        "a combined arms assault — classic KOTOR-era live-action film still"
    ),
    "other": (
        "A motley coalition of mercenary companies, pirate militia, and corporate security battalions "
        "assembled on a dusty Outer Rim spaceport tarmac: mismatched armor, alien species, hired gunships "
        "and cargo haulers, golden sunset over a frontier war camp"
    ),
}


def faction_prompt(slug: str, faction_name: str) -> str:
    scene = FACTION_SCENES.get(
        slug,
        f"Epic combined arms panorama of {faction_name} military forces at golden hour",
    )
    return f"{STYLE_PREFIX}{scene}{STYLE_SUFFIX}"


def faction_hero_filename(slug: str) -> str:
    return f"{slug}-faction-hero.webp"
