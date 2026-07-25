#!/usr/bin/env python3
"""Cinematic hero-banner prompts for Military Units directory entries."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks, no readable lettering."
)

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "Data" / "MilitaryUnitData.cs"
UNIT_CALL = re.compile(
    r'Unit\("([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)", "([^"]+)"\)',
)

UNIT_SCENES: dict[str, str] = {
    "clone-trooper-corps": (
        "Endless ranks of white-armored clone troopers marching across a Kamino landing platform "
        "in torrential rain with LAAT gunships overhead and teal ocean storms on the horizon"
    ),
    "arc-troopers": (
        "Advanced Recon Commandos in customized blue armor breaching a Separatist bunker on a "
        "jungle moon with explosions and tracer fire illuminating mud and foliage"
    ),
    "clone-commandos": (
        "Elite clone commando squad in katarn-class armor moving through a dim industrial corridor "
        "with wrist holo maps, crimson targeting lasers, and smoke from breaching charges"
    ),
    "501st-legion": (
        "The 501st Legion in blue-marked clone armor assaulting a burning city street with "
        "AT-TE walkers and LAAT/i gunships in orange dawn light"
    ),
    "212th-battalion": (
        "212th Attack Battalion clone troopers with orange markings advancing across a desert mesa "
        "under Obi-Wan Kenobi's campaign banners and distant Separatist artillery flashes"
    ),
    "wookiee-warriors": (
        "Wookiee warriors with bowcasters and wooden shields on Kashyyyk treetop platforms "
        "fighting alongside clone troopers beneath massive wroshyr trees and mist"
    ),
    "republic-navy": (
        "Venator-class Star Destroyers and Acclamator assault ships in formation above a "
        "battle-scarred planet with ARC-170 and V-wing starfighters launching from open bays"
    ),
    "jedi-generals": (
        "Jedi Generals with ignited lightsabers leading clone battalions across a Geonosis-style "
        "battlefield with dust, droid wreckage, and golden sunset rim light"
    ),
    "stormtrooper-corps": (
        "Columns of white-armored stormtroopers patrolling a grey Imperial city avenue with "
        "TIE fighters screaming overhead and searchlights cutting through smog at twilight"
    ),
    "death-troopers": (
        "Black-armored death troopers guarding a classified Imperial research facility on a "
        "volcanic world with green holographic data streams and crimson guard lights"
    ),
    "scout-troopers": (
        "Scout troopers on 74-Z speeder bikes weaving through Endor's towering redwood forest "
        "with sunlight shafts and distant rebel traps among the ferns"
    ),
    "imperial-navy": (
        "Imperial Star Destroyer fleet and TIE fighter swarms blockading a blue world with "
        "Executor-class silhouette looming in a violet nebula backdrop"
    ),
    "imperial-army": (
        "AT-AT walkers and AT-ST scouts advancing across Hoth's icy plains with snowtrooper "
        "escorts and blizzard wind tearing through tattered Imperial banners"
    ),
    "royal-guard": (
        "Emperor's Royal Guard in crimson robes and polished helmets standing at attention in a "
        "dark throne room antechamber with obsidian columns and pulsing red ambient light"
    ),
    "rebel-troopers": (
        "Rebel troopers in olive field gear manning a trench on a forest moon with homemade "
        "barricades, ion rifles, and an orange rebel starbird flag rippling in wind"
    ),
    "rebel-pathfinders": (
        "Rebel pathfinders in camouflage assaulting a tropical Imperial bunker with satchel "
        "charges, Y-wing flyover shadows, and palm fronds torn by blaster fire"
    ),
    "rebel-fleet": (
        "Mon Calamari cruisers and Nebulon-B frigates massing in orbit above Yavin with "
        "X-wings and corvettes preparing for a coordinated strike"
    ),
    "rogue-squadron": (
        "Rogue Squadron X-wings skimming a Death Star trench with exhaust port target lock glow "
        "and distant turbolaser bursts painting the black hull in orange light"
    ),
    "massassi-group": (
        "Rebel Massassi Group command center inside Yavin 4's stone temple hangar with "
        "starfighters under tarps, holo battle maps, and jungle vines on ancient walls"
    ),
    "b1-battle-droids": (
        "Massed B1 battle droids marching across Geonosis red rock arenas with STAP patrols "
        "and Lucrehulk battleship silhouettes in a dusty orange sky"
    ),
    "super-battle-droids": (
        "B2 super battle droids with wrist blasters advancing through a shattered Separatist "
        "factory with sparks, conveyor belts, and teal foundry glow"
    ),
    "droidekas": (
        "Droideka destroyer droids deployed with glowing personal shield domes on a polished "
        "Trade Federation bridge deck facing down clone infantry"
    ),
    "magna-guards": (
        "IG-100 MagnaGuards with electrostaffs and cape-like robes flanking a shadowy general "
        "atop a Separatist command spire during a lightning storm"
    ),
    "separatist-navy": (
        "Providence-class destroyers and vulture droid swarms engaging Republic Venators above "
        "a ringed gas giant with debris trails and ion cannon flashes"
    ),
    "techno-union-droids": (
        "Techno Union foundry world with assembly lines of skeletal battle droids, maglev cargo "
        "rails, and yellow hazard lights reflecting on oily factory floors"
    ),
    "flametroopers": (
        "First Order flametroopers incinerating a Resistance outpost on a scorched highland "
        "with roaring flamethrower arcs and blackened snow"
    ),
    "snowtroopers": (
        "First Order snowtroopers guarding a frozen mountain trench carved into Starkiller Base "
        "with red banner poles and aurora light over ice cliffs"
    ),
    "first-order-navy": (
        "Resurgent-class Star Destroyers and TIE/fo squadrons emerging from hyperspace above "
        "a burning Hosnian-era world with stark white hulls and crimson insignia glow"
    ),
    "knights-of-ren": (
        "Knights of Ren with mismatched dark armor and crackling red lightsabers on a ash-covered "
        "Sith world with ruined statues and smoke pillars"
    ),
    "resistance-troopers": (
        "Resistance troopers in hangar bay eight on D'Qar preparing blaster rifles beside "
        "orange resistance insignia panels and patched starfighter wings"
    ),
    "resistance-navy": (
        "Resistance MC85 cruiser Raddus leading a ragtag fleet through a violet nebula with "
        "T-70 X-wings and medical frigates in escort formation"
    ),
    "resistance-bombers": (
        "Resistance MG-100 StarFortress bombers dropping proton ordnance over a First Order "
        "dreadnought with cobalt squadron markings and flak bursts"
    ),
    "resistance-starfighter-corps": (
        "Resistance starfighter corps launching T-70 X-wings from a cliff-side base at sunrise "
        "with ion drives igniting and ocean spray below the runway"
    ),
    "new-republic-defense-fleet": (
        "New Republic Defense Fleet Mon Cal cruisers and X-wings patrolling a peaceful green "
        "member world with golden senate spires visible through clouds"
    ),
    "new-republic-soldiers": (
        "New Republic peacekeeping soldiers in blue-grey armor deploying on a city plaza with "
        "restored banners and civilian crowds under calm skies"
    ),
    "rapier-squadron": (
        "Rapier Squadron New Republic X-wings in close formation above Chandrila's oceans with "
        "contrails and distant training targets over the waves"
    ),
    "death-watch": (
        "Death Watch Mandalorian warriors with blue and grey armor on a Mandalore overlook at "
        "sunset with jetpacks, rally banners, and domed capital city below"
    ),
    "nite-owls": (
        "Nite Owls Mandalorians led by Bo-Katan with owl-themed helmets assaulting a "
        "Sundari palace balcony under indigo twilight and beskar sparks"
    ),
    "mandalorian-super-commandos": (
        "Imperial-aligned Mandalorian super commandos in red and black armor occupying a "
        "Mandalore street with occupation banners and Kom'rk fighters overhead"
    ),
    "mandalorian-fleet": (
        "Mandalorian Kom'rk-class assault fighters and cruisers emerging from a nebula with "
        "beskar-hulled warships and warrior clans visible on open decks"
    ),
    "nightsister-warriors": (
        "Nightsister warriors with staffs and magick green mist on Dathomir's swamp fortress "
        "with twisted trees, torchlight, and lightning over stone spires"
    ),
    "gungan-grand-army": (
        "Gungan Grand Army with shielded formations, kaadu cavalry, and booma catapults on "
        "Naboo's grassy plains beneath rolling thunderclouds"
    ),
    "naboo-royal-security-forces": (
        "Naboo Royal Security Forces and crimson Royal Guard in polished Theed palace courtyards "
        "with marble arches, waterfalls, and N-1 starfighters on nearby pads"
    ),
    "trade-federation-army": (
        "Trade Federation battle droid army deploying from C-9979 landing craft during the "
        "Naboo blockade with Lucrehulk sphere ships dominating a green world's sky"
    ),
    "hutt-cartel-enforcers": (
        "Hutt cartel enforcers with Gamorrean guards and armed mercenaries in a Tatooine palace "
        "courtyard with twin suns, sail barge silhouettes, and spice bazaar smoke"
    ),
    "crimson-dawn-soldiers": (
        "Crimson Dawn syndicate soldiers in crimson and black armor on a neon-lit urban underworld "
        "dock with stealth ships and holographic syndicate emblems"
    ),
    "pyke-syndicate-forces": (
        "Pyke syndicate guards escorting spice railcars through Oba Diah's industrial canyon "
        "with green-tinted smog, refinery towers, and armed convoy lights"
    ),
    "black-sun-enforcers": (
        "Black Sun enforcers in stealth armor on a Falleen crime lord's jungle palace terrace "
        "with black starfighters parked below and violet sunset haze"
    ),
}


def load_military_units() -> list[dict[str, str]]:
    text = DATA_FILE.read_text(encoding="utf-8")
    units: list[dict[str, str]] = []
    for match in UNIT_CALL.finditer(text):
        faction_slug, slug, name, unit_type, description, color = match.groups()
        units.append(
            {
                "factionSlug": faction_slug,
                "slug": slug,
                "name": name,
                "unitType": unit_type,
                "description": description,
                "color": color,
            }
        )
    return units


def unit_prompt(entry: dict[str, str]) -> str:
    scene = UNIT_SCENES.get(
        entry["slug"],
        f"Epic cinematic battlefield establishing shot of {entry['name']}, "
        f"{entry['unitType'].lower()} forces of the {entry['factionSlug'].replace('-', ' ')}. "
        f"{entry['description']}",
    )
    return f"{scene}. {STYLE_SUFFIX}"


def hero_filename(entry: dict[str, str]) -> str:
    return f"{entry['factionSlug']}-{entry['slug']}-hero.webp"


def all_military_unit_prompts() -> dict[str, str]:
    return {hero_filename(entry): unit_prompt(entry) for entry in load_military_units()}


if __name__ == "__main__":
    prompts = all_military_unit_prompts()
    print(f"Generated {len(prompts)} military unit hero prompts")
