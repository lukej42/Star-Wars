namespace StarWars.Data;

public record LightsaberFormContent(
    string Overview,
    string History,
    string Significance,
    IReadOnlyList<string> Practitioners,
    IReadOnlyList<string> References);

public static class LightsaberFormContentData
{
    private static readonly IReadOnlyDictionary<string, LightsaberFormContent> ContentBySlug =
        new Dictionary<string, LightsaberFormContent>(StringComparer.OrdinalIgnoreCase)
        {
            ["shii-cho"] = ShiiCho,
            ["makashi"] = Makashi,
            ["soresu"] = Soresu,
            ["ataru"] = Ataru,
            ["shien-djem-so"] = ShienDjemSo,
            ["niman"] = Niman,
            ["juyo-vaapad"] = JuyoVaapad
        };

    public static LightsaberFormContent? GetBySlug(string slug) =>
        ContentBySlug.TryGetValue(slug, out var content) ? content : null;

    private static LightsaberFormContent ShiiCho => new(
        Overview: "Shii-Cho, Form I, is the oldest and most basic lightsaber discipline—designed when Jedi first faced blaster-wielding opponents and needed to disarm rather than kill. Its wide, sweeping strikes and simple guards make it the foundation taught to every youngling before specialization.",
        History: "Form I evolved from traditional swordplay when lightsabers became the Jedi weapon of choice during the Great Hyperspace War era. Early Jedi on Ossus and Tython used Shii-Cho against pirates and Sith raiders who outnumbered them, prioritizing survival over elegance.\n\nThe form reached its battlefield peak during the Clone Wars, when Jedi led clone armies against droid swarms on Geonosis and across the Outer Rim, as depicted in Attack of the Clones, Revenge of the Sith, and The Clone Wars. Kit Fisto and other Masters relied on Shii-Cho's crowd-control strikes when surrounded.\n\nIn KOTOR, Revan and party members default to Form I fundamentals before advancing to specialized styles against Mandalorian clans and Sith troopers. The Old Sith Empire's warriors studied equivalent basic forms on Korriban before mastering aggressive variants.",
        Significance: "Shii-Cho embodies the Jedi ideal of minimum necessary force—disarming opponents rather than executing them. Its simplicity makes it the first and last form a Jedi learns; even Masters return to its principles under overwhelming odds.\n\nThe form's limitation against single skilled duelists led to Forms II through VII, yet Shii-Cho remains essential in galactic warfare. When blaster fire fills the air on Scarif or Hoth, the wide arcs of Form I keep defenders alive long enough to achieve their mission.",
        Practitioners:
        [
            "Kit Fisto",
            "Obi-Wan Kenobi (early training)",
            "Anakin Skywalker (Clone Wars campaigns)",
            "Revan (KOTOR foundational training)",
            "Clone Wars-era Jedi younglings"
        ],
        References:
        [
            "Films: Attack of the Clones · Revenge of the Sith",
            "Series: The Clone Wars · Tales of the Jedi",
            "KOTOR · The Old Republic",
            "Old Sith Empire basic combat rites"
        ]);

