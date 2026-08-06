using StarWars.Models;

namespace StarWars.Data;

public static class CreatureData
{
    public static IReadOnlyList<Creature> Creatures { get; } =
    [
        new()
        {
            Name = "Rancor",
            Slug = "rancor",
            Route = "creatures/rancor",
            Habitat = "Jungle & Forest",
            Homeworld = "Dathomir",
            Description = "Towering carnivores kept as pit beasts by Hutt crime lords, rancors combine brute strength with surprising agility in enclosed arenas.",
            Color = "#78350f",
        },
        new()
        {
            Name = "Wampa",
            Slug = "wampa",
            Route = "creatures/wampa",
            Habitat = "Arctic & Tundra",
            Homeworld = "Hoth",
            Description = "White-furred ice predators that ambush prey from snow caves; Luke Skywalker barely escaped one's lair after a patrol on Hoth.",
            Color = "#e2e8f0",
        },
        new()
        {
            Name = "Sarlacc",
            Slug = "sarlacc",
            Route = "creatures/sarlacc",
            Habitat = "Desert & Arid",
            Homeworld = "Tatooine",
            Description = "Immense subterranean predators whose Great Pit of Carkoon digests victims over centuries while anchoring Hutt execution rituals.",
            Color = "#a16207",
        },
        new()
        {
            Name = "Krayt Dragon",
            Slug = "krayt-dragon",
            Route = "creatures/krayt-dragon",
            Habitat = "Desert & Arid",
            Homeworld = "Tatooine",
            Description = "Colossal desert dragons whose pearl hoards and armored hides make them apex predators of the Dune Sea; pearl variants are exceedingly rare.",
            Color = "#ca8a04",
        },
        new()
        {
            Name = "Purrgil",
            Slug = "purrgil",
            Route = "creatures/purrgil",
            Habitat = "Space & Vacuum",
            Homeworld = "Unknown Regions",
            Description = "Hyperspace-navigating space whales whose natural routes inspired early hyperdrive mappers and whom Ezra Bridger communed with in the Unknown Regions.",
            Color = "#6366f1",
        },
        new()
        {
            Name = "Loth-Cat",
            Slug = "loth-cat",
            Route = "creatures/loth-cat",
            Habitat = "Grassland & Plains",
            Homeworld = "Lothal",
            Description = "Small feline hunters of Lothal's grasslands whose twitching ears and striped coats make them beloved—and occasionally Force-attuned—companions.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Loth-Wolf",
            Slug = "loth-wolf",
            Route = "creatures/loth-wolf",
            Habitat = "Grassland & Plains",
            Homeworld = "Lothal",
            Description = "Mystic wolves tied to Lothal's vergence who guided Ezra through the World Between Worlds and embodied the planet's Living Force.",
            Color = "#64748b",
        },
        new()
        {
            Name = "Convor",
            Slug = "convor",
            Route = "creatures/convor",
            Habitat = "Grassland & Plains",
            Homeworld = "Lothal",
            Description = "Owl-like birds linked to the Daughter of Mortis; Morai shadowed Ahsoka Tano as a symbol of the light side across the galaxy.",
            Color = "#22c55e",
        },
        new()
        {
            Name = "Zillo Beast",
            Slug = "zillo-beast",
            Route = "creatures/zillo-beast",
            Habitat = "Grassland & Plains",
            Homeworld = "Malastare",
            Description = "Ancient armored titan whose impenetrable plates resisted Republic artillery; Palpatine ordered cloning research before the original perished on Coruscant.",
            Color = "#84cc16",
        },
        new()
        {
            Name = "Nexu",
            Slug = "nexu",
            Route = "creatures/nexu",
            Habitat = "Jungle & Forest",
            Homeworld = "Cholganna",
            Description = "Quadruped arena killers with quilled backs and leaping strikes, deployed in Geonosis gladiatorial executions during the Clone Wars.",
            Color = "#b45309",
        },
        new()
        {
            Name = "Reek",
            Slug = "reek",
            Route = "creatures/reek",
            Habitat = "Jungle & Forest",
            Homeworld = "Ylesia",
            Description = "Horned charging beasts drugged for arena combat; one famously gored Jango Fett before Anakin Skywalker rode it in the Geonosis arena.",
            Color = "#92400e",
        },
        new()
        {
            Name = "Acklay",
            Slug = "acklay",
            Route = "creatures/acklay",
            Habitat = "Jungle & Forest",
            Homeworld = "Vendaxa",
            Description = "Three-legged crustacean predators with piercing forelimbs, unleashed against Jedi prisoners in the Petranaki arena on Geonosis.",
            Color = "#14b8a6",
        },
        new()
        {
            Name = "Tauntaun",
            Slug = "tauntaun",
            Route = "creatures/tauntaun",
            Habitat = "Arctic & Tundra",
            Homeworld = "Hoth",
            Description = "Reptomammal pack animals whose musk and warmth sustained Rebel patrols until nighttime freezes drove them back to Echo Base.",
            Color = "#cbd5e1",
        },
        new()
        {
            Name = "Dewback",
            Slug = "dewback",
            Route = "creatures/dewback",
            Habitat = "Desert & Arid",
            Homeworld = "Tatooine",
            Description = "Thick-skinned desert mounts used by Imperial sandtroopers and moisture farmers to cross Tatooine's scorching wastes at dawn.",
            Color = "#65a30d",
        },
        new()
        {
            Name = "Bantha",
            Slug = "bantha",
            Route = "creatures/bantha",
            Habitat = "Desert & Arid",
            Homeworld = "Tatooine",
            Description = "Shaggy herd giants whose milk, hides, and tusks sustain Tusken Raider clans across the Jundland Wastes.",
            Color = "#78716c",
        },
        new()
        {
            Name = "Rathtar",
            Slug = "rathtar",
            Route = "creatures/rathtar",
            Habitat = "Ocean & Aquatic",
            Homeworld = "Unknown",
            Description = "Tentacled carnivores prized by collectors for their lethality; Han Solo's freighter haul of rathtars endangered the Irving Boys on the Eravana.",
            Color = "#ec4899",
        },
        new()
        {
            Name = "Fyrnock",
            Slug = "fyrnock",
            Route = "creatures/fyrnock",
            Habitat = "Urban & Industrial",
            Homeworld = "Anaxes",
            Description = "Shadow-dwelling pack hunters that swarm under artificial light thresholds; Clone Wars garrisons learned to seal blast doors before nightfall.",
            Color = "#475569",
        },
        new()
        {
            Name = "Krykna",
            Slug = "krykna",
            Route = "creatures/krykna",
            Habitat = "Jungle & Forest",
            Homeworld = "Atollon",
            Description = "Acid-spitting spider predators immune to blaster fire whose nests forced Phoenix Squadron to abandon Chopper Base on Atollon.",
            Color = "#334155",
        },
        new()
        {
            Name = "Mudhorn",
            Slug = "mudhorn",
            Route = "creatures/mudhorn",
            Habitat = "Swamp & Wetlands",
            Homeworld = "Arvala-7",
            Description = "Horned marsh dwellers whose armored skulls and mud-caked hides challenged Din Djarin during his quest to protect Grogu.",
            Color = "#57534e",
        },
        new()
        {
            Name = "Blurrg",
            Slug = "blurrg",
            Route = "creatures/blurrg",
            Habitat = "Arctic & Tundra",
            Homeworld = "Ryloth",
            Description = "Two-legged riding beasts with snapping jaws, used by Twi'lek freedom fighters and Mandalorian clans on frontier worlds.",
            Color = "#a855f7",
        },
        new()
        {
            Name = "Varactyl",
            Slug = "varactyl",
            Route = "creatures/varactyl",
            Habitat = "Mountain & Highland",
            Homeworld = "Utapau",
            Description = "Colorful reptavian mounts prized for sure-footed cliff climbing; Obi-Wan Kenobi rode Boga across Utapau's sinkhole chasms hunting Grievous.",
            Color = "#059669",
        },
        new()
        {
            Name = "Exogorth",
            Slug = "exogorth",
            Route = "creatures/exogorth",
            Habitat = "Space & Vacuum",
            Homeworld = "Asteroid fields",
            Description = "Colossal space slugs that burrow into asteroids and swallow starships whole; Han Solo narrowly escaped one in the Hoth asteroid belt.",
            Color = "#7c2d12",
        },
        new()
        {
            Name = "Mynock",
            Slug = "mynock",
            Route = "creatures/mynock",
            Habitat = "Space & Vacuum",
            Homeworld = "Ord Mantell",
            Description = "Silicon-based parasites that feed on starship power cables and hull plating, infesting freighters from Ord Mantell to deep-space junkyards.",
            Color = "#6b7280",
        },
        new()
        {
            Name = "Colo Claw Fish",
            Slug = "colo-claw-fish",
            Route = "creatures/colo-claw-fish",
            Habitat = "Ocean & Aquatic",
            Homeworld = "Naboo",
            Description = "Bioluminescent abyss predators with luring head-spines that patrol the Naboo ocean depths beneath the Gungan city of Otoh Gunga.",
            Color = "#0284c7",
        },
        new()
        {
            Name = "Sando Aqua Monster",
            Slug = "sando-aqua-monster",
            Route = "creatures/sando-aqua-monster",
            Habitat = "Ocean & Aquatic",
            Homeworld = "Naboo",
            Description = "Titanic leviathan of Naboo's core lakes whose jaws dwarfed Trade Federation submersibles during the planetary invasion.",
            Color = "#0ea5e9",
        },
        new()
        {
            Name = "Opee Sea Killer",
            Slug = "opee-sea-killer",
            Route = "creatures/opee-sea-killer",
            Habitat = "Ocean & Aquatic",
            Homeworld = "Naboo",
            Description = "Chitinous ambush predator with extensible tongue-lure that hunts the Naboo abyssal zones beneath Gungan hydrostatic shields.",
            Color = "#f59e0b",
        },
        new()
        {
            Name = "Aiwha",
            Slug = "aiwha",
            Route = "creatures/aiwha",
            Habitat = "Ocean & Aquatic",
            Homeworld = "Kamino",
            Description = "Winged cetaceans that skim Kamino's endless oceans in pods, their calls echoing across the storm-swept platform cities.",
            Color = "#38bdf8",
        },
        new()
        {
            Name = "Bogling",
            Slug = "bogling",
            Route = "creatures/bogling",
            Habitat = "Swamp & Wetlands",
            Homeworld = "Various",
            Description = "Small swamp scavengers with oversized ears that nest in rotting marsh timber and startle travelers on Dagobah-like worlds.",
            Color = "#4ade80",
        },
        new()
        {
            Name = "Steelpecker",
            Slug = "steelpecker",
            Route = "creatures/steelpecker",
            Habitat = "Urban & Industrial",
            Homeworld = "Jakku",
            Description = "Metallophagic birds whose razor beaks strip wrecked Star Destroyer hulls on Jakku, nesting in the ribs of downed warships.",
            Color = "#94a3b8",
        },
        new()
        {
            Name = "Dark Side Spiders",
            Slug = "dark-side-spiders",
            Route = "creatures/dark-side-spiders",
            Habitat = "Dark Side & Exotic",
            Homeworld = "Malachor",
            Description = "Sith-temple arachnids warped by the dark side whose crystalline legs and hunger for Force-sensitive prey haunt Malachor's ruins.",
            Color = "#581c87",
        },
        new()
        {
            Name = "Charhound",
            Slug = "charhound",
            Route = "creatures/charhound",
            Habitat = "Volcanic & Wasteland",
            Homeworld = "Elphrona",
            Description = "Ash-coated pack hunters adapted to high-temperature wastelands, tracking prey across scorched plains with ember-glow eyes.",
            Color = "#ef4444",
        },
        new()
        {
            Name = "Roggwart",
            Slug = "roggwart",
            Route = "creatures/roggwart",
            Habitat = "Jungle & Forest",
            Homeworld = "Various",
            Description = "Horned ape-like brutes with prehensile tails, often chained as guard beasts in Hutt palaces and Separatist fortresses.",
            Color = "#713f12",
        },
        new()
        {
            Name = "Gundark",
            Slug = "gundark",
            Route = "creatures/gundark",
            Habitat = "Jungle & Forest",
            Homeworld = "Gundar",
            Description = "Aggressive primate predators whose immense strength and temper make them among the most feared jungle hunters in the Outer Rim.",
            Color = "#44403c",
        },
        new()
        {
            Name = "Wyyyschokk",
            Slug = "wyyyschokk",
            Route = "creatures/wyyyschokk",
            Habitat = "Jungle & Forest",
            Homeworld = "Kashyyyk",
            Description = "Massive Kashyyyk tree spiders whose webbed high-canopy lairs threaten Wookiee climbers and Clone Wars patrols alike.",
            Color = "#166534",
        },
        new()
        {
            Name = "Vornskr",
            Slug = "vornskr",
            Route = "creatures/vornskr",
            Habitat = "Jungle & Forest",
            Homeworld = "Myrkr",
            Description = "Force-sensitive hunting hounds that track Jedi by scent; Talon Karrde's vornskrs became legendary trackers during the Thrawn campaigns.",
            Color = "#854d0e",
        },
        new()
        {
            Name = "Tusk Cat",
            Slug = "tusk-cat",
            Route = "creatures/tusk-cat",
            Habitat = "Grassland & Plains",
            Homeworld = "Naboo",
            Description = "Saber-tusked felines that stalk Naboo's rolling plains and were domesticated for Gungan ceremonial hunts.",
            Color = "#eab308",
        },
        new()
        {
            Name = "Nuna",
            Slug = "nuna",
            Route = "creatures/nuna",
            Habitat = "Grassland & Plains",
            Homeworld = "Naboo",
            Description = "Plump flightless birds farmed across Naboo for meat and sport; their awkward waddling belies surprising sprint speed.",
            Color = "#16a34a",
        },
        new()
        {
            Name = "Falumpaset",
            Slug = "falumpaset",
            Route = "creatures/falumpaset",
            Habitat = "Swamp & Wetlands",
            Homeworld = "Naboo",
            Description = "Heavy swamp pachyderms used by Gungan armies as living siege engines, their thick hides shrugging off blaster fire.",
            Color = "#0d9488",
        },
        new()
        {
            Name = "Kaadu",
            Slug = "kaadu",
            Route = "creatures/kaadu",
            Habitat = "Swamp & Wetlands",
            Homeworld = "Naboo",
            Description = "Fast amphibious mounts ridden by Gungan cavalry through Naboo's swamps during the Battle of the Great Grass Plains.",
            Color = "#0891b2",
        },
        new()
        {
            Name = "Ronto",
            Slug = "ronto",
            Route = "creatures/ronto",
            Habitat = "Desert & Arid",
            Homeworld = "Tatooine",
            Description = "Large desert herbivores with broad backs used as caravan beasts between Mos Eisley and outlying moisture farms.",
            Color = "#d97706",
        },
        new()
        {
            Name = "Happabore",
            Slug = "happabore",
            Route = "creatures/happabore",
            Habitat = "Desert & Arid",
            Homeworld = "Jakku",
            Description = "Docile desert draught animals whose broad snouts and armored hides suit hauling salvage across Jakku's sun-baked flats.",
            Color = "#fb923c",
        },
        new()
        {
            Name = "Eopie",
            Slug = "eopie",
            Route = "creatures/eopie",
            Habitat = "Desert & Arid",
            Homeworld = "Tatooine",
            Description = "Long-legged pack beasts favored by Jawa traders for hauling scavenged droid parts across the Dune Sea.",
            Color = "#fbbf24",
        },
        new()
        {
            Name = "Dianoga",
            Slug = "dianoga",
            Route = "creatures/dianoga",
            Habitat = "Urban & Industrial",
            Homeworld = "Vodran",
            Description = "One-eyed sewer predators that infest garbage compactors and drainage systems; one nearly drowned Luke Skywalker aboard the first Death Star.",
            Color = "#15803d",
        },
        new()
        {
            Name = "Kowakian Monkey-Lizard",
            Slug = "kowakian-monkey-lizard",
            Route = "creatures/kowakian-monkey-lizard",
            Habitat = "Island & Coastal",
            Homeworld = "Kowak",
            Description = "Cackling reptavian pests whose shrieking mimicry amused Jabba the Hutt and tormented Salacious B. Crumb's rivals in the palace court.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "Porg",
            Slug = "porg",
            Route = "creatures/porg",
            Habitat = "Island & Coastal",
            Homeworld = "Ahch-To",
            Description = "Wide-eyed seabirds that overrun Jedi temple islands on Ahch-To, nesting in every cliff crevice after the Luke's exile years.",
            Color = "#78350f",
        },
        new()
        {
            Name = "Vulptex",
            Slug = "vulptex",
            Route = "creatures/vulptex",
            Habitat = "Crystal & Mineral",
            Homeworld = "Crait",
            Description = "Crystal-furred foxes whose luminous coats refract light through Crait's salt-crystal caverns, guiding Resistance survivors to hidden exits.",
            Color = "#f472b6",
        },
        new()
        {
            Name = "Tooka Cat",
            Slug = "tooka-cat",
            Route = "creatures/tooka-cat",
            Habitat = "Urban & Industrial",
            Homeworld = "Lothal",
            Description = "Common domestic felines sold as pets across the galaxy; Lothal's tooka dolls became iconic children's toys during the Imperial occupation.",
            Color = "#f97316",
        },
        new()
        {
            Name = "Loth-Bat",
            Slug = "loth-bat",
            Route = "creatures/loth-bat",
            Habitat = "Grassland & Plains",
            Homeworld = "Lothal",
            Description = "Nocturnal Lothal flyers whose echolocation squeaks fill the grasslands after dusk, roosting in cliffside colonies near mining settlements.",
            Color = "#312e81",
        },
        new()
        {
            Name = "Ice Spider",
            Slug = "ice-spider",
            Route = "creatures/ice-spider",
            Habitat = "Arctic & Tundra",
            Homeworld = "Ilum",
            Description = "Frozen-tunnel arachnids that nest in Ilum's crystal caves, their frost-coated legs clicking across ice shelves near Jedi harvesting sites.",
            Color = "#bae6fd",
        },
    ];

    public static Creature? GetBySlug(string slug) =>
        Creatures.FirstOrDefault(creature => creature.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));

    public static IReadOnlyList<Creature> GetByHabitat(string habitat) =>
        Creatures.Where(creature => creature.Habitat.Equals(habitat, StringComparison.OrdinalIgnoreCase))
            .OrderBy(creature => creature.Name)
            .ToList();

    public static IReadOnlyList<string> Habitats { get; } =
        Creatures.Select(creature => creature.Habitat)
            .Distinct(StringComparer.OrdinalIgnoreCase)
            .OrderBy(habitat => habitat, StringComparer.OrdinalIgnoreCase)
            .ToList();
}
