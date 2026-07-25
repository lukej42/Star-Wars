namespace StarWars.Data;

public record ForceTopicContent(
    string Overview,
    string History,
    string Significance,
    IReadOnlyList<string> NotableEvents,
    IReadOnlyList<string> References,
    string? Quote = null);

public static class TheForceContentData
{
    private static readonly IReadOnlyDictionary<string, ForceTopicContent> ContentBySlug =
        new Dictionary<string, ForceTopicContent>(StringComparer.OrdinalIgnoreCase)
        {
            ["conflict-between-light-and-dark-side"] = ConflictBetweenLightAndDark,
            ["lightsaber-forms"] = LightsaberForms,
            ["kyber-crystals"] = KyberCrystals,
            ["force-creatures"] = ForceCreatures,
            ["jedi-code"] = JediCode,
            ["sith-code"] = SithCode,
            ["force-philosophy"] = ForcePhilosophy,
            ["ancient-force-orders"] = AncientForceOrders
        };

    public static ForceTopicContent? GetBySlug(string slug) =>
        ContentBySlug.TryGetValue(slug, out var content) ? content : null;

    private static ForceTopicContent ConflictBetweenLightAndDark => new(
        Overview: "The eternal struggle between the light and dark sides of the Force is the central drama of galactic history—a cosmic balance tested by every generation of Jedi, Sith, and those who stand between them. From the Hundred-Year Darkness to Exegol, this conflict shapes empires, destroys worlds, and defines what it means to wield the Force responsibly.",
        History: "The schism began in the Hundred-Year Darkness, when rogue Jedi embraced passion and power, birthing the Sith and the Old Sith Empire on Korriban and Ziost. For millennia the Republic and Jedi Order fought successive Sith empires—the Great Sith War led by Exar Kun and Ulic Qel-Droma, the Mandalorian Wars and Jedi Civil War witnessed by Revan and Malak in KOTOR, and the Great Galactic War that culminated in the Sacking of Coruscant.\n\nThe Skywalker saga films trace the conflict's modern arc: Darth Sidious manipulates the Clone Wars in The Phantom Menace, Attack of the Clones, and Revenge of the Sith; the Galactic Empire crushes hope until A New Hope, The Empire Strikes Back, and Return of the Jedi; and the First Order resurrects the dark side in The Force Awakens, The Last Jedi, and The Rise of Skywalker. Series such as The Clone Wars, Rebels, and The Mandalorian show the war's daily toll on soldiers and civilians caught between Jedi ideals and Sith ambition.",
        Significance: "The light-dark conflict is not merely a battle of laser swords—it is a philosophical war over attachment, fear, and the nature of power. Yoda teaches Luke that fear leads to anger on Dagobah; Palpatine proves the same lesson by corrupting Anakin Skywalker. Revan's redemption in KOTOR demonstrates that the line between sides can blur, while Darth Bane's Rule of Two ensures the dark side survives every apparent defeat.\n\nBalance remains the elusive goal. The Jedi seek harmony with the Living Force; the Sith crave domination through the dark side. Rey and Ben Solo's dyad in the Sequel trilogy suggests a new synthesis—neither pure light nor unrestrained dark, but chosen compassion over inherited destiny. Until that balance holds, the galaxy will always know war.",
        NotableEvents:
        [
            "The Hundred-Year Darkness and the founding of the Old Sith Empire",
            "Exar Kun's Great Sith War and the devastation of Ossus",
            "Revan and Malak's fall and redemption during the Jedi Civil War (KOTOR)",
            "Darth Bane establishes the Rule of Two after the New Sith Wars",
            "Palpatine's execution of Order 66 and the rise of the Galactic Empire",
            "Luke Skywalker's refusal to kill Vader at Endor",
            "Rey's confrontation with Palpatine on Exegol"
        ],
        References:
        [
            "Films: The Phantom Menace · Attack of the Clones · Revenge of the Sith · A New Hope · The Empire Strikes Back · Return of the Jedi · The Force Awakens · The Last Jedi · The Rise of Skywalker",
            "Series: The Clone Wars · Rebels · The Mandalorian · Tales of the Jedi",
            "KOTOR · KOTOR II: The Sith Lords",
            "Old Sith Empire · Great Galactic War · The Old Republic"
        ]);