    private static LightsaberFormContent Makashi => new(
        Overview: "Makashi, Form II, is the dueling form—elegant, precise, and economical, built for lightsaber-against-lightsaber combat when the Sith returned to challenge the Republic. Its footwork and thrusting attacks exploit single-opponent weaknesses with minimal wasted motion.",
        History: "Form II arose during centuries of Sith resurgence when Jedi faced blade-wielding dark side adepts across the Old Republic. Count Dooku mastered Makashi after leaving the Jedi Order, refining it into a weapon of political terror in Attack of the Clones and Revenge of the Sith.\n\nDooku's duels with Obi-Wan and Anakin on Geonosis and aboard the Invisible Hand demonstrate Makashi's superiority against less specialized opponents—and its vulnerability to aggressive power forms. Asajj Ventress combined Makashi with Jar'Kai dual wielding in The Clone Wars, adapting the form for assassin work.\n\nKOTOR's Jedi Masters on Dantooine taught Makashi principles for confronting Dark Jedi, while the Old Sith Empire's Lords on Korriban developed mirror dueling styles preserved in tomb inscriptions.",
        Significance: "Makashi represents the apex of civilized combat—honor, precision, and psychological dominance. Its decline in the blaster-dominated Clone Wars made specialists like Dooku rare, yet the form never lost relevance against Sith Lords and dark side assassins.\n\nStudying Makashi teaches patience and reading an opponent's guard, skills that translate even to Force-powered negotiators. When diplomacy fails, Form II ends conflicts with surgical strikes rather than battlefield slaughter.",
        Practitioners:
        [
            "Count Dooku / Darth Tyranus",
            "Asajj Ventress",
            "Exar Kun (Great Sith War dueling)",
            "Jedi duelists of the Old Republic era",
            "KOTOR Dark Jedi instructors"
        ],
        References:
        [
            "Films: Attack of the Clones · Revenge of the Sith",
            "Series: The Clone Wars · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire dueling archives on Korriban"
        ]);

    private static LightsaberFormContent Soresu => new(
        Overview: "Soresu, Form III, is the ultimate defensive form—tight guard positions, minimal movement, and impenetrable deflection of blaster bolts and lightsaber strikes. It wins by outlasting the opponent, turning patience into inevitable counter-opportunity.",
        History: "Form III developed as blasters replaced swords across the galaxy, forcing Jedi to defend against sustained fire rather than single duels. Obi-Wan Kenobi became the form's greatest living master, surviving battles that killed lesser Jedi from the Prequel trilogy through the Imperial era.\n\nOn Geonosis, Utapau, and especially Mustafar in Revenge of the Sith, Obi-Wan's Soresu exhausted Anakin's aggressive Form V assault until a single opening decided the duel. General Grievous's defeat on Utapau showcased Soresu against a cybernetic opponent wielding multiple sabers.\n\nIn A New Hope, Obi-Wan's calm defense against Vader on the Death Star—though he chose martyrdom—reflects decades of Soresu discipline. KOTOR's Jedi guardians used Form III to protect allies during Mandalorian sieges, and Old Republic archives credit Soresu with surviving the Great Sith War's artillery bombardments.",
        Significance: "Soresu teaches that defense is not passivity—it is control. A Form III master dictates the duel's pace, forcing aggressors to spend energy against an immovable guard until frustration breeds mistakes.\n\nThe form's weakness in offensive finishing moves requires pairing with counter-forms or environmental awareness. Obi-Wan's victory on Mustafar came from Soresu patience combined with high-ground tactical advantage—a reminder that the greatest form mastery integrates terrain, psychology, and the Force.",
        Practitioners:
        [
            "Obi-Wan Kenobi",
            "Kan Jarrus (partial Soresu influence in Rebels)",
            "Jedi Temple Guard traditions",
            "KOTOR Jedi defenders on Dantooine",
            "Old Republic Soresu masters during the Great Sith War"
        ],
        References:
        [
            "Films: The Phantom Menace · Attack of the Clones · Revenge of the Sith · A New Hope",
            "Series: The Clone Wars · Rebels",
            "KOTOR · The Old Republic",
            "Old Sith Empire siege records"
        ]);

