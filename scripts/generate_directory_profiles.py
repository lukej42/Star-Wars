#!/usr/bin/env python3
"""Generate directory profile JSON and companion cartoon SVG assets."""

from __future__ import annotations

import hashlib
import json
import re
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "Data"
IMAGES = ROOT / "wwwroot" / "images"
PROFILES = ROOT / "wwwroot" / "data" / "profiles"
SCRIPTS = Path(__file__).resolve().parent

import sys
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

from directory_art import ship_blueprint_svg, ship_scene_svg
from jedi_sith_art import (
    jedi_emblem_svg,
    jedi_scene_svg,
    sith_emblem_svg,
    sith_scene_svg,
)

OUTLINE = "#1a1a2e"
ERAS = [
    "Ancient Era",
    "Old Republic",
    "High Republic",
    "Clone Wars",
    "Imperial Era",
    "Galactic Civil War",
    "New Republic",
    "First Order",
]


from ship_profile_enrichments import SHIP_ENRICHMENTS
ENRICHMENTS: dict[str, dict] = {
    "obi-wan-kenobi": {
        "overview": (
            "Obi-Wan Kenobi was a legendary Jedi Master whose calm wisdom and mastery of Form III "
            "made him one of the Order's most respected guardians. He trained Anakin Skywalker and "
            "later Luke Skywalker, shaping the fate of the galaxy across three generations. From the "
            "battlefields of Geonosis to exile on Tatooine, Kenobi embodied the Jedi ideal of restraint, "
            "sacrifice, and service to the light side of the Force."
        ),
        "history": (
            "Born on Stewjon, Obi-Wan Kenobi was discovered by the Jedi and apprenticed to Qui-Gon Jinn, "
            "whose unorthodox philosophy left a lasting mark on his outlook. After Qui-Gon's death on "
            "Naboo, Kenobi took Anakin Skywalker as his padawan despite grave reservations from the Council.\n\n"
            "Throughout the Clone Wars, General Kenobi became a master strategist and diplomat, leading "
            "Republic forces alongside Anakin while navigating the Order's growing entanglement with "
            "politics. His rivalry with Asajj Ventress and confrontations with Grievous cemented his "
            "reputation as a battlefield legend.\n\n"
            "When Order 66 shattered the Jedi, Kenobi survived and confronted his fallen apprentice on "
            "Mustafar. Unable to bring himself to finish Anakin, he retreated into exile on Tatooine, "
            "watching over Luke from afar and waiting for the moment the galaxy might need a Jedi again.\n\n"
            "In his final years, Kenobi sacrificed himself aboard the Death Star so Luke could escape, "
            "becoming one with the Force and continuing to guide the young Skywalker as a spirit."
        ),
        "significance": (
            "Obi-Wan Kenobi stands as the bridge between the golden age of the Jedi and their rebirth. "
            "His choices—training Anakin, sparing him on Mustafar, and mentoring Luke—echo through every "
            "major turning point of the saga.\n\n"
            "As a practitioner of Soresu, he demonstrated that defense and patience could defeat even "
            "the most aggressive opponents. His life illustrates both the nobility and the tragedy of "
            "the Jedi Code in an age of war.\n\n"
            "Generations of fans and in-universe historians regard Kenobi as the quintessential Jedi: "
            "humble, humorous when needed, and unwavering in duty even when the galaxy abandoned his Order."
        ),
        "notableEvents": [
            "Defeated Darth Maul on Naboo after Qui-Gon Jinn's death",
            "Led the rescue of Chancellor Palpatine during the Battle of Coruscant",
            "Survived Order 66 and duelled Darth Vader on Mustafar",
            "Exiled himself on Tatooine to protect Luke Skywalker",
            "Guided Luke to begin Jedi training in the Dune Sea",
            "Sacrificed himself aboard the Death Star to save the Rebel strike team",
            "Appeared as a Force spirit to Luke on Hoth and Endor",
        ],
        "affiliations": [
            "Jedi Order",
            "Jedi High Council",
            "Grand Army of the Republic",
            "212th Attack Battalion",
            "Hidden guardians of the Lars homestead",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Apprenticed to Qui-Gon Jinn and knighted after Naboo"},
            {"era": "Clone Wars", "event": "Led Republic campaigns as General Kenobi"},
            {"era": "Clone Wars", "event": "Defeated General Grievous on Utapau"},
            {"era": "Imperial Era", "event": "Duelled Darth Vader on Mustafar and faked his death"},
            {"era": "Imperial Era", "event": "Watched over Luke Skywalker on Tatooine"},
            {"era": "Galactic Civil War", "event": "Began Luke's training and fell to Vader on the Death Star"},
        ],
    },
    "luke-skywalker": {
        "overview": (
            "Luke Skywalker rose from a moisture farmer on Tatooine to become the last Jedi Knight of "
            "the Old Republic era and architect of a new generation of Force users. Prophesied as the "
            "one who would restore balance, he confronted the Empire, redeemed his father, and later "
            "attempted to rebuild the Jedi Order before withdrawing into exile after tragedy."
        ),
        "history": (
            "Raised by Owen and Beru Lars, Luke grew up unaware of his heritage until droids carrying "
            "Leia's message brought Obi-Wan Kenobi back into his life. After his aunt and uncle were "
            "killed by stormtroopers, he left Tatooine to join the Rebellion and learn the ways of the Force.\n\n"
            "Training under Kenobi and later Yoda on Dagobah, Luke struggled with impatience and fear "
            "but developed into a skilled pilot and Jedi. He destroyed the first Death Star, survived "
            "confrontations with Darth Vader, and learned the truth of his parentage on Cloud City.\n\n"
            "Rather than kill Vader, Luke believed redemption was possible. On the second Death Star, "
            "he refused the Emperor's temptations and awakened Anakin Skywalker's remaining light, "
            "fulfilling the prophecy in a way the Council never anticipated.\n\n"
            "Decades later, Luke founded a Jedi academy on Ossus and trained a new generation before "
            "Ben Solo's fall to the dark side shattered his hope. He vanished to Ahch-To until Rey "
            "called him back to face his failures and pass the torch."
        ),
        "significance": (
            "Luke embodies hope in the Star Wars mythos—the farmboy who becomes a galactic symbol. "
            "His journey proves that Jedi power need not come from lineage alone but from compassion "
            "and choice.\n\n"
            "His refusal to execute Vader redefined what 'bringing balance' could mean, prioritizing "
            "mercy over vengeance. That decision saved the soul of Anakin Skywalker and broke the "
            "Emperor's hold on the Skywalker line.\n\n"
            "Even in failure with Ben Solo, Luke's legacy inspired Rey and countless others to carry "
            "the light forward, ensuring the Jedi would not die with him."
        ),
        "notableEvents": [
            "Destroyed the first Death Star during the Battle of Yavin",
            "Duelled Darth Vader on Cloud City and lost his hand",
            "Confronted the Emperor aboard the second Death Star",
            "Helped redeem Anakin Skywalker and witnessed his death",
            "Founded a new Jedi training temple on Ossus",
            "Exiled himself to Ahch-To after Ben Solo's destruction of the temple",
            "Projected a Force illusion at Crait to save the Resistance",
        ],
        "affiliations": [
            "Alliance to Restore the Republic",
            "New Republic",
            "Jedi Order (restored)",
            "Red Five squadron",
            "Resistance (spiritual ally)",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Left Tatooine with Obi-Wan Kenobi and joined the Rebellion"},
            {"era": "Galactic Civil War", "event": "Destroyed the Death Star at Yavin"},
            {"era": "Galactic Civil War", "event": "Trained under Yoda on Dagobah"},
            {"era": "Galactic Civil War", "event": "Redeemed Darth Vader and ended the Emperor's reign"},
            {"era": "New Republic", "event": "Established a Jedi academy and trained new knights"},
            {"era": "First Order", "event": "Returned as a Force spirit to inspire Rey on Ahch-To"},
        ],
    },
    "yoda": {
        "overview": (
            "Yoda was the oldest and wisest master of the Jedi Order, serving on the High Council for "
            "centuries and shaping generations of knights. Small in stature but immense in power, he "
            "embodied the philosophical heart of the Jedi—patience, humility, and deep communion with "
            "the Living Force."
        ),
        "history": (
            "For over eight centuries, Yoda trained padawans, mediated Council disputes, and guarded "
            "Jedi secrets from the heights of the Coruscant Temple. His unique speech and playful "
            "demeanor concealed one of the galaxy's greatest duelists and Force prodigies.\n\n"
            "During the Clone Wars, Yoda led troops on worlds such as Rugosa while sensing the dark "
            "side thickening around the Republic. He grew suspicious of the war's design yet struggled "
            "to act without proof against Chancellor Palpatine.\n\n"
            "When Order 66 struck, Yoda survived an assassination attempt in the Senate and confronted "
            "Darth Sidious in the Chancellor's office. Unable to defeat the Emperor, he fled into exile "
            "on Dagobah, its strong dark-side nexus masking his presence.\n\n"
            "There he waited for Luke Skywalker, training the last hope of the Jedi before becoming "
            "one with the Force and appearing to Luke and others as a guiding spirit."
        ),
        "significance": (
            "Yoda represents the accumulated wisdom of the Jedi Order at its height—and its blind spots. "
            "His teachings on attachment, fear, and the dark side shaped Luke and, indirectly, Rey.\n\n"
            "As Grand Master, he balanced martial skill with contemplative philosophy, proving that "
            "true strength in the Force flows from serenity rather than aggression.\n\n"
            "His exile and final lessons on Dagobah mark the transition from the old Jedi institution "
            "to a more personal, spiritual understanding of the Force."
        ),
        "notableEvents": [
            "Served on the Jedi High Council for centuries",
            "Negotiated with King Katuunko on Rugosa during the Clone Wars",
            "Survived Order 66 and duelled Darth Sidious in the Senate",
            "Exiled himself to Dagobah to hide from the Empire",
            "Trained Luke Skywalker in the ways of the Force",
            "Died at peace, becoming a Force spirit",
            "Appeared to Luke on Dagobah and later at Endor",
        ],
        "affiliations": [
            "Jedi Order",
            "Jedi High Council",
            "Grand Army of the Republic (advisory)",
            "Hidden exile community on Dagobah",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Rose to Grand Master of the Jedi Order"},
            {"era": "Clone Wars", "event": "Led diplomatic and military missions for the Republic"},
            {"era": "Imperial Era", "event": "Fought Darth Sidious and retreated into exile"},
            {"era": "Imperial Era", "event": "Watched over Dagobah for decades in hiding"},
            {"era": "Galactic Civil War", "event": "Trained Luke Skywalker as the last Jedi pupil"},
            {"era": "Galactic Civil War", "event": "Passed into the Force after completing Luke's training"},
        ],
    },
    "darth-vader": {
        "overview": (
            "Darth Vader, once the heroic Jedi Knight Anakin Skywalker, became the Emperor's black-armored "
            "enforcer and the most feared figure in the Galactic Empire. Bonded to life-support systems "
            "after his duel on Mustafar, he hunted surviving Jedi and crushed rebellion with ruthless "
            "efficiency while conflict between light and dark warred within him."
        ),
        "history": (
            "Anakin Skywalker was a prodigy discovered on Tatooine, whose power and impatience worried "
            "the Council even as they knighted him during the Clone Wars. Secretly married to Padmé "
            "Amidala, he fell under Palpatine's influence, fearing loss and craving forbidden knowledge.\n\n"
            "Manipulated into believing the Jedi had betrayed him, Anakin helped purge the Temple and "
            "assassinate the Separatist leadership on Mustafar. Mutilated by Obi-Wan Kenobi, he was "
            "rebuilt as Darth Vader, bound to armor and machinery.\n\n"
            "For two decades Vader served Palpatine, commanding the Imperial fleet, hunting Jedi survivors, "
            "and enforcing terror from the Death Star to Cloud City. The discovery that Luke Skywalker "
            "was his son reawakened long-buried conflict.\n\n"
            "On the second Death Star, Vader chose to save Luke by throwing the Emperor into the reactor "
            "shaft, redeeming Anakin Skywalker in his final moments and fulfilling his role in restoring balance."
        ),
        "significance": (
            "Vader is the saga's central tragedy—a hero whose fear became tyranny, and a villain whose "
            "love ultimately saved the galaxy. His image defines the Empire's iron fist.\n\n"
            "Mechanically sustained and emotionally severed from his past, he illustrates how the dark "
            "side consumes identity while leaving fragments of humanity that can still choose redemption.\n\n"
            "His legacy haunted the Skywalker family for generations, shaping Kylo Ren, Luke's guilt, "
            "and Rey's search for belonging."
        ),
        "notableEvents": [
            "Massacred Jedi younglings during Order 66",
            "Duelled Obi-Wan Kenobi on Mustafar and was rebuilt in armor",
            "Captured Princess Leia aboard the Tantive IV",
            "Duelled Obi-Wan Kenobi aboard the Death Star",
            "Revealed he was Luke Skywalker's father on Cloud City",
            "Turned against Emperor Palpatine to save Luke",
            "Died redeemed as Anakin Skywalker aboard the second Death Star",
        ],
        "affiliations": [
            "Sith Order",
            "Galactic Empire",
            "Imperial Navy",
            "501st Legion",
            "Death Star command",
        ],
        "timeline": [
            {"era": "Clone Wars", "event": "Fell to the dark side and became Darth Vader"},
            {"era": "Imperial Era", "event": "Hunted surviving Jedi across the galaxy"},
            {"era": "Imperial Era", "event": "Oversaw the Death Star's construction and deployment"},
            {"era": "Galactic Civil War", "event": "Captured Han Solo and tortured Leia on Cloud City"},
            {"era": "Galactic Civil War", "event": "Duelled Luke Skywalker aboard the Emperor's throne room"},
            {"era": "Galactic Civil War", "event": "Destroyed the Emperor and died as Anakin Skywalker"},
        ],
    },
    "darth-sidious": {
        "overview": (
            "Darth Sidious, publicly known as Supreme Chancellor and later Emperor Palpatine, was the "
            "Sith mastermind who engineered the fall of the Republic and ruled the galaxy through fear. "
            "A master of manipulation, dark-side sorcery, and long-range planning, he brought the Sith "
            "Grand Plan to fruition after centuries of secrecy."
        ),
        "history": (
            "Trained by Darth Plagueis, Sheev Palpatine of Naboo embraced the Sith teachings while "
            "building a political career. As senator and later chancellor, he orchestrated the Separatist "
            "Crisis, controlled both sides of the Clone Wars, and eroded Jedi authority.\n\n"
            "With Anakin Skywalker as his new apprentice Darth Vader, Sidious issued Order 66, declared "
            "the Empire, and hunted the remaining Jedi. He ruled from Imperial Center, constructing "
            "superweapons and subverting every institution of the Old Republic.\n\n"
            "Thought destroyed aboard the second Death Star, Palpatine's dark-side experiments and "
            "cloning efforts eventually allowed a return in the Unknown Regions, threatening the "
            "New Republic and Resistance once more.\n\n"
            "His final defeat required the combined efforts of Rey, the redeemed Ben Solo, and the "
            "spirits of Jedi past, ending the Sith Eternal's bid for eternal dominion."
        ),
        "significance": (
            "Sidious represents institutional corruption weaponized through the dark side. His rise "
            "demonstrates how democracies can vote themselves into tyranny when fear goes unchecked.\n\n"
            "As the architect of Order 66, the Empire, and the Sith Eternal, he is the through-line "
            "villain connecting prequel, original, and sequel eras.\n\n"
            "His obsession with immortality and absolute control stands in stark contrast to the Jedi "
            "acceptance of death and service to the Living Force."
        ),
        "notableEvents": [
            "Manipulated the Trade Federation invasion of Naboo",
            "Engineered the Clone Wars as Darth Sidious",
            "Declared himself Emperor after Order 66",
            "Corrupted Anakin Skywalker to become Darth Vader",
            "Destroyed Alderaan via the Death Star's superlaser",
            "Was thrown down a reactor shaft by Darth Vader",
            "Returned via cloning and was defeated at Exegol",
        ],
        "affiliations": [
            "Sith Order",
            "Galactic Republic (as Chancellor Palpatine)",
            "Galactic Empire",
            "Sith Eternal",
            "Confederacy of Independent Systems (secret patron)",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Trained in the Sith arts under Darth Plagueis"},
            {"era": "Clone Wars", "event": "Ruled the Republic as Supreme Chancellor Palpatine"},
            {"era": "Imperial Era", "event": "Proclaimed the Galactic Empire and ruled as Emperor"},
            {"era": "Galactic Civil War", "event": "Commanded the Death Star and hunted the Rebel Alliance"},
            {"era": "Galactic Civil War", "event": "Was defeated aboard the second Death Star"},
            {"era": "First Order", "event": "Returned and led the Final Order from Exegol"},
        ],
    },
    "ahsoka-tano": {
        "overview": (
            "Ahsoka Tano was Anakin Skywalker's Togruta padawan who grew from an eager young learner "
            "into a formidable independent Force wielder. After leaving the Jedi Order disillusioned "
            "by its politics, she fought in the Clone Wars, survived Order 66, challenged the Empire, "
            "and eventually searched the galaxy for Grand Admiral Thrawn."
        ),
        "history": (
            "Assigned to Anakin Skywalker by Yoda, Ahsoka learned unconventional tactics and bold "
            "leadership on battlefronts from Christophsis to Mandalore. Her frame-up in the Temple "
            "bombing trial shattered her faith in the Council, and she walked away from the Order.\n\n"
            "She continued to aid the Republic as a free agent, fighting at the Siege of Mandalore "
            "alongside Bo-Katan Kryze. When Order 66 came, former clone captain Rex removed her inhibitor "
            "chip and they faked their deaths, going into hiding.\n\n"
            "During the Imperial era, Ahsoka joined the nascent Rebellion under the codename Fulcrum, "
            "guiding cells from the shadows. She confronted Darth Vader at Malachor and later walked "
            "into the World Between Worlds seeking answers.\n\n"
            "Decades later, she appeared in the search for Ezra Bridger and Grand Admiral Thrawn, "
            "carrying white lightsabers that signified her path outside traditional Jedi or Sith doctrine."
        ),
        "significance": (
            "Ahsoka embodies moral clarity without institutional loyalty. Her departure from the Order "
            "foreshadowed its failure while proving one could serve the light without its bureaucracy.\n\n"
            "Her bond with Anakin humanized the Chosen One for audiences and added weight to his fall, "
            "since she survived to witness the Empire he helped build.\n\n"
            "As Fulcrum and later a wandering knight, she bridged Clone Wars, Rebels, and live-action "
            "storytelling, becoming a fan-favorite symbol of resilience."
        ),
        "notableEvents": [
            "Was assigned as Anakin Skywalker's padawan during the Clone Wars",
            "Was falsely accused of bombing the Jedi Temple and left the Order",
            "Fought in the Siege of Mandalore alongside Bo-Katan",
            "Survived Order 66 with Captain Rex's help",
            "Operated as the spy Fulcrum for the Rebellion",
            "Duelled Darth Vader at the Sith temple on Malachor",
            "Searched for Ezra Bridger and Grand Admiral Thrawn in the Unknown Regions",
        ],
        "affiliations": [
            "Jedi Order (former)",
            "501st Legion (associated)",
            "Mandalore resistance",
            "Alliance to Restore the Republic (Fulcrum)",
            "New Republic era independents",
        ],
        "timeline": [
            {"era": "Clone Wars", "event": "Became Anakin Skywalker's padawan"},
            {"era": "Clone Wars", "event": "Left the Jedi Order after the Temple bombing trial"},
            {"era": "Clone Wars", "event": "Led Republic forces at the Siege of Mandalore"},
            {"era": "Imperial Era", "event": "Survived Order 66 and went into hiding"},
            {"era": "Galactic Civil War", "event": "Served the Rebellion as Fulcrum"},
            {"era": "New Republic", "event": "Pursued Thrawn and searched for Ezra Bridger"},
        ],
    },
    "darth-revan": {
        "overview": (
            "Darth Revan was a Jedi Knight and Sith Lord whose crusades reshaped the Old Republic era. "
            "A brilliant strategist and charismatic leader, Revan fell to the dark side during the "
            "Mandalorian Wars, built a Sith Empire, was redeemed, and later became a legendary figure "
            "whose mask and memory haunted both Jedi and Sith for millennia."
        ),
        "history": (
            "Revan defied the Jedi Council to fight the Mandalorian invaders, earning devotion from "
            "followers such as Malak. Exposure to Sith artifacts on Malachor and in the Unknown Regions "
            "corrupted the crusaders, and Revan declared himself Dark Lord of the Sith.\n\n"
            "His Sith Empire nearly conquered the Republic before Malak betrayed him, leaving Revan "
            "captured and mind-wiped by the Jedi Council. Reprogrammed as a loyal agent, Revan "
            "rediscovered his past and confronted Malak above the Star Forge.\n\n"
            "Choosing the light, Revan destroyed the Star Forge and Malak, saving the Republic—but "
            "later vanished pursuing remnants of the True Sith in the Unknown Regions.\n\n"
            "Legends and Sith cults preserved Revan's mask and teachings, and the Emperor Vitiate "
            "attempted to consume Revan's power on Yavin 4 centuries later."
        ),
        "significance": (
            "Revan illustrates how righteous war can slide into tyranny when the ends justify any means. "
            "Their dual legacy as savior and conqueror made them a touchstone for debates within both Orders.\n\n"
            "The Star Forge campaign and fall of Malak mark one of the Republic's gravest existential "
            "crises before Palpatine's era.\n\n"
            "Revan's mask became an icon of Old Republic heroism and Sith temptation, referenced in "
            "temples from Dromund Kaas to the Unknown Regions."
        ),
        "notableEvents": [
            "Led Jedi crusaders against the Mandalorian Neo-Crusaders",
            "Declared himself Dark Lord of the Sith and built a new Sith Empire",
            "Was betrayed by Darth Malak and captured by the Jedi",
            "Rediscovered identity and defeated Malak at the Star Forge",
            "Vanished while searching for the True Sith threat",
            "Was imprisoned and tortured by the Sith Emperor on Yavin 4",
            "Influenced Sith and Jedi doctrine for centuries after death",
        ],
        "affiliations": [
            "Jedi Order",
            "Revanchist movement",
            "Sith Empire (Old Republic era)",
            "Republic Navy (after redemption)",
            "Companion crew of the Ebon Hawk",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Defied the Council to fight the Mandalorian Wars"},
            {"era": "Old Republic", "event": "Fell to the dark side and ruled as Darth Revan"},
            {"era": "Old Republic", "event": "Was captured and mind-wiped by the Jedi Council"},
            {"era": "Old Republic", "event": "Redeemed and destroyed the Star Forge"},
            {"era": "Old Republic", "event": "Disappeared pursuing threats in the Unknown Regions"},
            {"era": "Old Republic", "event": "Became a legendary figure studied by later Sith Lords"},
        ],
    },
    "han-solo": {
        "overview": (
            "Han Solo is the quintessential Corellian smuggler whose fast ship and faster mouth made him "
            "a legend from the Outer Rim to the Rebel Alliance. Captain of the Millennium Falcon, he "
            "claimed to care only about credits until friendship with Luke Skywalker and love for Leia "
            "Organa pulled him into the fight against the Empire."
        ),
        "history": (
            "Han grew up on the streets of Corellia under Imperial exploitation before escaping to "
            "carve out a life as a pilot and smuggler. Winning the Falcon from Lando Calrissian in "
            "a sabacc game became the turning point that defined his career.\n\n"
            "Hired by Obi-Wan Kenobi and Luke to reach Alderaan, Han initially planned to collect "
            "his fee and leave. Instead he returned during the Death Star escape and later led the "
            "Rebel strike on Yavin, earning a medal he famously claimed he never sought.\n\n"
            "Frozen in carbonite by Jabba the Hutt after a debt gone wrong, Han was rescued by his "
            "friends on Tatooine. He commanded the Alliance fleet at Endor and continued serving the "
            "New Republic as a general despite preferring private life.\n\n"
            "Even in later years, Han struggled to reconcile fatherhood with his past, a tension "
            "that resurfaced when Ben Solo fell to the dark side and Han made one final attempt at redemption."
        ),
        "significance": (
            "Han Solo represents the reluctant hero—proof that ordinary scoundrels can choose "
            "extraordinary loyalty when the stakes demand it.\n\n"
            "The Millennium Falcon and Han's partnership with Chewbacca became symbols of found family "
            "throughout the Rebellion era.\n\n"
            "His arc from cynic to general influenced countless recruits who believed the Alliance "
            "needed heart as much as it needed Jedi."
        ),
        "notableEvents": [
            "Won the Millennium Falcon from Lando Calrissian",
            "Transported Luke and Obi-Wan on the Falcon's first famous run",
            "Returned to save Luke during the Death Star trench run",
            "Led the strike team that destroyed the shield generator on Endor",
            "Rescued from carbonite in Jabba's palace on Tatooine",
            "Served as a general in the New Republic Defense Force",
            "Confronted Kylo Ren on Starkiller Base in a final act of love",
        ],
        "affiliations": [
            "Millennium Falcon crew",
            "Rebel Alliance",
            "New Republic",
            "Smugglers' networks",
            "Chewbacca's honor debt",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Escaped Corellia and became an independent smuggler"},
            {"era": "Galactic Civil War", "event": "Joined the Rebellion after the Battle of Yavin"},
            {"era": "Galactic Civil War", "event": "Frozen in carbonite and later rescued from Jabba"},
            {"era": "Galactic Civil War", "event": "Commanded the Endor ground assault"},
            {"era": "New Republic", "event": "Retired briefly before returning to frontline service"},
            {"era": "First Order", "event": "Attempted to reach his son Ben Solo on Starkiller Base"},
        ],
    },
    "leia-organa": {
        "overview": (
            "Leia Organa was princess of Alderaan, senator, general, and one of the founding architects "
            "of the Rebel Alliance. Adopted by Bail and Breha Organa, she carried both royal dignity and "
            "revolutionary fire, becoming a symbol of resistance long before the galaxy learned she was "
            "Luke Skywalker's twin and daughter of Anakin Skywalker."
        ),
        "history": (
            "Raised on Alderaan with secret training in diplomacy and covert operations, Leia served "
            "in the Imperial Senate while secretly funneling resources to the Rebellion. Her capture "
            "aboard the Tantive IV led to the Death Star plans reaching the Alliance.\n\n"
            "After Alderaan's destruction, Leia became the emotional center of the Rebellion, inspiring "
            "cells across the galaxy. She helped coordinate the Battle of Yavin, the evacuation of Hoth, "
            "and the mission to Endor.\n\n"
            "In the New Republic era she founded the Resistance when political complacency ignored the "
            "First Order threat. Mother to Ben Solo, she endured his fall to the dark side and continued "
            "leading until her death, passing the torch to Rey and the next generation.\n\n"
            "Leia's holo-messages, tactical brilliance, and refusal to compromise made her one of the "
            "most influential non-Jedi leaders in galactic history."
        ),
        "significance": (
            "Leia proved that leadership in Star Wars extends far beyond lightsabers—strategy, compassion, "
            "and moral clarity can unite disparate worlds.\n\n"
            "Her white robes and braided hair became iconic symbols of defiance against tyranny.\n\n"
            "As a Skywalker who never fully trained as a Jedi yet still touched the Force, she bridges "
            "political and spiritual resistance."
        ),
        "notableEvents": [
            "Smuggled Death Star plans aboard the Tantive IV",
            "Survived interrogation aboard the first Death Star",
            "Coordinated the Rebel victory at the Battle of Yavin",
            "Led the evacuation from Hoth and later the Endor mission",
            "Founded the Resistance against the First Order",
            "Trained Rey in the ways of the Force",
            "Appeared as a Force spirit to guide the final defeat of Palpatine",
        ],
        "affiliations": [
            "House of Organa",
            "Alliance to Restore the Republic",
            "New Republic Senate",
            "Resistance",
            "Skywalker family",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Served as senator while secretly aiding the Rebellion"},
            {"era": "Galactic Civil War", "event": "Became a principal leader after Alderaan's destruction"},
            {"era": "New Republic", "event": "Helped govern and later warned of rising threats"},
            {"era": "First Order", "event": "Founded and led the Resistance"},
            {"era": "First Order", "event": "Mentored Rey and passed on the Skywalker legacy"},
        ],
    },
    "din-djarin": {
        "overview": (
            "Din Djarin is a Mandalorian bounty hunter who found a new creed protecting Grogu, the "
            "Force-sensitive foundling known to fans as the Child. Bound by the Way of Mandalore yet "
            "willing to break clan rules for honor, he became a symbol of quiet heroism in the Outer Rim."
        ),
        "history": (
            "Rescued from a Separatist attack as a child and raised as a foundling by the Children of "
            "the Watch, Din learned to never remove his helmet in the presence of others. He built a "
            "reputation as a skilled if solitary hunter working through the Bounty Hunters' Guild.\n\n"
            "A commission to capture Grogu ended when Din chose the child's safety over payment, "
            "making enemies of Moff Gideon and Imperial remnants. Allies like Cara Dune, Bo-Katan, "
            "and later the Armorer shaped his path back toward Mandalorian unity.\n\n"
            "Din wielded the Darksaber briefly, attempted to redeem Mandalore, and ultimately took "
            "Grogu as his formal apprentice in the ways of Mandalore while allowing the foundling to "
            "train with Luke Skywalker.\n\n"
            "His story reframed Mandalorian culture for a new era—honor, found family, and the creed "
            "above fame."
        ),
        "significance": (
            "Din Djarin revitalized Mandalorian mystique for modern audiences, blending western and "
            "samurai tropes with Star Wars frontier politics.\n\n"
            "His bond with Grogu became a cultural phenomenon, illustrating guardianship over conquest.\n\n"
            "By reuniting scattered Mandalorian clans, Din helped restore a people nearly erased by "
            "the Great Purge."
        ),
        "notableEvents": [
            "Saved Grogu from Imperial remnant forces on Nevarro",
            "Defeated an Imperial light cruiser with allies above Nevarro",
            "Wielded the Darksaber in Mandalorian succession rites",
            "Journeyed to Mandalore seeking redemption for his people",
            "Formally adopted Grogu as a Mandalorian apprentice",
            "Worked with Bo-Katan to reclaim Mandalore",
        ],
        "affiliations": [
            "Children of the Watch",
            "Bounty Hunters' Guild",
            "Clan Mudhorn",
            "Nevarro community",
            "Mandalorian survivors",
        ],
        "timeline": [
            {"era": "Clone Wars", "event": "Rescued by Mandalorian warriors as a foundling"},
            {"era": "Imperial Era", "event": "Raised in the covert and became a bounty hunter"},
            {"era": "New Republic", "event": "Protected Grogu and turned against Imperial clients"},
            {"era": "New Republic", "event": "Led efforts to restore Mandalore and unite clans"},
        ],
    },
    "boba-fett": {
        "overview": (
            "Boba Fett is the silent, armor-clad bounty hunter whose reputation was built on fear, "
            "precision, and the legacy of his father Jango Fett. Clone of the Mandalorian template and "
            "survivor of the Sarlacc, he evolved from Imperial enforcer to crime lord of Mos Espa."
        ),
        "history": (
            "Witnessing Jango's death on Geonosis left Boba obsessed with honor, credits, and the "
            "Mandalorian armor his father wore. He quickly became the galaxy's most feared hunter, "
            "working for Jabba the Hutt and the Empire alike.\n\n"
            "Tracking Han Solo to Bespin, Boba delivered the frozen smuggler to Jabba and met his "
            "apparent end in the Sarlacc pit on Tatooine—though he survived through sheer will and "
            "beskar.\n\n"
            "Decades later Boba reclaimed his armor from Din Djarin, took over Jabba's former territory, "
            "and ruled Mos Espa with Fennec Shand at his side, balancing brutality with pragmatic stability.\n\n"
            "His story ties together clone legacy, Mandalorian heritage, and the underworld economics "
            "of the Outer Rim."
        ),
        "significance": (
            "Boba Fett's minimal screen time in the original trilogy paradoxically made him a fan icon, "
            "proving mystique can outweigh dialogue.\n\n"
            "He embodies the mercenary ethic of the galaxy's margins—loyalty sold to the highest bidder "
            "until personal honor intervenes.\n\n"
            "His survival and later rule on Tatooine show how Empire-era hunters adapted to New Republic "
            "power vacuums."
        ),
        "notableEvents": [
            "Witnessed Jango Fett's death during the Battle of Geonosis",
            "Tracked Han Solo and delivered him to Jabba the Hutt",
            "Survived the Sarlacc pit on Tatooine",
            "Reclaimed his father's Mandalorian armor",
            "Became daimyo of Mos Espa and Jabba's former territories",
            "Allied with Din Djarin against Pyke Syndicate forces",
        ],
        "affiliations": [
            "Bounty Hunters' Guild",
            "Jabba's criminal empire",
            "Fennec Shand's syndicate",
            "Mandalorian armor tradition",
            "Pyke Syndicate ( enemy )",
        ],
        "timeline": [
            {"era": "Clone Wars", "event": "Lost Jango Fett and began his bounty hunting career"},
            {"era": "Imperial Era", "event": "Captured Han Solo for Jabba the Hutt"},
            {"era": "Galactic Civil War", "event": "Fell into the Sarlacc and was presumed dead"},
            {"era": "New Republic", "event": "Reclaimed armor and seized control of Mos Espa"},
        ],
    },
    "thrawn": {
        "overview": (
            "Grand Admiral Thrawn is a brilliant Chiss tactician who rose through the Imperial Navy "
            "by studying art, culture, and enemy psychology. His blue skin and red eyes marked him as "
            "alien in a human-dominated Empire, yet his victories made him one of Palpatine's most "
            "dangerous servants."
        ),
        "history": (
            "Exiled from the Unknown Regions, Thrawn offered his services to the Empire and quickly "
            "proved his strategic genius against insurgents and rival officers. He commanded the "
            "Seventh Fleet and dismantled Rebel cells with surgical precision.\n\n"
            "During the Liberation of Lothal he faced Ezra Bridger and the Ghost crew, ultimately "
            "disappearing with Ezra into hyperspace aboard a purrgil swarm—a fate that removed him "
            "from Imperial politics but not from galactic consequence.\n\n"
            "Years later Thrawn returned from exile in the Unknown Regions to aid the Imperial "
            "remnants and Morgan Elsbeth, threatening the New Republic's fragile peace.\n\n"
            "His methodical cruelty and respect for worthy opponents made him a unique villain among "
            "Imperial leadership."
        ),
        "significance": (
            "Thrawn expanded Star Wars storytelling into the Unknown Regions and proved the Empire "
            "relied on intellect as much as terror.\n\n"
            "His study of art as military intelligence introduced a distinctive tactical philosophy "
            "rarely seen in space opera villains.\n\n"
            "As one of the few non-human Imperial grand admirals, he highlights the Empire's hypocrisy "
            "and pragmatic exceptions."
        ),
        "notableEvents": [
            "Joined the Imperial Navy and rapidly earned command rank",
            "Led the Seventh Fleet against Lothal and Phoenix Squadron",
            "Vanished with Ezra Bridger via purrgil during the Liberation of Lothal",
            "Returned from the Unknown Regions in the New Republic era",
            "Allied with Morgan Elsbeth and the Nightsister remnant",
            "Threatened the New Republic from the shadows of Peridea",
        ],
        "affiliations": [
            "Chiss Ascendancy",
            "Galactic Empire",
            "Seventh Fleet",
            "Imperial Remnant",
            "Night Troopers",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Entered Imperial service and rose to Grand Admiral"},
            {"era": "Imperial Era", "event": "Commanded the siege of Lothal"},
            {"era": "Imperial Era", "event": "Disappeared with Ezra Bridger in the purrgil jump"},
            {"era": "New Republic", "event": "Re-emerged as a leader of Imperial remnants"},
        ],
    },
    "cassian-andor": {
        "overview": (
            "Cassian Andor was a hardened Rebel intelligence officer whose moral compromises and "
            "ultimate sacrifice defined the spirit of Rogue One. Raised in war, he learned that "
            "revolution requires difficult choices—and that knowing the cost makes heroism sharper."
        ),
        "history": (
            "Cassian lost his father to Republic protest violence and grew up fighting Separatists, "
            "then the Empire, across a dozen shadow wars. He did unpleasant work for Rebel intelligence "
            "long before the Alliance went public.\n\n"
            "Tasked with protecting Jyn Erso and verifying the Death Star plans, Cassian assembled "
            "Rogue One on Scarif. Despite orders to kill Galen Erso, he chose hope and led the suicide "
            "mission that transmitted the plans to Leia Organa.\n\n"
            "His earlier years on Ferrix, Aldhani, and in prison camps showed how ordinary people "
            "become radicals when institutions fail them.\n\n"
            "Cassian's death on Scarif ensured the Rebellion could strike the Death Star, linking "
            "everyday sacrifice to galactic salvation."
        ),
        "significance": (
            "Cassian represents the morally gray heart of the Rebellion—not fairy-tale heroes but "
            "people who carry guilt and still fight.\n\n"
            "His relationship with K-2SO and Bix Caleen humanized intelligence operatives often hidden "
            "from myth.\n\n"
            "Rogue One's success rests on his choice to lead a mission with no return."
        ),
        "notableEvents": [
            "Served in Rebel intelligence before the Battle of Yavin",
            "Met Jyn Erso and debated killing her father Galen",
            "Led the assault on Scarif to steal the Death Star plans",
            "Transmitted the plans before dying on the beach",
            "Inspired cells across the Mid Rim during the Aldhani heist",
            "Endured Imperial imprisonment on Narkina 5",
        ],
        "affiliations": [
            "Alliance to Restore the Republic",
            "Rebel intelligence",
            "Rogue One squad",
            "Ferrix community",
            "Mon Mothma's network",
        ],
        "timeline": [
            {"era": "Clone Wars", "event": "Lost family and learned to fight in proxy wars"},
            {"era": "Imperial Era", "event": "Operated as a covert Rebel agent"},
            {"era": "Galactic Civil War", "event": "Led Rogue One on Scarif"},
            {"era": "Galactic Civil War", "event": "Died ensuring the Death Star plans reached the Alliance"},
        ],
    },
    "tatooine": {
        "overview": (
            "Tatooine is a harsh desert world orbiting twin suns at the edge of the Outer Rim, famous "
            "as the homeworld of Anakin and Luke Skywalker. Lawless spaceports, moisture farms, and "
            "Hutt-controlled crime dominate life beneath endless dunes, while ancient secrets lie buried "
            "in the Jundland Wastes and beyond."
        ),
        "history": (
            "Once lush according to legend, Tatooine's oceans vanished millennia ago, leaving a scorched "
            "landscape ruled by jawas, tusken raiders, and off-world miners. The planet avoided Republic "
            "oversight for centuries, becoming a haven for smugglers and slavers.\n\n"
            "The Boonta Eve Classic podrace and Mos Eisley cantina epitomized Tatooine's frontier culture "
            "when Qui-Gon Jinn discovered young Anakin Skywalker in Mos Espa. The boy's victory in the "
            "podrace freed him from Watto and set galactic history in motion.\n\n"
            "Under the Empire, Tatooine remained a backwater yet hosted fugitive Jedi in exile. Obi-Wan "
            "Kenobi guarded Luke on a moisture farm while the Lars family tried to live quietly.\n\n"
            "Jabba the Hutt's death and later cartel shifts changed the underworld balance, but Tatooine "
            "stayed synonymous with destiny, hardship, and the Skywalker saga's beginnings."
        ),
        "significance": (
            "Tatooine is the mythic starting point of the hero's journey in Star Wars—remote, dusty, "
            "and seemingly insignificant until the Force reveals otherwise.\n\n"
            "Its twin suns and endless desert visually symbolize isolation and longing, themes repeated "
            "whenever characters return to the world.\n\n"
            "Economically, Tatooine's moisture farming, podracing, and Hutt racketeering illustrate "
            "how the Outer Rim survives without Core World infrastructure."
        ),
        "notableEvents": [
            "Qui-Gon Jinn discovered Anakin Skywalker in Mos Espa",
            "Anakin won the Boonta Eve Classic podrace and left the planet",
            "Obi-Wan Kenobi brought infant Luke Skywalker to the Lars homestead",
            "Luke Skywalker joined the Rebellion after stormtroopers killed the Lars family",
            "Jabba the Hutt held Han Solo captive in his palace",
            "Luke and allies rescued Han Solo and destroyed Jabba's sail barge",
            "Boba Fett returned to rule Mos Espa in the New Republic era",
        ],
        "affiliations": [
            "Hutt Cartel",
            "Galactic Republic ( nominal )",
            "Galactic Empire (occupation-light)",
            "Moisture farmers' guilds",
            "Jawa clans and Tusken tribes",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Became a backwater after ecological collapse"},
            {"era": "Clone Wars", "event": "Hosted Jabba negotiations and Clone Wars skirmishes"},
            {"era": "Imperial Era", "event": "Sheltered Obi-Wan Kenobi and Luke Skywalker in hiding"},
            {"era": "Galactic Civil War", "event": "Luke left to join the Rebellion after personal tragedy"},
            {"era": "Galactic Civil War", "event": "Saw Jabba's criminal empire destroyed"},
            {"era": "New Republic", "event": "Remained a frontier hub for smugglers and settlers"},
        ],
    },
    "coruscant": {
        "overview": (
            "Coruscant is the gleaming ecumenopolis at the galactic core, seat of the Senate, Jedi Temple, "
            "and Imperial Palace across millennia. Its planet-wide cityscape of towering skycar lanes and "
            "level-spanning districts embodies both cosmopolitan achievement and the concentration of "
            "power that enabled Palpatine's rise."
        ),
        "history": (
            "Continuously urbanized for over twenty thousand years, Coruscant became the administrative "
            "heart of every major galactic government. The Jedi built their great temple above the "
            "sacred world core, anchoring the Order to Republic politics.\n\n"
            "During the Clone Wars, Coruscant suffered Separatist terror attacks and the dramatic "
            "kidnapping of Chancellor Palpatine, which Anakin Skywalker and Obi-Wan Kenobi thwarted "
            "above the city-world's skyline.\n\n"
            "Order 66 transformed the Temple into a massacre site, and the Imperial Palace replaced "
            "it as the Emperor's throne. Coruscant's lower levels sank into poverty while the elite "
            "flourished under Imperial rule.\n\n"
            "After Endor, the New Republic initially avoided Coruscant as capital, yet the world "
            "remained a symbol of galactic unity and bureaucratic inertia."
        ),
        "significance": (
            "Coruscant represents civilization at scale—beauty and corruption stacked in endless vertical "
            "layers. Every regime claims its center while struggling to govern fairly.\n\n"
            "The Jedi Temple's fall on Coruscant marks the Order's public death, while the Senate "
            "Rotunda witnessed democracy's slow strangulation.\n\n"
            "As a setting, Coruscant connects prequel politics, noir underworld stories, and the "
            "grandeur of space opera chase sequences."
        ),
        "notableEvents": [
            "Hosted the Galactic Senate and Jedi Temple for millennia",
            "Survived Separatist bombing and terror campaigns",
            "Was the site of the Battle of Coruscant over the cityscape",
            "Saw the Jedi Temple purge during Order 66",
            "Became the Emperor's throne world as Imperial Center",
            "Hosted underworld intrigue in the lower levels",
            "Remained a political prize in the New Republic era",
        ],
        "affiliations": [
            "Galactic Republic",
            "Jedi Order",
            "Galactic Empire",
            "Coruscant Security Force",
            "New Republic (eventual seat)",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Rose as the capital of galactic civilization"},
            {"era": "Clone Wars", "event": "Endured Separatist attacks and the Battle of Coruscant"},
            {"era": "Imperial Era", "event": "Temple fell and Imperial Palace was established"},
            {"era": "Imperial Era", "event": "Ruled as Imperial Center under Palpatine"},
            {"era": "Galactic Civil War", "event": "Celebrated the Emperor's death in public riots"},
            {"era": "New Republic", "event": "Remained a cultural and political hub"},
        ],
    },
    "naboo": {
        "overview": (
            "Naboo is a pastoral Core world of rolling plains, great lakes, and underwater Gungan cities. "
            "Known for art, diplomacy, and constitutional monarchy, it produced Queen Amidala and Emperor "
            "Palpatine—linking beauty and idealism with the seeds of galactic tyranny."
        ),
        "history": (
            "Human Naboo colonists and the amphibious Gungans long shared the world uneasily until the "
            "Trade Federation invasion forced Queen Amidala to forge an alliance with Boss Nass. The "
            "combined assault on Theed ended the blockade and introduced Anakin Skywalker to the Jedi.\n\n"
            "Senator Palpatine leveraged Naboo's crisis to become Supreme Chancellor, beginning his "
            " ascent while his homeworld remained a symbol of Republic virtue.\n\n"
            "During the Clone Wars, Naboo hosted diplomatic summits and faced Separatist schemes, "
            "including attempts to exploit Gungan traditions.\n\n"
            "Under the Empire, Naboo was occupied lightly but remembered as Palpatine's birthplace, "
            "a fact the New Republic wrestled with when rebuilding identity."
        ),
        "significance": (
            "Naboo's aesthetic—rococo architecture and lush landscapes—contrasts with war, highlighting "
            "what the Republic claimed to protect.\n\n"
            "The Gungan-human alliance models cooperation across deep cultural divides, a theme repeated "
            "when Naboo sends aid to other worlds.\n\n"
            "Politically, Naboo's elective monarchy and Palpatine's origin make it a case study in how "
            "democratic ideals can coexist with hidden authoritarian ambition."
        ),
        "notableEvents": [
            "Trade Federation blockaded and invaded Naboo",
            "Queen Amidala retook Theed with Gungan allies at the Battle of Naboo",
            "Hosted a Clone Wars peace conference at the Varykino lake retreat",
            "Was targeted by Separatist bioweapon and cult plots",
            "Celebrated the end of the Empire with liberation festivals",
            "Produced Senator and Chancellor Sheev Palpatine",
            "Maintained Gungan-human shared governance after the invasion",
        ],
        "affiliations": [
            "Royal House of Naboo",
            "Gungan Grand Army",
            "Galactic Republic",
            "Galactic Empire (reluctantly)",
            "New Republic",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Human settlers and Gungans established shared world"},
            {"era": "Clone Wars", "event": "Trade Federation invasion sparked galactic crisis"},
            {"era": "Clone Wars", "event": "Hosted diplomacy amid Separatist threats"},
            {"era": "Imperial Era", "event": "Lived under subtle Imperial occupation"},
            {"era": "Galactic Civil War", "event": "Supported Rebellion sympathizers quietly"},
            {"era": "New Republic", "event": "Rebuilt reputation apart from Palpatine's shadow"},
        ],
    },
    "hoth": {
        "overview": (
            "Hoth is a remote ice planet in the Anoat sector, infamous as the site of Echo Base and the "
            "Empire's crushing assault during the Galactic Civil War. Blizzards, wampas, and frozen wastes "
            "make it uninhabitable except for brief military encampments and mining ventures."
        ),
        "history": (
            "The Rebel Alliance selected Hoth's sixth moon for Echo Base because its obscurity and "
            "sensor-scrambling meteor activity hid fleet movements. Tauntauns replaced speeders in "
            "extreme cold while shield generators protected the underground complex.\n\n"
            "An Imperial probe droid discovered the base, leading to a massive AT-AT assault on the "
            "ice fields. Luke Skywalker led Rogue Squadron in delaying actions while transports escaped.\n\n"
            "Han Solo and Leia Organa fled aboard the Millennium Falcon through the asteroid belt after "
            "the battle, deepening their bond. Luke received guidance from Obi-Wan's Force spirit to seek Yoda.\n\n"
            "Echo Base was abandoned, but Hoth became legendary as the Rebellion's most desperate "
            "stand and a symbol of survival against overwhelming force."
        ),
        "significance": (
            "Hoth defines the visual language of Star Wars ice warfare—from white armor against white "
            "snow to the lonely silhouette of a tauntaun at dawn.\n\n"
            "The battle proved the Rebellion could survive Imperial might even in defeat, preserving "
            "leadership and hope.\n\n"
            "Environmentally, Hoth shows how hostile worlds become strategic precisely because others "
            "underestimate them."
        ),
        "notableEvents": [
            "Rebel Alliance established Echo Base in the ice caves",
            "Luke Skywalker was attacked by a wampa and escaped",
            "Imperial probe droid discovered the hidden base",
            "Battle of Hoth saw AT-AT walkers assault the shield generator",
            "Rebel transports escaped while troops held the line",
            "Han Solo and Leia Organa fled Hoth aboard the Millennium Falcon",
            "Luke Skywalker departed for Dagobah after receiving Obi-Wan's message",
        ],
        "affiliations": [
            "Alliance to Restore the Republic",
            "Echo Base command",
            "Rogue Squadron",
            "Galactic Empire (invader)",
            "Anoat sector miners",
        ],
        "timeline": [
            {"era": "Galactic Civil War", "event": "Rebel scouts selected Hoth as a hidden base site"},
            {"era": "Galactic Civil War", "event": "Echo Base became operational with shield defenses"},
            {"era": "Galactic Civil War", "event": "Imperial forces detected the base via probe droid"},
            {"era": "Galactic Civil War", "event": "Battle of Hoth forced Rebel evacuation"},
            {"era": "Galactic Civil War", "event": "Base abandoned after successful transport escape"},
            {"era": "New Republic", "event": "Remembered as a pivotal Rebellion battleground"},
        ],
    },
    "mustafar": {
        "overview": (
            "Mustafar is a volcanic hellscape in the Outer Rim where rivers of lava pour between jagged "
            "cliffs beneath a choking ash sky. Sacred to Sith cultists and chosen by Darth Sidious for "
            "Anakin's fall, it later housed Vader's fortress and dark-side alchemy experiments."
        ),
        "history": (
            "Mustafar's native Mustafarians mined the planet's energy-rich minerals from skimming lava "
            "rivers long before off-worlders exploited it. Separatist leadership gathered here under "
            "Sidious's orders, unaware they were walking into betrayal.\n\n"
            "Anakin Skywalker slaughtered the Separatist council before dueling Obi-Wan Kenobi on the "
            "mining platforms. Kenobi's victory left Anakin mutilated and Sidious rebuilt him as Vader.\n\n"
            "The Empire established facilities to refine cortosis and experiment with dark-side artifacts. "
            "Vader's castle, built atop a Sith cave, became a meditation site for his rage and grief.\n\n"
            "Mustafar later attracted Sith cultists of the Sith Eternal and was scoured by Imperial "
            "remnants seeking Vader's legacy after the Emperor's death."
        ),
        "significance": (
            "Mustafar is the crucible of Anakin's transformation into Vader—visually and mythically "
            "the point of no return.\n\n"
            "Its lava rivers symbolize destructive passion, mirroring the duel's emotional intensity "
            "and the physical scarring of the Chosen One.\n\n"
            "As a Sith-adjacent world, Mustafar connects prequel tragedy, Vader's ongoing story, and "
            "sequel-era cult movements."
        ),
        "notableEvents": [
            "Separatist leaders were assassinated by Anakin Skywalker",
            "Anakin Skywalker duelled Obi-Wan Kenobi on lava mining platforms",
            "Darth Vader was born from Anakin's defeat and rescue by Sidious",
            "Fortress Vader was constructed over an ancient Sith cave",
            "Kanan Jarrus and Ezra Bridger infiltrated Imperial facilities",
            "Sith cultists gathered for dark-side rituals",
            "Imperial remnants sought Vader's relics after Endor",
        ],
        "affiliations": [
            "Confederacy of Independent Systems (final council)",
            "Galactic Empire",
            "Sith cultists",
            "Mustafarian miners",
            "Fortress Vader garrison",
        ],
        "timeline": [
            {"era": "Clone Wars", "event": "Hosted Separatist leadership near war's end"},
            {"era": "Imperial Era", "event": "Witnessed Anakin's fall and Vader's birth"},
            {"era": "Imperial Era", "event": "Fortress Vader established as dark-side sanctum"},
            {"era": "Imperial Era", "event": "Imperial mining expanded under harsh conditions"},
            {"era": "Galactic Civil War", "event": "Rebel cells raided Imperial installations"},
            {"era": "New Republic", "event": "Cultists and scavengers contested Vader's legacy"},
        ],
    },
    "korriban": {
        "overview": (
            "Korriban, known in later eras as Moraband, is the ancestral homeworld of the Sith in the "
            "Outer Rim's Stygian Caldera. Valley of the Dark Lords tombs, academy ruins, and shrouds of "
            "the dark side make it a pilgrimage site for aspirants and a warning to Jedi explorers."
        ),
        "history": (
            "The native Sith species built tombs for their greatest kings in the Valley of the Dark Lords, "
            "infusing the world with dark-side energy that persists millennia after their empire fell.\n\n"
            "Exiled Dark Jedi merged with Sith culture here, founding orders that eventually challenged "
            "the Republic. Korriban's academies trained generations of Sith Lords before the Great "
            "Hyperspace War scattered survivors.\n\n"
            "Revan, Malak, and later Bane-era Sith returned to plunder knowledge and confront spirits "
            "of ancient rulers. The Jedi Council eventually quarantined the world, yet expeditions continued.\n\n"
            "Yoda visited Moraband during the Clone Wars to face Sith sorcery trials, proving the planet "
            "still tested even the wisest masters."
        ),
        "significance": (
            "Korriban is the spiritual heart of Sith tradition—where ambition, death, and legacy intertwine "
            "in stone mausoleums.\n\n"
            "Its tombs preserve the memory of Naga Sadow, Marka Ragnos, and other kings who shaped "
            "dark-side philosophy long before Sidious.\n\n"
            "Renamed Moraband in some records to break superstitious hold, the world remains synonymous "
            "with the Sith's origin and their eternal return."
        ),
        "notableEvents": [
            "Ancient Sith kings were entombed in the Valley of the Dark Lords",
            "Exiled Dark Jedi formed the first Sith Empire on Korriban",
            "Revan and Malak plundered tombs during the Jedi Civil War",
            "Darth Bane studied the Rule of Two amid Korriban's ruins",
            "Jedi quarantined the world after repeated Sith resurgences",
            "Yoda underwent trials on Moraband during the Clone Wars",
            "Sith cultists continued pilgrimages in the Imperial era",
        ],
        "affiliations": [
            "Sith Empire (ancient)",
            "Sith Order",
            "Sith Academy of Korriban",
            "Jedi Order (quarantine missions)",
            "Sith cult pilgrimages",
        ],
        "timeline": [
            {"era": "Ancient Era", "event": "Sith species built valley tombs for their kings"},
            {"era": "Old Republic", "event": "Dark Jedi exiles founded Sith traditions here"},
            {"era": "Old Republic", "event": "Great Hyperspace War devastated Korriban"},
            {"era": "Old Republic", "event": "Revan and Malak recovered Sith artifacts"},
            {"era": "Clone Wars", "event": "Yoda faced Sith trials on Moraband"},
            {"era": "Imperial Era", "event": "Remained a forbidden world for Jedi explorers"},
        ],
    },
}


