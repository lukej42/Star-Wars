#!/usr/bin/env python3
"""Distinct cinematic scene descriptions for Wars & Conflicts hero banners."""

from __future__ import annotations

STYLE_PREFIX = (
    "Photorealistic cinematic Star Wars live-action film still hero banner, 1536x1024, 16:9. "
    "Hyper-realistic practical effects quality matching all nine saga films, Clone Wars, Rebels, "
    "The Mandalorian, Knights of the Old Republic, and Old Sith Empire visuals. "
    "Film grain, dramatic rim lighting, IMAX composition. "
)

STYLE_SUFFIX = " No text, no logos, no watermarks, no readable lettering."

WAR_SCENES: dict[str, str] = {
    "clone-wars": (
        "Panoramic Clone Wars battlefield on Geonosis red rock spires with white clone troopers "
        "advancing against silver battle droid legions, LAAT gunships streaking overhead and "
        "Separatist core ships on the horizon"
    ),
    "galactic-civil-war": (
        "Rebel Alliance X-wing and Y-wing squadrons diving past a massive Imperial Star Destroyer "
        "while ground forces clash on a burning colony world under twin suns"
    ),
    "mandalorian-wars": (
        "Mandalorian Neo-Crusaders in blue armor riding Basilisk war droids across a scorched "
        "Republic world while Jedi defenders hold a shattered fortress line"
    ),
    "great-sith-war": (
        "Exar Kun's Sith Massassi warriors and Krath cultists assaulting the Jedi library world "
        "Ossus as green Force storms tear the sky above falling temple spires"
    ),
    "great-galactic-war": (
        "Sith Empire Harrower battlecruisers bombarding Coruscant's senate district with "
        "Republic troop transports burning in orbit and invasion dropships descending"
    ),
    "stark-hyperspace-war": (
        "Trade Federation Lucrehulk blockade sphere and corporate frigates encircling Troiken "
        "while Republic Judicial Forces and Stark Commercial Combine soldiers clash on icy ridges"
    ),
    "hundred-year-darkness": (
        "Fallen Dark Jedi and loyalist Jedi Order knights facing each other on volcanic Corbos "
        "with crimson Force lightning arcing between ancient temple ruins"
    ),
    "new-sith-wars": (
        "Brotherhood of Darkness Sith armies and Republic Light Army soldiers locked in close "
        "combat across misty Ruusan valleys before the thought bomb horizon glow"
    ),
    "cold-war": (
        "Resistance T-70 X-wings skimming red salt flats on Crait while First Order AT-M6 walkers "
        "and Resurgent-class Star Destroyers advance under a blood-red sky"
    ),
    "great-war": (
        "SWTOR-era Republic Havoc Squad and Sith Imperial troopers fighting amid burning "
        "Corellian skyscrapers while orbital bombardment flashes reflect off durasteel towers"
    ),
}

