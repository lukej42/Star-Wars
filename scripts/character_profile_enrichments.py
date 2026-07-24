#!/usr/bin/env python3
"""Hand-crafted detailed profiles for major Characters Directory entries."""

from __future__ import annotations

CHARACTER_ENRICHMENTS: dict[str, dict] = {
    "han-solo": {
        "overview": (
            "Han Solo is the quintessential Corellian smuggler whose fast ship and faster mouth made him a legend "
            "from the Outer Rim to the Rebel Alliance. Captain of the Millennium Falcon, he claimed to care only "
            "about credits until friendship with Luke Skywalker and love for Leia Organa pulled him into the fight "
            "against the Empire."
        ),
        "history": (
            "Han grew up on the streets of Corellia under Imperial exploitation before escaping to carve out a life "
            "as a pilot and smuggler. Winning the Falcon from Lando Calrissian in a sabacc game became the turning "
            "point that defined his career.\n\n"
            "Hired by Obi-Wan Kenobi and Luke to reach Alderaan, Han initially planned to collect his fee and leave. "
            "Instead he returned during the Death Star escape and later led the Rebel strike on Yavin, earning a medal "
            "he famously claimed he never sought.\n\n"
            "Frozen in carbonite by Jabba the Hutt after a debt gone wrong, Han was rescued by his friends on Tatooine. "
            "He commanded the Alliance fleet at Endor and continued serving the New Republic as a general despite "
            "preferring private life.\n\n"
            "Even in later years, Han struggled to reconcile fatherhood with his past, a tension that resurfaced when "
            "Ben Solo fell to the dark side and Han made one final attempt at redemption."
        ),
        "significance": (
            "Han Solo represents the reluctant hero—proof that ordinary scoundrels can choose extraordinary loyalty "
            "when the stakes demand it.\n\n"
            "The Millennium Falcon and Han's partnership with Chewbacca became symbols of found family throughout the "
            "Rebellion era.\n\n"
            "His arc from cynic to general influenced countless recruits who believed the Alliance needed heart as much "
            "as it needed Jedi."
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
            {"era": "First Order", "event": "Attempted to reach Ben Solo on Starkiller Base"},
        ],
    },
    "shmi-skywalker": {
        "overview": (
            "Shmi Skywalker is the gentle heart of Anakin's origin—a slave on Tatooine whose faith in her son's "
            "goodness outlasted her own suffering until tragedy pushed him toward the dark side."
        ),
        "history": (
            "Shmi was sold to Watto along with young Anakin, raising him in the harsh Jundland Wastes with love despite "
            "their bondage. She told Anakin he was a miracle with no father, a mystery Qui-Gon Jinn sensed in the Force.\n\n"
            "When Anakin left with the Jedi, Shmi remained behind, later freed and married Cliegg Lars. Her brief happiness "
            "ended when Tusken Raiders abducted her; Cliegg's rescue attempt cost him a leg, and Shmi died in Anakin's arms "
            "after he slaughtered the entire Tusken camp in grief and rage.\n\n"
            "That loss became the first great wound in Anakin's fall—proof that even Jedi power could not protect those "
            "he loved most."
        ),
        "significance": (
            "Shmi embodies the civilian cost of galactic war and slavery that the Republic ignored.\n\n"
            "Her death is the emotional hinge between Anakin the hero and Anakin the avenger.\n\n"
            "Luke Skywalker's later life on Tatooine echoes the homestead she never saw freed in her lifetime."
        ),
        "notableEvents": [
            "Raised Anakin Skywalker under Watto's ownership",
            "Released Anakin to Qui-Gon Jinn after the Boonta Eve podrace",
            "Married Cliegg Lars and gained freedom briefly",
            "Abducted and tortured by Tusken Raiders",
            "Died in Anakin's arms on Tatooine",
        ],
        "affiliations": [
            "Lars homestead",
            "Watto's junk shop",
            "Tatooine moisture farming community",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Gave birth to Anakin Skywalker on Tatooine"},
            {"era": "Old Republic", "event": "Parted from Anakin when he left for Jedi training"},
            {"era": "Clone Wars", "event": "Killed by Tusken Raiders; found by Anakin"},
        ],
    },
    "leia-organa": {
        "overview": (
            "Leia Organa was a princess, senator, general, and symbol of resistance whose courage held the Rebel Alliance "
            "together from the Death Star's corridors to the birth of the New Republic."
        ),
        "history": (
            "Adopted by Bail and Breha Organa of Alderaan, Leia grew up as royalty while secretly learning statecraft and "
            "rebellion. She became the youngest Imperial senator while ferrying plans for the Death Star to Obi-Wan Kenobi.\n\n"
            "Captured by Darth Vader, she endured interrogation aboard the Death Star yet never betrayed the Alliance. "
            "Rescued by Luke and Han, she coordinated the Battle of Yavin and later the evacuation of Hoth.\n\n"
            "When Alderaan was destroyed, Leia channeled grief into leadership, helping build the New Republic and later "
            "founding the Resistance when the First Order rose.\n\n"
            "She trained briefly as a Jedi under Luke before returning to politics, ultimately passing her legacy to Rey "
            "and the next generation of freedom fighters."
        ),
        "significance": (
            "Leia proves that leadership in Star Wars is not limited to lightsabers—diplomacy, strategy, and moral clarity "
            "can move galaxies.\n\n"
            "Her twin bond with Luke and complicated history with Han define the Skywalker saga's emotional core.\n\n"
            "The Resistance she built carried the Rebellion's ideals into a new era of tyranny."
        ),
        "notableEvents": [
            "Carried Death Star plans hidden in R2-D2",
            "Survived Alderaan's destruction",
            "Led the Battle of Endor's coordination",
            "Founded the Resistance against the First Order",
            "Confronted Kylo Ren on the Supremacy",
            "Became one with the Force after guiding Rey",
        ],
        "affiliations": [
            "House of Organa",
            "Alliance to Restore the Republic",
            "New Republic Senate",
            "Resistance",
        ],
        "timeline": [
            {"era": "Imperial Era", "event": "Served as senator while aiding the Rebellion"},
            {"era": "Galactic Civil War", "event": "Commanded key Rebel operations"},
            {"era": "New Republic", "event": "Helped govern the post-Empire galaxy"},
            {"era": "First Order", "event": "Led the Resistance until her death"},
        ],
    },
}