    private static ForceTopicContent LightsaberForms => new(
        Overview: "The seven classical lightsaber forms—Shii-Cho through Juyo/Vaapad—are the martial language of Force users, codifying thousands of years of dueling tradition. Each form answers a specific combat problem, from disarming mobs to dueling Sith Lords, and mastery of multiple forms marks the galaxy's greatest warriors.",
        History: "Form I, Shii-Cho, emerged when lightsabers replaced traditional swords, teaching Jedi to fight multiple bladed opponents. Form II, Makashi, rose during an age of Sith dueling when elegance mattered as much as power—Count Dooku exemplified its precision across the Prequel trilogy. Form III, Soresu, answered the spread of blasters; Obi-Wan Kenobi's defense on Mustafar and against General Grievous in Revenge of the Sith is its definitive demonstration.\n\nForm IV, Ataru, channeled acrobatic Force leaps—Yoda's duel with Dooku in Attack of the Clones and his fight against Palpatine in Revenge of the Sith showcase its mobility. Form V, Shien and Djem So, turned defense into overwhelming counter-attack; Anakin Skywalker and later Darth Vader dominated with Djem So's power. Form VI, Niman, balanced blade work with Force powers for diplomats and generals. Form VII, Juyo and its Jedi variant Vaapad, pushed aggression to its limit—Mace Windu's Vaapad channeled the dark side without surrendering to it, as seen when he confronted Palpatine.\n\nIn KOTOR, Revan and the Jedi Exile studied multiple forms against Mandalorian and Sith opponents. The Old Sith Empire's warriors developed parallel traditions on Korriban, where ancient Sith Lords inscribed combat rites into tombs still studied in The Old Republic era.",
        Significance: "Lightsaber forms encode philosophy as much as technique. Soresu teaches patience; Ataru demands physical communion with the Force; Vaapad confronts the darkness within. A Jedi who knows only one form is vulnerable—Grievous exploited Form I's limitations, while blaster-heavy battlefields rendered Makashi impractical.\n\nThe forms evolve with warfare. Clone troopers and droid armies changed how Jedi fought on Geonosis; Imperial-era rebels rarely dueled, shifting emphasis to Form V counter-attacks and Force-enhanced marksmanship. Luke Skywalker's raw Form V instincts in Return of the Jedi defeated Vader through emotional clarity rather than formal training, proving that form serves the wielder's spirit—not the reverse.",
        NotableEvents:
        [
            "Codification of the seven forms during the Old Republic era",
            "Count Dooku's Makashi mastery in Attack of the Clones and Revenge of the Sith",
            "Obi-Wan Kenobi's Soresu duel on Mustafar",
            "Mace Windu's Vaapad confrontation with Chancellor Palpatine",
            "Revan's form-switching combat in KOTOR against Malak",
            "Ahsoka Tano's Jar'Kai dual-blade adaptation in The Clone Wars"
        ],
        References:
        [
            "Films: All nine Skywalker saga entries",
            "Series: The Clone Wars · Rebels · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire · Jedi Order archives"
        ]);