def starfield() -> str:
    coords = [
        (42, 38, 1.2, 0.7), (118, 92, 1.5, 0.5), (380, 54, 1, 0.65), (460, 120, 1.8, 0.45),
        (88, 180, 1, 0.55), (430, 210, 1.2, 0.75), (250, 44, 1.6, 0.6), (310, 150, 1, 0.4),
        (170, 420, 1.3, 0.5), (480, 380, 1, 0.55), (60, 340, 1.7, 0.35), (400, 460, 1.2, 0.65),
        (200, 480, 1, 0.5), (340, 40, 1.4, 0.7), (28, 260, 1.1, 0.45), (490, 260, 1.5, 0.6),
    ]
    return "\n".join(
        f'  <circle cx="{x}" cy="{y}" r="{r}" fill="#ffffff" opacity="{o}"/>'
        for x, y, r, o in coords
    )


def svg_wrap(title: str, accent: str, body: str, extra_style: str = "") -> str:
    style = textwrap.dedent(
        f"""
        <style>
          .bg {{ fill: url(#bgGrad); }}
          .outline {{ fill: none; stroke: {OUTLINE}; stroke-width: 3; stroke-linecap: round; stroke-linejoin: round; }}
          .fill-accent {{ fill: {accent}; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-dark {{ fill: #1a1a2e; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-light {{ fill: #f8fafc; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-mid {{ fill: #94a3b8; stroke: {OUTLINE}; stroke-width: 3; }}
          .fill-red {{ fill: #dc2626; stroke: {OUTLINE}; stroke-width: 3; }}
          .stroke-red {{ fill: none; stroke: #ef4444; stroke-width: 4; stroke-linecap: round; }}
          {extra_style}
        </style>
        """
    )
    return textwrap.dedent(
        f"""\
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="{title}">
          <defs>
            <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stop-color="{accent}" stop-opacity="0.55"/>
              <stop offset="100%" stop-color="#050814" stop-opacity="0.95"/>
            </linearGradient>
          </defs>
          {style}
          <rect class="bg" width="512" height="512" rx="24"/>
          {starfield()}
          {body}
        </svg>
        """
    )


