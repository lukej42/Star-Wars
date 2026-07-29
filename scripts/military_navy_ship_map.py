#!/usr/bin/env python3
"""Map military navy unit slugs to ships directory scene assets."""

from __future__ import annotations

# Navy unit slug -> ships/{slug}-scene.webp stem (without -scene)
NAVY_SHIP_MAP: dict[str, str] = {
    "providence-class-dreadnought": "providence-class",
    "lucrehulk-class-battleship": "lucrehulk-class",
    "munificent-class-frigate": "munificent-class",
    "recusant-class-destroyer": "recusant-class",
    "hardcell-class-transport": "hardcell-class",
    "vulture-droid-starfighter-wing": "vulture-droid",
    "tri-fighter-escort-wing": "droid-tri-fighter",
    "hyena-class-bomber-wing": "hyena-class",
    "c9979-landing-craft-squadron": "c-9979",
    "subjugator-class-heavy-cruiser": "subjugator-class",
    "diamond-class-cruiser": "banking-clan-frigate",
    "separatist-blockade-fleet": "lucrehulk-class",
    "invisible-hand-flagship-group": "invisible-hand",
    "venator-class-star-destroyer": "venator-class",
    "acclamator-assault-group": "acclamator-class",
    "pelta-class-frigate-group": "pelta-class",
    "consular-class-cruiser-escort": "consular-class",
    "arc-170-starfighter-wing": "arc-170",
    "v-wing-starfighter-wing": "v-wing",
    "y-wing-bomber-wing": "y-wing",
    "republic-venator-battle-group": "venator-class",
    "coruscant-home-defense-fleet": "venator-class",
    "kashyyyk-defense-fleet": "acclamator-class",
    "hardcell-class-republic-transport": "hardcell-class",
    "light-cruiser-patrol-squadron": "arquitens-class",
    "imperial-i-class-star-destroyer": "imperial-i-class",
    "imperial-ii-class-star-destroyer": "imperial-ii-class",
    "executor-class-super-star-destroyer": "executor-class",
    "interdictor-class-cruiser": "interdictor-class",
    "arquitens-class-light-cruiser": "arquitens-class",
    "raider-class-corvette-squadron": "raider-class",
    "gozanti-class-cruiser-group": "gozanti-class",
    "tie-fighter-wing": "tie-fighter",
    "tie-interceptor-squadron": "tie-interceptor",
    "tie-bomber-wing": "tie-bomber",
    "tie-defender-squadron": "tie-defender",
    "death-squadron": "executor-class",
    "scarif-orbital-defense-group": "imperial-i-class",
    "coruscant-defense-fleet": "imperial-i-class",
    "inquisitorius-task-force": "tie-advanced-x1",
    "home-one-fleet-group": "mc80-cruiser",
    "mon-calamari-cruiser-group": "mc80-cruiser",
    "nebulon-b-frigate-group": "nebulon-b",
    "corellian-corvette-squadron": "cr90-corvette",
    "x-wing-starfighter-wing": "x-wing",
    "rogue-squadron": "x-wing",
    "y-wing-bomber-wing-rebel": "y-wing",
    "a-wing-interceptor-wing": "a-wing",
    "b-wing-assault-wing": "b-wing",
    "rebel-fleet-command": "mc80-cruiser",
    "battle-of-scarif-task-group": "hammerhead-corvette",
    "endor-fleet-battle-group": "mc80-cruiser",
    "rebel-transport-convoy": "gr-75-transport",
    "pelta-class-rebel-support": "pelta-class",
    "liberation-of-sullust-group": "x-wing",
    "snowspeeder-wing": "snowspeeder",
    "resurgent-class-star-destroyer": "resurgent-class",
    "mandator-iv-class-siege-dreadnought": "mandator-iv-class",
    "tie-fo-fighter-wing": "tie-fo",
    "tie-sf-squadron": "tie-sf",
    "tie-bomber-wing-fo": "tie-bomber",
    "tie-silencer-squadron": "tie-sf",
    "first-order-transport-fleet": "first-order-transporter",
    "finalizer-battle-group": "resurgent-class",
    "supremacy-flagship-group": "supremacy",
    "starkiller-base-defense-fleet": "resurgent-class",
    "hosnian-cataclysm-group": "xyston-class",
    "crait-invasion-force": "first-order-dreadnought",
    "first-order-expeditionary-fleet": "resurgent-class",
    "interdictor-resurgent-group": "resurgent-class",
    "kylo-ren-command-group": "tie-sf",
    "resistance-navy": "mc85-cruiser",
    "resistance-starfighter-corps": "t-70-x-wing",
    "resistance-bombers": "mg-100-bomber",
    "raptor-squadron": "t-70-x-wing",
    "black-squadron": "t-70-x-wing",
    "mc85-star-cruiser-group": "mc85-cruiser",
    "resistance-frigate-escort-group": "nebulon-b",
    "resistance-corvette-strike-group": "cr90-corvette",
    "resistance-transport-group": "gr-75-transport",
    "crait-evacuation-force": "gr-75-transport",
    "dqar-evacuation-fleet": "mc85-cruiser",
    "resistance-a-wing-interceptor-wing": "rz-2-a-wing",
    "resistance-legacy-cruiser-group": "mc80-cruiser",
    "resistance-legacy-pilot-veterans": "x-wing",
    "new-republic-defense-fleet": "mc80-cruiser",
    "mon-calamari-new-republic-cruiser-group": "mc80-cruiser",
    "nebulon-k-frigate-group": "nebulon-b",
    "new-republic-corvette-patrol": "cr90-corvette",
    "rapier-squadron": "x-wing",
    "new-republic-starfighter-corps": "x-wing",
    "new-republic-bomber-wing": "y-wing",
    "new-republic-transport-command": "gr-75-transport",
    "outer-rim-patrol-fleet": "nebulon-b",
    "hosnian-defense-squadron": "x-wing",
    "jakkuvian-remnant-hunt-group": "x-wing",
    "new-republic-scout-frigate-squadron": "carrack-class",
    "new-republic-carrier-battle-group": "venator-class",
    "mandalorian-fleet": "komrk-class",
    "komrk-class-assault-wing": "komrk-class",
    "fang-class-escort-squadron": "fang-class",
    "mandalorian-gauntlet-fighter-wing": "gauntlet-fighter",
    "mandalorian-boarding-corps": "komrk-class",
    "shadow-collective-mandalorian-wing": "komrk-class",
    "mandalorian-resistance-strike-flotilla": "komrk-class",
    "mandalorian-orbital-defense-wing": "komrk-class",
    "mandalorian-orbital-salvage-group": "komrk-class",
    "mandalorian-clan-carrier-group": "komrk-class",
    "imperial-light-cruiser-patrol": "arquitens-class",
    "mandalorian-mercenary-fleet-detachment": "komrk-class",
    "mandalorian-hyperspace-raider-squadron": "komrk-class",
    "gungan-submarine-flotilla": "n-1-starfighter",
    "naboo-n-1-patrol-wing": "n-1-starfighter",
    "lucrehulk-blockade-group": "lucrehulk-class",
    "corporate-patrol-frigate-group": "munificent-class",
    "hutt-skiff-patrol": "bantha-ii-skiff",
    "hutt-yacht-escort-squadron": "j-type-327",
    "crimson-dawn-strike-flotilla": "ginivex-class",
    "pyke-spice-hauler-convoy": "action-vi",
    "black-sun-frigate-patrol": "lancer-class",
    "techno-union-support-fleet": "hardcell-class",
    "nightsister-swarm-squadron": "ginivex-class",
    "dathomirian-orbital-shaman-guard": "nightbrother",
    "shadow-collective-combined-fleet": "komrk-class",
    "harrower-class-dreadnought": "harrower-class",
    "terminus-class-destroyer": "harrower-class",
    "sith-interceptor-wing": "sith-interceptor",
    "sith-bomber-wing": "sith-interceptor",
    "mark-vi-supremacy-class": "harrower-class",
    "sith-fleet-command": "harrower-class",
    "korriban-defense-fleet": "harrower-class",
    "dromund-kaas-home-fleet": "harrower-class",
    "sith-blockade-group": "harrower-class",
    "sith-transport-convoy": "harrower-class",
    "sith-hypergate-strike-group": "harrower-class",
    "sith-ambassador-escort-squadron": "harrower-class",
    "hammerhead-class-cruiser-group": "endar-spire",
    "endar-spire-assault-group": "endar-spire",
    "republic-aurek-fighter-wing": "x-wing",
    "republic-bomber-wing": "y-wing",
    "thranta-class-corvette-squadron": "consular-class",
    "valor-class-cruiser-group": "endar-spire",
    "open-circle-old-republic-fleet": "endar-spire",
    "coruscant-home-defense-squadron": "endar-spire",
    "republic-blockade-interdiction-group": "hammerhead-corvette",
    "republic-transport-command": "gr-75-transport",
    "pelta-class-support-group": "pelta-class",
    "republic-carrier-battle-group": "venator-class",
}

