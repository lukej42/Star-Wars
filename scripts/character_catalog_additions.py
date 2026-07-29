#!/usr/bin/env python3
"""Additional Characters Directory entries beyond the original roster."""

from __future__ import annotations

# name, role, description, color
ADDITIONAL_CHARACTERS: list[dict[str, str]] = [
    {
        "name": "Shmi Skywalker",
        "slug": "shmi-skywalker",
        "role": "Moisture Farmer",
        "description": (
            "Anakin Skywalker's devoted mother who endured slavery on Tatooine with quiet strength, "
            "believing in her son's goodness until her death at the hands of Tusken Raiders shattered "
            "the last tether to his compassion."
        ),
        "color": "#d4a574",
    },
    {
        "name": "Beru Lars",
        "slug": "beru-lars",
        "role": "Moisture Farmer",
        "description": (
            "Owen Lars's wife and Luke Skywalker's aunt, who raised the boy as her own with warmth and "
            "practical wisdom until Imperial stormtroopers burned the Lars homestead on Tatooine."
        ),
        "color": "#ca8a04",
    },
    {
        "name": "Cliegg Lars",
        "slug": "cliegg-lars",
        "role": "Moisture Farmer",
        "description": (
            "Owen's father who freed and married Shmi Skywalker, losing a leg rescuing her from "
            "Tusken captivity before Anakin returned to Tatooine during the Clone Wars."
        ),
        "color": "#a16207",
    },
    {
        "name": "Watto",
        "slug": "watto",
        "role": "Junk Dealer",
        "description": (
            "A Toydarian junk shop owner on Tatooine who owned Anakin and Shmi Skywalker until Qui-Gon "
            "Jinn won the boy's freedom in a podrace wager with a rigged chance cube."
        ),
        "color": "#84cc16",
    },
    {
        "name": "Jar Jar Binks",
        "slug": "jar-jar-binks",
        "role": "Gungan Representative",
        "description": (
            "An awkward Gungan outcast whose clumsy heroism helped unite Naboo against the Trade Federation "
            "and who later, tragically, proposed the emergency powers that enabled Palpatine's rise."
        ),
        "color": "#22c55e",
    },
    {
        "name": "Sebulba",
        "slug": "sebulba",
        "role": "Podracer Pilot",
        "description": (
            "A ruthless Dug podracing champion on Tatooine who sabotaged rivals and nearly killed Anakin "
            "Skywalker during the Boonta Eve Classic before the young human won against all odds."
        ),
        "color": "#7c3aed",
    },
    {
        "name": "Boss Nass",
        "slug": "boss-nass",
        "role": "Gungan Leader",
        "description": (
            "The bombastic Boss of the Gungan Grand Army who reluctantly allied with Queen Amidala to "
            "drive the Trade Federation from Naboo after centuries of tension between Gungans and humans."
        ),
        "color": "#16a34a",
    },
    {
        "name": "Captain Panaka",
        "slug": "captain-panaka",
        "role": "Royal Security",
        "description": (
            "Head of security for Naboo's monarch who protected Queen Amidala through invasion, exile, "
            "and return, exemplifying loyal service to the throne across the Prequel era."
        ),
        "color": "#6366f1",
    },
    {
        "name": "Ric Olié",
        "slug": "ric-olie",
        "role": "Naboo Pilot",
        "description": (
            "A veteran Naboo Royal Space Fighter Corps pilot who flew the queen's starship through the "
            "blockade and later led Bravo Squadron against the Trade Federation droid control ship."
        ),
        "color": "#818cf8",
    },
    {
        "name": "Dormé",
        "slug": "dorme",
        "role": "Handmaiden",
        "description": (
            "One of Padmé Amidala's loyal handmaidens who served as decoy and confidante during the "
            "Separatist crisis, risking her life to protect the senator's identity and mission."
        ),
        "color": "#c084fc",
    },
    {
        "name": "Dexter Jettster",
        "slug": "dexter-jettster",
        "role": "Diner Owner",
        "description": (
            "A Besalisk informant and diner owner on Coruscant whose vast underworld contacts helped "
            "Obi-Wan Kenobi identify a Kamino saberdart during the clone army investigation."
        ),
        "color": "#ea580c",
    },
    {
        "name": "Onaconda Farr",
        "slug": "onaconda-farr",
        "role": "Senator",
        "description": (
            "Rodian senator from Savareen whose desperation during the Clone Wars led him to briefly "
            "betray Padmé Amidala before redeeming himself with a sacrificial act in the Senate."
        ),
        "color": "#4ade80",
    },
    {
        "name": "Rush Clovis",
        "slug": "rush-clovis",
        "role": "Banking Clan Senator",
        "description": (
            "A charismatic InterGalactic Banking Clan operative entangled with Padmé Amidala and Anakin "
            "Skywalker's jealousy, whose schemes drew him into Separatist finance and a fatal conspiracy."
        ),
        "color": "#94a3b8",
    },
    {
        "name": "Ziro the Hutt",
        "slug": "ziro-the-hutt",
        "role": "Crime Lord",
        "description": (
            "Jabba the Hutt's flamboyant uncle who conspired with Count Dooku to kidnap Rotta the Huttlet "
            "and later paid Sy Snootles to silence him before the galaxy's underworld caught up."
        ),
        "color": "#a855f7",
    },
    {
        "name": "Sy Snootles",
        "slug": "sy-snootles",
        "role": "Singer",
        "description": (
            "A Pa'lowick singer and spy for the Hutt Clan who infiltrated Ziro's entourage and "
            "assassinated him on Teth to protect Jabba's criminal interests."
        ),
        "color": "#ec4899",
    },
    {
        "name": "Bib Fortuna",
        "slug": "bib-fortuna",
        "role": "Majordomo",
        "description": (
            "Jabba the Hutt's Twi'lek majordomo who managed the palace's daily cruelty until Boba Fett "
            "seized power on Tatooine and removed him from court."
        ),
        "color": "#6b7280",
    },
    {
        "name": "Lor San Tekka",
        "slug": "lor-san-tekka",
        "role": "Church of the Force Elder",
        "description": (
            "An explorer and faith keeper who guarded map fragments to Luke Skywalker until the First "
            "Order's Kylo Ren executed him on Jakku searching for the missing Jedi."
        ),
        "color": "#78716c",
    },
    {
        "name": "Unkar Plutt",
        "slug": "unkar-plutt",
        "role": "Jakku Scrapper",
        "description": (
            "A Crolute junk boss on Jakku who exploited scavengers including Rey for rations until she "
            "escaped offworld with BB-8 and Finn toward a destiny among the stars."
        ),
        "color": "#57534e",
    },
    {
        "name": "Amilyn Holdo",
        "slug": "amilyn-holdo",
        "role": "Resistance Vice Admiral",
        "description": (
            "Leia Organa's eccentric and brilliant friend who sacrificed the Raddus in hyperspace to "
            "destroy the First Order fleet at Crait, saving the Resistance remnant."
        ),
        "color": "#a855f7",
    },
    {
        "name": "Rose Tico",
        "slug": "rose-tico",
        "role": "Resistance Mechanic",
        "description": (
            "A Canto Bight maintenance worker who joined the Resistance after losing her sister Paige, "
            "teaching Finn that saving what you love matters more than destroying what you hate."
        ),
        "color": "#f472b6",
    },
    {
        "name": "Temmin Wexley",
        "slug": "temmin-wexley",
        "role": "Resistance Pilot",
        "description": (
            "Snap Wexley's son and a skilled pilot-mechanic from Akiva who flew with Black Squadron "
            "and helped the Resistance against the First Order alongside his droid Mister Bones."
        ),
        "color": "#fb923c",
    },
    {
        "name": "Snap Wexley",
        "slug": "snap-wexley",
        "role": "Resistance Pilot",
        "description": (
            "A veteran Rebellion pilot who flew at Endor and later led Black Squadron until his death "
            "during the assault on Starkiller Base flying alongside Poe Dameron."
        ),
        "color": "#f97316",
    },
    {
        "name": "Dryden Vos",
        "slug": "dryden-vos",
        "role": "Crimson Dawn Leader",
        "description": (
            "A scarred near-human crime lord who led Crimson Dawn from his yacht, manipulating Han Solo "
            "and Qi'ra until betrayal ended his reign in a violent standoff."
        ),
        "color": "#dc2626",
    },
    {
        "name": "Enfys Nest",
        "slug": "enfys-nest",
        "role": "Cloud-Riders Leader",
        "description": (
            "The masked leader of the Cloud-Riders who fought Crimson Dawn and revealed herself as a "
            "revolutionary building an alliance against galactic exploitation."
        ),
        "color": "#f59e0b",
    },
    {
        "name": "Tobias Beckett",
        "slug": "tobias-beckett",
        "role": "Criminal Mentor",
        "description": (
            "A seasoned outlaw who mentored Han Solo during a coaxium heist before attempting to "
            "double-cross the young smuggler and dying on Savareen."
        ),
        "color": "#78716c",
    },
    {
        "name": "Val",
        "slug": "val",
        "role": "Professional Thief",
        "description": (
            "Tobias Beckett's partner and wife whose sacrifice during the Vandor train heist forced "
            "Beckett down a path of increasingly ruthless survival."
        ),
        "color": "#64748b",
    },
    {
        "name": "Rio Durant",
        "slug": "rio-durant",
        "role": "Ardennian Pilot",
        "description": (
            "A four-armed Ardennian pilot and Beckett crew member whose cheerful competence ended when "
            "he was killed during the failed Vandor coaxium robbery."
        ),
        "color": "#38bdf8",
    },
    {
        "name": "Allegiant General Pryde",
        "slug": "general-pryde",
        "role": "First Order General",
        "description": (
            "A veteran Imperial officer who served Palpatine and later commanded the Final Order's "
            "Sith fleet until he died aboard the Steadfast during the Battle of Exegol."
        ),
        "color": "#334155",
    },
    {
        "name": "Gar Saxon",
        "slug": "gar-saxon",
        "role": "Imperial Super Commando",
        "description": (
            "Mandalore's Imperial viceroy who enforced occupation with brutality until Bo-Katan Kryze "
            "and Sabine Wren ended his tyranny in a civil war for Mandalore's soul."
        ),
        "color": "#64748b",
    },
    {
        "name": "Cham Syndulla",
        "slug": "cham-syndulla",
        "role": "Ryloth Freedom Fighter",
        "description": (
            "Hera Syndulla's father and the legendary Twi'lek resistance leader who fought Separatists "
            "and Empire alike to free Ryloth from occupation."
        ),
        "color": "#059669",
    },
    {
        "name": "Governor Pryce",
        "slug": "governor-pryce",
        "role": "Imperial Governor",
        "description": (
            "Lothal's ambitious Imperial governor who destroyed her homeworld's economy chasing "
            "promotion, clashing with the Ghost crew until her defeat at the Lothal liberation."
        ),
        "color": "#475569",
    },
    {
        "name": "The Armorer",
        "slug": "the-armorer",
        "role": "Mandalorian Smith",
        "description": (
            "A mysterious Mandalorian keeper of the covert forge on Nevarro who forged Din Djarin's "
            "beskar armor and guarded the secrets of the Darksaber and Mandalorian Creed."
        ),
        "color": "#71717a",
    },
    {
        "name": "Dr. Pershing",
        "slug": "dr-pershing",
        "role": "Imperial Scientist",
        "description": (
            "A Kaminoan-trained scientist recruited by Moff Gideon to study Grogu's blood for cloning "
            "research tied to the Emperor's posthumous designs."
        ),
        "color": "#e2e8f0",
    },
    {
        "name": "Zaalbar",
        "slug": "zaalbar",
        "role": "Wookiee Warrior",
        "description": (
            "Mission Vao's loyal Wookiee companion whose life-debt and ferocious strength aided Revan "
            "during the Jedi Civil War on Taris and beyond."
        ),
        "color": "#92400e",
    },
    {
        "name": "Bastila Shan",
        "slug": "bastila-shan",
        "role": "Jedi Padawan",
        "description": (
            "A young Jedi Battle Meditation prodigy captured by Darth Malak whose bond with Revan "
            "became central to the galaxy's fate during the Jedi Civil War."
        ),
        "color": "#3b82f6",
    },
    {
        "name": "Jolee Bindo",
        "slug": "jolee-bindo",
        "role": "Hermit Jedi",
        "description": (
            "A cynical former Jedi who exiled himself on Kashyyyk's shadowlands, offering Revan "
            "unorthodox wisdom about the Force, love, and the gray paths between light and dark."
        ),
        "color": "#15803d",
    },
    {
        "name": "Meetra Surik",
        "slug": "meetra-surik",
        "role": "Jedi Exile",
        "description": (
            "A Jedi General exiled after the Mandalorian Wars who returned to face the Sith "
            "Triumvirate and ended the threat on Malachor V."
        ),
        "color": "#2563eb",
    },
    {
        "name": "Satele Shan",
        "slug": "satele-shan",
        "role": "Jedi Grand Master",
        "description": (
            "A legendary Jedi Battle Meditation master who led the Republic against the "
            "resurgent Sith Empire and later served as Grand Master during the Great Galactic War era."
        ),
        "color": "#1d4ed8",
    },
]