def parse_ships(path: Path) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        ship_class = re.search(r'Class = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        production = re.search(r'ProductionCount = "(.*?)"', block)
        era = re.search(r'Era = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "role": ship_class.group(1) if ship_class else "",
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                    "production": production.group(1) if production else "Unknown",
                    "era": era.group(1) if era else "Unknown era",
                }
            )
    return entries


def ship_archetype(entry: dict) -> str:
    blob = f"{entry['name']} {entry['role']} {entry['desc']}".lower()
    if any(k in blob for k in ("battle station", "dreadnought", "star destroyer", "cruiser", "battleship", "carrier", "frigate", "corvette")):
        if "battle station" in blob or "death star" in blob:
            return "station"
        return "capital"
    if any(k in blob for k in ("bomber", "gunship", "dropship", "lander", "transport", "freighter", "yacht", "shuttle")):
        if any(k in blob for k in ("bomber", "gunship")):
            return "bomber"
        if "shuttle" in blob or "lander" in blob:
            return "shuttle"
        return "freighter"
    if "droid" in blob:
        return "droid"
    if any(k in blob for k in ("speeder", "airspeeder")):
        return "speeder"
    return "fighter"


def generic_ship_profile(entry: dict) -> dict:
    name = entry["name"]
    ship_class = entry["role"]
    desc = entry["desc"]
    production = entry.get("production", "Unknown")
    era = entry.get("era", "Unknown era")
    slug = entry["slug"]

    overview = (
        f"The {name} is a {ship_class.lower()} whose service history spans {era}. "
        f"{desc} Imperial archives, Rebel intelligence briefings, and Mandalorian "
        f"shipyard records estimate total production at {production}, though wartime "
        f"losses and black-market refits make exact counts difficult to verify."
    )

    history_paras = [
        (
            f"Design bureaus first drafted the {name} during the political tensions that "
            f"defined {era}. Engineers prioritised capabilities suited to its role as a "
            f"{ship_class.lower()}, balancing armour, manoeuvrability, and crew requirements "
            f"against the industrial capacity of the factions that ordered it into production."
        ),
        (
            f"As fleet doctrine evolved, the {name} entered front-line service in convoy "
            f"escort, planetary assault, and deep-space patrol missions. {desc} Veterans "
            f"praised its reliability under fire while analysts debated whether mass production "
            f"at {production} diluted quality control across shipyard lines."
        ),
        (
            f"Major campaigns cemented the vessel's reputation — whether as a terror weapon, "
            f"a rebel lifeline, or a smuggler's last hope. Battle damage reports show the "
            f"{ship_class.lower()} could absorb punishment that would destroy lighter craft, "
            f"though attrition rates climbed sharply during the bloodiest years of galactic war."
        ),
        (
            f"In the modern era, surviving hulls appear in private collections, museum "
            f"orbits, and covert fleets. Restorers hunt spare parts across scrap worlds while "
            f"historians argue the {name} symbolises the industrial scale of conflict more "
            f"than any single battle honour."
        ),
    ]

    significance_paras = [
        (
            f"The {name} illustrates how shipwright traditions and wartime desperation "
            f"combine to shape galactic warfare. Its {ship_class.lower()} layout influenced "
            f"successor designs long after production lines fell silent."
        ),
        (
            f"Approximately {production} hulls served during {era}, making the class one of "
            f"the most visible symbols of its faction's naval power. Colour markings and "
            f"unit insignia turned anonymous factory output into icons recognised across "
            f"holonet broadcasts."
        ),
        (
            f"For engineers and tacticians, the {name} remains a case study in trade-offs "
            f"between firepower, crew survival, and maintenance — lessons still taught at "
            f"academies from Coruscant to Mandalore."
        ),
    ]

    eras = pick_eras(slug, 6)
    notable = [
        f"Entered service during {era}",
        f"Estimated production run of {production}",
        f"Deployed in fleet actions tied to {desc.split('.')[0].lower()}",
        f"Survived or inflicted decisive damage in a major naval engagement",
        f"Refitted by field crews to extend operational lifespan",
        f"Captured or scuttled hulls studied by rival factions",
        f"Featured in propaganda celebrating {ship_class.lower()} crews",
        f"Preserved in memorial fleets or scrapped after wars ended",
    ]

    faction = affiliation_from_color(entry["color"])
    affiliations = [
        faction,
        f"{ship_class} fleet wings",
        "Naval shipwright guilds",
        "Fleet maintenance corps",
        "Combat flight schools",
        "Salvage and retrofit yards",
    ][:6]

    timeline = [
        {"era": era.split("(")[0].strip() if "(" in era else eras[0], "event": f"{name} design approved and prototype tested"},
        {"era": eras[1], "event": f"Mass production reaches {production} across active shipyards"},
        {"era": eras[2], "event": f"First major fleet deployment of the {ship_class.lower()}"},
        {"era": eras[3], "event": f"Notable battle honour linked to {name} class actions"},
        {"era": eras[4], "event": f"Late-war refits and attrition reduce active hull numbers"},
        {"era": eras[5], "event": f"Remaining hulls retired, preserved, or lost to scrap raids"},
    ]

    return {
        "overview": overview,
        "history": "\n\n".join(history_paras),
        "significance": "\n\n".join(significance_paras),
        "notableEvents": notable[:8],
        "affiliations": affiliations,
        "timeline": timeline[:7],
    }


