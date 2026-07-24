#!/usr/bin/env python3
"""Cinematic hero-banner prompts for individual Droid Directory entries."""

from __future__ import annotations

STYLE_SUFFIX = (
    "Cinematic Star Wars digital illustration hero banner, 1536x1024, 16:9. "
    "Hyper-detailed sci-fi matte painting, dramatic rim lighting, rich atmospheric depth, "
    "premium encyclopedia header art quality. No text, no logos, no watermarks."
)

# slug -> visual scene description (avoid proper names in generation prompts)
DROID_HERO_PROMPTS: dict[str, str] = {
    "r2-d2": "A brave blue-and-white domed astromech repair droid with a red optical sensor, centered in a rebel starfighter hangar with fighter silhouettes and warm engine glow",
    "c-3po": "A tall golden humanoid protocol translator droid with polished plating and elegant posture, inside a luxurious starship corridor with holo displays and amber lighting",
    "bb-8": "An orange and white spherical rolling astromech droid with free-moving head dome, crossing a Resistance base hangar with starlight through blast doors",
    "k-2so": "Tall black Imperial security droid with skeletal frame and glowing photoreceptors, standing in a rainy Scarif beach assault with rebel troops in background haze",
    "chopper": "Battle-scarred orange and grey C1 astromech with mismatched parts and attitude, aboard the Ghost starship cockpit over Lothal clouds at sunset",
    "hk-47": "Red-armored assassin droid with angular chassis and rifle posture, on a dusty Taris rooftop under twin moons with neon city sprawl below",
    "hk-50": "Sleek red HK-series assassin droid disguised among protocol units, inside a Peragus mining facility with steam and emergency red lighting",
    "hk-51": "Mass-produced red HK assassin droid in combat stance, on a SWTOR-era battlefield with energy shields and distant capital ships",
    "ig-88": "Tall thin silver assassin droid with elongated head and multiple arms, in a smoky bounty hunter docking bay with holo wanted screens",
    "ig-11": "Silver assassin droid cradling an infant silhouette in soft light, Mandalorian camp at twilight with protective gentle mood",
    "t3-m4": "Blue astromech companion droid beside ancient Jedi ruins on Taris, green rakghoul mist and broken columns in background",
    "bd-1": "Small bird-like exploration droid with glowing blue sensor, deep Ilum ice cave with kyber crystal luminosity and fallen Jedi statues",
    "t7-o1": "Purple-accent astromech with friendly posture, Old Republic Tython training grounds and ancient temple steps",
    "g0-t0": "Spherical floating G0-T0 planning droid with red core eye, Nar Shaddaa neon skyline and smuggler traffic lanes",
    "b1-battle-droid": "Thin skeletal tan battle droid infantry row on Geonosis red desert with droid factory spires and Trade Federation staging",
    "b2-super-battle-droid": "Bulky wrist-mounted super battle droid advancing through Clone Wars urban rubble with smoke and laser fire bokeh",
    "droideka": "Rolling destroyer droid deployed with shield shimmer and twin blasters, Theed palace plaza battle with polished marble reflections",
    "bx-commando-droid": "Black commando battle droid with white markings in stealth crouch, Rishi moon listening post corridor with red alarm lights",
    "magnaguard": "Cape-wearing electrostaff guard droid with rigid posture, General Grievous flagship bridge with holographic star charts",
    "tactical-droid": "Tall narrow tactical droid with yellow photoreceptor band, Separatist command center overlooking fleet deployment",
    "super-tactical-droid": "Imposing super tactical droid with armored shoulders, Muun officer silhouettes and banking clan war room",
    "vulture-droid": "Bat-wing vulture droid starfighter transforming in orbit above Coruscant with traffic lanes and planet curve",
    "buzz-droid": "Small spidery buzz droid crawling on starfighter hull in zero-g with planet limb and laser scorch marks",
    "hailfire-droid": "Wheel-driven hailfire droid launching missiles, Geonosis arena horizon with dust trails and distant AT-TE silhouettes",
    "dwarf-spider-droid": "Four-legged dwarf spider droid on Utapau sinkhole ledge with mist and clone trooper scale reference",
    "octuptarra-droid": "Three-eyed octuptarra tri-droid on Utapau platforms with tri-barrel cannons and industrial catwalks",
    "probe-droid": "Spindly Imperial probe droid on Hoth ice ridge during blizzard with AT-AT walkers far in whiteout",
    "it-o": "Black floating interrogation droid with needle arms, Death Star detention block corridor with cold blue cells",
    "2-1b": "White medical droid with red cross emblem treating wounded in rebel med bay under soft clinical lighting",
    "mse-6-mouse-droid": "Small boxy mouse droid scurrying along Death Star corridor with stormtrooper boots passing by",
    "gnk-power-droid": "Chunky GONK power droid on Tatooine moisture farm at twin sunset with vaporators and sand glow",
    "pit-droid": "Compact orange pit droid tightening bolts in Mos Espa podrace pit lane with crowd blur and flags",
    "dark-trooper": "Heavy black dark trooper phase III in Moff Gideon cruiser hangar with blue magnetic lift glow",
    "0-0-0": "Sinister golden protocol-assassin hybrid droid with exposed weapons, Darth Vader's castle workshop shadows",
    "bt-1": "Round black assassin torpedo droid with red eye, Dr Aphra ship corridor with sparking panels",
    "l3-37": "Self-modified protocol droid with exposed wiring and attitude, Kessel spice mine revolt with chains and industrial pipes",
    "d-o": "Small anxious wheeled droid with stammering posture, Sith wayfinder desert ruins with ancient stone and windblown sand",
    "r5-d4": "Red-domed astromech with bad motivator sparking, Lars homestead garage with Tatooine afternoon heat haze",
    "4-lom": "Insectoid-headed bounty hunter droid with respirator, Bespin cloud city external platform and orange sky",
    "ev-9d9": "Bird-like torture droid overseer on Jabba's palace dungeon balcony with furnace glow below",
    "8d8": "Thin torture droid attendant in Jabba palace throne room shadows with chains and greenish torchlight",
    "aqua-droid": "Aquatic battle droid emerging from Mon Calamari ocean battle with bioluminescent water spray",
    "lr-57-combat-droid": "Crab-legged retail droid sentry on Christophsis crystal battlefield with blue hex shield walls",
    "oom-command-battle-droid": "Yellow-marked OOM command battle droid gesturing on Trade Federation bridge with nebula viewport",
    "fa-4-pilot-droid": "Pilot battle droid in Vulture droid cockpit with Separatist insignia HUD glow",
    "ap-5": "Gangly rebel supply protocol droid with exasperated pose, Phoenix Squadron cargo bay inventory stacks",
    "war-droid-mark-iv": "Ancient Mark IV war droid relic activated in Korriban tomb with Sith holocron light",
    "mark-vii-inquisitor-droid": "Spiked inquisitor droid in Imperial base interrogation chamber with red holographic evidence boards",
    "s-0d": "Sith-aligned protocol droid with dark gold plating, ancient Sith academy archive shelves",
    "b-4d4": "Administrative protocol droid in Trade Federation bureaucracy office with endless data stacks",
    "asp-7-labor-droid": "Heavy labor droid lifting cargo crates in Coruscant underlevel dock with speeder traffic overhead",
    "wed-treadwell": "Multi-arm treadwell repair droid in moisture farm workshop surrounded by tools and vaporator parts",
    "tt-8l-gatekeeper": "Retractable eye gatekeeper droid embedded in Jabba palace door with orange security scanner beam",
    "asn-courier-droid": "Courier droid with message tube on Coruscant mid-level walkway rain and holographic ads",
    "ric-920": "RIC pit droid variant polishing a podracer engine in Boonta Eve eve pit with neon reflections",
    "pk-worker-droid": "PK worker droid assembling components in droid factory line matching directory hero factory aesthetic",
    "crab-droid": "Crab droid climbing Separatist fortress wall during aquatic invasion with spray and laser impacts",
    "firefighter-b1": "Firefighter battle droid with suppression tank on Republic cruiser hangar fire with foam and steam",
    "rocket-battle-droid": "Rocket battle droid with jetpack over Coruscant orbital shipyard with open space and construction beams",
    "b3-ultra-battle-droid": "Massive ultra battle droid towering over clone troopers in devastated city square",
    "scorpenek-annihilator": "Enormous scorpenek annihilator droid with shield dome on Arvala-7 desert with Mandalorian camp scale",
    "kx-security-droid": "KX security droid patrol in Imperial facility white corridors with detention blocks",
    "ra-7": "Black RA-7 bug-eyed protocol droid in Death Star conference room with Death Star hologram table",
    "cl-4d-4": "Administrative protocol droid in Cloud City bureaucracy office with Bespin sunset windows",
    "j9-worker-droid": "J9 worker droid maintaining reactor conduits in industrial Core shipyard catwalks",
    "r2-q5": "Black Imperial astromech with red sensors in Death Star II maintenance bay with imperial engineers",
    "r4-p17": "Red-domed astromech plugged into Jedi starfighter socket in Clone Wars hangar",
    "r3-s6": "Gold-domed traitor astromech with hidden blaster reveal, Jedi cruiser vent shaft shadows",
    "r2-kt": "Pink-accent charity astromech R2-KT at rebel base celebration with balloons and warm lights",
    "fx-7": "Multi-arm FX-7 medical droid over Hoth bacta tank with Luke silhouette submerged glow",
    "tc-14": "Feminine silver TC-14 protocol droid greeting Trade Federation delegation in palace antechamber",
    "oom-9": "OOM-9 tactical droid commander overlooking Naboo invasion holographic map table",
    "proxy": "Shapeshifting PROXY droid mid-transformation between holo forms on Starkiller base snow trench",
    "u9-c4": "Green-accent astromech in Old Republic flashpoint battlefield wreckage with energy fires",
    "r1-g4": "Grey R1-series astromech in junkyard sale row on Tatooine with Jawas and sandcrawler silhouette",
    "c-21-highsinger": "Heavy weapons bounty droid with multiple arms in post-battle cantina smoke and sparks",
    "id-9-seeker-droid": "Imperial seeker probe with aggressive red sensor hunting rebels on Lothal grasslands at dusk",
    "mse-14": "Imperial mouse droid variant on Star Destroyer bridge cable trench with rank insignia glow",
    "lothal-astromech": "Orange-accent Lothal-built astromech in Imperial-occupied Lothal city street with graffiti resistance tags",
}


def prompt_for(entry: dict) -> str:
    slug = entry["slug"]
    base = DROID_HERO_PROMPTS.get(slug)
    if not base:
        name = entry["name"]
        dtype = entry["droid_type"]
        mfr = entry["manufacturer"]
        base = (
            f"{name}, a {dtype.lower()} manufactured by {mfr}, hero portrait centered "
            f"in a cinematic Star Wars factory hangar with teal industrial lighting and assembly lines"
        )
    return f"{base}. {STYLE_SUFFIX}"


def all_prompts(entries: list[dict]) -> dict[str, str]:
    return {e["slug"]: prompt_for(e) for e in entries}