# Representative ship scene for each faction's navy branch listing hero
FACTION_NAVY_BRANCH_SHIP: dict[str, str] = {
    "confederacy-of-independent-systems": "lucrehulk-class",
    "first-order": "resurgent-class",
    "galactic-empire": "imperial-i-class",
    "galactic-republic": "venator-class",
    "mandalorian": "komrk-class",
    "new-republic": "mc80-cruiser",
    "other": "lucrehulk-class",
    "rebel-alliance": "mc80-cruiser",
    "resistance": "mc85-cruiser",
    "sith-empire": "harrower-class",
    "old-republic": "endar-spire",
}

STYLE_PREFIX = (
    "Photorealistic cinematic Star Wars live-action film still hero banner, 1536x1024, 16:9. "
    "Hyper-realistic practical effects quality matching the nine saga films, Clone Wars, Rebels, "
    "The Mandalorian, Knights of the Old Republic, and Old Sith Empire visuals. "
    "Film grain, dramatic rim lighting, IMAX composition. "
)

STYLE_SUFFIX = " No text, no logos, no watermarks, no readable lettering."


def army_prompt(name: str, unit_type: str, description: str) -> str:
    scene = (
        f"Ground forces scene featuring {name} ({unit_type}). "
        f"{description[:320]}"
    )
    return f"{STYLE_PREFIX}{scene}{STYLE_SUFFIX}"


def branch_prompt(faction_name: str, branch: str) -> str:
    if branch == "army":
        scene = (
            f"Epic panoramic ground army of {faction_name} with infantry columns, armor, "
            f"and battlefield smoke at golden hour, live-action Star Wars film aesthetic"
        )
    else:
        scene = (
            f"Epic fleet formation of {faction_name} capital ships and starfighters in deep space, "
            f"live-action Star Wars film aesthetic with nebula backlight"
        )
    return f"{STYLE_PREFIX}{scene}{STYLE_SUFFIX}"


def navy_fallback_prompt(name: str, unit_type: str, description: str) -> str:
    scene = (
        f"Space naval scene featuring {name} ({unit_type}). "
        f"{description[:320]}"
    )
    return f"{STYLE_PREFIX}{scene}{STYLE_SUFFIX}"