    private static LightsaberFormContent Ataru => new(
        Overview: "Ataru, Form IV, is the acrobatic form—leaping, spinning, and using the Force to enhance speed and agility for overwhelming offensive momentum. It favors open spaces and younger, physically capable warriors who can sustain its exhausting pace.",
        History: "Form IV emerged when Jedi realized the Force could augment physical combat beyond human limits. Yoda's mastery proved size irrelevant—in Attack of the Clones he duelled Count Dooku with acrobatic ferocity, and in Revenge of the Sith he confronted Chancellor Palpatine with Ataru's full aerial arsenal.\n\nQui-Gon Jinn employed Ataru against Darth Maul on Naboo in The Phantom Menace, though Maul's own Form VII endurance outlasted the older master's stamina. Anakin Skywalker blended Ataru leaps with Form V power throughout the Clone Wars, visible in The Clone Wars series.\n\nKOTOR's Revan and Bastila Shan used Ataru against crowded Sith ranks on the Star Forge, while the Old Sith Empire's warriors developed parallel leaping techniques in Korriban's tomb trials.",
        Significance: "Ataru embodies the Living Force made kinetic—combat as expression of joy, speed, and physical communion with the galaxy's energy. Its spectacular nature inspires allies and demoralizes foes, as Yoda's duels proved against entire Senate chambers.\n\nThe form demands peak physical condition and open terrain; prolonged engagements drain even Masters, as Qui-Gon's duel on Naboo demonstrated. Ataru practitioners must know when to transition to Soresu or Djem So, making Form IV a specialty rather than a complete philosophy.",
        Practitioners:
        [
            "Yoda",
            "Qui-Gon Jinn",
            "Anakin Skywalker (acrobatic elements)",
            "Bastila Shan (KOTOR)",
            "Old Republic Force-leap duelists"
        ],
        References:
        [
            "Films: The Phantom Menace · Attack of the Clones · Revenge of the Sith",
            "Series: The Clone Wars · Tales of the Jedi",
            "KOTOR · The Old Republic",
            "Old Sith Empire aerial combat trials"
        ]);

    private static LightsaberFormContent ShienDjemSo => new(
        Overview: "Shien and Djem So, Form V, turn defense into devastating offense—Shien redirects blaster bolts with a reversed grip, while Djem So absorbs an opponent's momentum and answers with crushing counter-strikes. It is the form of power, dominance, and battlefield authority.",
        History: "Form V evolved from Soresu when Jedi decided that endless defense wasted the Force's offensive potential. Anakin Skywalker naturally gravitated toward Djem So's power, visible in his aggressive Clone Wars style and his Mustafar duel in Revenge of the Sith.\n\nDarth Vader perfected Form V after his injuries on Mustafar, replacing Ataru's acrobatics with unstoppable strength in A New Hope, The Empire Strikes Back, and Return of the Jedi. Luke Skywalker inherited the form instinctively, defeating Vader at Endor through emotional clarity channeled into Form V strikes.\n\nKOTOR's Revan switched to Form V against Malak's brutal assault on the Star Forge. The Old Sith Empire's Sith Marauders codified similar counter-offensive techniques, blending Shien's bolt deflection with Djem So's kinetic punishment.",
        Significance: "Form V walks the edge between light and dark—its aggression tempts practitioners toward rage, as Anakin's fall demonstrated. Yet controlled Form V can end wars: Luke's refusal to kill Vader combined with Form V power broke the Emperor's hold.\n\nShien remains vital for Jedi facing blaster-heavy armies; Djem So dominates single-opponent duels. The form's popularity during the Clone Wars and Galactic Civil War reflects galactic warfare's shift from elegant dueling to total conflict.",
        Practitioners:
        [
            "Anakin Skywalker / Darth Vader",
            "Luke Skywalker",
            "Revan (KOTOR)",
            "Ahsoka Tano (Djem So elements)",
            "Old Sith Empire Sith Marauders"
        ],
        References:
        [
            "Films: All nine Skywalker saga entries",
            "Series: The Clone Wars · Rebels",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire Form V combat manuals"
        ]);