    private static ForceTopicContent KyberCrystals => new(
        Overview: "Kyber crystals are rare, Force-attuned gems that focus energy into a lightsaber's blade. They choose their wielder as much as the wielder chooses them, glowing blue or green for Jedi, red when bled by the Sith, and occasionally purple, yellow, or white for those who walk unique paths.",
        History: "Kyber deposits on Ilum, Jedha, Lothal, and distant worlds supplied the Jedi Order for millennia. Younglings harvested crystals in the Gathering ritual—a tradition shown in The Clone Wars when Ahsoka Tano guides padawans through Ilum's ice caves. The Empire strip-mined Ilum to power the Death Star's superlaser, transforming the sacred world into a weapon forge visible in Jedi: Fallen Order and Rebels.\n\nAnakin Skywalker's blue crystal powered his weapon through the Clone Wars until Obi-Wan kept it on Tatooine; Luke rebuilt the saber with a green crystal in Return of the Jedi after losing his father's blade on Cloud City. Kylo Ren cracked his crystal, producing an unstable crossguard blade in The Force Awakens and The Last Jedi. Rey later forged a yellow-bladed saber with fragments from Luke and Leia's crystals in The Rise of Skywalker.\n\nIn KOTOR, Bastila Shan and other Jedi attuned crystals on the Star Forge's battlefields, while the Old Sith Empire's acolytes performed the bleeding ritual on Korriban—twisting a crystal's connection to the Force through pain and domination, a practice Darth Vader taught inquisitors during the Imperial era.",
        Significance: "Kyber crystals embody the bond between warrior and Force. A bled crystal screams with the dark side; a naturally attuned crystal harmonizes with its owner's temperament. The Death Star's kyber core perverted this sacred relationship, turning spiritual focus into planet-killing fire—a crime the Rebel Alliance answered at Yavin and Endor.\n\nCrystal scarcity drives conflict. The Guardians of the Whills protected Jedha's temple until the Empire's mining operations, depicted in Rogue One, desecrated the Holy City. Resistance-era Jedi like Rey and Cal Kestis must scavenge Imperial caches and ancient ruins, linking modern heroes to traditions older than the Republic Senate.",
        NotableEvents:
        [
            "The Gathering on Ilum in The Clone Wars",
            "Anakin Skywalker's crystal lost on Mustafar; Luke's green blade in Return of the Jedi",
            "Imperial strip-mining of Ilum for the Death Star",
            "Jedha's destruction in Rogue One",
            "Kylo Ren's cracked crystal and Rey's yellow saber in the Sequel trilogy",
            "Sith bleeding rituals on Korriban in KOTOR and The Old Republic"
        ],
        References:
        [
            "Films: The Phantom Menace · Attack of the Clones · Revenge of the Sith · A New Hope · The Empire Strikes Back · Return of the Jedi · The Force Awakens · The Last Jedi · The Rise of Skywalker · Rogue One",
            "Series: The Clone Wars · Rebels · The Mandalorian",
            "KOTOR · Jedi: Fallen Order · The Old Republic",
            "Old Sith Empire · Jedha temple archives"
        ]);

    private static ForceTopicContent ForceCreatures => new(
        Overview: "Force creatures are beings whose biology intertwines with the Living Force—wielding natural abilities that mirror Jedi and Sith powers, or serving as conduits for vergence sites where the Force flows strongest. They remind the galaxy that the Force extends beyond sentient doctrine.",
        History: "The convor owls of Lothal, the loth-wolves of Lothal, and the purrgil space whales navigated hyperspace long before starships—Ezra Bridger communed with them throughout Rebels, learning that the Force speaks through all life. Yoda's exile on Dagobah placed him among serpents, spiders, and mist that amplified Force visions in The Empire Strikes Back.\n\nThe Zillo Beast of Malastare, unleashed in The Clone Wars, carried armor impervious to Republic weaponry and an ancient connection to the Force predating the Jedi. The Bendu of Atollon embodied balance between light and dark, refusing allegiance to either side. Mortis's Force wielders—the Father, Daughter, and Son—manifested cosmic aspects of the Force in an arc spanning The Clone Wars, foreshadowing Anakin's destiny.\n\nKOTOR introduced terentateks and other Force-fed predators on Korriban and Kashyyyk, beasts the Jedi hunted during the Old Sith Empire's wars. The Old Republic era added vynock flocks and other creatures drawn to dark-side nexuses, while KOTOR II's Malachor V harbored fauna twisted by the Mass Shadow Generator's devastation.",
        Significance: "Force creatures challenge the arrogance of civilizations that treat the Force as property of Orders and Empires. When Ezra rode a purrgil pod into the Unknown Regions, he proved that hyperspace itself can be a Force expression. The Bendu's warning—that the hubris of both Jedi and Sith would destroy Atollon—shows that ignoring natural Force balance invites catastrophe.\n\nStudying these beings enriches Jedi philosophy. Luke's training included listening to the swamp's life on Dagobah; Rey's island apprenticeship on Ahch-To in The Last Jedi connected her to seabirds and ocean rhythms. The galaxy's sentients are one thread in a Living Force tapestry woven through every ecosystem from Felucia's jungles to Ilum's ice.",
        NotableEvents:
        [
            "Ezra Bridger's bond with loth-wolves and purrgil in Rebels",
            "The Mortis trilogy in The Clone Wars",
            "The Bendu's intervention at the Battle of Atollon",
            "Zillo Beast rampage on Coruscant in The Clone Wars",
            "Terentatek hunts on Korriban in KOTOR",
            "Vergence creatures on Ahch-To during Rey's training in The Last Jedi"
        ],
        References:
        [
            "Films: The Empire Strikes Back · The Last Jedi · The Rise of Skywalker",
            "Series: The Clone Wars · Rebels · The Mandalorian · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire · Lothal Force vergence studies"
        ]);