def affiliation_from_color(color: str) -> str:
    mapping = {
        "#e11d48": "Alliance to Restore the Republic",
        "#64748b": "Galactic Empire",
        "#6366f1": "Galactic Republic",
        "#0891b2": "Confederacy of Independent Systems",
        "#ca8a04": "Trade Federation",
        "#eab308": "Royal Naboo fleet",
        "#0284c7": "Mandalorian clans",
        "#d97706": "Independent spacers",
        "#2563eb": "Old Republic Navy",
        "#991b1b": "Sith Empire",
        "#334155": "First Order",
        "#f97316": "Resistance",
        "#65a30d": "Bounty hunter guilds",
    }
    return mapping.get(color.lower(), "Independent operators")


def parse_members(path: Path, role_field: str) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        role = re.search(rf'{role_field} = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        if name and slug:
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "role": role.group(1) if role else "",
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                }
            )
    return entries


def parse_planets(path: Path) -> list[dict]:
    text = path.read_text()
    entries = []
    for block in re.findall(r"new\(\)\s*\{(.*?)\}", text, re.DOTALL):
        name = re.search(r'Name = "(.*?)"', block)
        slug = re.search(r'Slug = "(.*?)"', block)
        region = re.search(r'Region = "(.*?)"', block)
        desc = re.search(r'Description = "(.*?)"', block)
        color = re.search(r'Color = "(.*?)"', block)
        image = re.search(r'ImagePath = "(.*?)"', block)
        if name and slug:
            image_path = image.group(1) if image else None
            entries.append(
                {
                    "name": name.group(1),
                    "slug": slug.group(1),
                    "role": region.group(1) if region else "",
                    "desc": desc.group(1) if desc else "",
                    "color": color.group(1) if color else "#7eb8ff",
                    "image_path": image_path,
                    "has_png": bool(image_path and image_path.lower().endswith(".webp")),
                }
            )
    return entries