    private static LightsaberFormContent Niman => new(
        Overview: "Niman, Form VI, is the \"Way of the Rancor\"—a balanced hybrid drawing elements from all previous forms while integrating Force powers like push, pull, and throw into combat rhythm. It suits diplomats, generals, and Jedi who cannot specialize in one environment.",
        History: "Form VI was codified when the Jedi Order needed versatile knights who could negotiate peace and fight credibly if talks failed. Its practitioners rarely excel in any single specialty but adapt to varied threats—a philosophy suited to the Clone Wars' multi-front chaos.\n\nCin Drallig, the Temple battlemaster in Revenge of the Sith, taught Niman alongside other forms before falling defending the Jedi Temple during Order 66. Obi-Wan Kenobi incorporated Niman's Force integration into his broader repertoire across the Prequel trilogy.\n\nKOTOR's Jedi Consular path emphasized Niman-like balance, pairing blade work with Force healing and battlefield control. The Old Republic's Jedi Battlemasters archived Form VI for knights serving as Republic ambassadors to Sith-contested worlds.",
        Significance: "Niman rejects the myth that one form solves every problem—it teaches adaptability as the highest skill. In an era spanning Geonosis droid factories, Hoth ice plains, and Exegol lightning storms, versatility keeps Jedi alive when pure specialists falter.\n\nCritics call Form VI the \"diplomat's form\"—adequate at everything, master of nothing—yet Adept Niman practitioners who combine Force mastery with competent saber work often outlast pure duelists in extended campaigns. Rey's eclectic fighting style in the Sequel trilogy reflects Niman's modern spirit.",
        Practitioners:
        [
            "Cin Drallig",
            "Obi-Wan Kenobi (integrated Niman techniques)",
            "Jedi Consulars in KOTOR",
            "Clone Wars-era Jedi Generals",
            "Old Republic diplomatic knights"
        ],
        References:
        [
            "Films: Revenge of the Sith · The Force Awakens · The Last Jedi · The Rise of Skywalker",
            "Series: The Clone Wars · Tales of the Jedi",
            "KOTOR · The Old Republic",
            "Old Sith Empire diplomatic combat records"
        ]);

    private static LightsaberFormContent JuyoVaapad => new(
        Overview: "Juyo and Vaapad, Form VII, are the most aggressive lightsaber disciplines—Juyo unleashes ferocious offense that borders on the dark side, while Mace Windu's Vaapad channels an opponent's darkness through the wielder without succumbing to it. Form VII is dangerous to master and devastating when controlled.",
        History: "Juyo originated among Sith warriors of the Old Sith Empire, who valued its unpredictability and emotional intensity. Jedi adapted a restricted variant, but only Mace Windu perfected Vaapad—a form named after a predator, requiring the practitioner to enjoy battle while remaining spiritually anchored.\n\nWindu's Vaapad duel with Chancellor Palpatine in Revenge of the Sith nearly ended the Sith plot before Anakin's intervention—a moment when Form VII's dark-side channeling matched Sidious's own fury. Darth Maul's relentless Form VII assault killed Qui-Gon Jinn on Naboo in The Phantom Menace.\n\nKOTOR's Sith Lords and Marauders wielded Juyo on Korriban and the Star Forge, while KOTOR II explored Form VII's psychological toll through Sith training grounds on Malachor V. The Old Republic's Sith Warriors continued Juyo traditions in open war against the Jedi.",
        Significance: "Form VII forces confrontation with inner darkness. Most Jedi who attempted Juyo fell to the dark side; Vaapad's invention was Windu's answer—using the dark side as a mirror rather than a master. The form's rarity after Order 66 reflects the Order's fear of its seductive power.\n\nWhen galactic stakes are existential, Form VII ends threats faster than Soresu's patience—but at moral cost. Studying Vaapad teaches that the light side wins not by denying darkness but by integrating and transcending it, a lesson echoing from Korriban to Exegol.",
        Practitioners:
        [
            "Mace Windu (Vaapad creator)",
            "Darth Maul (Juyo)",
            "Depa Billaba (Vaapad student)",
            "Sith Marauders in KOTOR",
            "Old Sith Empire Juyo adepts on Korriban"
        ],
        References:
        [
            "Films: The Phantom Menace · Revenge of the Sith",
            "Series: The Clone Wars · Tales of the Jedi",
            "KOTOR · KOTOR II · The Old Republic",
            "Old Sith Empire Form VII combat inscriptions"
        ]);
}