    private static ForceTopicContent JediCode => new(
        Overview: "The Jedi Code is the foundational mantra of the Jedi Order—a distillation of millennia of wisdom urging practitioners to transcend emotion, ignorance, passion, chaos, and fear of death in favor of peace, knowledge, serenity, harmony, and unity with the Force.",
        History: "The Code evolved from Je'daii teachings on Tython and Ahch-To, refined as the Jedi Order centralized on Coruscant. Padawans recited it daily in temples from the Prequel era through the Clone Wars, where Obi-Wan Kenobi, Anakin Skywalker, and Ahsoka Tano grappled with its strictures against attachment.\n\nQui-Gon Jinn's maverick interpretation in The Phantom Menace emphasized living in the moment—a tension with the Council's orthodoxy. Anakin's secret marriage to Padmé Amidala in Attack of the Clones and Revenge of the Sith directly violated the Code's rejection of attachment, proving Palpatine's claim that Jedi dogma could be as destructive as Sith ambition.\n\nAfter Order 66, Luke Skywalker rebuilt training in A New Hope, The Empire Strikes Back, and Return of the Jedi with a more compassionate reading. In The Last Jedi he rejected the Order's hubris; Rey carried a revised understanding into The Rise of Skywalker. KOTOR's Jedi Council on Dantooine enforced similar precepts against Revan's crew, while the Old Republic's Jedi archives preserved earlier variants predating the Ruusan Reformation.",
        Significance: "The Code aims to prevent the emotional spiral Yoda describes on Dagobah—fear to anger to hate to suffering. Yet its prohibition on attachment created blind spots: the Order failed to see Palpatine's plot, to support Anakin's grief, or to recognize that love can strengthen rather than weaken the light side, as Luke proved when he refused to kill his father.\n\nModern Jedi like Ahsoka Tano and Rey interpret the Code as aspiration rather than suppression—seeking serenity without denying compassion. The text remains a mirror: those who recite it without self-examination repeat the Order's fall; those who live its ideals without rigidity may finally achieve the balance the galaxy needs.",
        NotableEvents:
        [
            "Je'daii origins of the Code on Tython and Ahch-To",
            "Qui-Gon Jinn's unorthodox teachings in The Phantom Menace",
            "Anakin's conflict between the Code and attachment in the Prequel trilogy",
            "Luke Skywalker's training reinterpretation on Dagobah",
            "Luke's rejection of Jedi hubris in The Last Jedi",
            "Rey's adoption of a compassionate reading in The Rise of Skywalker"
        ],
        References:
        [
            "Films: All nine Skywalker saga entries",
            "Series: The Clone Wars · Rebels · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire · Jedi Order historical archives"
        ],
        Quote: "There is no emotion, there is peace.\nThere is no ignorance, there is knowledge.\nThere is no passion, there is serenity.\nThere is no chaos, there is harmony.\nThere is no death, there is the Force.");