def slug_seed(slug: str) -> int:
    return int(hashlib.md5(slug.encode()).hexdigest(), 16)


def pick_eras(slug: str, count: int) -> list[str]:
    start = slug_seed(slug) % len(ERAS)
    return [ERAS[(start + i) % len(ERAS)] for i in range(count)]


def character_archetype(entry: dict) -> str:
    blob = f"{entry['name']} {entry['role']} {entry['desc']}".lower()
    if any(k in blob for k in ("droid", "astromech", "protocol", "assassin droid", "utility droid", "security droid")):
        return "droid"
    if any(k in blob for k in ("smuggler", "scoundrel", "bounty hunter", "mercenary", "assassin")):
        return "underworld"
    if any(k in blob for k in ("admiral", "general", "captain", "commander", "trooper", "pilot", "soldier")):
        return "military"
    if any(k in blob for k in ("senator", "leader", "queen", "diplomat", "magistrate")):
        return "political"
    if any(k in blob for k in ("hutt", "crime", "pirate", "cartel")):
        return "criminal"
    if any(k in blob for k in ("mandalorian", "warrior", "guardian")):
        return "warrior"
    return "general"


def generic_character_profile(entry: dict) -> dict:
    name = entry["name"]
    role = entry["role"]
    desc = entry["desc"]
    slug = entry["slug"]
    role_phrase = role or "galactic figure"
    archetype = character_archetype(entry)
    force_line = (
        "The Force rarely dictated their choices, yet their actions still shaped galactic fate."
        if archetype == "droid"
        else "Allies and rivals alike noted a distinctive presence shaped by skill, culture, and circumstance."
    )

    overview = (
        f"{name} stands among the saga's most memorable figures, known throughout the galaxy as a {role_phrase.lower()}. "
        f"{desc} From backwater cantinas to senate chambers and fleet command centers, {name}'s story illustrates "
        f"how individuals outside the Jedi and Sith orders can still move history."
    )

    history_paras = [
        (
            f"Early life records for {name} are fragmentary, yet every account agrees that ambition and survival "
            f"forged their path long before the galactic civil war dominated headlines. {desc} {force_line}"
        ),
        (
            f"As the Republic collapsed and the Empire rose, {name} was pulled into conflicts that rewarded cunning "
            f"as much as courage. Intelligence briefings, smuggler networks, and battlefield communiques all "
            f"reference moments where {name} tipped a local struggle toward a wider consequence."
        ),
        (
            f"The Rebellion, the New Republic, and later remnant powers all kept files on {name}. Some entries "
            f"flatter, others condemn, but historians agree that ignoring {name} makes any chronicle of the era "
            f"incomplete."
        ),
        (
            f"Modern scholars cite {name} when teaching how ordinary citizens, soldiers, and scoundrels responded "
            f"to tyranny. Whether through loyalty, profit, or conscience, {name} demonstrates that the galaxy's "
            f"future is never decided solely in Jedi temples or Sith tombs."
        ),
    ]

    significance_paras = [
        (
            f"As a {role_phrase.lower()}, {name} connects grassroots stories to epic campaigns. Their biography "
            f"helps explain how supply lines, spy rings, and frontier communities sustained the larger factions."
        ),
        (
            f"Popular culture keeps {name} alive in holodramas, recruitment posters, and cantina songs. The color "
            f"{entry['color']} often appears in fan art and reenactment banners associated with their legacy."
        ),
        (
            f"For researchers mapping the Star Wars saga, {name} marks a node where personal loyalty meets "
            f"institutional change—proof that heroism and villainy alike can wear many faces."
        ),
    ]

    eras = pick_eras(slug, 7)
    notable = [
        f"First widely documented appearance of {name} in galactic records",
        f"Rose to prominence as a {role_phrase.lower()} during the {eras[1]}",
        f"Survived or orchestrated a pivotal encounter tied to {name}'s reputation",
        f"Formed alliances that reflected the priorities of their faction and homeworld",
        f"Opposed rivals who threatened {name}'s crew, family, or command",
        f"Witnessed the fall of the Republic and the rise of the Empire firsthand",
        f"Contributed to a turning point still debated by historians of the {eras[4]}",
        f"Inspired later generations who retold {name}'s choices in myth and media",
    ]

    affiliation_pool = {
        "droid": ["Independent operators", "Mechanic guilds", "Companion crews", "Memory archives", "Salvage markets"],
        "underworld": ["Smuggler rings", "Bounty hunter guilds", "Outer Rim ports", "Shadow brokers", "Freighter captains"],
        "military": ["Fleet command", "Ground assault units", "Intelligence corps", "Veterans' networks", "Training academies"],
        "political": ["Senate delegations", "Royal courts", "Diplomatic corps", "Relief foundations", "Allied systems"],
        "criminal": ["Hutt syndicates", "Black-market cartels", "Gambling dens", "Slaver routes", "Pirate fleets"],
        "warrior": ["Mercenary companies", "Clan alliances", "Colonial militias", "Honor societies", "Arms dealers"],
        "general": ["Independent agents", "Allied factions", "Local militias", "Trade consortiums", "Historians' guilds"],
    }
    affiliations = [role] + [a for a in affiliation_pool[archetype] if a != role][:5]

    timeline = [
        {"era": eras[0], "event": f"{name} enters the historical record as a {role_phrase.lower()}"},
        {"era": eras[1], "event": f"Builds a reputation during the {eras[1]}"},
        {"era": eras[2], "event": f"Acts decisively in events tied to {desc.split('.')[0].lower()}"},
        {"era": eras[3], "event": f"Navigates crisis as galactic institutions fracture"},
        {"era": eras[4], "event": f"Plays a role in campaigns associated with the {eras[4]}"},
        {"era": eras[5], "event": f"Legacy debated and commemorated across the {eras[5]}"},
    ]

    return {
        "overview": overview,
        "history": "\n\n".join(history_paras),
        "significance": "\n\n".join(significance_paras),
        "notableEvents": notable[:8],
        "affiliations": affiliations[:6],
        "timeline": timeline[:7],
    }


