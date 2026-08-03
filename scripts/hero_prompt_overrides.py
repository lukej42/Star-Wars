#!/usr/bin/env python3
"""Hand-crafted cinematic hero prompts for iconic directory entries."""

from __future__ import annotations

JEDI: dict[str, str] = {
    "aayla-secura": "Blue-skinned Twi'lek Jedi Master in battle stance on Felucia jungle battlefield with clone troopers and pink fungal trees at dusk",
    "adi-gallia": "Tholothian Jedi Council member with headdress and regal robes in Coruscant Jedi Temple war room with holo star maps",
    "agen-kolar": "Zabrak horned Jedi Master with green lightsaber in Chancellor's office confrontation, dramatic red emergency lighting",
    "ahsoka-tano": "Togruta warrior with white montrals and dual white lightsabers on snowy moon fortress bridge at twilight",
    "anakin-skywalker": "Heroic Jedi Knight in dark robes with blue lightsaber leading starfighter squadron over volcanic industrial world",
    "barriss-offee": "Mirialan padawan in healer's posture inside Jedi Temple medical bay with soft blue light and meditation circles",
    "depa-billaba": "Chalactan Jedi Master seated in meditation circle on Haruun Kal jungle plateau with mist and purple kyber glow",
    "eeth-koth": "Zabrak Jedi Council member with orange lightsaber on Geonosis arena rim overlooking droid army deployment",
    "even-piell": "Lannik Jedi Master with scarred face in Separatist prison citadel corridor escape with clone commandos",
    "ezra-bridger": "Young human rebel Jedi with green lightsaber on Lothal grasslands with Ghost starship silhouette at sunset",
    "grogu": "Small green Force-sensitive foundling in hovering pram with silver ball toy in mudhorn cave with warm firelight",
    "gungi": "Wookiee youngling with wooden lightsaber in Jedi Temple training circle with golden afternoon beams",
    "jocasta-nu": "Elderly human Jedi archivist in vast temple library stacks with floating holocrons and amber lamp light",
    "kanan-jarrus": "Blind Jedi in mask and armor with blue lightsaber on Lothal rooftop with twin moons rising",
    "kit-fisto": "Nautolan Jedi Master with tentacle head and green lightsaber underwater battle on Mon Calamari coral city",
    "luminara-unduli": "Mirialan Jedi Master with elegant green saber on Geonosis droid factory catwalk with industrial sparks",
    "luke-skywalker": "Farm boy turned Jedi in black tunic raising green lightsaber on cloudy cliff with X-wing in distance",
    "mace-windu": "Bald human Jedi Master with purple lightsaber in rain-soaked city plaza battle with armored droids",
    "obi-wan-kenobi": "Bearded Jedi Master in desert robes on rocky canyon ledge at twin sunset with distant moisture vaporators",
    "plo-koon": "Kel Dor masked Jedi Master in flight suit with yellow lightsaber above Cato Neimoidia bridge battle",
    "qui-gon-jinn": "Long-haired maverick Jedi with green lightsaber in Naboo plasma mining facility with glowing red core",
    "shaak-ti": "Togruta Jedi Council member meditating in Kamino cloning facility observation deck with rain streaks",
    "satele-shan": "Human female Jedi Grand Master with brown hair in white and blue Old Republic battle robes, ignited blue lightsaber, Battle Meditation aura over ruined Coruscant Jedi Temple and invasion smoke during the Great Galactic War",
    "stass-allie": "Tholothian Jedi in Clone Wars urban ruins with blue lightsaber and smoke-filled skyline",
    "yaddle": (
        "Photorealistic cinematic Star Wars live-action film still hero banner, 1536x1024, 16:9. "
        "Hyper-realistic practical effects quality matching The Phantom Menace Jedi Council scenes. "
        "Yaddle, female member of Yoda's species: small green wrinkled skin, large pointed ears, "
        "gentle wise eyes, brown Jedi robes, distinctive brown cloth head wrap with topknot. "
        "Seated in the Coruscant Jedi High Council chamber with warm golden window light, "
        "marble pillars, and serene Jedi Master composure. Film grain, dramatic rim lighting, IMAX composition. "
        "No text, no logos, no watermarks, no readable lettering."
    ),
    "yoda": (
        "Photorealistic cinematic Star Wars live-action film still hero banner, 1536x1024, 16:9. "
        "Hyper-realistic practical effects quality matching Revenge of the Sith and The Empire Strikes Back. "
        "Master Yoda: small green wrinkled alien Jedi Grand Master with large pointed ears, "
        "wise ancient face, sparse white hair, traditional brown Jedi robes, ignited green lightsaber. "
        "Dynamic Form IV Ataru combat pose with acrobatic Force energy in a Jedi Temple duelling chamber "
        "or Senate rotunda backdrop with dramatic rim lighting. Film grain, IMAX composition. "
        "No text, no logos, no watermarks, no readable lettering."
    ),
}

