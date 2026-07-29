#!/usr/bin/env python3
"""Rich profile content for Knights of the Old Republic / Old Republic Jedi and Sith."""

from __future__ import annotations

KOTOR_ENRICHMENTS: dict[str, dict] = {
    "bastila-shan": {
        "overview": (
            "Bastila Shan was a Jedi Padawan whose mastery of Battle Meditation made her one of the "
            "Republic's most valuable assets during the Jedi Civil War. Captured by Darth Malak and "
            "forged into a Force bond with the amnesiac Revan, she became the moral fulcrum of the "
            "Star Forge campaign—proof that even prodigies could waver between light and dark."
        ),
        "history": (
            "Trained on Dantooine under the enclave's masters, Bastila demonstrated rare Battle "
            "Meditation that could tilt entire fleet engagements. When Malak turned on Revan above "
            "Taris, Bastila escaped aboard the Endar Spire with the mind-wiped former Sith Lord, "
            "binding their fates through the Force.\n\n"
            "Their journey across Taris, Dantooine, and the Rakata homeworld tested Bastila's "
            "conviction. Malak's torture and Revan's past tempted her toward the dark side, yet "
            "redemption on the Star Forge restored her to the light and secured the Republic's "
            "survival at Rakata Prime.\n\n"
            "Bastila later helped rebuild Jedi training traditions and became an ancestor of the "
            "Shan bloodline that would produce Grand Master Satele Shan during the Great Galactic War."
        ),
        "significance": (
            "Bastila embodies the Jedi struggle against pride and attachment in wartime. Her Battle "
            "Meditation links personal discipline to galactic strategy—a theme the Old Republic era "
            "returns to again and again.\n\n"
            "Her bond with Revan remains one of Legends' defining Force connections, cited whenever "
            "masters debate whether shared destiny strengthens or corrupts knights.\n\n"
            "The Shan lineage connects the Jedi Civil War to the TOR-era Republic, bridging KOTOR "
            "and The Old Republic MMO storytelling."
        ),
        "notableEvents": [
            "Demonstrated Battle Meditation during the opening battles of the Jedi Civil War",
            "Escaped Taris with Revan after the Endar Spire was destroyed",
            "Was captured and tempted by Darth Malak",
            "Helped lead the assault on the Star Forge at Rakata Prime",
            "Survived the fall of Malak and the collapse of Revan's Sith Empire",
        ],
        "affiliations": [
            "Jedi Order",
            "Galactic Republic",
            "Dantooine Jedi Enclave",
            "Ebon Hawk crew",
            "Shan family lineage",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Trained as a Battle Meditation prodigy on Dantooine"},
            {"era": "Old Republic", "event": "Bonded with Revan during the escape from Taris"},
            {"era": "Old Republic", "event": "Was captured and corrupted by Darth Malak"},
            {"era": "Old Republic", "event": "Returned to the light at the Battle of Rakata Prime"},
            {"era": "Old Republic", "event": "Became ancestor of the Shan Jedi bloodline"},
        ],
    },
    "jolee-bindo": {
        "overview": (
            "Jolee Bindo was a hermit Jedi who abandoned the Order after tragedy on Kashyyyk, yet "
            "returned to the galaxy's wars with sardonic wisdom and unorthodox light-side philosophy. "
            "His exile in the Shadowlands made him a living critique of Jedi dogma—and an indispensable "
            "ally during Revan's quest."
        ),
        "history": (
            "Once a conventional Jedi, Jolee left the Order when rigid doctrine failed to prevent "
            "personal loss. He settled in Kashyyyk's Shadowlands, studying the Force outside temple "
            "politics until Revan's crew required a guide through the ancient forest.\n\n"
            "Jolee rejoined the fight against Malak's Sith Empire aboard the Ebon Hawk, offering "
            "pragmatic counsel on love, attachment, and the gray paths between light and dark. His "
            "Mind Trick mastery and battlefield experience proved that exile had sharpened rather "
            "than diminished his Jedi skills.\n\n"
            "After the Star Forge's destruction, Jolee vanished from major chronicles, but his "
            "recorded holocrons influenced later masters who questioned the Council's absolutism."
        ),
        "significance": (
            "Jolee represents Jedi who serve the light without institutional loyalty—a precursor to "
            "figures like Ahsoka Tano and Luke Skywalker's later Order.\n\n"
            "His Kashyyyk exile connects the Wookiee homeworld to Old Republic Jedi history beyond "
            "the Clone Wars massacres.\n\n"
            "KOTOR II's Kreia often echoes debates Jolee began: whether the Jedi Code protects the "
            "galaxy or merely comforts the Council."
        ),
        "notableEvents": [
            "Left the Jedi Order after personal tragedy on Kashyyyk",
            "Lived as a hermit in the Kashyyyk Shadowlands for decades",
            "Joined Revan's crew against Darth Malak's Sith Empire",
            "Advised the Republic assault on the Star Forge",
            "Recorded unorthodox teachings on attachment and the Force",
        ],
        "affiliations": [
            "Jedi Order (former)",
            "Galactic Republic",
            "Ebon Hawk crew",
            "Kashyyyk Shadowlands exiles",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Served as a Jedi before leaving the Order"},
            {"era": "Old Republic", "event": "Exiled himself to Kashyyyk's Shadowlands"},
            {"era": "Old Republic", "event": "Guided Revan through Kashyyyk during the Jedi Civil War"},
            {"era": "Old Republic", "event": "Fought in the Battle of Rakata Prime"},
        ],
    },
    "meetra-surik": {
        "overview": (
            "Meetra Surik—the Jedi Exile—was a general of the Mandalorian Wars who cut herself off "
            "from the Force after activating the Mass Shadow Generator on Malachor V. Her return to "
            "galactic events exposed the Sith Triumvirate and ended Darth Traya's plot to wound the "
            "Force itself."
        ),
        "history": (
            "Meetra followed Revan against the Jedi Council's orders, leading Republic troops until "
            "Malachor V's devastation broke her connection to the Force. The Council exiled her, "
            "stripping her title while the galaxy forgot the general who ended the Mandalorian threat.\n\n"
            "When the Sith Lords Nihilus, Sion, and Traya hunted the remaining Jedi, Meetra gathered "
            "scattered survivors aboard the Ebon Hawk. On Dantooine, Telos, Dxun, and Malachor V she "
            "relearned what it meant to wield the Force through choice rather than instinct.\n\n"
            "The final confrontation on Malachor V destroyed the Triumvirate and sealed the wound "
            "Revan's wars had opened—yet Meetra departed for the Unknown Regions to aid Revan against "
            "the True Sith, completing the crusade she began years earlier."
        ),
        "significance": (
            "Meetra embodies consequences the Jedi Council refused to acknowledge after the "
            "Mandalorian Wars. Her exile arc questions whether disconnection from the Force can be "
            "redemption or another form of denial.\n\n"
            "The Triumvirate crisis proves Sith can metastasize from Jedi hubris even when "
            "open empires fall—an lesson Palpatine would exploit millennia later.\n\n"
            "KOTOR II uses Meetra to explore whether the galaxy needs Jedi institutions or merely "
            "individuals willing to act when the Council will not."
        ),
        "notableEvents": [
            "Led Republic forces during the Mandalorian Wars under Revan",
            "Ordered the Mass Shadow Generator at Malachor V",
            "Was exiled by the Jedi Council and severed from the Force",
            "Reassembled a crew to oppose the Sith Triumvirate",
            "Defeated Darth Traya, Sion, and Nihilus on Malachor V",
            "Departed to find Revan in the Unknown Regions",
        ],
        "affiliations": [
            "Jedi Order (exiled)",
            "Galactic Republic",
            "Ebon Hawk crew",
            "Mandalorian Wars veterans",
            "Telos Restoration Project allies",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Fought in the Mandalorian Wars as a Jedi General"},
            {"era": "Old Republic", "event": "Survived Malachor V and was exiled by the Council"},
            {"era": "Old Republic", "event": "Returned to oppose the Sith Triumvirate"},
            {"era": "Old Republic", "event": "Destroyed the Triumvirate at Malachor V"},
            {"era": "Old Republic", "event": "Pursued Revan into the Unknown Regions"},
        ],
    },
    "satele-shan": {
        "overview": (
            "Satele Shan was a Jedi Battle Meditation master and eventual Grand Master who led the "
            "Galactic Republic against the resurgent Sith Empire during the Great Galactic War. "
            "Descended from Bastila Shan and Revan's legacy, she united Jedi and military leaders "
            "when Coruscant itself fell to Sith invasion."
        ),
        "history": (
            "Born into the Shan lineage centuries after the Jedi Civil War, Satele trained on Tython "
            "and Coruscant as the Old Republic rebuilt from Darth Bane's long shadow. Her Battle "
            "Meditation turned desperate fleet actions into Republic victories during the Great "
            "Galactic War against Darth Malgus and the reconstituted Sith Empire.\n\n"
            "When Sith forces sacked Coruscant and destroyed the Jedi Temple, Satele helped negotiate "
            "the uneasy Cold War truce while preparing the Republic for renewed conflict. She "
            "mentored generations of Jedi—including her descendant Theron Shan—and held the Order "
            "together when public faith in both Jedi and Senate faltered.\n\n"
            "As Grand Master, Satele advocated cooperation with the Republic military rather than "
            "the Jedi generals' role Revan and Meetra once embodied, seeking to prevent another "
            "Mandalorian Wars catastrophe."
        ),
        "significance": (
            "Satele links KOTOR-era heroes to The Old Republic MMO era, proving the Shan legacy "
            "shaped galactic history across centuries.\n\n"
            "Her leadership during the Sacking of Coruscant defines TOR-era Jedi as public defenders "
            "rather than hidden monks.\n\n"
            "Satele's Battle Meditation continues Bastila's tradition, showing how family lineages "
            "carry Force talents through eras of war and reform."
        ),
        "notableEvents": [
            "Led Republic forces with Battle Meditation during the Great Galactic War",
            "Fought Darth Malgus and Sith invasion fleets across the Core",
            "Survived the Sacking of Coruscant and the Jedi Temple's destruction",
            "Helped broker the Cold War truce between Republic and Sith Empire",
            "Ascended to Jedi Grand Master and rebuilt the Order on Tython",
        ],
        "affiliations": [
            "Jedi Order",
            "Jedi High Council",
            "Galactic Republic",
            "Shan family lineage",
            "Republic Special Forces allies",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Rose as a Battle Meditation prodigy on Tython"},
            {"era": "Old Republic", "event": "Led Jedi and Republic fleets in the Great Galactic War"},
            {"era": "Old Republic", "event": "Defended the Republic after the Sacking of Coruscant"},
            {"era": "Old Republic", "event": "Became Grand Master during the Cold War era"},
        ],
    },
    "revan": {
        "overview": (
            "Revan was a Jedi Knight whose charisma and tactical genius ended the Mandalorian Wars—"
            "and whose fall created a new Sith Empire. Redeemed after the Jedi Council wiped his "
            "memory, Revan destroyed the Star Forge, defeated Darth Malak, and vanished pursuing "
            "threats in the Unknown Regions, leaving both Orders debating his true legacy."
        ),
        "history": (
            "When the Mandalorian Neo-Crusaders threatened the Republic, Revan defied the Jedi Council "
            "and led Revanchist knights to victory on Dxun, Malachor V, and countless Rim battlefields. "
            "Exposure to Sith artifacts in the Unknown Regions corrupted the crusaders; Revan and "
            "Malak returned as Sith Lords wielding the Star Forge.\n\n"
            "Malak's betrayal left Revan captured. The Council reprogrammed him as a loyal agent who "
            "rediscovered his past aboard the Ebon Hawk with Bastila Shan, Carth Onasi, and companions "
            "across Taris and Dantooine. Choosing the light, Revan struck down Malak at Rakata Prime "
            "and dismantled the Sith fleet.\n\n"
            "Revan then disappeared searching for the True Sith, was imprisoned by the Sith Emperor "
            "Vitiate on Yavin 4, and became a myth cited by both Jedi reformers and Sith cultists for "
            "millennia."
        ),
        "significance": (
            "Revan's redemption arc defines the Old Republic era's moral complexity—hero and tyrant "
            "in one lifetime.\n\n"
            "The Revanchist movement foreshadows Anakin Skywalker's preemptive wars and the Jedi "
            "Council's paralysis when the galaxy demands action.\n\n"
            "Revan's mask, lightsaber forms, and Ebon Hawk crew remain touchstones linking KOTOR games "
            "to broader galactic chronology."
        ),
        "notableEvents": [
            "Defied the Council to fight the Mandalorian Wars",
            "Fell to the dark side and ruled as Darth Revan",
            "Was mind-wiped and rebuilt as a Jedi agent",
            "Redeemed and destroyed the Star Forge at Rakata Prime",
            "Vanished pursuing the True Sith in the Unknown Regions",
        ],
        "affiliations": [
            "Jedi Order",
            "Revanchist movement",
            "Galactic Republic",
            "Ebon Hawk crew",
            "Dantooine Jedi Enclave (after redemption)",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Led the Revanchist crusade against the Mandalorians"},
            {"era": "Old Republic", "event": "Ruled as Darth Revan before Malak's betrayal"},
            {"era": "Old Republic", "event": "Was redeemed and defeated Malak at Rakata Prime"},
            {"era": "Old Republic", "event": "Disappeared into the Unknown Regions"},
        ],
    },
    "darth-malak": {
        "overview": (
            "Darth Malak was Revan's Sith apprentice who usurped the Star Forge empire and waged the "
            "Jedi Civil War with brutal efficiency. His disfigured jaw, Force Lightning, and orbital "
            "bombardment of Taris made him one of the Old Republic's most feared Dark Lords."
        ),
        "history": (
            "Once Revan's closest friend and fellow Revanchist, Malak embraced the dark side during "
            "the Mandalorian Wars and helped build a Sith fleet around the Star Forge. When he turned "
            "on Revan above Malachor and Rakata Prime, Malak seized the empire and hunted the "
            "mind-wiped Jedi across Taris, Dantooine, and the Rim.\n\n"
            "Malak's cruelty peaked with Taris's destruction and Bastila Shan's torture, yet his "
            "reliance on the Star Forge's infinite droid armies masked strategic rigidity. Revan's "
            "return culminated in a final duel aboard the factory station where Malak fell, ending "
            "the Jedi Civil War."
        ),
        "significance": (
            "Malak illustrates how apprentice ambition destroys Sith partnerships outside Bane's "
            "Rule of Two—yet produces the same betrayal dynamic.\n\n"
            "Taris's bombardment remains a benchmark for Sith atrocities before the Death Star era.\n\n"
            "Malak's reign bridges Mandalorian Wars veterans to the quieter Ruusan Reformations."
        ),
        "notableEvents": [
            "Turned on Darth Revan and seized the Sith Empire",
            "Ordered the orbital bombardment of Taris",
            "Captured Bastila Shan and corrupted her toward the dark side",
            "Commanded the Star Forge against the Republic at Rakata Prime",
            "Was defeated in a final duel with the redeemed Revan",
        ],
        "affiliations": [
            "Sith Empire (Old Republic era)",
            "Star Forge command",
            "Revanchist veterans (former)",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Fell to the dark side during the Mandalorian Wars"},
            {"era": "Old Republic", "event": "Betrayed Revan and claimed the Sith throne"},
            {"era": "Old Republic", "event": "Destroyed Taris and hunted the Republic fleet"},
            {"era": "Old Republic", "event": "Died aboard the Star Forge against Revan"},
        ],
    },
    "darth-traya": {
        "overview": (
            "Darth Traya—Kreia, the former Jedi Master—was the hidden architect of the Sith "
            "Triumvirate who sought to destroy the Force itself after the Jedi and Sith both failed "
            "her. Her manipulation of Meetra Surik exposed the hypocrisy of both Orders on Telos, "
            "Malachor V, and Dantooine."
        ),
        "history": (
            "Cast out by the Jedi and mutilated by the Sith, Kreia rejected binary dogma and trained "
            "Meetra Surik to see the galaxy without the Force's whisper. She engineered Darth Nihilus "
            "and Darth Sion's rise while posing as an ally aboard the Ebon Hawk.\n\n"
            "On Malachor V, Traya revealed her plan to wound the Force through Surik's unique "
            "connection—the echo of the Mass Shadow Generator. Defeated by her former pupil, Traya's "
            "death closed one path to ending the Jedi–Sith cycle, yet her questions linger in every "
            "debate about the Council's role in galactic war."
        ),
        "significance": (
            "Traya voices KOTOR II's central thesis: institutions that claim moral monopoly can "
            "cause as much harm as Sith empires.\n\n"
            "Her Triumvirate proves Sith can evolve beyond armies into metaphysical threats.\n\n"
            "Jedi masters still cite Kreia's holocron fragments when discussing attachment and exile."
        ),
        "notableEvents": [
            "Was exiled by the Jedi and betrayed by the Sith",
            "Formed the Sith Triumvirate with Nihilus and Sion",
            "Manipulated Meetra Surik across the Outer Rim",
            "Revealed her plan to destroy the Force on Malachor V",
            "Was defeated by the Jedi Exile",
        ],
        "affiliations": [
            "Sith Triumvirate",
            "Jedi Order (former)",
            "Malachor V survivors",
        ],
        "timeline": [
            {"era": "Old Republic", "event": "Fell from the Jedi Order after the Mandalorian Wars"},
            {"era": "Old Republic", "event": "Created the Sith Triumvirate"},
            {"era": "Old Republic", "event": "Was defeated at Malachor V by Meetra Surik"},
        ],
    },
}