def generic_profile(entry: dict, category: str) -> dict:
    if category == "characters":
        return generic_character_profile(entry)

    if category == "ships":
        return generic_ship_profile(entry)

    name = entry["name"]
    role = entry["role"]
    desc = entry["desc"]
    slug = entry["slug"]
    labels = {"jedi": "Jedi", "sith": "Sith Lord", "planets": "world", "characters": "galactic figure"}
    label = labels[category]
    role_phrase = role or f"noted {label}"

    overview = (
        f"{name} is remembered across the galaxy as a {role_phrase.lower()} whose story intersects "
        f"with pivotal eras of Star Wars history. {desc} Scholars of the {role_phrase.split()[0] if role else 'Republic'} "
        f"traditions cite {name} when explaining how individual choices ripple through wars, councils, "
        f"and frontier worlds alike."
    )

    history_paras = [
        (
            f"Early records place {name} within the broader tapestry of the {role_phrase}, long before "
            f"the conflicts that would define modern galactic politics. {desc} Allies and rivals alike "
            f"noted a distinctive presence shaped by training, culture, and the constant pull of the Force."
        ),
        (
            f"As tensions escalated between major factions, {name} was drawn into campaigns that tested "
            f"conviction as much as skill. Field reports describe decisive moments where strategy, diplomacy, "
            f"or raw power shifted the balance—often at personal cost."
        ),
        (
            f"The fall of old institutions did not erase {name}'s influence. Survivors, historians, and "
            f"later movements retold their deeds, sometimes mythologizing details yet preserving the core "
            f"truth that one figure can anchor hope or fear across decades."
        ),
        (
            f"In contemporary chronicles, {name} serves as a lens for understanding the {role_phrase.lower()} "
            f"and its legacy. Whether celebrated or condemned, their story invites new generations to "
            f"question what duty demands when the galaxy burns."
        ),
    ]

    significance_paras = [
        (
            f"{name} embodies the ideals and contradictions associated with the {role_phrase.lower()}. "
            f"Their biography helps explain how local choices on distant worlds connect to senate halls "
            f"and temple councils."
        ),
        (
            f"Cultural memory keeps {name} alive in holodramas, academy lectures, and pilgrim routes. "
            f"The accent color {entry['color']} often appears in fan art and ceremonial banners tied "
            f"to their legacy."
        ),
        (
            f"For researchers mapping galactic history, {name} marks a node where personal narrative "
            f"meets institutional change—proof that individuals can steer eras even when structures "
            f"claim inevitability."
        ),
    ]

    eras = pick_eras(slug, 7)
    notable = [
        f"First documented emergence of {name} within galactic records",
        f"Played a key role during the {eras[1]} in {role or 'their sphere of influence'}",
        f"Survived or shaped a major battle linked to {name}'s reputation",
        f"Formed alliances that reflected the priorities of the {role_phrase.lower()}",
        f"Confronted rivals who challenged {name}'s vision of order",
        f"Witnessed the transformation of the galaxy's ruling powers",
        f"Left artifacts, teachings, or monuments still cited in the {eras[4]}",
        f"Inspired later movements that reinterpreted {name}'s choices",
    ]

    affiliations = [
        role or "Independent agents",
        f"Allies of {name}",
        "Galactic historians' archives",
        f"{role.split()[0] if role else 'Regional'} networks",
        "Local defense militias",
        "Neutral observers of the Force",
    ][:5]

    timeline = [
        {"era": eras[0], "event": f"{name} enters historical record as {role_phrase.lower()}"},
        {"era": eras[1], "event": f"Participates in a pivotal campaign during the {eras[1]}"},
        {"era": eras[2], "event": f"Becomes widely known for actions tied to {desc.split('.')[0].lower()}"},
        {"era": eras[3], "event": f"Navigates crisis as institutions around {name} fracture"},
        {"era": eras[4], "event": f"Legacy debated by scholars of the {eras[4]}"},
        {"era": eras[5], "event": f"Commemorated in archives celebrating {role or 'galactic history'}"},
    ]

    return {
        "overview": overview,
        "history": "\n\n".join(history_paras),
        "significance": "\n\n".join(significance_paras),
        "notableEvents": notable[:8],
        "affiliations": affiliations[:6],
        "timeline": timeline[:7],
    }