SITH: dict[str, str] = {
    "asajj-ventress": "Bald Dathomirian assassin with curved red lightsabers on snowy fortress battlements under aurora sky",
    "darth-bane": "Black-robed Sith with red blade establishing Rule of Two on Moraband temple steps with lightning sky",
    "darth-maul": "Red-and-black Zabrak Sith with double-bladed red lightsaber in Theed power generator reactor pit",
    "darth-malak": "Bald jawless Sith Lord with metal jaw plate and red lightsaber on Star Forge command bridge",
    "darth-malgus": "Masked Sith warrior with respirator and red saber breaching Jedi Temple gates during orbital invasion",
    "darth-nihilus": "Mask-wrapped Sith entity draining life force above ravaged world with fleet silhouettes",
    "darth-plagueis": "Pale Muun Sith Lord in luxurious private sanctum with midi-chlorian charts and dim candlelight",
    "darth-revan": "Masked Sith Lord with violet-red lightsaber on Rakata Prime beach with ancient star maps",
    "darth-sidious": "Hooded Emperor in dark robe with forked Force lightning in Senate rotunda with red emergency glow",
    "darth-sion": "Cracked undead Sith with glowing fissures and red saber in Sith academy torture chamber",
    "darth-traya": "Blind elderly Sith with staff and three lightsabers floating in Malachor V Trayus Academy ruins",
    "darth-tyranus": "Elegant elderly Sith Lord in cape with curved red lightsaber in Geonosis arena executive box overlooking battle",
    "darth-vader": "Black-armored Sith Lord with red lightsaber on Mustafar lava river platform with volcanic glow",
    "darth-vitiate": "Ethereal Sith Emperor with dark energy aura on Dromund Kaas citadel spire",
    "darth-zannah": "Young Sith apprentice with red saber beside holocron archive on Ambria desert cliff",
    "exar-kun": "Dark Jedi spirit with twin red sabers in Massassi temple on Yavin 4 moon with giant pyramids",
    "grand-inquisitor": "Pau'an dark side inquisitor with spinning double-bladed red saber on Star Destroyer bridge",
    "marka-ragnos": "Ancient Sith spirit with golden crown and spectral red energy on Korriban Valley of Dark Lords",
    "naga-sadow": "Ancient Sith with pale skin and red blade in tomb ship chamber with stasis pods",
    "savage-opress": "Massive Zabrak dark warrior with pike weapon on Dathomir misty village night",
    "second-sister": "Armored inquisitor with red saber in Fortress Inquisitorius icy training chamber",
    "seventh-sister": "Mirialan inquisitor with spinning saber on abandoned Jedi temple moon with green mist",
}

SHIPS: dict[str, str] = {
    "millennium-falcon": "Iconic saucer-shaped freighter with forward mandibles banking through asteroid field with blue hyperspace streak",
    "x-wing": "Red-striped X-wing starfighter in trench run above Death Star surface with laser fire",
    "tie-fighter": "Twin-panel Imperial TIE fighter in squadron formation against star destroyer backdrop",
    "star-destroyer": "Massive wedge Imperial Star Destroyer emerging from hyperspace over blue planet limb",
    "death-star": "Planet-killing battle station superlaser dish firing green beam with rebel fleet silhouettes",
    "slave-i": "Green-and-red Mandalorian patrol craft in asteroid chase with engine glow trails",
    "venator": "Republic Venator-class destroyer launching ARC-170 fighters over Coruscant cityscape",
    "y-wing": "Gold squadron Y-wing bomber approaching Death Star trench with ion cannon turret visible",
    "a-wing": "Sleek A-wing interceptor weaving through Star Destroyer bridge tower at Endor battle",
    "b-wing": "Rotating B-wing assault fighter approaching Death Star II with S-foils extended",
    "u-wing": "UT-60 U-wing troop transport skimming Scarif beach with rebel soldiers deploying",
    "ghost": "Spectral rebel VCX freighter with nose turret over Lothal clouds at sunset",
    "razor-crest": "Gunmetal Mandalorian bounty hunter ship landed on icy Nevarro cantina outpost",
    "naboo-royal-starship": "Chrome Naboo J-type diplomatic starship in Theed palace hangar with polished reflections",
    "jedi-starfighter": "Delta-7 Aethersprite with astromech socket in Jedi Temple hangar launch bay",
    "eta-2": "Eta-2 Actis interceptor with red trim in open space battle over ring world",
}