    private static ForceTopicContent SithCode => new(
        Overview: "The Sith Code is the dark-side antithesis of Jedi doctrine—a declaration that peace is illusion, passion is strength, and only through power and victory can one break the chains of fate. It drives every Sith Lord from the Old Sith Empire to Darth Sidious and beyond.",
        History: "Forged during the Hundred-Year Darkness and refined on Korriban and Ziost, the Code accompanied the Sith Empire's conquests across the Great Sith War and Great Galactic War. Exar Kun and Ulic Qel-Droma embodied its promise of victory through passion; Darth Revan and Darth Malak reinterpreted it during the Jedi Civil War in KOTOR, using the Star Forge to convert passion into galactic dominion.\n\nDarth Bane's Rule of Two in the New Sith Wars ensured only two Sith lived at a time, each reciting the Code while plotting to surpass their master. Darth Sidious whispered its logic to Anakin Skywalker throughout the Prequel trilogy, culminating in Revenge of the Sith's tragedy. Vader lived the Code's chains until Luke's compassion in Return of the Jedi broke them.\n\nKylo Ren and Snoke revived Sith rhetoric in The Force Awakens and The Last Jedi, promising power through rage until The Rise of Skywalker revealed Palpatine's ultimate victory obsession. The Old Republic's Sith Inquisitors and KOTOR's Sith Academy on Korriban drilled the Code into acolytes who bled kyber crystals and hunted Jedi across the galaxy.",
        Significance: "The Sith Code honestly names desire where Jedi doctrine often suppresses it—making it seductive to those who feel betrayed or powerless. Anakin turned because the Code's logic matched his fear of loss; Revan fell chasing a pragmatic end to the Mandalorian Wars. Yet every Sith who achieves victory discovers new chains: apprentices plot, masters cling to power, and the dark side consumes its servants.\n\nUnderstanding the Code is essential to defeating the Sith. Mace Windu's Vaapad channeled its energy without belief; Luke rejected its binary in favor of redemption. The Code's final line—\"The Force shall free me\"—remains the darkest irony, for no Sith Lord has ever found freedom in the dark side.",
        NotableEvents:
        [
            "Composition of the Code during the Hundred-Year Darkness",
            "Exar Kun and the Brotherhood of the Sith in the Great Sith War",
            "Revan and Malak's Sith Empire in KOTOR",
            "Darth Bane's Rule of Two after the New Sith Wars",
            "Palpatine's corruption of Anakin Skywalker in Revenge of the Sith",
            "Palpatine's return and final defeat at Exegol in The Rise of Skywalker"
        ],
        References:
        [
            "Films: The Phantom Menace · Attack of the Clones · Revenge of the Sith · Return of the Jedi · The Force Awakens · The Last Jedi · The Rise of Skywalker",
            "Series: The Clone Wars · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire · Korriban Sith Academy"
        ],
        Quote: "Peace is a lie, there is only passion.\nThrough passion, I gain strength.\nThrough strength, I gain power.\nThrough power, I gain victory.\nThrough victory, my chains are broken.\nThe Force shall free me.");

    private static ForceTopicContent ForcePhilosophy => new(
        Overview: "Force philosophy encompasses every tradition's attempt to explain the Living Force, the Unifying Force, balance, destiny, and free will. Jedi, Sith, Bendu, Nightsisters, and independent scholars have debated these questions since the dawn of sentient civilization.",
        History: "The Je'daii on Tython taught balance between Ashla (light) and Bogan (dark)—a synthesis lost when the Jedi Order and Old Sith Empire diverged. Qui-Gon Jinn's studies of the Living Force in The Phantom Menace clashed with the Jedi Council's focus on the Unifying Force and prophecy. Yoda's Dagobah lessons in The Empire Strikes Back emphasized size matters not, teaching Luke that consciousness, not muscle, binds the galaxy.\n\nSith philosophy centers on power through suffering—Palpatine's lectures to Anakin in Revenge of the Sith mirror Darth Traya's cynicism in KOTOR II, who argued that both Jedi and Sith were pawns of the Force itself. The Bendu of Rebels rejected binary labels, while the Nightsisters of Dathomir channeled the Force through magick distinct from Jedi or Sith orthodoxy, as seen in The Clone Wars.\n\nRevan's journey in KOTOR questioned whether the light side's detachment could save the galaxy from the Mandalorian Wars. The Old Republic's Jedi and Sith empires produced libraries of competing treatises on Coruscant and Korriban, many destroyed in the Great Sith War and New Sith Wars but echoed in every film from A New Hope's \"hokey religions\" skepticism to The Last Jedi's insistence that the Force belongs to everyone.",
        Significance: "Force philosophy determines policy. The Jedi Council's fatalism about Anakin's prophecy enabled Palpatine's rise; Luke's belief in redemption ended the Empire. Rey's discovery that she is nobody—and therefore free to choose heroism—in The Last Jedi reframes destiny as decision rather than bloodline.\n\nThe Sequel trilogy's dyad between Rey and Ben Solo suggests a third path: connection without domination, power shared rather than hoarded. As long as sentients debate whether the Force has a will, a dark side, or a balance to maintain, philosophy will remain as decisive as any lightsaber form in shaping galactic fate.",
        NotableEvents:
        [
            "Je'daii balance teachings on Tython",
            "Qui-Gon Jinn's Living Force heresy in The Phantom Menace",
            "Yoda's training philosophy on Dagobah in The Empire Strikes Back",
            "Darth Traya's Force nihilism in KOTOR II",
            "The Bendu's neutrality doctrine in Rebels",
            "Luke's lesson that the Force belongs to all in The Last Jedi"
        ],
        References:
        [
            "Films: All nine Skywalker saga entries",
            "Series: The Clone Wars · Rebels · The Mandalorian · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire · Dathomir Nightsister traditions"
        ]);