def merge_profile(entry: dict, category: str) -> dict:
    base = generic_profile(entry, category)
    enriched = ENRICHMENTS.get(entry["slug"], {})
    if category == "ships":
        enriched = {**SHIP_ENRICHMENTS.get(entry["slug"], {}), **enriched}
    for key, value in enriched.items():
        base[key] = value
    return base


def portrait_path(category: str, entry: dict) -> str:
    if category == "planets":
        if entry.get("has_png"):
            return entry["image_path"]
        return f"/images/planets/{entry['slug']}.svg"
    return f"/images/{category}/{entry['slug']}.webp"


def gallery_for(entry: dict, category: str) -> list[dict]:
    slug = entry["slug"]
    name = entry["name"]
    portrait = portrait_path(category, entry)
    if category == "jedi":
        return [
            {"path": f"/images/jedi/{slug}-scene.webp", "caption": f"Cinematic illustration — {name}"},
        ]
    if category == "sith":
        return [
            {"path": f"/images/sith/{slug}-scene.webp", "caption": f"Cinematic illustration — {name}"},
        ]
    if category == "characters":
        return [
            {"path": f"/images/characters/{slug}-scene.webp", "caption": f"Cinematic illustration — {name}"},
        ]
    if category == "ships":
        return [
            {"path": f"/images/ships/{slug}-scene.webp", "caption": f"Cinematic illustration — {name}"},
        ]
    if category == "planets":
        return [
            {"path": f"/images/planets/{slug}-hero.webp", "caption": f"Cinematic view of {name}"},
        ]
    return []


