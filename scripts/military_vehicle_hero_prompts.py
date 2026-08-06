#!/usr/bin/env python3
"""Cinematic hero-banner prompts for military ground/air craft pages."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

STYLE_PREFIX = (
    "Photorealistic cinematic science-fiction live-action film still hero banner, 1536x1024, 16:9. "
    "Hyper-realistic practical effects quality matching premium space opera films. "
    "Film grain, dramatic rim lighting, IMAX composition. "
)

STYLE_SUFFIX = " No text, no logos, no watermarks, no readable lettering."

VEHICLE_SCENES: dict[str, str] = {
    "galactic-republic-ground-at-rt": (
        "A lone two-legged scout walker with open cockpit and blaster cannon striding through misty "
        "alien forest undergrowth, clone trooper pilot visible, dappled sunlight and battle smoke"
    ),
    "galactic-republic-ground-spha-t": (
        "Massive tracked turbolaser artillery platform firing a brilliant beam across a besieged city "
        "plain, clone gunners on deck, Christophsis-style crystalline skyline in distance"
    ),
    "galactic-republic-air-laat-c": (
        "Heavy repulsorlift gunship variant carrying an assault walker beneath its hull over red "
        "desert mesas, clone escort starfighters in formation, Clone Wars orbital drop scene"
    ),
    "galactic-republic-air-v-19-torrent": (
        "Squadron of angular early-war starfighters banking through orange cloud layers above a "
        "Republic fleet, contrails and laser fire, dramatic sunset atmosphere"
    ),
    "galactic-republic-air-arc-170": (
        "Heavy three-wing Republic starfighters in combat spread with rear gunners visible, "
        "explosions and flak over a Separatist dreadnought, deep space battle lighting"
    ),
    "confederacy-of-independent-systems-ground-hailfire-droid": (
        "Wheel-mode missile droid tank launching salvos of rockets across a banking clan battlefield, "
        "smoke trails and craters, Muunilinst-style urban backdrop"
    ),
    "confederacy-of-independent-systems-ground-og-9-spider-droid": (
        "Tall four-legged spider droid with central blaster cannon on a rocky ridge overlooking "
        "clone infantry advance, Geonosis red dust and laser streaks"
    ),
    "confederacy-of-independent-systems-air-hyena-bomber": (
        "Hyena-class droid bomber wing diving through flak above a Republic cruiser, missile bays "
        "open, violet nebula and capital ship superstructure"
    ),
    "confederacy-of-independent-systems-air-tri-fighter": (
        "Aggressive three-wing droid starfighters in tight attack formation, glowing red photoreceptor "
        "eyes, swirling dogfight above a ringed planet"
    ),
    "galactic-empire-ground-at-dp": (
        "Two-legged Imperial defense walker on patrol in a neon-lit city street, stormtrooper escort, "
        "searchlights and propaganda holos on towering buildings"
    ),
    "galactic-empire-ground-imperial-troop-transport": (
        "Open-top Imperial repulsorlift troop carrier loaded with white-armored soldiers rolling through "
        "a dusty occupation zone, TIE fighters overhead at dusk"
    ),
    "galactic-empire-air-tie-interceptor": (
        "Squadron of dagger-wing Imperial interceptors screaming through a Death Star trench run, "
        "green laser fire and engine glow, high-speed motion blur"
    ),
    "rebel-alliance-ground-t2-b-repulsor-tank": (
        "Rebel repulsor tank with twin turrets advancing across a grassy plain toward Imperial lines, "
        "orange rebellion markings, smoke and distant walkers"
    ),
    "rebel-alliance-ground-aac-1-speeder-tank": (
        "Low-profile Rebel speeder tank skimming over scrubland at high speed, dust plume trailing, "
        "infantry support and distant X-wing flyover"
    ),
    "rebel-alliance-ground-74-z-speeder-bike": (
        "Scout speeder bikes weaving at high velocity through towering Endor redwood forest, "
        "sunbeams and ferns, pursuit chase atmosphere"
    ),
    "rebel-alliance-ground-a-a5-speeder-truck": (
        "Armored Rebel repulsor truck convoy moving between jungle hidden base bunkers, technicians "
        "and soldiers loading crates at dawn"
    ),
    "rebel-alliance-air-x-wing": (
        "Classic four-wing Rebel starfighter in attack position with S-foils open, proton torpedo launch "
        "toward a Death Star thermal exhaust port, space battle debris"
    ),
    "rebel-alliance-air-a-wing": (
        "Sleek wedge-shaped Rebel interceptors cutting through a fleet battle at Endor, green laser "
        "trails, exploding Star Destroyer bridge in background"
    ),
    "first-order-ground-first-order-treadspeeder": (
        "Single-pilot First Order treaded speeder pursuing through rain-slick industrial city ruins, "
        "stormtrooper rider, red sensor glow and sparks"
    ),
    "first-order-ground-first-order-at-at": (
        "Updated four-legged First Order assault walker advancing across Jakku desert wreckage field, "
        "chin cannons firing, scavenger settlement ruins and twin suns"
    ),
    "first-order-ground-light-infantry-utility-vehicle": (
        "Open-top First Order transport deploying stormtrooper squads onto a landing pad under "
        "Resurgent-class destroyer shadow, searchlights and ash"
    ),
    "first-order-air-tie-sf": (
        "Two-seat First Order special forces fighter with enhanced sensor dome banking over Jakku "
        "graveyard of ships, desert haze and fleet above"
    ),
    "first-order-air-tie-se-bomber": (
        "First Order bomber wing releasing ordnance over a Resistance coastal base, payload trails "
        "and rising fireballs, grey ocean and cliffs"
    ),
    "resistance-ground-v-4x-d-ski-speeder": (
        "Crait salt-flats ski speeder kicking up crimson dust trails while strafing a distant mega "
        "walker silhouette, white crystal plain and violet sky"
    ),
    "resistance-ground-resistance-troop-transport": (
        "Resistance armored troop carrier racing between hidden outpost bunkers on a forest moon, "
        "Marines in tactical gear, MC85 cruiser in cloudy sky"
    ),
    "resistance-ground-cdf-7620-landspeeder": (
        "Modified civilian landspeeder with jury-rigged blaster mounts speeding through narrow "
        "Mid Rim canyon town, Resistance cell operators, golden hour"
    ),
    "resistance-air-t-70-x-wing": (
        "Next-generation blue-and-white X-wing flown by ace pilot in attack run on Starkiller Base "
        "shield gate, snow mountains and flak bursts"
    ),
    "resistance-air-rz-2-a-wing": (
        "Resistance A-wing interceptors escorting bombers through heavy TIE swarms, engine trails "
        "and explosions above D'Qar evacuation"
    ),
    "resistance-air-resistance-bomber": (
        "MG-100 StarFortress heavy bomber with cobalt squadron markings releasing payload over "
        "Fulminatrix dreadnought, tragic heroic last-run lighting"
    ),
    "mandalorian-ground-mandalorian-speeder-bike": (
        "Beskar-trimmed Mandalorian scout bike parked on rocky ridge at sunset, warrior in full "
        "armor checking blaster, clan banner and starfield"
    ),
    "mandalorian-ground-akajor-assault-shuttle": (
        "Mandalorian assault shuttle landing vertically in narrow desert canyon staging area, "
        "ramp deploying armored troops, dust and jet wash"
    ),
    "mandalorian-ground-canderous-assault-tank": (
        "Heavy Mandalorian hover tank with mass-driver cannons breaching a siege line on contested "
        "Rim world, beskar hull gleaming, explosions"
    ),
    "mandalorian-air-komrk-fighter-transport": (
        "Rotating-wing Mandalorian gunship in flight mode over Mandalore cityscape ruins, Nite Owl "
        "markings, troop bay doors open"
    ),
    "mandalorian-air-gauntlet-starfighter": (
        "Forked-prow Mandalorian starfighter in dogfight above Concord Dawn gas giant clouds, "
        "Protector squadron colors, laser fire"
    ),
    "mandalorian-air-fang-class-fighter": (
        "Compact Mandalorian interceptor weaving through shattered orbital debris above Mandalore, "
        "heavy chin cannons firing, clan insignia on wings"
    ),
    "sith-empire-ground-sith-imperial-assault-tank": (
        "Sith Empire hover tank with red-trim dark hull advancing through rain on invaded Republic "
        "border world, lightning and urban ruins, KOTOR era aesthetic"
    ),
    "sith-empire-ground-sith-troop-carrier": (
        "Sith Imperial armored troop carrier breaching fortified city gate, red-armored soldiers "
        "deploying, smoke and crumbling statuary"
    ),
    "sith-empire-ground-mark-vi-land-crawler": (
        "Massive Sith siege land crawler with treads and heavy cannons crushing Republic bastion "
        "walls on Alderaan-style world, apocalyptic scale"
    ),
    "sith-empire-air-fury-interceptor": (
        "Sith Fury-class interceptors in attack formation above Korriban red sky, acolyte pilots, "
        "ancient Sith temples below"
    ),
    "sith-empire-air-b28-extinction-bomber": (
        "Sith Extinction-class bomber releasing fusion payloads against Republic orbital shipyard, "
        "fireballs and docking arms, deep space"
    ),
    "sith-empire-air-sith-imperial-assault-shuttle": (
        "Heavily armed Sith assault shuttle descending through smoke onto captured world plaza, "
        "Inquisitor escort and fighter wing overhead"
    ),
}

# Good AI assets that use legacy filenames in the assets folder.
ASSET_ALIASES: dict[str, tuple[str, ...]] = {
    "galactic-republic-air-laat-i": ("galactic-republic-air-laat", "galactic-republic-air-laat-i"),
    "galactic-republic-ground-havw-a6-juggernaut": (
        "galactic-republic-ground-juggernaut",
        "galactic-republic-ground-havw-a6-juggernaut",
    ),
    "confederacy-of-independent-systems-air-vulture-droid": (
        "confederacy-air-vulture-droid",
        "confederacy-of-independent-systems-air-vulture-droid",
    ),
    "confederacy-of-independent-systems-ground-mtt": (
        "confederacy-ground-mtt",
        "confederacy-of-independent-systems-ground-mtt",
    ),
    "confederacy-of-independent-systems-ground-aat": (
        "confederacy-ground-aat",
        "confederacy-of-independent-systems-ground-aat",
    ),
}

GOOD_SIZE_THRESHOLD = 500_000
ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "Data" / "VehicleData.cs"
ASSETS = Path.home() / ".cursor/projects/Users-luke-gumbleton-Documents-Azure-Github-Star-Wars/assets"
OUTPUT = ROOT / "wwwroot" / "images" / "military-vehicles"


def parse_vehicles() -> list[dict[str, str]]:
    text = DATA_FILE.read_text(encoding="utf-8")
    vehicles: list[dict[str, str]] = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        entry: dict[str, str] = {}
        for match in re.finditer(r'(\w+) = "(.*?)"', block):
            entry[match.group(1)] = match.group(2)
        type_match = re.search(r"Type = MilitaryVehicleType\.(\w+)", block)
        if type_match:
            entry["Type"] = type_match.group(1)
        if "Slug" in entry:
            vehicles.append(entry)
    return vehicles


def asset_slug(vehicle: dict[str, str]) -> str:
    type_slug = "ground" if vehicle["Type"] == "Ground" else "air"
    return f"{vehicle['FactionSlug']}-{type_slug}-{vehicle['Slug']}"


def hero_filename(vehicle: dict[str, str]) -> str:
    return f"{asset_slug(vehicle)}-hero.webp"


def vehicle_prompt(slug: str, name: str, vehicle_class: str, description: str) -> str:
    scene = VEHICLE_SCENES.get(
        slug,
        f"Epic cinematic scene featuring {name} ({vehicle_class}). {description[:280]}",
    )
    return f"{STYLE_PREFIX}{scene}{STYLE_SUFFIX}"


def find_best_source(slug: str) -> Path | None:
    names = ASSET_ALIASES.get(slug, (slug,))
    best: Path | None = None
    best_size = 0
    for name in names:
        for ext in (".png", ".webp", ".jpg", ".jpeg"):
            candidate = ASSETS / f"{name}{ext}"
            if candidate.is_file():
                size = candidate.stat().st_size
                if size > best_size:
                    best = candidate
                    best_size = size
    return best