    private static ForceTopicContent AncientForceOrders => new(
        Overview: "Before the modern Jedi and Sith, ancient Force orders shaped galactic spirituality—the Je'daii of Tython, the Dai Bendu, the Guardians of the Whills, the Ordu Aspectu, and countless regional traditions that predated the Republic and informed every later doctrine.",
        History: "The Je'daii Order on Tython balanced Ashla and Bogan, sending pilgrims to worlds that became Jedi temples. Their successors, the Jedi, migrated to Ossus and eventually Coruscant, while exiled dark Jedi founded the Old Sith Empire on Korriban after the Hundred-Year Darkness. The Dai Bendu monks' texts influenced early Jedi scripture; the Guardians of the Whills protected Jedha's kyber temple until Rogue One's devastation.\n\nThe Ordu Aspectu sought immortality through the Force—a heresy that ended in catastrophe, echoes of which appear in Expanded lore and inspire Imperial research into eternal life, a goal Palpatine pursued through clone bodies in The Rise of Skywalker. The Zeffo of Jedi: Fallen Order left tomb inscriptions describing the Life Wind, a Force concept predating Jedi terminology.\n\nKOTOR revealed the Jedi Enclave on Dantooine and the Sith Academy on Korriban as heirs to these ancient divisions. The Old Republic era's Jedi Council and Dark Council both claimed lineage from Tython's schism. Series like Tales of the Jedi visualize the Order's early centuries, while The Clone Wars' Mortis arc presents mythic Force entities older than any institution.",
        Significance: "Ancient orders remind modern Force users that Jedi and Sith are not eternal absolutes—they are factions in a longer story. The Je'daii's balance philosophy may hold keys the Ruusan Reformation discarded. Jedha's Guardians prove that non-combatant orders can protect the Force's sacred materials without wielding lightsabers.\n\nArchaeology drives contemporary conflict: Imperial and First Order agents loot Zeffo and Sith tombs; Rey recovers texts from Ahch-To in The Last Jedi; Cal Kestis explores ruins in Jedi: Fallen Order. Recovering ancient wisdom without repeating ancient hubris is the challenge facing every new generation from Luke's academy to Rey's rebuilt Order.",
        NotableEvents:
        [
            "Je'daii establishment on Tython and the Force Wars",
            "Exile of dark Jedi and founding of the Old Sith Empire on Korriban",
            "Guardians of the Whills protecting Jedha's temple",
            "Ordu Aspectu heresy and collapse",
            "Jedi Enclave on Dantooine in KOTOR",
            "Recovery of Jedi texts on Ahch-To in The Last Jedi"
        ],
        References:
        [
            "Films: The Phantom Menace · Rogue One · The Last Jedi · The Rise of Skywalker",
            "Series: The Clone Wars · Rebels · Tales of the Jedi · The Mandalorian",
            "KOTOR · KOTOR II · Jedi: Fallen Order · The Old Republic",
            "Old Sith Empire · Tython Je'daii archives · Jedha temple records"
        ]);
}
