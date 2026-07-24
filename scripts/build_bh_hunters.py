#!/usr/bin/env python3
"""Hunter catalog data — imported by _gen_bounty_hunters.py"""
from __future__ import annotations

HUNTERS: list[tuple] = []


def _add(*args):
    HUNTERS.append(args)


def L(**kw):
    return kw


# Boba and Jango with full lore (defined inline)
_add(
    "Boba Fett", "Mandalorian Bounty Hunter", "Kamino (clone origin); raised Concord Dawn",
    "The most feared bounty hunter of the Imperial Era, Boba Fett inherited Jango's beskar and tracked Han Solo for Vader and Jabba before surviving the Sarlacc to become Daimyo of Mos Espa.",
    "#0284c7", "All 9 Films · Clone Wars · Mandalorian · Book of Boba Fett", "mando",
    L(
        origin_detail="Created as Jango Fett's unaltered clone on Kamino, young Boba watched his father decapitated by Mace Windu on Geonosis and spent his adolescence assembling a crew with Aurra Sing and Bossk to avenge the loss.",
        ancient_detail="Concord Dawn's True Mandalorian diaspora and Kaminoian cloning contracts linked Boba to martial lineages stretching back to KOTOR-era Neo-Crusader mercenary rolls and TOR-era Mandalorian enclaves on Dxun.",
        modern_detail="After escaping the Sarlacc pit, Boba reclaimed his father's beskar from Cobb Vanth, healed in a bacta tank with Fennec Shand, and seized Mos Espa's Daimyo throne from Bib Fortuna during the Pyke syndicate war.",
        conflict_detail="Boba hunted Jedi and clones as a teenager, dominated Vader's six-hunter roster on the Executor, delivered carbonite-frozen Han Solo to Jabba, fell into the Sarlacc during the sail barge battle, and later fought Pyke capos in Mos Espa's streets.",
        methods_detail="Boba favors Slave I interceptions, Z-6 jetpack ambushes, fibercord whips, wrist-mounted flamethrowers, and disintegration threats—lethal precision backed by Mandalorian armor that survived acid, blaster fire, and Sarlacc digestion.",
        reputation_detail="Darth Vader singled Boba out among six elite hunters on the Executor; Jabba's court treated him as untouchable; post-Sarlacc Tatooine whispers hold that crossing Fett means death or a lifetime of looking over your shoulder.",
        impact_detail="Boba's capture of Han Solo enabled Jabba's sail barge trap that nearly killed Luke Skywalker; his Daimyo period reshaped Hutt-Pyke power on Tatooine and proved Mandalorian hunters can become planetary rulers without a fleet.",
        events=["Watches Jango die on Geonosis during arena battle", "Accepts Vader's bounty on Han Solo aboard Executor", "Delivers frozen Han to Jabba's palace on Tatooine", "Falls into Sarlacc during sail barge fight", "Becomes Daimyo of Mos Espa after reclaiming beskar armor"],
        affiliations=["Bounty Hunters' Guild", "Jabba the Hutt's court", "Galactic Empire (contracted)", "Mandalorian warrior culture", "Crime syndicates of Tatooine", "Concord Dawn traditions via Jango"],
        timeline=[("Clone Wars", "Teenage Boba seeks revenge against Mace Windu"), ("Imperial Era", "Galaxy's most feared hunter"), ("Bespin", "Tracks Millennium Falcon for Vader"), ("Sarlacc", "Presumed dead after Return of the Jedi"), ("Book of Boba Fett", "Rules Mos Espa as Daimyo")],
    ),
)
_add(
    "Jango Fett", "Mandalorian Bounty Hunter & Clone Template", "Concord Dawn",
    "The last Mandalorian recruited as genetic template for the Grand Army of the Republic, Jango combined guild prestige with Kaminoian cloning before dying at Mace Windu's hand on Geonosis.",
    "#0284c7", "Attack of the Clones · Clone Wars · Mandalorian lore", "mando",
    L(
        origin_detail="Orphaned by civil war on Concord Dawn, Jango was taken in by Jaster Mereel's True Mandalorians, earned beskar armor through the Mandalorian Civil War, and became the galaxy's most expensive genetic donor.",
        ancient_detail="Concord Dawn's warrior exiles supplied Old Republic mercenary companies centuries before Jango; his beskar-and-blaster ethos mirrors KOTOR Mandalorian wars and TOR-era Great Hunt charters on Dromund Kaas.",
        modern_detail="Jango's DNA produced millions of clone troopers and one unaltered son, Boba—making him biological architect of the Clone Wars and the template controversy that haunted Imperial stormtrooper recruitment debates for decades.",
        conflict_detail="Jango assassinated for Count Dooku using Kamino saberdarts, fought Obi-Wan Kenobi on Kamino's rain-swept landing platforms, and led Separatist escape at Geonosis before Mace Windu killed him in the arena that ignited open galactic war.",
        methods_detail="Dual WESTAR-34 blasters, Z-6 jetpack mobility, Kamino saberdarts for silent kills, and brutal hand-to-hand training defined Jango's preference for lethal precision over prolonged sieges or orbital bombardment.",
        reputation_detail="Sifo-Dyas and Dooku chose Jango over every other hunter in the galaxy; Tyranus presented him to Separatist leadership as proof that one Mandalorian can change the course of history.",
        impact_detail="Without Jango there is no clone army, no Boba Fett, and no Kamino conspiracy—the entire Clone Wars timeline pivots on his decision to sell his face to the Kaminoians.",
        events=["Recruited as clone template on Bogden for Kamino project", "Attempts assassination of Senator Padmé Amidala", "Fights Obi-Wan Kenobi on Kamino landing platform", "Leads Separatist escape at Battle of Geonosis", "Killed by Mace Windu in Geonosis arena"],
        affiliations=["True Mandalorians (historical)", "Count Dooku / CIS", "Kamino cloners", "Bounty Hunters' Guild", "Concord Dawn exile networks"],
        timeline=[("Concord Dawn", "Orphaned; joins Jaster Mereel"), ("Mandalorian Civil War", "Earns beskar armor"), ("Kamino Contract", "Provides DNA for Grand Army"), ("Kamino Incident", "Obi-Wan discovers clones"), ("Geonosis", "Dies; Boba inherits legacy")],
    ),
)

from build_bh_hunters_rest import register_rest  # noqa: E402

register_rest(_add, L)

assert len(HUNTERS) >= 65, f"Only {len(HUNTERS)} hunters"