def planet_globe_svg(entry: dict) -> str:
    accent = entry["color"]
    seed = slug_seed(entry["slug"])
    cx = 256 + (seed % 21) - 10
    cy = 260 + ((seed // 21) % 17) - 8
    body = textwrap.dedent(
        f"""
          <circle cx="{cx}" cy="{cy}" r="148" fill="#000" opacity="0.25"/>
          <circle class="fill-accent" cx="{cx}" cy="{cy}" r="138"/>
          <ellipse class="fill-light" cx="{cx - 40}" cy="{cy - 30}" rx="58" ry="34" opacity="0.55"/>
          <ellipse class="fill-accent" cx="{cx + 30}" cy="{cy + 20}" rx="72" ry="40" opacity="0.75"/>
          <ellipse class="fill-light" cx="{cx + 10}" cy="{cy - 50}" rx="46" ry="22" opacity="0.45"/>
          <ellipse fill="none" stroke="{OUTLINE}" stroke-width="4" cx="{cx}" cy="{cy}" rx="148" ry="138"/>
          <ellipse fill="none" stroke="#ffffff" stroke-width="3" opacity="0.35" cx="{cx - 55}" cy="{cy - 65}" rx="90" ry="28" transform="rotate(-18 {cx - 55} {cy - 65})"/>
          <circle class="fill-light" cx="{cx - 70}" cy="{cy - 80}" r="22" opacity="0.25"/>
        """
    )
    return svg_wrap(f"{entry['name']} globe", accent, body)


def planet_scene_svg(entry: dict) -> str:
    accent = entry["color"]
    blob = entry["desc"].lower()
    if any(k in blob for k in ("desert", "dune", "sand", "arid")):
        ground = '<rect class="fill-accent" x="0" y="360" width="512" height="152"/>\n  <path class="fill-light" d="M0 390 Q128 350 256 390 T512 390 L512 512 H0 Z" opacity="0.5"/>'
    elif any(k in blob for k in ("ice", "snow", "frozen", "glacier")):
        ground = '<rect class="fill-light" x="0" y="350" width="512" height="162"/>\n  <path class="fill-accent" d="M0 380 L120 320 L220 390 L340 300 L512 370 L512 512 H0 Z" opacity="0.6"/>'
    elif any(k in blob for k in ("ocean", "water", "sea", "jungle", "forest")):
        ground = '<rect class="fill-accent" x="0" y="370" width="512" height="142"/>\n  <circle class="fill-light" cx="120" cy="390" r="28"/>\n  <circle class="fill-light" cx="380" cy="410" r="36"/>'
    elif any(k in blob for k in ("volcan", "lava", "molten")):
        ground = '<rect class="fill-red" x="0" y="360" width="512" height="152"/>\n  <path class="fill-accent" d="M80 360 L140 300 L200 360 L260 290 L320 360 L380 310 L440 360 Z"/>'
    elif any(k in blob for k in ("gas", "cloud", "tibanna")):
        ground = '<ellipse class="fill-light" cx="256" cy="380" rx="200" ry="70"/>\n  <ellipse class="fill-accent" cx="256" cy="360" rx="160" ry="50" opacity="0.7"/>'
    else:
        ground = '<rect class="fill-accent" x="0" y="370" width="512" height="142"/>\n  <path class="fill-light" d="M0 400 Q256 340 512 400 L512 512 H0 Z" opacity="0.45"/>'
    body = textwrap.dedent(
        f"""
          <circle class="fill-light" cx="420" cy="110" r="36" opacity="0.85"/>
          {ground}
          <path class="fill-dark" d="M40 380 Q256 320 472 380" fill="none" stroke="{OUTLINE}" stroke-width="4"/>
        """
    )
    return svg_wrap(f"{entry['name']} landscape", accent, body)


def character_scene_svg(entry: dict) -> str:
    accent = entry["color"]
    archetype = character_archetype(entry)
    if archetype == "droid":
        body = textwrap.dedent(
            """
          <rect class="fill-mid" x="80" y="120" width="352" height="280" rx="24"/>
          <rect class="fill-light" x="120" y="160" width="120" height="90" rx="12"/>
          <rect class="fill-light" x="272" y="160" width="120" height="90" rx="12"/>
          <circle class="fill-accent" cx="180" cy="320" r="22"/>
          <circle class="fill-accent" cx="332" cy="320" r="22"/>
          <line class="outline" x1="256" y1="80" x2="256" y2="140"/>
          <rect class="fill-dark" x="220" y="360" width="72" height="100" rx="10"/>
        """
        )
    elif archetype == "military":
        body = textwrap.dedent(
            """
          <rect class="fill-mid" x="0" y="360" width="512" height="152"/>
          <path class="fill-accent" d="M60 360 L140 220 L220 360 Z"/>
          <path class="fill-accent" d="M292 360 L372 200 L452 360 Z"/>
          <rect class="fill-light" x="220" y="280" width="72" height="80" rx="8"/>
          <line class="outline" x1="120" y1="300" x2="220" y2="340"/>
          <line class="outline" x1="392" y1="300" x2="292" y2="340"/>
        """
        )
    elif archetype == "political":
        body = textwrap.dedent(
            """
          <rect class="fill-light" x="96" y="100" width="320" height="220" rx="16"/>
          <rect class="fill-accent" x="130" y="140" width="252" height="36" rx="8"/>
          <rect class="fill-accent" x="130" y="200" width="180" height="24" rx="6" opacity="0.7"/>
          <rect class="fill-accent" x="130" y="240" width="210" height="24" rx="6" opacity="0.7"/>
          <path class="fill-dark" d="M0 380 Q256 320 512 380 L512 512 H0 Z" opacity="0.35"/>
        """
        )
    elif archetype == "criminal":
        body = textwrap.dedent(
            """
          <rect class="fill-accent" x="0" y="380" width="512" height="132"/>
          <ellipse class="fill-light" cx="256" cy="300" rx="120" ry="70"/>
          <rect class="fill-dark" x="180" y="220" width="152" height="80" rx="20"/>
          <circle class="fill-accent" cx="140" cy="260" r="16"/>
          <circle class="fill-accent" cx="372" cy="260" r="16"/>
        """
        )
    else:
        body = textwrap.dedent(
            """
          <rect class="fill-dark" x="40" y="320" width="432" height="140" rx="20" opacity="0.5"/>
          <circle class="fill-light" cx="420" cy="120" r="34"/>
          <path class="fill-accent" d="M80 360 Q256 280 432 360"/>
          <rect class="fill-light" x="196" y="180" width="120" height="160" rx="12"/>
          <path class="fill-accent" d="M256 120 L286 180 L226 180 Z"/>
          <line class="outline" x1="90" y1="390" x2="170" y2="330"/>
          <line class="outline" x1="422" y1="390" x2="342" y2="330"/>
        """
        )
    return svg_wrap(f"{entry['name']} scene", accent, body)


def character_emblem_svg(entry: dict) -> str:
    accent = entry["color"]
    archetype = character_archetype(entry)
    if archetype == "droid":
        inner = '<rect class="fill-accent" x="196" y="196" width="120" height="120" rx="24"/>'
    elif archetype == "military":
        inner = '<polygon class="fill-accent" points="256,150 330,290 182,290"/>'
    elif archetype == "political":
        inner = '<circle class="fill-accent" cx="256" cy="256" r="72"/>'
    elif archetype == "criminal":
        inner = '<polygon class="fill-accent" points="256,160 340,260 256,360 172,260"/>'
    else:
        inner = '<path class="fill-accent" d="M256 150 L300 250 L390 250 L320 310 L345 400 L256 350 L167 400 L192 310 L122 250 L212 250 Z"/>'
    body = textwrap.dedent(
        f"""
          <circle class="fill-light" cx="256" cy="256" r="148"/>
          <circle class="outline" cx="256" cy="256" r="148"/>
          {inner}
          <circle class="fill-light" cx="256" cy="256" r="28"/>
        """
    )
    return svg_wrap(f"Emblem — {entry['name']}", accent, body)


def planet_chart_svg(entry: dict) -> str:
    accent = entry["color"]
    seed = slug_seed(entry["slug"])
    x = 140 + (seed % 220)
    y = 140 + ((seed // 220) % 180)
    body = textwrap.dedent(
        f"""
          <rect class="fill-dark" x="64" y="64" width="384" height="384" rx="24" opacity="0.85"/>
          <circle class="outline" cx="256" cy="256" r="160"/>
          <circle class="fill-light" cx="180" cy="180" r="4"/>
          <circle class="fill-light" cx="320" cy="150" r="3"/>
          <circle class="fill-light" cx="360" cy="280" r="3"/>
          <circle class="fill-light" cx="210" cy="330" r="4"/>
          <circle class="fill-light" cx="300" cy="340" r="3"/>
          <circle class="fill-accent" cx="{x}" cy="{y}" r="14"/>
          <line class="outline" x1="{x}" y1="{y}" x2="{x + 40}" y2="{y - 30}"/>
          <text x="72" y="100" fill="#f8fafc" font-family="sans-serif" font-size="22">{entry['name']}</text>
        """
    )
    return svg_wrap(f"Star chart — {entry['name']}", accent, body)


def write_always(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content)


def main() -> None:
    datasets = [
        ("jedi", parse_members(DATA / "JediData.cs", "Rank")),
        ("sith", parse_members(DATA / "SithData.cs", "Title")),
        ("planets", parse_planets(DATA / "GalaxyData.cs")),
        ("characters", parse_members(DATA / "CharacterData.cs", "Role")),
        ("ships", parse_ships(DATA / "ShipData.cs")),
    ]

    counts = {
        "profiles": 0,
        "planet_globes": 0,
        "jedi_scenes": 0,
        "sith_scenes": 0,
        "character_scenes": 0,
        "planet_scenes": 0,
        "ship_scenes": 0,
        "jedi_emblems": 0,
        "sith_emblems": 0,
        "character_emblems": 0,
        "planet_charts": 0,
        "ship_blueprints": 0,
    }

    for category, entries in datasets:
        img_dir = IMAGES / category
        profile_dir = PROFILES / category
        for entry in entries:
            slug = entry["slug"]
            profile = merge_profile(entry, category)
            profile["gallery"] = gallery_for(entry, category)
            profile_path = profile_dir / f"{slug}.json"
            write_always(profile_path, json.dumps(profile, indent=2, ensure_ascii=False) + "\n")
            counts["profiles"] += 1

            if category == "jedi":
                write_always(img_dir / f"{slug}-scene.svg", jedi_scene_svg(entry))
                write_always(img_dir / f"{slug}-emblem.svg", jedi_emblem_svg(entry))
                counts["jedi_scenes"] += 1
                counts["jedi_emblems"] += 1
            elif category == "sith":
                write_always(img_dir / f"{slug}-scene.svg", sith_scene_svg(entry))
                write_always(img_dir / f"{slug}-emblem.svg", sith_emblem_svg(entry))
                counts["sith_scenes"] += 1
                counts["sith_emblems"] += 1
            elif category == "characters":
                write_always(img_dir / f"{slug}-scene.svg", character_scene_svg(entry))
                write_always(img_dir / f"{slug}-emblem.svg", character_emblem_svg(entry))
                counts["character_scenes"] += 1
                counts["character_emblems"] += 1
            elif category == "ships":
                write_always(img_dir / f"{slug}-scene.svg", ship_scene_svg(entry))
                write_always(img_dir / f"{slug}-blueprint.svg", ship_blueprint_svg(entry))
                counts["ship_scenes"] += 1
                counts["ship_blueprints"] += 1
            else:
                if not entry.get("has_png"):
                    write_always(img_dir / f"{slug}.svg", planet_globe_svg(entry))
                    counts["planet_globes"] += 1
                write_always(img_dir / f"{slug}-scene.svg", planet_scene_svg(entry))
                write_always(img_dir / f"{slug}-chart.svg", planet_chart_svg(entry))
                counts["planet_scenes"] += 1
                counts["planet_charts"] += 1

    total_images = (
        counts["planet_globes"]
        + counts["jedi_scenes"]
        + counts["sith_scenes"]
        + counts["character_scenes"]
        + counts["planet_scenes"]
        + counts["ship_scenes"]
        + counts["jedi_emblems"]
        + counts["sith_emblems"]
        + counts["character_emblems"]
        + counts["planet_charts"]
        + counts["ship_blueprints"]
    )

    print("Directory profile generation complete.")
    print(f"  Profiles JSON:       {counts['profiles']}")
    print(f"  Planet globes:       {counts['planet_globes']} (skipped PNG ImagePath planets)")
    print(f"  Jedi scene SVGs:     {counts['jedi_scenes']}")
    print(f"  Sith scene SVGs:     {counts['sith_scenes']}")
    print(f"  Character scene SVGs:{counts['character_scenes']}")
    print(f"  Planet scene SVGs:   {counts['planet_scenes']}")
    print(f"  Ship scene SVGs:     {counts['ship_scenes']}")
    print(f"  Jedi emblems:        {counts['jedi_emblems']}")
    print(f"  Sith emblems:        {counts['sith_emblems']}")
    print(f"  Character emblems:   {counts['character_emblems']}")
    print(f"  Planet charts:       {counts['planet_charts']}")
    print(f"  Ship blueprints:     {counts['ship_blueprints']}")
    print(f"  Total images:        {total_images}")


if __name__ == "__main__":
    main()
