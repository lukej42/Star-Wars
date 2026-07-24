using StarWars.Models;

namespace StarWars.Data;

public static class ForcePowerData
{
    public static IReadOnlyList<ForcePower> Powers { get; } =
    [
        // Light Side — Telekinesis
        new()
        {
            Name = "Force Push",
            Slug = "force-push",
            Route = "force-powers/force-push",
            Side = ForceSide.Light,
            Category = "Telekinesis",
            Difficulty = "Novice",
            Description = "A fundamental telekinetic shove that repels objects and opponents through the Force, often used to create distance or knock enemies off balance. Obi-Wan Kenobi famously employed it against battle droids on Naboo and again to dispatch General Grievous on Utapau.",
            Color = "#3b82f6",
            Sources = "Films · The Phantom Menace · Attack of the Clones · Revenge of the Sith · Clone Wars"
        },
        new()
        {
            Name = "Force Pull",
            Slug = "force-pull",
            Route = "force-powers/force-pull",
            Side = ForceSide.Light,
            Category = "Telekinesis",
            Difficulty = "Novice",
            Description = "Draws objects, weapons, or opponents toward the wielder through concentrated telekinetic attraction. Luke Skywalker's retrieval of his lightsaber from beneath Cloud City remains one of the most iconic demonstrations of this technique.",
            Color = "#06b6d4",
            Sources = "Films · Empire Strikes Back · Return of the Jedi · The Last Jedi"
        },
        new()
        {
            Name = "Force Repulse",
            Slug = "force-repulse",
            Route = "force-powers/force-repulse",
            Side = ForceSide.Light,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Unleashes a radial telekinetic burst that hurls everything nearby outward in all directions, trading precision for overwhelming area denial. Jedi in the Old Republic era used repulse to scatter groups of Sith troopers during large-scale engagements.",
            Color = "#3b82f6",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },
        new()
        {
            Name = "Force Throw",
            Slug = "force-throw",
            Route = "force-powers/force-throw",
            Side = ForceSide.Light,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Hurls heavy objects—or entire opponents—across a battlefield with telekinetic force, turning the environment itself into a weapon. Yoda demonstrated this mastery by redirecting droid attacks and flinging Separatist machinery during the Clone Wars.",
            Color = "#06b6d4",
            Sources = "Films · Attack of the Clones · Revenge of the Sith · Clone Wars"
        },
        new()
        {
            Name = "Force Wave",
            Slug = "force-wave",
            Route = "force-powers/force-wave",
            Side = ForceSide.Light,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Projects a sweeping telekinetic wave across a wide arc, toppling multiple foes or deflecting volleys of blaster fire in a single motion. High Republic Jedi used waves to protect civilians during the Nihil conflict when surrounded on open ground.",
            Color = "#22c55e",
            Sources = "High Republic · Clone Wars · KOTOR II"
        },
        new()
        {
            Name = "Force Stasis",
            Slug = "force-stasis",
            Route = "force-powers/force-stasis",
            Side = ForceSide.Light,
            Category = "Telekinesis",
            Difficulty = "Master",
            Description = "Suspends a target in a telekinetic stasis field, immobilizing limbs and freezing motion without inflicting direct harm. Master-level practitioners can hold multiple assailants at once, as seen when senior Jedi subdued rampaging foes during Temple disturbances.",
            Color = "#eab308",
            Sources = "KOTOR · KOTOR II · Clone Wars · The Old Republic"
        },

        // Light Side — Protection
        new()
        {
            Name = "Force Barrier",
            Slug = "force-barrier",
            Route = "force-powers/force-barrier",
            Side = ForceSide.Light,
            Category = "Protection",
            Difficulty = "Adept",
            Description = "Manifests an invisible wall of Force energy that absorbs blaster bolts, shrapnel, and kinetic impacts before they reach the wielder or allies. Battlefront Jedi frequently erected barriers to shield clone troopers during exposed advances across Separatist kill zones.",
            Color = "#3b82f6",
            Sources = "Clone Wars · KOTOR · KOTOR II · The Old Republic"
        },
        new()
        {
            Name = "Tutaminis",
            Slug = "tutaminis",
            Route = "force-powers/tutaminis",
            Side = ForceSide.Light,
            Category = "Protection",
            Difficulty = "Master",
            Description = "The advanced discipline of absorbing, dissipating, or redirecting concentrated energy—including Force lightning—through the body without injury. Yoda and Darth Vader both demonstrated tutaminis when catching and neutralizing Palpatine's lightning, though Vader's prosthetics limited his endurance.",
            Color = "#eab308",
            Sources = "Films · Revenge of the Sith · Return of the Jedi · Clone Wars"
        },
        new()
        {
            Name = "Force Deflection",
            Slug = "force-deflection",
            Route = "force-powers/force-deflection",
            Side = ForceSide.Light,
            Category = "Protection",
            Difficulty = "Adept",
            Description = "Deflects incoming blaster bolts and energy weapons using bare hands or a gauntlet of Force energy, without relying on a lightsaber. Kanan Jarrus and other survivors of Order 66 used deflection when caught without their sabers during Imperial hunts.",
            Color = "#22c55e",
            Sources = "Rebels · Clone Wars · KOTOR · Films"
        },
        new()
        {
            Name = "Force Resistance",
            Slug = "force-resistance",
            Route = "force-powers/force-resistance",
            Side = ForceSide.Light,
            Category = "Protection",
            Difficulty = "Adept",
            Description = "Fortifies the mind and body against dark-side assaults, mental intrusion, and debilitating Force powers through disciplined inner calm. Jedi Council members trained in resistance to withstand Sith sorcery and interrogation during the Clone Wars.",
            Color = "#06b6d4",
            Sources = "Clone Wars · KOTOR II · The Old Republic · Films"
        },

        // Light Side — Healing
        new()
        {
            Name = "Force Heal",
            Slug = "force-heal",
            Route = "force-powers/force-heal",
            Side = ForceSide.Light,
            Category = "Healing",
            Difficulty = "Adept",
            Description = "Channels the living Force to mend wounds, purge toxins, and restore vitality in oneself or others through focused compassion. Rey healed the serpent on Pasaana and later transferred life energy to save Ben Solo, demonstrating healing at its most selfless and costly.",
            Color = "#22c55e",
            Sources = "Films · The Rise of Skywalker · Mandalorian · Ahsoka · Clone Wars"
        },
        new()
        {
            Name = "Force Body",
            Slug = "force-body",
            Route = "force-powers/force-body",
            Side = ForceSide.Light,
            Category = "Healing",
            Difficulty = "Master",
            Description = "Draws on the Force to sustain the physical body beyond its natural limits, suppressing pain, fatigue, and even mortal injury for a time. Darth Plagueis's teachings touched on related principles, while light-side masters used Force Body to endure extreme environments and prolonged combat.",
            Color = "#06b6d4",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },

        // Light Side — Support
        new()
        {
            Name = "Battle Meditation",
            Slug = "battle-meditation",
            Route = "force-powers/battle-meditation",
            Side = ForceSide.Light,
            Category = "Support",
            Difficulty = "Master",
            Description = "A deep meditative state through which a Jedi subtly coordinates allied forces, bolstering morale and tactical cohesion across an entire fleet or army. Bastila Shan's battle meditation was pivotal to the Republic's victory at the Battle of Rakata Prime during the Jedi Civil War.",
            Color = "#eab308",
            Sources = "KOTOR · The Old Republic · Clone Wars · High Republic"
        },
        new()
        {
            Name = "Force Valor",
            Slug = "force-valor",
            Route = "force-powers/force-valor",
            Side = ForceSide.Light,
            Category = "Support",
            Difficulty = "Adept",
            Description = "Infuses allies with heightened courage, reflexes, and clarity in combat, turning wavering soldiers into resolute fighters. Jedi Generals on the front lines of the Clone Wars routinely projected valor to steady clone battalions under heavy fire.",
            Color = "#3b82f6",
            Sources = "KOTOR · Clone Wars · The Old Republic · KOTOR II"
        },
        new()
        {
            Name = "Force Empower",
            Slug = "force-empower",
            Route = "force-powers/force-empower",
            Side = ForceSide.Light,
            Category = "Support",
            Difficulty = "Adept",
            Description = "Temporarily amplifies an ally's physical strength, speed, or Force sensitivity through a direct transfer of the wielder's own energy. Masters used empowerment to enable padawans to overcome obstacles that would otherwise exceed their training.",
            Color = "#22c55e",
            Sources = "KOTOR · Clone Wars · High Republic · The Old Republic"
        },

        // Light Side — Mind
        new()
        {
            Name = "Mind Trick",
            Slug = "mind-trick",
            Route = "force-powers/mind-trick",
            Side = ForceSide.Light,
            Category = "Mind",
            Difficulty = "Novice",
            Description = "Influences weak-minded individuals through a subtle telepathic suggestion, causing them to comply with simple commands or overlook the Jedi's presence. Obi-Wan's 'These aren't the droids you're looking for' on Tatooine remains the definitive example of this technique.",
            Color = "#3b82f6",
            Sources = "Films · A New Hope · Attack of the Clones · The Phantom Menace · Clone Wars"
        },
        new()
        {
            Name = "Force Persuasion",
            Slug = "force-persuasion",
            Route = "force-powers/force-persuasion",
            Side = ForceSide.Light,
            Category = "Mind",
            Difficulty = "Adept",
            Description = "An advanced form of mental influence that plants deeper, longer-lasting suggestions in a target's subconscious, useful for diplomacy and intelligence work. Jedi negotiators employed persuasion during the waning days of the Republic to avert conflicts without drawing a lightsaber.",
            Color = "#06b6d4",
            Sources = "KOTOR · Clone Wars · The Old Republic · High Republic"
        },
        new()
        {
            Name = "Force Illusion",
            Slug = "force-illusion",
            Route = "force-powers/force-illusion",
            Side = ForceSide.Light,
            Category = "Mind",
            Difficulty = "Master",
            Description = "Projects a convincing false image or duplicate of the wielder across vast distances through the Force, taxing the body but deceiving even powerful enemies. Luke Skywalker's astral projection on Crait bought the Resistance critical time, though the effort ultimately proved fatal.",
            Color = "#22c55e",
            Sources = "Films · The Last Jedi · Clone Wars · Rebels"
        },

        // Light Side — Sense
        new()
        {
            Name = "Psychometry",
            Slug = "psychometry",
            Route = "force-powers/psychometry",
            Side = ForceSide.Light,
            Category = "Sense",
            Difficulty = "Adept",
            Description = "Reads the history and emotional residue imprinted on objects through touch, revealing past events as vivid sensory flashes. Quinlan Vos was renowned for psychometric tracking, using a mere fragment of cloth to locate abducted targets across the galaxy.",
            Color = "#eab308",
            Sources = "Clone Wars · High Republic · Dark Disciple · KOTOR II"
        },
        new()
        {
            Name = "Force Sense",
            Slug = "force-sense",
            Route = "force-powers/force-sense",
            Side = ForceSide.Light,
            Category = "Sense",
            Difficulty = "Novice",
            Description = "Extends awareness beyond the physical senses to detect life forms, emotional states, and disturbances in the Force across great distances. Every Jedi learns to sense danger before it strikes—a skill that saved countless lives during the Clone Wars.",
            Color = "#3b82f6",
            Sources = "Films · Clone Wars · Rebels · KOTOR · Empire Strikes Back"
        },
        new()
        {
            Name = "Force Vision",
            Slug = "force-vision",
            Route = "force-powers/force-vision",
            Side = ForceSide.Light,
            Category = "Sense",
            Difficulty = "Adept",
            Description = "Grants prophetic glimpses of possible futures, past events, or hidden truths through vivid waking or meditative visions. Anakin Skywalker's nightmares of Padmé's death and Rey's vision in the Mirror of Darth Vader both shaped the fate of the galaxy.",
            Color = "#06b6d4",
            Sources = "Films · Revenge of the Sith · The Force Awakens · Clone Wars · Rebels"
        },
        new()
        {
            Name = "Shatterpoint",
            Slug = "shatterpoint",
            Route = "force-powers/shatterpoint",
            Side = ForceSide.Light,
            Category = "Sense",
            Difficulty = "Master",
            Description = "Perceives critical fault lines in people, objects, and situations—the precise points where the smallest action can collapse an entire system. Mace Windu wielded shatterpoint to dismantle droid armies and recognized Palpatine as the shatterpoint of the Republic itself.",
            Color = "#eab308",
            Sources = "Films · Revenge of the Sith · Shatterpoint novel · Clone Wars"
        },

        // Light Side — Physical
        new()
        {
            Name = "Force Speed",
            Slug = "force-speed",
            Route = "force-powers/force-speed",
            Side = ForceSide.Light,
            Category = "Physical",
            Difficulty = "Adept",
            Description = "Accelerates the wielder's movement to superhuman velocity, blurring across battlefields to strike or evade before opponents can react. Qui-Gon Jinn and Obi-Wan Kenobi burst through droideka fire on Naboo using Force speed to reach the bridge controls in seconds.",
            Color = "#3b82f6",
            Sources = "Films · The Phantom Menace · Clone Wars · KOTOR · KOTOR II"
        },
        new()
        {
            Name = "Force Jump",
            Slug = "force-jump",
            Route = "force-powers/force-jump",
            Side = ForceSide.Light,
            Category = "Physical",
            Difficulty = "Novice",
            Description = "Enhances leg strength to achieve extraordinary leaps, allowing Jedi to reach high platforms, cross gaps, and gain tactical elevation in combat. From Yoda's acrobatic duels to Luke's training on Dagobah, Force jump is among the most visible expressions of a Jedi's power.",
            Color = "#22c55e",
            Sources = "Films · Empire Strikes Back · Attack of the Clones · Clone Wars · Rebels"
        },
        new()
        {
            Name = "Force Dash",
            Slug = "force-dash",
            Route = "force-powers/force-dash",
            Side = ForceSide.Light,
            Category = "Physical",
            Difficulty = "Adept",
            Description = "Propels the wielder forward in a sudden burst of Force-enhanced momentum, closing distance on enemies or escaping encirclement in an instant. Jedi Knights on the battlefields of the Old Republic relied on Force dash to intercept Sith marauders before they reached vulnerable positions.",
            Color = "#06b6d4",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },
        new()
        {
            Name = "Force Stealth",
            Slug = "force-stealth",
            Route = "force-powers/force-stealth",
            Side = ForceSide.Light,
            Category = "Physical",
            Difficulty = "Adept",
            Description = "Masks the wielder's presence in the Force, rendering them invisible to Force-sensitive detection and difficult to track through conventional means. Jedi sent on covert missions during the Clone Wars used stealth to infiltrate Separatist installations undetected.",
            Color = "#22c55e",
            Sources = "Clone Wars · KOTOR II · High Republic · Rebels"
        },
        new()
        {
            Name = "Force Camouflage",
            Slug = "force-camouflage",
            Route = "force-powers/force-camouflage",
            Side = ForceSide.Light,
            Category = "Physical",
            Difficulty = "Master",
            Description = "Bends light and perception around the body to blend seamlessly into the surrounding environment, achieving near-perfect visual concealment. The Jedi Temple's Shadow Guard and certain High Republic operatives mastered camouflage for reconnaissance in hostile territory.",
            Color = "#06b6d4",
            Sources = "High Republic · KOTOR II · Clone Wars · The Old Republic"
        },

        // Light Side — Nature
        new()
        {
            Name = "Animal Bond",
            Slug = "animal-bond",
            Route = "force-powers/animal-bond",
            Side = ForceSide.Light,
            Category = "Nature",
            Difficulty = "Adept",
            Description = "Establishes a telepathic connection with non-sentient creatures, calming them, sharing senses, or calling upon them for aid. Obi-Wan Kenobi tamed a raging acklay on Geonosis, and Rey communicated with creatures across her journeys through instinctive animal bonding.",
            Color = "#22c55e",
            Sources = "Films · Attack of the Clones · The Rise of Skywalker · Clone Wars · High Republic"
        },
        new()
        {
            Name = "Plant Surge",
            Slug = "plant-surge",
            Route = "force-powers/plant-surge",
            Side = ForceSide.Light,
            Category = "Nature",
            Difficulty = "Adept",
            Description = "Accelerates the growth of plant life, causing vines, roots, and foliage to burst forth and entangle foes or restore damaged ecosystems. High Republic Jedi on lush frontier worlds used plant surge to rapidly reforest areas devastated by the Nihil's raids.",
            Color = "#22c55e",
            Sources = "High Republic · Clone Wars · KOTOR · The Old Republic"
        },

        // Light Side — Purification
        new()
        {
            Name = "Force Light",
            Slug = "force-light",
            Route = "force-powers/force-light",
            Side = ForceSide.Light,
            Category = "Purification",
            Difficulty = "Master",
            Description = "Emits a radiant burst of light-side energy that purges dark-side corruption from places, objects, and even afflicted individuals. Jedi of the Old Republic deployed Force Light to cleanse Sith-tainted temples and holocrons that poisoned the minds of those nearby.",
            Color = "#eab308",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },
        new()
        {
            Name = "Sever Force",
            Slug = "sever-force",
            Route = "force-powers/sever-force",
            Side = ForceSide.Light,
            Category = "Purification",
            Difficulty = "Master",
            Description = "Cuts a Force-sensitive individual off from the Force entirely, leaving them unable to sense or wield its power—a punishment reserved for the gravest betrayals. The Jedi Council considered severing as an alternative to execution for fallen members who could not be redeemed.",
            Color = "#06b6d4",
            Sources = "KOTOR II · The Old Republic · Clone Wars · High Republic"
        },
        new()
        {
            Name = "Morichro",
            Slug = "morichro",
            Route = "force-powers/morichro",
            Side = ForceSide.Light,
            Category = "Purification",
            Difficulty = "Master",
            Description = "Induces a deep Force trance that slows bodily functions to near zero, preserving life in stasis for extended periods without aging or decay. Ancient Jedi used morichro to survive catastrophic events and to imprison dangerous dark-side entities in suspended animation.",
            Color = "#3b82f6",
            Sources = "High Republic · The Old Republic · Clone Wars · KOTOR II"
        },

        // Light Side — Connection
        new()
        {
            Name = "Force Bond",
            Slug = "force-bond",
            Route = "force-powers/force-bond",
            Side = ForceSide.Light,
            Category = "Connection",
            Difficulty = "Adept",
            Description = "Creates a persistent telepathic link between two Force-sensitive individuals, allowing them to share thoughts, emotions, and visions across any distance. The bond between Rey and Ben Solo grew so powerful that it eventually transcended death itself.",
            Color = "#3b82f6",
            Sources = "Films · The Last Jedi · The Rise of Skywalker · Clone Wars · KOTOR"
        },
        new()
        {
            Name = "Force Meld",
            Slug = "force-meld",
            Route = "force-powers/force-meld",
            Side = ForceSide.Light,
            Category = "Connection",
            Difficulty = "Master",
            Description = "Merges the minds of multiple Jedi into a unified consciousness, combining their strength for tasks no individual could accomplish alone. Luke and Leia Organa performed a Force meld to locate their lost brother Jacen during the dark days of the Yuuzhan Vong invasion.",
            Color = "#06b6d4",
            Sources = "Films · KOTOR · Clone Wars · High Republic · Rebels"
        },

        // Light Side — Transcendence
        new()
        {
            Name = "Force Spirit",
            Slug = "force-spirit",
            Route = "force-powers/force-spirit",
            Side = ForceSide.Light,
            Category = "Transcendence",
            Difficulty = "Master",
            Description = "Allows a deceased Jedi to retain consciousness and manifest as a luminous Force ghost, continuing to guide the living long after physical death. Qui-Gon Jinn discovered the path; Yoda and Obi-Wan mastered it, appearing to Luke on Dagobah, Endor, and beyond.",
            Color = "#eab308",
            Sources = "Films · Revenge of the Sith · Return of the Jedi · Empire Strikes Back · Clone Wars"
        },
        new()
        {
            Name = "Force Enlightenment",
            Slug = "force-enlightenment",
            Route = "force-powers/force-enlightenment",
            Side = ForceSide.Light,
            Category = "Transcendence",
            Difficulty = "Master",
            Description = "Represents the ultimate union with the living Force—a state of perfect balance, clarity, and harmony achieved only by the most disciplined masters after lifetimes of meditation. Enlightened Jedi transcend attachment and fear, acting as pure conduits of the Force's will.",
            Color = "#eab308",
            Sources = "Clone Wars · High Republic · KOTOR II · The Old Republic"
        },

        // Light Side — Energy
        new()
        {
            Name = "Electric Judgment",
            Slug = "electric-judgment",
            Route = "force-powers/electric-judgment",
            Side = ForceSide.Light,
            Category = "Energy",
            Difficulty = "Master",
            Description = "Channels the Force into golden electrical energy that incapacitates rather than kills, serving as the light-side counterpart to Sith lightning. Jedi Master Plo Koon developed electric judgment as a non-lethal alternative for subduing criminals who resisted arrest.",
            Color = "#3b82f6",
            Sources = "Clone Wars · KOTOR II · The Old Republic · Jedi Council novels"
        },
        new()
        {
            Name = "Force Orb",
            Slug = "force-orb",
            Route = "force-powers/force-orb",
            Side = ForceSide.Light,
            Category = "Energy",
            Difficulty = "Adept",
            Description = "Concentrates light-side energy into a sustained sphere that can be hurled at enemies or held as a shield against dark-side projectiles. Jedi Guardians of the Old Republic favored Force orbs when fighting Sith in close quarters where lightsaber strikes were insufficient.",
            Color = "#06b6d4",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },

        // Dark Side — Telekinesis
        new()
        {
            Name = "Force Choke",
            Slug = "force-choke",
            Route = "force-powers/force-choke",
            Side = ForceSide.Dark,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Constricts a victim's throat with invisible telekinetic force, lifting them off the ground while cutting off their airway—a signature intimidation technique of the Sith. Darth Vader used Force choke to discipline incompetent officers and subdue rebels aboard the Tantive IV.",
            Color = "#dc2626",
            Sources = "Films · A New Hope · Empire Strikes Back · Return of the Jedi · Rogue One"
        },
        new()
        {
            Name = "Force Grip",
            Slug = "force-grip",
            Route = "force-powers/force-grip",
            Side = ForceSide.Dark,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Seizes an opponent with telekinetic force and holds them suspended and helpless, often as a prelude to execution or torture. Count Dooku gripped Obi-Wan Kenobi mid-duel on Geonosis, demonstrating the cruel precision with which Sith Lords dominate their prey.",
            Color = "#991b1b",
            Sources = "Films · Attack of the Clones · Revenge of the Sith · Clone Wars · Rebels"
        },
        new()
        {
            Name = "Force Crush",
            Slug = "force-crush",
            Route = "force-powers/force-crush",
            Side = ForceSide.Dark,
            Category = "Telekinesis",
            Difficulty = "Master",
            Description = "Applies overwhelming telekinetic pressure to compress and destroy a target's body, armor, or internal organs in a gruesome display of dark-side power. Darth Vader crushed the throat and chest of rebels who stood in his path during the assault on the Tantive IV.",
            Color = "#7f1d1d",
            Sources = "Films · Rogue One · Clone Wars · KOTOR · The Old Republic"
        },
        new()
        {
            Name = "Force Whirlwind",
            Slug = "force-whirlwind",
            Route = "force-powers/force-whirlwind",
            Side = ForceSide.Dark,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Lifts and spins enemies in a violent telekinetic vortex before slamming them into the ground or surrounding obstacles. Sith warriors across the Old Republic era used Force whirlwind to scatter Jedi formations and create openings for devastating follow-up strikes.",
            Color = "#dc2626",
            Sources = "KOTOR · KOTOR II · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Force Net",
            Slug = "force-net",
            Route = "force-powers/force-net",
            Side = ForceSide.Dark,
            Category = "Telekinesis",
            Difficulty = "Adept",
            Description = "Weaves strands of dark-side telekinetic energy into a binding net that ensnares and immobilizes multiple targets at once. Sith Inquisitors and Nightsister acolytes deployed Force nets to capture fleeing Jedi and Force-sensitive children for the Empire's Project Harvester.",
            Color = "#7c3aed",
            Sources = "Rebels · Clone Wars · KOTOR II · The Old Republic"
        },

        // Dark Side — Energy
        new()
        {
            Name = "Force Lightning",
            Slug = "force-lightning",
            Route = "force-powers/force-lightning",
            Side = ForceSide.Dark,
            Category = "Energy",
            Difficulty = "Adept",
            Description = "Channels raw dark-side hatred into crackling bolts of blue or purple electricity that torture, burn, and kill targets at range. Emperor Palpatine's Force lightning nearly killed Luke Skywalker aboard the second Death Star and defined the terrifying arsenal of the Sith.",
            Color = "#dc2626",
            Sources = "Films · Return of the Jedi · Revenge of the Sith · Empire Strikes Back · Clone Wars"
        },
        new()
        {
            Name = "Force Storm",
            Slug = "force-storm",
            Route = "force-powers/force-storm",
            Side = ForceSide.Dark,
            Category = "Energy",
            Difficulty = "Master",
            Description = "Summons a cataclysmic tempest of dark-side energy capable of annihilating fleets, ravaging planets, and tearing holes in the fabric of hyperspace. Only the most powerful Sith Lords—such as Palpatine in his clone bodies—could sustain a Force storm without being consumed by it.",
            Color = "#7c3aed",
            Sources = "Dark Empire · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Force Destruction",
            Slug = "force-destruction",
            Route = "force-powers/force-destruction",
            Side = ForceSide.Dark,
            Category = "Energy",
            Difficulty = "Master",
            Description = "Unleashes a concentrated sphere of annihilating dark-side energy that detonates on impact, obliterating everything in a wide blast radius. Sith Lords of the Old Republic used Force destruction to breach fortified Jedi enclaves during the Great Galactic War.",
            Color = "#991b1b",
            Sources = "KOTOR · KOTOR II · The Old Republic · Sith Empire"
        },
        new()
        {
            Name = "Dark Side Burst",
            Slug = "dark-side-burst",
            Route = "force-powers/dark-side-burst",
            Side = ForceSide.Dark,
            Category = "Energy",
            Difficulty = "Adept",
            Description = "Releases a sudden radial explosion of dark-side energy from the wielder's body, damaging all nearby enemies and often staggering even armored foes. Inquisitors and Sith acolytes favored dark-side burst when surrounded, turning desperation into a devastating counterattack.",
            Color = "#dc2626",
            Sources = "KOTOR · Rebels · The Old Republic · Clone Wars"
        },
        new()
        {
            Name = "Chain Lightning",
            Slug = "chain-lightning",
            Route = "force-powers/chain-lightning",
            Side = ForceSide.Dark,
            Category = "Energy",
            Difficulty = "Master",
            Description = "Fires a bolt of Force lightning that arcs from the primary target to nearby enemies, chaining destruction across an entire group. Darth Sidious and his Sith apprentices used chain lightning to slaughter multiple opponents during the fall of the Jedi Temple.",
            Color = "#7c3aed",
            Sources = "Films · Revenge of the Sith · KOTOR · The Old Republic · Sith Empire"
        },
        new()
        {
            Name = "Force Lightning Shield",
            Slug = "force-lightning-shield",
            Route = "force-powers/force-lightning-shield",
            Side = ForceSide.Dark,
            Category = "Energy",
            Difficulty = "Master",
            Description = "Surrounds the wielder in a crackling aura of Force lightning that electrocutes anyone who comes into contact while deflecting incoming energy attacks. Sith Emperors and elite dark-side warriors maintained lightning shields during prolonged sieges against Jedi strongholds.",
            Color = "#450a0a",
            Sources = "The Old Republic · Sith Empire · KOTOR II · Clone Wars"
        },

        // Dark Side — Drain
        new()
        {
            Name = "Force Drain",
            Slug = "force-drain",
            Route = "force-powers/force-drain",
            Side = ForceSide.Dark,
            Category = "Drain",
            Difficulty = "Adept",
            Description = "Siphons the life energy and Force connection from a victim, transferring their vitality to the wielder to restore strength or extend their own power. Darth Nihilus became a wound in the Force itself, draining entire worlds to sustain his hollow existence.",
            Color = "#7c3aed",
            Sources = "KOTOR II · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Drain Life",
            Slug = "drain-life",
            Route = "force-powers/drain-life",
            Side = ForceSide.Dark,
            Category = "Drain",
            Difficulty = "Master",
            Description = "A more aggressive variant of Force drain that rapidly extracts the life essence of a target, often leaving them desiccated corpses while the Sith grows stronger. Sith alchemists combined drain life with ritual sacrifice to fuel their darkest experiments.",
            Color = "#991b1b",
            Sources = "KOTOR II · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Force Wound",
            Slug = "force-wound",
            Route = "force-powers/force-wound",
            Side = ForceSide.Dark,
            Category = "Drain",
            Difficulty = "Adept",
            Description = "Inflicts internal injuries—ruptured organs, severed blood vessels, and shattered bones—through the Force without any visible external wound. Sith assassins used Force wound to eliminate targets silently, leaving no trace of the killer's method.",
            Color = "#dc2626",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },
        new()
        {
            Name = "Force Kill",
            Slug = "force-kill",
            Route = "force-powers/force-kill",
            Side = ForceSide.Dark,
            Category = "Drain",
            Difficulty = "Master",
            Description = "Instantly terminates a target's life by severing their connection to the Force and collapsing their vital functions in a single, focused dark-side assault. Only the most ruthless Sith Lords mastered Force kill, using it to execute Jedi who had become too dangerous to capture.",
            Color = "#450a0a",
            Sources = "KOTOR · KOTOR II · The Old Republic · Sith Empire"
        },
        new()
        {
            Name = "Force Plague",
            Slug = "force-plague",
            Route = "force-powers/force-plague",
            Side = ForceSide.Dark,
            Category = "Drain",
            Difficulty = "Master",
            Description = "Projects a dark-side affliction that spreads sickness, decay, and Force corruption through a target and potentially to those nearby. Sith sorcerers on Korriban weaponized Force plague during ancient wars, turning entire battalions into rotting, mindless husks.",
            Color = "#7c3aed",
            Sources = "The Old Republic · Sith Empire · KOTOR II · Clone Wars"
        },

        // Dark Side — Mind
        new()
        {
            Name = "Force Slow",
            Slug = "force-slow",
            Route = "force-powers/force-slow",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Adept",
            Description = "Dampens a target's reflexes, perception, and physical speed through dark-side mental interference, making even skilled warriors feel as though they move through treacle. Sith duelists opened combat with Force slow to gain a decisive edge before blades ever crossed.",
            Color = "#7c3aed",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },
        new()
        {
            Name = "Force Fear",
            Slug = "force-fear",
            Route = "force-powers/force-fear",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Novice",
            Description = "Projects a wave of primal terror into the minds of enemies, causing panic, flight, or paralysis through the dark side's corrupting influence. The Sith feed on fear, and even a novice dark-side adept can scatter untrained soldiers with a single burst of dread.",
            Color = "#dc2626",
            Sources = "KOTOR · Clone Wars · Rebels · The Old Republic"
        },
        new()
        {
            Name = "Force Horror",
            Slug = "force-horror",
            Route = "force-powers/force-horror",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Adept",
            Description = "Amplifies Force fear into vivid, personalized nightmares that overwhelm a target's sanity and can incapacitate groups simultaneously. Sith sorcerers on Dromund Kaas used Force horror to break the wills of prisoners before interrogation.",
            Color = "#991b1b",
            Sources = "KOTOR II · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Force Insanity",
            Slug = "force-insanity",
            Route = "force-powers/force-insanity",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Master",
            Description = "Shatters a victim's mind entirely, driving them to permanent madness through relentless dark-side psychic assault. The ancient Sith Emperor used Force insanity to create fanatically loyal servants whose broken minds could never betray him.",
            Color = "#7c3aed",
            Sources = "The Old Republic · Sith Empire · KOTOR II · Clone Wars"
        },
        new()
        {
            Name = "Force Corrupt",
            Slug = "force-corrupt",
            Route = "force-powers/force-corrupt",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Master",
            Description = "Gradually twists a target's thoughts, values, and moral compass toward the dark side, eroding their resistance over time rather than in a single assault. Palpatine's entire manipulation of Anakin Skywalker was a masterclass in long-form Force corruption.",
            Color = "#450a0a",
            Sources = "Films · Revenge of the Sith · Clone Wars · The Old Republic · KOTOR"
        },
        new()
        {
            Name = "Force Affliction",
            Slug = "force-affliction",
            Route = "force-powers/force-affliction",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Adept",
            Description = "Inflicts debilitating pain, nausea, or weakness directly through the Force, wearing down opponents without ever touching them. Nightsister magick and Sith torture techniques both drew upon affliction to break captives during the Clone Wars.",
            Color = "#991b1b",
            Sources = "Clone Wars · KOTOR II · The Old Republic · Rebels"
        },
        new()
        {
            Name = "Force Blind",
            Slug = "force-blind",
            Route = "force-powers/force-blind",
            Side = ForceSide.Dark,
            Category = "Mind",
            Difficulty = "Adept",
            Description = "Strips away a target's connection to the Force, leaving Force-sensitive individuals temporarily unable to sense, predict, or respond to threats through their usual abilities. Sith hunters used Force blind to level the battlefield when facing powerful Jedi opponents.",
            Color = "#dc2626",
            Sources = "KOTOR · KOTOR II · The Old Republic · Clone Wars"
        },

        // Dark Side — Enhancement
        new()
        {
            Name = "Force Rage",
            Slug = "force-rage",
            Route = "force-powers/force-rage",
            Side = ForceSide.Dark,
            Category = "Enhancement",
            Difficulty = "Adept",
            Description = "Channels anger and hatred into a surge of physical strength, speed, and pain tolerance that dramatically amplifies combat prowess at the cost of reason. Anakin Skywalker repeatedly surrendered to Force rage during the Clone Wars, foreshadowing his fall to the dark side.",
            Color = "#dc2626",
            Sources = "Films · Revenge of the Sith · Clone Wars · KOTOR · KOTOR II"
        },
        new()
        {
            Name = "Force Scream",
            Slug = "force-scream",
            Route = "force-powers/force-scream",
            Side = ForceSide.Dark,
            Category = "Enhancement",
            Difficulty = "Adept",
            Description = "Releases a sonic blast of dark-side energy through a horrifying scream that shatters eardrums, staggers Force users, and damages nearby structures. Darth Vader's anguished cry upon learning of Padmé's death on Mustafar echoed through the Force itself.",
            Color = "#991b1b",
            Sources = "Films · Revenge of the Sith · Clone Wars · KOTOR II · The Old Republic"
        },

        // Dark Side — Offensive
        new()
        {
            Name = "Force Stun",
            Slug = "force-stun",
            Route = "force-powers/force-stun",
            Side = ForceSide.Dark,
            Category = "Offensive",
            Difficulty = "Novice",
            Description = "Delivers a concussive blast of dark-side energy that knocks targets unconscious or temporarily paralyzes their motor functions. Inquisitors used Force stun to incapacitate fleeing Force-sensitive children without killing them, preserving targets for the Empire's harvesting programs.",
            Color = "#7c3aed",
            Sources = "Rebels · Clone Wars · KOTOR · Mandalorian"
        },

        // Dark Side — Illusion
        new()
        {
            Name = "Force Phantom",
            Slug = "force-phantom",
            Route = "force-powers/force-phantom",
            Side = ForceSide.Dark,
            Category = "Illusion",
            Difficulty = "Master",
            Description = "Creates semi-corporeal dark-side apparitions that can interact with the physical world and engage in combat, drawing power from the wielder's own life force. Sith sorcerers on Korriban summoned phantoms of fallen warriors to guard their tombs for millennia.",
            Color = "#7c3aed",
            Sources = "The Old Republic · Sith Empire · KOTOR II · Clone Wars"
        },
        new()
        {
            Name = "Force Projection",
            Slug = "force-projection",
            Route = "force-powers/force-projection",
            Side = ForceSide.Dark,
            Category = "Illusion",
            Difficulty = "Master",
            Description = "Projects a false image or duplicate of oneself—or another person—across great distances to deceive, intimidate, or misdirect enemies. Sith holocrons recorded projection techniques used by ancient Lords to appear in multiple places simultaneously during wars.",
            Color = "#450a0a",
            Sources = "Films · The Last Jedi · The Old Republic · Clone Wars · KOTOR II"
        },
        new()
        {
            Name = "Force Shadow",
            Slug = "force-shadow",
            Route = "force-powers/force-shadow",
            Side = ForceSide.Dark,
            Category = "Illusion",
            Difficulty = "Adept",
            Description = "Conceals the wielder's presence in the Force behind a veil of dark-side energy, making them undetectable to Jedi while appearing as a void or absence rather than simply invisible. Sith assassins and Inquisitors relied on Force shadow for stealth kills and ambushes.",
            Color = "#991b1b",
            Sources = "Rebels · KOTOR II · The Old Republic · Clone Wars"
        },

        // Dark Side — Ritual
        new()
        {
            Name = "Thought Bomb",
            Slug = "thought-bomb",
            Route = "force-powers/thought-bomb",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "A devastating Sith ritual that detonates the collective dark-side energies of multiple participants, annihilating Force-sensitive minds across a vast area while trapping the souls of the casters in stasis. The Brotherhood of Darkness unleashed a thought bomb on Ruusan that ended the New Sith Wars at terrible cost.",
            Color = "#450a0a",
            Sources = "Jedi vs Sith · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Sith Alchemy",
            Slug = "sith-alchemy",
            Route = "force-powers/sith-alchemy",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "A forbidden science that combines dark-side sorcery with chemical and biological manipulation to create monsters, poison worlds, and forge unnatural artifacts. Naga Sadow and later Sith Lords bred Sithspawn—mutated creatures warped into living weapons through alchemical rituals.",
            Color = "#7c3aed",
            Sources = "Tales of the Jedi · The Old Republic · Sith Empire · Clone Wars"
        },
        new()
        {
            Name = "Sith Sorcery",
            Slug = "sith-sorcery",
            Route = "force-powers/sith-sorcery",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "Encompasses the deepest dark-side rituals—curses, binding spells, and reality-warping incantations passed down through Sith holocrons and tomes on Korriban. Mother Talzin and the Nightsisters practiced a Dathomirian variant of Sith sorcery that rivaled the power of the Sith Lords themselves.",
            Color = "#7c3aed",
            Sources = "Clone Wars · The Old Republic · Sith Empire · Tales of the Jedi"
        },
        new()
        {
            Name = "Essence Transfer",
            Slug = "essence-transfer",
            Route = "force-powers/essence-transfer",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "Transfers a Sith Lord's consciousness into a new body or vessel, achieving a form of immortality by escaping death through dark-side will alone. Palpatine's return in clone bodies and Darth Andeddu's ancient teachings both stemmed from essence transfer rituals perfected on Korriban.",
            Color = "#991b1b",
            Sources = "Films · The Rise of Skywalker · The Old Republic · Sith Empire · Dark Empire"
        },
        new()
        {
            Name = "Force Corruption",
            Slug = "force-corruption",
            Route = "force-powers/force-corruption",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "Taints places, objects, and living beings with concentrated dark-side energy over time, transforming verdant worlds into lifeless wastelands and holocrons into vessels of malevolence. Korriban, Malachor, and Exegol all bear the scars of centuries of Force corruption.",
            Color = "#450a0a",
            Sources = "KOTOR II · The Old Republic · Sith Empire · Films · Rise of Skywalker"
        },
        new()
        {
            Name = "Sith Magic",
            Slug = "sith-magic",
            Route = "force-powers/sith-magic",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "A broad tradition of dark-side rituals practiced by the Sith and their allied cults, encompassing illusions, curses, spirit binding, and the creation of dark-side artifacts. The Sith Eternal on Exegol preserved ancient Sith magic for generations in preparation for the Final Order.",
            Color = "#7c3aed",
            Sources = "Films · The Rise of Skywalker · Clone Wars · The Old Republic · Sith Empire"
        },
        new()
        {
            Name = "Dark Side Tendrils",
            Slug = "dark-side-tendrils",
            Route = "force-powers/dark-side-tendrils",
            Side = ForceSide.Dark,
            Category = "Ritual",
            Difficulty = "Master",
            Description = "Manifests writhing tendrils of pure dark-side energy that erupt from the ground or air to grasp, crush, and drain victims in a display of sorcerous might. The Sith Emperor and powerful Nightsister shamans summoned dark-side tendrils during ritual combat to overwhelm multiple Jedi at once.",
            Color = "#dc2626",
            Sources = "The Old Republic · Sith Empire · Clone Wars · KOTOR II"
        }
    ];

    public static IReadOnlyList<ForcePower> LightSidePowers =>
        Powers.Where(p => p.Side == ForceSide.Light).ToList();

    public static IReadOnlyList<ForcePower> DarkSidePowers =>
        Powers.Where(p => p.Side == ForceSide.Dark).ToList();

    public static ForcePower? GetBySlug(string slug) =>
        Powers.FirstOrDefault(power => power.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
