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
    "battle-of-anaxes": (
        "Republic naval yard siege on Anaxes with Bad Batch commandos infiltrating Separatist algorithm core while Venator Star Destroyers exchange turbolaser fire over shipyards"
    ),
    "battle-of-boz-pity": (
        "Republic assault on Separatist hospital world Boz Pity with gunships landing amid ruined medical towers while Asajj Ventress and General Grievous counterattack"
    ),
    "battle-of-cato-neimoidia": (
        "Plo Koon's starfighter wing patrolling bridge cities of Cato Neimoidia when clone wingmen open fire during Order 66 over the Neimoidian purse world"
    ),
    "battle-of-christophsis": (
        "Clone troopers and Jedi Generals Anakin Skywalker and Obi-Wan Kenobi defending crystal cities from Separatist droid armies while AV-7 Anti-Vehicle cannons fire across Christophsis skyline"
    ),
    "battle-of-coruscant": (
        "Cinematic Battle of Coruscant (19 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    "battle-of-felucia": (
        "Jungle war on Felucia's fungal plains as Aayla Secura's clone troopers advance through giant mushroom forests before Order 66 turns their blasters on their Jedi commander"
    ),
    "battle-of-kashyyyk": (
        "Cinematic Battle of Kashyyyk (19 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    "battle-of-malastare": (
        "Republic electro-proton bomb detonating on Malastare plains to collapse Separatist droid ranks while the Zillo Beast awakens beneath the battlefield rubble"
    ),
    "battle-of-mon-cala": (
        "Cinematic Battle of Mon Cala (20 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    "battle-of-mygeeto": (
        "Ki-Adi-Mundi leading clone troopers across Mygeeto's crystalline ice bridges while Separatist banking clan droids defend InterGalactic Banking Clan vaults under aurora skies"
    ),
    "battle-of-quell": (
        "Republic cruiser convoy ambushed over Quell as Ahsoka Tano and Anakin Skywalker crash-land on a Resolute-class carrier amid flaming debris and vulture droid swarms"
    ),
    "battle-of-ringo-vinda": (
        "Orbital ring-world battle station above Ringo Vinda with Tup's inhibitor chip malfunction triggering premature Order 66 execution in a crowded clone trooper barracks"
    ),
    "battle-of-ryloth": (
        "Republic LAAT gunships and Mace Windu's assault force liberating Ryloth's dusty mesas from Separatist occupation while Twi'lek resistance fighters ambush droid patrols"
    ),
    "battle-of-saleucami": (
        "Stass Allie's 91st Mobile Recon Corps pursuing Separatist forces across Saleucami's misty wetlands on speeder bikes before clone troopers execute Order 66"
    ),
    "battle-of-sullust": (
        "Asajj Ventress and Count Dooku dueling amid volcanic Sullust factory districts while Separatist and Republic starfighter wings clash over glowing magma vents"
    ),
    "battle-of-umbara": (
        "501st clone troopers marching through bioluminescent Umbaran jungle under treasonous General Pong Krell while AT-RT scouts clash with shadowy Umbaran militia"
    ),
    "battle-of-utapau": (
        "Cinematic Battle of Utapau (19 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    "defense-of-kamino": (
        "Tipoca City under aquatic assault as Separatist aqua droids and Trident drills breach Kamino cloning facilities while ARC troopers and Jedi defend the rainy ocean platforms"
    ),
    "first-battle-of-geonosis": (
        "Cinematic First Battle of Geonosis (22 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    "jedi-purge": (
        "Cinematic Jedi Purge (19 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    "second-battle-of-geonosis": (
        "Republic forces assaulting Geonosis droid foundries with AT-TE walkers crossing red rock plains while Luminara Unduli and Anakin Skywalker strike the primary factory complex"
    ),
    "siege-of-mandalore": (
        "Cinematic Siege of Mandalore (19 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Clone Wars engagement"
    ),
    # Cold War (First Order)
    "assault-on-starkiller-base-trench": (
        "Resistance X-wings diving through Starkiller Base thermal oscillator trenches while Han Solo's strike team plants charges inside icy corridors"
    ),
    "attack-on-ahch-to": (
        "Luke Skywalker confronting Kylo Ren with a Force projection on Ahch-To's storm cliffs while Resistance evacuates from Crait in the distance"
    ),
    "battle-of-ajan-kloss": (
        "Resistance command center on Ajan Kloss mobilizing the final fleet muster against Exegol while starfighters launch through jungle canopy bunkers"
    ),
    "battle-of-crait": (
        "Cinematic Battle of Crait (34 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Cold War (First Order) engagement"
    ),
    "battle-of-d-qar": (
        "Cinematic Battle of D'Qar (34 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Cold War (First Order) engagement"
    ),
    "battle-of-exegol": (
        "Cinematic Battle of Exegol (35 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Cold War (First Order) engagement"
    ),
    "battle-of-kef-bir": (
        "Rey and Resistance strike team navigating Death Star II wreckage oceans on Kef Bir while First Order treadspeeders chase them across rusted superstructure"
    ),
    "battle-of-kijimi": (
        "First Order occupation troops patrolling Kijimi's snow alleys while Resistance saboteurs extract droidsmiths from crimson-lit workshops"
    ),
    "battle-of-ord-mantell-cold-war": (
        "Mandalorian covert team rescuing Grogu from Imperial remnant forces on Ord Mantell spaceport while TIE fighters strafe docking rings"
    ),
    "battle-of-pasaana": (
        "Speeder chase through Pasaana desert festival canyons as Resistance agents flee First Order jet troopers amid cheering crowds and spice mines"
    ),
    "battle-of-starkiller-base": (
        "Cinematic Battle of Starkiller Base (34 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Cold War (First Order) engagement"
    ),
    "battle-of-takodana": (
        "Cinematic Battle of Takodana (34 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Cold War (First Order) engagement"
    ),
    "destruction-of-hosnian-prime": (
        "Cinematic Destruction of Hosnian Prime (34 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Cold War (First Order) engagement"
    ),
    "siege-of-maz-kanatas-castle": (
        "First Order TIE fighters and stormtroopers destroying Maz Kanata's lakeside castle while Resistance X-wings arrive through forest canopy"
    ),
    # Galactic Civil War
    "assault-on-cloud-city": (
        "Cinematic Assault on Cloud City (3 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Galactic Civil War engagement"
    ),
    "battle-of-atollon": (
        "Grand Admiral Thrawn's Seventh Fleet blockading Atollon with Interdictor cruisers while Phoenix Squadron X-wings attempt to break through over coral mesas and Chopper Base"
    ),
    "battle-of-endor": (
        "Cinematic Battle of Endor (4 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Galactic Civil War engagement"
    ),
    "battle-of-hoth": (
        "Cinematic Battle of Hoth (3 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Galactic Civil War engagement"
    ),
    "battle-of-jakku": (
        "Cinematic Battle of Jakku (5 ABY) on the battlefield: armies, starfighters, and environmental details unique to this Galactic Civil War engagement"
    ),
    "battle-of-kessel": (
        "Millennium Falcon leading a spice mine revolt on Kessel while coaxium coaxing through the Kessel Run pursued by Imperial TIE patrols and pyke syndicate guards"
    ),
    "battle-of-mimban": (
        "Imperial mud trenches on Mimban with swamp troopers and Han Solo's infantry unit advancing through toxic fog while AT-HA walkers sink into the mire"
    ),
    "battle-of-scarif": (
        "Cinematic Battle of Scarif (0 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Galactic Civil War engagement"
    ),
    "battle-of-yavin": (
        "Cinematic Battle of Yavin (0 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Galactic Civil War engagement"
    ),
    "battle-on-eadu": (
        "Rebel commandos raiding Imperial kyber research facility on storm-lashed Eadu cliffs while X-wings strafe landing platforms above the research spire"
    ),
    "defense-of-naboo-galactic-civil-war": (
        "Rebel fleet and Naboo starfighters repelling Imperial Operation: Cinder bombardment of Naboo's oceans while Leia Organa coordinates planetary defense from Theed"
    ),
    "liberation-of-sullust": (
        "New Republic commandos and Sullustan resistance fighters seizing Imperial factory districts after Endor while Star Destroyer debris still burns in orbit"
    ),
    "siege-of-lothal": (
        "Imperial Star Destroyers bombarding Lothal's capital while Spectre cell rebels defend dome settlements and Ezra Bridger summons purrgil to cripple the blockade"
    ),
    "skirmish-on-jedha": (
        "Saw Gerrera's Partisans ambushing Imperial patrols in Jedha City's desert shrines while Kyber crystal convoys move toward the Death Star under crimson kyber-lit skies"
    ),
    # Great Galactic War
    "battle-of-alderaan-great-galactic-war": (
        "Cinematic Battle of Alderaan (Great Galactic War) (3667 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Galactic War engagement"
    ),
    "battle-of-ilum-great-galactic-war": (
        "Cinematic Battle of Ilum (Great Galactic War) (3665 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Galactic War engagement"
    ),
    "battle-of-manaan-great-galactic-war": (
        "Underwater Selkath cities on Manaan rocked by depth charges as Republic submersibles skirmish with Sith aqua troopers near kolto harvesting stations"
    ),
    "battle-of-quesh-great-galactic-war": (
        "Toxic Quesh venom refineries exploding as Republic and Sith troopers fight in hazmat armor amid yellow-green chemical fog"
    ),
    "battle-of-tython-great-galactic-war": (
        "Sith invasion force breaching Je'daii temple mesas on Tython with crimson saber fire reflecting off ancient stone arches"
    ),
    "battle-of-voss": (
        "Republic and Sith forces clashing on Voss's misty mountain plateaus near Mystic temples while Gormak war parties watch from ridgelines"
    ),
    "invasion-of-ord-mantell": (
        "Cinematic Invasion of Ord Mantell (3665 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Galactic War engagement"
    ),
    "recapture-of-korriban": (
        "Cinematic Recapture of Korriban (3681 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Galactic War engagement"
    ),
    "sacking-of-coruscant": (
        "Cinematic Sacking of Coruscant (3653 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Galactic War engagement"
    ),
    "siege-of-balmorra": (
        "Cinematic Siege of Balmorra (3667 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Galactic War engagement"
    ),
    "siege-of-nal-hutta-great-galactic-war": (
        "Republic blockade of Nal Hutta's polluted swamps while Hutt Cartel mercenaries negotiate with both Sith and Republic envoys under neon-lit palaces"
    ),
    "sith-assault-on-dromund-kaas": (
        "Republic infiltration teams sabotaging Sith citadel landing platforms on storm-wracked Dromund Kaas while Imperial guards mobilize in rain-swept plazas"
    ),
    "sith-invasion-of-taris": (
        "Sith Imperial troopers marching through Taris Undercity rubble while Republic evacuation transports lift off under orbital bombardment"
    ),
    "sith-victory-at-ziost": (
        "Sith Imperial occupation of Ziost's frozen citadels with dark-side ice storms swirling above ancient Sith monoliths and chained prisoners"
    ),
    # Great Sith War
    "assault-on-ossus-library": (
        "Jedi evacuating holocrons from Ossus Great Library mesas as Sith warships bombard mountain archives and Naga Sadow's forces storm terraced campuses"
    ),
    "battle-of-coruscant-great-sith-war": (
        "Cinematic Battle of Coruscant (Great Sith War) (3996 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Sith War engagement"
    ),
    "battle-of-foerost": (
        "Krath and Sith fleet capturing Republic shipyards at Foerost with Sith sorcery storms rolling over orbital construction rings and fleeing Jedi cruisers"
    ),
    "battle-of-kemplex-nine": (
        "Cinematic Battle of Kemplex IX (3996 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Sith War engagement"
    ),
    "battle-of-ossus": (
        "Cinematic Battle of Ossus (3996 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Sith War engagement"
    ),
    "battle-of-yavin-4-exar-kun": (
        "Cinematic Battle of Yavin 4 (Exar Kun) (3997 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Sith War engagement"
    ),
    "battle-of-cyax-system": (
        "Republic and Jedi fleet engaging Sith battle groups near Ossus with capital ship broadside exchanges lighting the nebula between wrecked frigates"
    ),
    "duel-on-ossus": (
        "Cinematic Duel on Ossus (3996 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Sith War engagement"
    ),
    "duel-on-yavin-4-great-sith-war": (
        "Exar Kun corrupting Jedi apprentices in Massassi temples on Yavin 4 jungle moon with Sith alchemical pyramids glowing under green canopies"
    ),
    "invasion-of-korriban-great-sith-war": (
        "Sith Massassi warriors reclaiming Korriban tombs while Republic expeditionary forces descend into the Valley of the Dark Lords under crimson storm clouds"
    ),
    "krath-coup-of-empress-teta": (
        "Krath cultists seizing Empress Teta's carbonite palaces with dark-side ritual fires reflecting off tetan spires as Jedi negotiators are massacred"
    ),
    "sith-bombardment-of-ambria": (
        "Sith fleet glassing Ambria's wasteland surface where Naddist cultists once ruled, Jedi evacuation shuttles lifting off through ash clouds"
    ),
    "sith-invasion-of-ossus": (
        "Cinematic Sith Invasion of Ossus (3996 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great Sith War engagement"
    ),
    # Great War (SWTOR)
    "battle-of-alderaan-great-war": (
        "Cinematic Battle of Alderaan (Great War) (3643 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great War (SWTOR) engagement"
    ),
    "battle-of-corellia": (
        "Cinematic Battle of Corellia (3641 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great War (SWTOR) engagement"
    ),
    "battle-of-dantooine-great-war": (
        "Republic troopers defending Dantooine agricultural settlements against Sith Imperial invasion dropships over grassy plains"
    ),
    "battle-of-dromund-kaas-great-war": (
        "Republic covert assault on Dromund Kaas Imperial citadel spires during renewed war offensives with lightning storms over the Sith capital"
    ),
    "battle-of-hoth-great-war": (
        "SWTOR-era Republic and Imperial forces clashing in Hoth's ice trenches around downed dreadnought wreckage under blizzard-white skies"
    ),
    "battle-of-ilum-great-war": (
        "Cinematic Battle of Ilum (Great War) (3640 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great War (SWTOR) engagement"
    ),
    "battle-of-makeb": (
        "Cinematic Battle of Makeb (3638 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great War (SWTOR) engagement"
    ),
    "battle-of-manaan-great-war": (
        "Underwater battle for Manaan kolto fields with Republic submarines engaging Imperial depth charges near Ahto City domes"
    ),
    "battle-of-nal-hutta-great-war": (
        "Hutt Cartel mercenaries fighting alongside Sith Imperial units in Nal Hutta swamp palace districts during a Republic raid"
    ),
    "battle-of-ord-mantell-great-war": (
        "Separatist-style urban warfare on Ord Mantell junkyard plains as Republic militia engage Sith Imperial troopers among rusted starship hulks"
    ),
    "battle-of-taris-great-war": (
        "Republic restoration efforts on Taris overrun by Sith Imperial invasion with undercity rakghoul outbreaks amid orbital bombardment"
    ),
    "battle-of-voss-great-war": (
        "Republic and Imperial forces skirmishing on Voss mountain shrines while Voss Mystics observe from mist-shrouded cliffs"
    ),
    "battle-of-ziost-great-war": (
        "Vitiate's Sith ritual consuming Ziost's surface in black-winged dark-side energy while Republic evac ships flee the frozen world"
    ),
    "fall-of-balmorra-great-war": (
        "Cinematic Fall of Balmorra (Great War) (3642 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great War (SWTOR) engagement"
    ),
    "siege-of-kaon": (
        "Cinematic Siege of Kaon (3641 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Great War (SWTOR) engagement"
    ),
    "siege-of-kaon-great-war": (
        "Imperial troopers defending Kaon weapon forges while Republic assault pods breach red-lit industrial hive spires"
    ),
    # Hundred-Year Darkness
    "battle-of-corbos": (
        "Cinematic Battle of Corbos (6900 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Hundred-Year Darkness engagement"
    ),
    "battle-of-korriban-ancient": (
        "Dark Jedi conquerors dueling native Sith kings in Korriban tombs with red blades reflecting off desert cliffs and Sith holocrons"
    ),
    "battle-of-tython": (
        "Cinematic Battle of Tython (6950 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Hundred-Year Darkness engagement"
    ),
    "dark-jedi-uprising-on-coruscant": (
        "Fallen Jedi battling loyalist Knights on Coruscant temple steps during the Hundred-Year Darkness schism with Force storms tearing skyscrapers"
    ),
    "duel-of-the-first-sith": (
        "Cinematic Duel of the First Sith Lords (6900 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Hundred-Year Darkness engagement"
    ),
    "exile-to-korriban": (
        "Exiled Dark Jedi fleet arriving on Korriban red deserts to subjugate native Sith species and forge the first Sith Empire beneath thunderous violet skies"
    ),
    "fall-of-the-dark-jedi": (
        "Cinematic Fall of the Dark Jedi (6900 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Hundred-Year Darkness engagement"
    ),
    "founding-of-the-sith-empire": (
        "First Sith Lords crowning themselves in Korriban's Valley of the Dark Lords with crimson Force lightning illuminating ancient tombs and Massassi slaves"
    ),
    "sith-exodus": (
        "Cinematic Sith Exodus (6900 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Hundred-Year Darkness engagement"
    ),
    "sith-temple-construction-on-korriban": (
        "Massassi slaves raising monolithic Sith temples on Korriban ridgelines while Dark Jedi architects channel Force energy into stone foundations"
    ),
    # Mandalorian Wars
    "assault-on-dantooine-enclave": (
        "Mandalorian raiders bombarding the Jedi Enclave on Dantooine's grassy plains while Padawans evacuate through subterranean root cellars"
    ),
    "battle-of-althir": (
        "Cinematic Battle of Althir (3965 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Mandalorian Wars engagement"
    ),
    "battle-of-dxun": (
        "Cinematic Battle of Dxun (3963 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Mandalorian Wars engagement"
    ),
    "battle-of-jagelland": (
        "Republic hammerhead cruisers engaging Mandalorian warships over Althir's polar seas while boarding parties clash on frost-covered carrier decks"
    ),
    "battle-of-malachor-v": (
        "Cinematic Battle of Malachor V (3960 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Mandalorian Wars engagement"
    ),
    "battle-of-onderon-mandalorian-wars": (
        "Mandalorian Basilisk war droids strafing Onderon's jungle canopy while Republic forces and beast-riders counterattack beneath Iziz city walls"
    ),
    "battle-of-serroco": (
        "Mandalorian nuclear bombardment flattening Serroco's Stereb cities while Republic fleet officers watch frigates vaporize from Basilisk war droid strikes"
    ),
    "battle-of-telos-iv": (
        "Cinematic Battle of Telos IV (3958 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Mandalorian Wars engagement"
    ),
    "battle-of-vanquo": (
        "Republic miners and Jedi strike teams ambushing Mandalorian convoys on Vanquo's dusty mining mesas before the front collapses toward Taris"
    ),
    "devastation-of-cathar": (
        "Cinematic Devastation of Cathar (3973 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Mandalorian Wars engagement"
    ),
    "final-confrontation-at-malachor-v": (
        "Revan and Malak leading Republic forces against Mandalorian clans at the mass shadow generator superweapon site with fractured ground and violet energy storms"
    ),
    "mandalorian-siege-of-taris": (
        "Mandalorian Neo-Crusaders besieging Taris upper city while Republic evacuation ships lift off from the Undercity as orbital bombardment lights the skyline"
    ),
    "raid-on-cathar-survivors": (
        "Mandalorian extermination squads hunting remaining Cathar refugees across coastal cliffs years after the Devastation of Cathar under blood-red skies"
    ),
    "siege-of-rhen-var": (
        "Frozen citadel siege on Rhen Var with Republic soldiers defending ice temples against Mandalorian shock troops under aurora-lit polar storms"
    ),
    "siege-of-tar-is": (
        "Cinematic Siege of Taris (3962 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Mandalorian Wars engagement"
    ),
    # New Sith Wars
    "battle-of-jabiim-new-sith-wars": (
        "Cinematic Battle of Jabiim (New Sith Wars) (1032 BBY) on the battlefield: armies, starfighters, and environmental details unique to this New Sith Wars engagement"
    ),
    "battle-of-ruusan": (
        "Cinematic Battle of Ruusan (1000 BBY) on the battlefield: armies, starfighters, and environmental details unique to this New Sith Wars engagement"
    ),
    "fifth-battle-of-ruusan": (
        "Sith counteroffensive breaking Jedi perimeter defenses on Ruusan canyon passes with Brotherhood warlords fighting among themselves"
    ),
    "first-battle-of-ruusan": (
        "Opening clash of the Ruusan campaign with Jedi Army of Light skirmishing Brotherhood of Darkness Sith infantry across misty Ruusan valleys"
    ),
    "fourth-battle-of-ruusan": (
        "Close-quarters trench warfare between Sith and Jedi on Ruusan muddy front lines with artillery shells carving glowing craters"
    ),
    "reformation-of-the-jedi-order": (
        "Cinematic Reformation of the Jedi Order (1000 BBY) on the battlefield: armies, starfighters, and environmental details unique to this New Sith Wars engagement"
    ),
    "rise-of-darth-bane": (
        "Lone Sith survivor Darth Bane observing the thought bomb detonation from Ruusan cliffs and forging the Rule of Two amid violet Force energy"
    ),
    "second-battle-of-ruusan": (
        "Lord Kaan's Sith forces pushing Jedi lines back through Ruusan forests under perpetual storm clouds and crimson banners"
    ),
    "seventh-battle-of-ruusan": (
        "Cinematic Seventh Battle of Ruusan (1000 BBY) on the battlefield: armies, starfighters, and environmental details unique to this New Sith Wars engagement"
    ),
    "sith-brotherhood-collapse": (
        "Cinematic Sith Brotherhood Collapse (1000 BBY) on the battlefield: armies, starfighters, and environmental details unique to this New Sith Wars engagement"
    ),
    "sith-lord-skirmish-on-tython": (
        "Brotherhood of Darkness acolytes raiding Jedi outposts on Tython's mountain mesas before the Ruusan campaign escalates"
    ),
    "sixth-battle-of-ruusan": (
        "Final approach to the thought bomb valley as Jedi and Sith armies converge on Ruusan underground caverns under grey storm skies"
    ),
    "third-battle-of-ruusan": (
        "Jedi Lord Hoth's Army of Light encircling Sith fortifications on Ruusan ridges before the thought bomb campaign begins"
    ),
    "thought-bomb-detonation": (
        "Cinematic Thought Bomb Detonation (1000 BBY) on the battlefield: armies, starfighters, and environmental details unique to this New Sith Wars engagement"
    ),
    # Stark Hyperspace War
    "battle-of-primus-goluud": (
        "Cinematic Battle of Primus Goluud (44 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Stark Hyperspace War engagement"
    ),
    "battle-of-qika": (
        "Cinematic Battle of Qika (44 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Stark Hyperspace War engagement"
    ),
    "battle-of-troiken": (
        "Cinematic Battle of Troiken (44 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Stark Hyperspace War engagement"
    ),
    "blockade-of-thyferra": (
        "Trade Federation Lucrehulk blockade sphere holding Thyferra bacta convoys hostage while Republic negotiators arrive under fighter escort"
    ),
    "coruscant-financial-crisis": (
        "Cinematic Coruscant Financial Crisis (44 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Stark Hyperspace War engagement"
    ),
    "jedi-intervention-at-coruscant": (
        "Jedi negotiators and Republic troops intervening in Bordal corporate riots sparked by Stark Hyperspace War economic collapse under senate spires"
    ),
    "naval-battle-over-troiken": (
        "Republic Judicial Forces frigates exchanging turbolaser fire with Stark Combine cruisers above Troiken's ice world while troop shuttles descend to frozen caves"
    ),
    "siege-of-formos": (
        "Stark Commercial Combine mercenaries defending Formos mining colonies against Trade Federation droid landing craft in dusty canyon firefights"
    ),
    "stark-alliance-collapse": (
        "Cinematic Stark Alliance Collapse (44 BBY) on the battlefield: armies, starfighters, and environmental details unique to this Stark Hyperspace War engagement"
    ),
    "stark-hyperspace-ambush-at-taanab": (
        "Corporate raiders ambushing Republic spice convoys near Taanab's agricultural orbital stations with hyperspace mines detonating among cargo freighters"
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