BATTLE_SCENES: dict[str, str] = {
    # Clone Wars
    "first-battle-of-geonosis": (
        "First Battle of Geonosis arena spillover: clone trooper platoons in white armor firing "
        "blaster rifles at advancing B1 battle droids and droidekas on red Geonosis rock fields, "
        "AT-TE walkers and Hailfire droids exchanging fire, LAAT/i gunships dropping reinforcements"
    ),
    "battle-of-coruscant": (
        "Battle of Coruscant orbital siege: Venator and Separatist warships colliding above the "
        "city-planet while ARC-170 starfighters weave through turbolaser fire over the senate dome"
    ),
    "battle-of-utapau": (
        "Battle of Utapau sinkhole city: 212th clone troopers on varactyl mounts pursuing battle "
        "droids across tiered Pau'an platforms with UT-AT walkers descending the chasms"
    ),
    "battle-of-kashyyyk": (
        "Battle of Kashyyyk treetop war: clone troopers and Wookiee warriors defending wooden "
        "platforms from droid invaders among giant wroshyr trees and misty canopy"
    ),
    "siege-of-mandalore": (
        "Siege of Mandalore capital: 501st clone troopers and Bo-Katan's Nite Owls assaulting "
        "Maul's Shadow Collective holdout amid domed city rooftops under orange twilight"
    ),
    "battle-of-mon-cala": (
        "Battle of Mon Cala underwater conflict: Republic SCUBA clone troopers and Mon Calamari "
        "militia battling Quarren and Separatist aqua droids in bioluminescent ocean trenches"
    ),
    "jedi-purge": (
        "Jedi Purge Order 66 on Coruscant: clone troopers firing blaster rifles at a Jedi Knight "
        "defending the Temple's columned entrance while smoke rises from the High Council spire "
        "and crimson emergency lighting washes the sacred steps"
    ),
    # Galactic Civil War
    "battle-of-yavin": (
        "Battle of Yavin trench run: Rebel X-wings diving through the Death Star meridian trench "
        "pursued by TIE fighters with Yavin 4's green moon looming in the background"
    ),
    "battle-of-hoth": (
        "Battle of Hoth ice plain: snowspeeders harpooning AT-AT walkers across blizzard-white "
        "tundra while Rebel soldiers retreat toward Echo Base's shield generator"
    ),
    "battle-of-endor": (
        "Battle of Endor forest moon: Ewok ambushes and Rebel commandos attacking Imperial "
        "shield bunker while Millennium Falcon leads starfighters toward the unfinished Death Star"
    ),
    "battle-of-scarif": (
        "Battle of Scarif tropical beachhead: Rogue One rebels transmitting Death Star plans "
        "while AT-ACT walkers and shore troopers advance through palm-lined surf under orbital barrage"
    ),
    "battle-of-jakku": (
        "Battle of Jakku desert wreckage field: New Republic Star Destroyers crashing into sands "
        "while X-wings and TIE remnants dogfight above fallen Imperial walkers"
    ),
    "assault-on-cloud-city": (
        "Assault on Cloud City: Imperial stormtroopers marching through Bespin's golden corridors "
        "as carbon-freeze chamber steam billows and Cloud Cars flee the occupied platform city"
    ),
    # Mandalorian Wars
    "battle-of-malachor-v": (
        "Battle of Malachor V superweapon site: Revan's Republic forces and Mandalorian clans "
        "trapped around a mass shadow generator crater with fractured ground and violet energy"
    ),
    "battle-of-dxun": (
        "Battle of Dxun Onderon moon jungle: Mandalorian beskar-clad raiders ambushing Republic "
        "soldiers among giant beast nests and dense moonlit foliage"
    ),
    "devastation-of-cathar": (
        "Devastation of Cathar: Mandalorian Basilisk war droids strafing feline Cathar refugees "
        "on coastal cliffs with burning settlements and blood-red sunset skies"
    ),
    "battle-of-telos-iv": (
        "Battle of Telos IV restoration world: Republic fleet bombarding Citadel Station orbit "
        "while Sith troopers and HK-series droids fight across sterile white recovery platforms"
    ),
    "siege-of-tar-is": (
        "Siege of Taris Undercity: Mandalorian shock troops descending into rust-red Taris slums "
        "while Republic defenders hold barricades beneath the upper city skyline"
    ),
    "battle-of-althir": (
        "Battle of Althir frozen tundra: Mandalorian Crusader columns advancing across ice fields "
        "against Republic artillery emplacements under aurora-lit polar skies"
    ),
    # Great Sith War
    "battle-of-ossus": (
        "Battle of Ossus Great Library: Jedi evacuating holocrons as Sith warships bombard "
        "mountain archives and Naga Sadow's forces storm terraced temple campuses"
    ),
    "battle-of-coruscant-great-sith-war": (
        "Battle of Coruscant Great Sith War: Krath cult war droids and Sith warriors breaching "
        "the Jedi Temple district while Coruscant skylines burn under crimson Force storms"
    ),
    "battle-of-yavin-4-exar-kun": (
        "Battle of Yavin 4 Exar Kun era: Massassi warriors constructing Sith temples while "
        "Republic forces land on jungle moon beaches under ancient pyramid silhouettes"
    ),
    "battle-of-kemplex-nine": (
        "Battle of Kemplex Nine Cron Cluster: Sith superweapon detonation ripping a nebula apart "
        "as Jedi starfighters flee collapsing stellar nurseries in blinding white light"
    ),
    "duel-on-ossus": (
        "Duel on Ossus between Jedi Master Ood Bnar rooted as a tree and Sith Lord Qordis amid "
        "falling library towers and emerald Force energy on a crumbling cliff"
    ),
    "sith-invasion-of-ossus": (
        "Sith invasion of Ossus landing beaches: Sith dropships unloading Massassi legions "
        "against Jedi barricades below the Great Jedi Library mesa at dawn"
    ),
    # Great Galactic War
    "sacking-of-coruscant": (
        "Sacking of Coruscant Treaty of Coruscant era: Sith Imperial troops marching through "
        "smoke-filled senate plaza while Jedi Temple spires burn and shuttles evacuate civilians"
    ),
    "battle-of-alderaan-great-galactic-war": (
        "Battle of Alderaan Great Galactic War: Sith invasion force landing on Alderaan's green "
        "hills while noble house soldiers and Republic troopers defend mountain passes"
    ),
    "recapture-of-korriban": (
        "Recapture of Korriban: Republic assault shuttles descending on red desert Valley of "
        "the Dark Lords as Sith acolytes defend ancient tombs beneath storm clouds"
    ),
    "battle-of-ilum-great-galactic-war": (
        "Battle of Ilum crystal caves Great Galactic War: Republic and Sith troopers fighting "
        "in icy blue caverns lit by exposed kyber crystal veins and frozen waterfalls"
    ),
    "siege-of-balmorra": (
        "Siege of Balmorra weapons factories: colossal war droid assembly lines exploding as "
        "Republic commandos and Sith marauders clash on industrial catwalks"
    ),
    "invasion-of-ord-mantell": (
        "Invasion of Ord Mantell junkyard plains: Sith drop pods landing among rusted starship "
        "hulks while Republic militia engage in close quarters across scrap canyons"
    ),
    # Stark Hyperspace War
    "battle-of-troiken": (
        "Battle of Troiken ice caves: Ithorian and Stark Combine soldiers sheltering in frozen "
        "caverns while Trade Federation droid army probes the blizzard outside"
    ),
    "battle-of-qika": (
        "Battle of Qika arid trade world: corporate security droids and Stark mercenaries "
        "defending spice convoy landing pads against Republic Judicial Forces"
    ),
    "battle-of-primus-goluud": (
        "Battle of Primus Goluud solar flare crisis: Jedi and Republic fleet caught in "
        "scorching red stellar radiation above a dying star with failing deflector shields"
    ),
    "stark-alliance-collapse": (
        "Stark Alliance collapse summit chaos: holographic treaty tables shattering as corporate "
        "fleets withdraw and panicked diplomats flee a orbiting conference station"
    ),
    "coruscant-financial-crisis": (
        "Coruscant financial crisis riots: senate district crowds and corporate lobbyists "
        "clashing with Republic security droids beneath towering banking spires after Stark fallout"
    ),
    # Hundred-Year Darkness
    "battle-of-corbos": (
        "Battle of Corbos volcanic purge: Dark Jedi exiles and loyalist Jedi knights dueling "
        "on basalt plains with lava rivers and collapsing obsidian fortresses"
    ),
    "fall-of-the-dark-jedi": (
        "Fall of the Dark Jedi schism: robed fallen Jedi facing their former brethren on a "
        "storm-wracked temple plateau as Force lightning splits the sky"
    ),
    "sith-exodus": (
        "Sith Exodus starship departure: battered exiled Dark Jedi fleet fleeing known space "
        "into unknown hyperspace routes beyond the Republic frontier nebula"
    ),
    "battle-of-tython": (
        "Battle of Tython ancient cradle: early Je'daii masters channeling Force storms on "
        "mountain mesas while dark-side schismatics assault the first temple city"
    ),
    "duel-of-the-first-sith": (
        "Duel of the First Sith Lords on a desolate alien world: two armored Sith founders "
        "crossing red lightsabers amid thunder and crimson aurora over Sith temple foundations"
    ),
    # New Sith Wars
    "battle-of-ruusan": (
        "Battle of Ruusan mist valleys: Jedi Army of Light and Brotherhood of Darkness infantry "
        "exchanging blaster and lightsaber fire across fog-shrouded Ruusan hills"
    ),
    "seventh-battle-of-ruusan": (
        "Seventh Battle of Ruusan final campaign: Lord Kaan's Sith forces charging Jedi "
        "fortifications under grey storm clouds before the thought bomb valley"
    ),
    "thought-bomb-detonation": (
        "Thought bomb detonation cavern: blinding violet Force energy sphere consuming Sith "
        "and Jedi spirits in Ruusan underground chasm with collapsing rock faces"
    ),
    "battle-of-jabiim-new-sith-wars": (
        "Battle of Jabiim New Sith Wars mud front: Republic soldiers and Sith troopers slogging "
        "through rain-soaked trenches on Jabiim's industrial mining plateaus"
    ),
    "sith-brotherhood-collapse": (
        "Sith Brotherhood collapse on Ruusan ridge: rival Sith warlords turning on each other "
        "as Jedi scouts observe from distant cliffs before the final thought bomb"
    ),
    "reformation-of-the-jedi-order": (
        "Reformation of the Jedi Order Ruusan aftermath: surviving Jedi knights gathering "
        "younglings on a quiet hillside as Ruusan mists clear and new galactic peace begins"
    ),
    # Cold War (First Order)
    "destruction-of-hosnian-prime": (
        "Destruction of Hosnian Prime: Starkiller Base superlaser beam splitting across Hosnian "
        "system worlds with New Republic fleet disintegrating in silent orbital fireballs"
    ),
    "battle-of-starkiller-base": (
        "Battle of Starkiller Base snow trenches: Resistance X-wings attacking oscillator "
        "facility while Han Solo's team plants charges inside icy First Order megastructure"
    ),
    "battle-of-crait": (
        "Battle of Crait salt flats: Resistance speeders leaving red dust trails skimming toward "
        "First Order AT-M6 walkers as Luke Skywalker projects Force illusion on horizon"
    ),
    "battle-of-exegol": (
        "Battle of Exegol Sith Eternal fleet: thousands of Xyston-class Star Destroyers rising "
        "from lightning-lit canyons as Lando's citizen fleet and Resistance starfighters arrive"
    ),
    "battle-of-takodana": (
        "Battle of Takodana castle ruins: First Order TIE fighters strafing Maz Kanata's lakeside "
        "fortress while Resistance reinforcements land in misty forest clearings"
    ),
    "battle-of-d-qar": (
        "Battle of D'Qar Resistance base evacuation: First Order dreadnought bombardment of "
        "orange desert outpost while Resistance bombers launch last-ditch trench attack"
    ),
    # Great War (SWTOR)
    "battle-of-corellia": (
        "Battle of Corellia metropolitan warzone: Havoc Squad and Sith Warriors fighting through "
        "Corellian corvette shipyards with burning sky bridges and orbital strikes"
    ),
    "battle-of-alderaan-great-war": (
        "Battle of Alderaan Great War castle siege: House Organa soldiers and Republic troopers "
        "defending marble palaces against Sith Imperial invasion on green Alderaan highlands"
    ),
    "battle-of-ilum-great-war": (
        "Battle of Ilum Great War ice plains: Republic and Imperial forces clashing near "
        "exposed kyber crystal pillars on windswept frozen tundra under aurora skies"
    ),
    "battle-of-makeb": (
        "Battle of Makeb hovering continent: Hutt Cartel mercenaries and Republic strike teams "
        "fighting on Makeb's unstable floating mesas above toxic green cloud layers"
    ),
    "siege-of-kaon": (
        "Siege of Kaon Sith factory world: Imperial troopers defending weapon forges while "
        "Republic assault pods breach red-lit industrial hive spires"
    ),
    "fall-of-balmorra-great-war": (
        "Fall of Balmorra Great War final offensive: colossal Imperial war droids crushing "
        "Republic barricades outside Balmorran arms factories at dusk"
    ),
}


def war_prompt(name: str, slug: str) -> str:
    scene = WAR_SCENES.get(slug, f"Epic cinematic battlefront of the {name}")
    return f"{STYLE_PREFIX}{scene}.{STYLE_SUFFIX}"


def battle_prompt(name: str, slug: str, era: str, war_slug: str) -> str:
    scene = BATTLE_SCENES.get(
        slug,
        f"Cinematic depiction of the {name} ({era}) with distinct armies, starfighters, "
        f"and environment unique to this engagement during the {war_slug.replace('-', ' ')}",
    )
    return f"{STYLE_PREFIX}{scene}.{STYLE_SUFFIX}"