FORCE_POWERS: dict[str, str] = {
    "force-push": "Jedi hand gesture repelling battle droids across Naboo hangar with blue Force shockwave ripple",
    "force-pull": "Telekinetic retrieval of lightsaber through Bespin cloud city air shaft with cyan energy trail",
    "force-lightning": "Forked Sith Force lightning arcing from raised hands in dark throne room with red ambient glow",
    "force-choke": "Invisible dark side grip lifting officer over Death Star conference table with choking aura",
    "mind-trick": "Rippling blue-green wave distorting perception in Mos Eisley cantina doorway with desert light",
    "force-heal": "Golden healing light flowing from hands over wounded warrior in forest battlefield med camp",
    "force-speed": "Blurred Jedi sprinting through Geonosis droid factory with motion streak and green saber trail",
    "force-vision": "Force user surrounded by swirling holo-like future visions in cave with ethereal blue mist",
    "battle-meditation": "Jedi Master seated in meditation circle boosting allied fleet morale with golden aura over star chart",
    "force-projection": "Holographic Force projection of Jedi on Crait salt plains with blue snow spray",
    "chain-lightning": "Multiple branching Sith lightning bolts striking troop formation on rainy battlefield",
    "force-repulse": "Radial telekinetic explosion scattering debris in Jedi Temple courtyard with dust ring",
    "tutaminis": "Jedi absorbing Force lightning into open palms with blue-white energy cocoon",
    "shatterpoint": "Force user seeing glowing fracture lines on armored opponent in duel with strategic focus",
    "thought-bomb": "Ancient Sith ritual sphere of purple dark side energy over Ruusan valley army",
    "force-spirit": "Translucent blue Force ghost appearing in misty swamp with serene glow",
    "sith-alchemy": "Sith alchemist forging red crystal in crucible with dark smoke and crimson runes",
}

BOUNTY_HUNTERS: dict[str, str] = {
    "boba-fett": "Green Mandalorian armor bounty hunter with jetpack and blaster rifle on Tatooine desert ridge twin suns",
    "jango-fett": "Blue Mandalorian armor hunter with dual blasters in Kamino cloning facility rain platform",
    "cad-bane": "Blue-skinned Duro hunter with wide hat and twin pistols in hostage standoff on Coruscant rooftop",
    "dengar": "Bandaged bounty hunter with heavy weapons on Hoth snow battlefield wreckage",
    "ig-88": "Tall silver assassin droid hunter in smoky docking bay with holo wanted puck displays",
    "bossk": "Trandoshan reptilian hunter with rifle in Star Destroyer trash compactor green glow",
    "zam-wesell": "Clawdite shapeshifter hunter mid-transformation in Coruscant speeder chase night rain",
    "din-djarin": "Beskar-armored hunter with rifle beside landed gunship on Nevarro frontier outpost",
    "greedo": "Rodian green hunter with blaster in Mos Eisley cantina booth with alien crowd blur",
    "aurra-sing": "Pale bald sniper hunter with rifle on Coruscant underworld bridge with speeder traffic",
}

SPECIES: dict[str, str] = {
    "human": "Diverse human colonists and soldiers across Core Worlds city plaza with starships overhead",
    "twilek": "Twi'lek community with lekku head-tails in Ryloth underground resistance cavern with orange glow",
    "wookiee": "Towering furry Wookiee warriors in Kashyyyk wroshyr tree village with mist and rope bridges",
    "zabrak": "Horned Zabrak warriors training on Dathomir red rock cliffs under storm clouds",
    "togruta": "Togruta with colorful montrals and head-tails in Jedi temple gathering with soft light",
    "chiss": "Blue-skinned Chiss with red eyes in Chiss Ascendancy command bridge with star map",
    "rodian": "Green-skinned Rodian hunters in jungle stalking scene with tribal markers",
    "bothan": "Furry Bothan spies in war room with tactical holo displays and dim amber lighting",
    "gungan": "Amphibious Gungan warriors on Naboo underwater bubble city with bioluminescent flora",
    "ewok": "Small furry Ewok villagers in Endor forest village with rope bridges and torchlight",
}

SETTLEMENTS: dict[str, str] = {
    "coruscant": "Layered ecumenopolis cityscape with endless skyscrapers traffic lanes and golden sunset haze",
    "mos-eisley": "Tatooine spaceport cantina town with domed buildings sand dunes and twin suns",
    "theed": "Naboo royal city with golden domes waterfalls and green cliffs reflected in river",
    "cloud-city": "Bespin floating tibanna mining city in orange cloud sea with sunset silhouette",
    "mos-espa": "Tatooine podracing arena settlement with crowded grandstands and sandstorm haze",
    "anchorhead": "Remote Tatooine moisture farming outpost with vaporators and dusty settlement shacks",
    "bestine": "Tatooine capital settlement with administrative buildings and desert trade routes",
    "jabbas-palace": "Desert palace fortress on Tatooine cliff with sail barge dock and dune sea",
    "tipoca-city": "Kamino stilt city above storm ocean with cloning facility spires and landing platforms",
    "senate-district": "Coruscant Senate District with rotunda dome and aerial traffic at twilight",
}

OVERRIDES: dict[str, dict[str, str]] = {
    "jedi": JEDI,
    "sith": SITH,
    "ships": SHIPS,
    "force-powers": FORCE_POWERS,
    "bounty-hunters": BOUNTY_HUNTERS,
    "species": SPECIES,
    "settlements": SETTLEMENTS,
}
