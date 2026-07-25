using StarWars.Models;

namespace StarWars.Data;

public static class GalaxyData
{
    // Map coordinates use GalaxyMapSettings (8000 x 5000). Place planets with spacing
    // across the galaxy arms — X between 900–7100, Y between 700–4300.
    public static IReadOnlyList<GalaxyPlanet> Planets { get; } =
    [
        new()
        {
            Name = "Ahch-To",
            Slug = "ahch-to",
            Route = "planet/ahch-to",
            Region = "Unknown Regions",
            Description = "A remote ocean world of storm-lashed islands where the first Jedi temple lies hidden.",
            X = 1200,
            Y = 900,
            Color = "#3d6b8a"
        },
        new()
        {
            Name = "Ajan Kloss",
            Slug = "ajan-kloss",
            Route = "planet/ajan-kloss",
            Region = "Outer Rim Territories",
            Description = "A jungle moon in the Ceros system that served as a hidden Resistance base.",
            X = 2200,
            Y = 3200,
            Color = "#2d6b3a"
        },
        new()
        {
            Name = "Alderaan",
            Slug = "alderaan",
            Route = "planet/alderaan",
            Region = "Core Worlds",
            Description = "A peaceful Core world of snow-capped mountains, verdant valleys, and cultured cities.",
            X = 4200,
            Y = 2300,
            Color = "#6aafd4"
        },
        new()
        {
            Name = "Ashas Ree",
            Slug = "ashas-ree",
            Route = "planet/ashas-ree",
            Region = "Sith Space",
            Description = "An ancient Sith tomb world shrouded in dark side energy and crumbling sanctuaries.",
            X = 6800,
            Y = 3900,
            Color = "#5c3a6b"
        },
        new()
        {
            Name = "Atollon",
            Slug = "atollon",
            Route = "planet/atollon",
            Region = "Outer Rim Territories",
            Description = "A remote desert planet of coral mesas where Phoenix Squadron established Chopper Base.",
            X = 1800,
            Y = 2800,
            Color = "#c4956a"
        },
        new()
        {
            Name = "Bespin",
            Slug = "bespin",
            Route = "bespin",
            Region = "Outer Rim Territories",
            Description = "A gas giant famed for Cloud City, floating refineries mining valuable tibanna gas.",
            X = 2720,
            Y = 1580,
            Color = "#e8c88a",
            ImagePath = "/images/bespin-space.webp"
        },
        new()
        {
            Name = "Bracca",
            Slug = "bracca",
            Route = "planet/bracca",
            Region = "Mid Rim",
            Description = "A junkyard world of scrapped starships where Clone Force 99 began their exile.",
            X = 3100,
            Y = 3400,
            Color = "#7a8a7a"
        },
        new()
        {
            Name = "Cantonica",
            Slug = "cantonica",
            Route = "planet/cantonica",
            Region = "Outer Rim Territories",
            Description = "A desert planet whose Canto Bight resort city caters to the galaxy's wealthy elite.",
            X = 5200,
            Y = 4100,
            Color = "#d4a843"
        },
        new()
        {
            Name = "Carida",
            Slug = "carida",
            Route = "planet/carida",
            Region = "Colonies",
            Description = "A Coreward world renowned for its brutal Imperial Academy and military training grounds.",
            X = 4600,
            Y = 2100,
            Color = "#8a9098"
        },
        new()
        {
            Name = "Cato Neimoidia",
            Slug = "cato-neimoidia",
            Route = "planet/cato-neimoidia",
            Region = "Colonies",
            Description = "A wealthy Trade Federation purse world of bridge cities suspended above fungal forests.",
            X = 4300,
            Y = 2000,
            Color = "#9a8a6a"
        },
        new()
        {
            Name = "Christophsis",
            Slug = "christophsis",
            Route = "planet/christophsis",
            Region = "Outer Rim Territories",
            Description = "A crystalline world of green mesas that saw early battles of the Clone Wars.",
            X = 2800,
            Y = 2600,
            Color = "#4a9a6a"
        },
        new()
        {
            Name = "Coruscant",
            Slug = "coruscant",
            Route = "coruscant",
            Region = "Core Worlds",
            Description = "The galactic capital — a planet-wide ecumenopolis at the heart of the Core Worlds.",
            X = 4000,
            Y = 2500,
            Color = "#f4c542",
            ImagePath = "/images/coruscant-space.webp"
        },
        new()
        {
            Name = "Crait",
            Slug = "crait",
            Route = "planet/crait",
            Region = "Outer Rim Territories",
            Description = "A salt-covered mineral planet where the Resistance made its last stand against the First Order.",
            X = 1400,
            Y = 3600,
            Color = "#c44a6a"
        },
        new()
        {
            Name = "D'Qar",
            Slug = "d-qar",
            Route = "planet/d-qar",
            Region = "Outer Rim Territories",
            Description = "A lush planet that served as the primary base of the Resistance during the cold war.",
            X = 1700,
            Y = 3100,
            Color = "#4a8a5a"
        },
        new()
        {
            Name = "Dagobah",
            Slug = "dagobah",
            Route = "planet/dagobah",
            Region = "Outer Rim Territories",
            Description = "A mist-shrouded swamp world where Yoda lived in exile after the fall of the Jedi.",
            X = 2400,
            Y = 4000,
            Color = "#3a5a3a"
        },
        new()
        {
            Name = "Daiyu",
            Slug = "daiyu",
            Route = "planet/daiyu",
            Region = "Outer Rim Territories",
            Description = "A crowded industrial city-planet where Obi-Wan Kenobi searched for the kidnapped Leia.",
            X = 6400,
            Y = 3800,
            Color = "#6a5a4a"
        },
        new()
        {
            Name = "Dantooine",
            Slug = "dantooine",
            Route = "dantooine",
            Region = "Outer Rim Territories",
            Description = "A remote agrarian world in the Outer Rim — quiet plains and scattered settlements.",
            X = 5360,
            Y = 3000,
            Color = "#4a8c5c",
            ImagePath = "/images/dantooine-space.webp"
        },
        new()
        {
            Name = "Dathomir",
            Slug = "dathomir",
            Route = "planet/dathomir",
            Region = "Outer Rim Territories",
            Description = "A foreboding world of red skies and jungles, home to the Nightsisters and dark side cults.",
            X = 5800,
            Y = 2600,
            Color = "#8b2020"
        },
        new()
        {
            Name = "Dromund Kaas",
            Slug = "dromund-kaas",
            Route = "planet/dromund-kaas",
            Region = "Sith Space",
            Description = "The capital of the Old Sith Empire — a storm-wracked jungle world dominated by Kaas City.",
            X = 7000,
            Y = 3500,
            Color = "#2a4a2a"
        },
        new()
        {
            Name = "Endor",
            Slug = "endor",
            Route = "planet/endor",
            Region = "Outer Rim Territories",
            Description = "A forest moon orbiting a gas giant, site of the decisive Battle of Endor.",
            X = 1900,
            Y = 2200,
            Color = "#2d5a2d"
        },
        new()
        {
            Name = "Exegol",
            Slug = "exegol",
            Route = "planet/exegol",
            Region = "Unknown Regions",
            Description = "A hidden Sith world of eternal darkness where Palpatine rebuilt his final fleet.",
            X = 900,
            Y = 1200,
            Color = "#1a1a2a"
        },
        new()
        {
            Name = "Felucia",
            Slug = "felucia",
            Route = "planet/felucia",
            Region = "Outer Rim Territories",
            Description = "A vibrant jungle world of giant fungi and bioluminescent flora teeming with life.",
            X = 3800,
            Y = 3800,
            Color = "#c44a8a"
        },
        new()
        {
            Name = "Ferrix",
            Slug = "ferrix",
            Route = "planet/ferrix",
            Region = "Outer Rim Territories",
            Description = "A grimy industrial planet whose salvage yards and foundries fuel the Imperial war machine.",
            X = 3300,
            Y = 1800,
            Color = "#8a7a6a"
        },
        new()
        {
            Name = "Florrum",
            Slug = "florrum",
            Route = "planet/florrum",
            Region = "Outer Rim Territories",
            Description = "A sulfurous pirate haven of canyons and caverns ruled by Hondo Ohnaka's gang.",
            X = 5500,
            Y = 4000,
            Color = "#b8860b"
        },
        new()
        {
            Name = "Geonosis",
            Slug = "geonosis",
            Route = "planet/geonosis",
            Region = "Outer Rim Territories",
            Description = "A red-rock desert world where the Clone Wars began and the Death Star was first planned.",
            X = 4500,
            Y = 3200,
            Color = "#c4783a"
        },
        new()
        {
            Name = "Hoth",
            Slug = "hoth",
            Route = "hoth",
            Region = "Outer Rim Territories",
            Description = "An icy wasteland of frozen plains, buried in snow and swept by brutal blizzards.",
            X = 1680,
            Y = 1750,
            Color = "#b8d4e8",
            ImagePath = "/images/hoth-space.webp"
        },
        new()
        {
            Name = "Ilum",
            Slug = "ilum",
            Route = "planet/ilum",
            Region = "Unknown Regions",
            Description = "An ice planet sacred to the Jedi Order, source of kyber crystals and later Starkiller Base.",
            X = 1100,
            Y = 2800,
            Color = "#a8d8f0"
        },
        new()
        {
            Name = "Jabiim",
            Slug = "jabiim",
            Route = "planet/jabiim",
            Region = "Outer Rim Territories",
            Description = "A rain-soaked battlefield world scarred by one of the Clone Wars' bloodiest campaigns.",
            X = 6200,
            Y = 3000,
            Color = "#4a6a5a"
        },
        new()
        {
            Name = "Jakku",
            Slug = "jakku",
            Route = "planet/jakku",
            Region = "Western Reaches",
            Description = "A desert world littered with starship graveyards from the Battle of Jakku.",
            X = 1500,
            Y = 4200,
            Color = "#c9a070"
        },
        new()
        {
            Name = "Jedha",
            Slug = "jedha",
            Route = "planet/jedha",
            Region = "Outer Rim Territories",
            Description = "A cold desert moon sacred to believers of the Force and a center of kyber crystal mining.",
            X = 3600,
            Y = 1600,
            Color = "#9a8a7a"
        },
        new()
        {
            Name = "Kamino",
            Slug = "kamino",
            Route = "planet/kamino",
            Region = "Outer Rim Territories",
            Description = "A water world beyond the Outer Rim where clone troopers were engineered in secret.",
            X = 3200,
            Y = 1400,
            Color = "#6ab0d4"
        },
        new()
        {
            Name = "Kashyyyk",
            Slug = "kashyyyk",
            Route = "planet/kashyyyk",
            Region = "Mid Rim",
            Description = "The Wookiee homeworld — towering wroshyr forests spanning a lush jungle planet.",
            X = 3700,
            Y = 2900,
            Color = "#2a6a3a"
        },
        new()
        {
            Name = "Kef Bir",
            Slug = "kef-bir",
            Route = "planet/kef-bir",
            Region = "Outer Rim Territories",
            Description = "An ocean moon of Endor where wreckage of the second Death Star rests on turbulent seas.",
            X = 2100,
            Y = 3800,
            Color = "#4a8aaa"
        },
        new()
        {
            Name = "Kijimi",
            Slug = "kijimi",
            Route = "planet/kijimi",
            Region = "Mid Rim",
            Description = "A snowbound planet whose spice-mining cities harbor scoundrels and Resistance sympathizers.",
            X = 2900,
            Y = 2000,
            Color = "#d0d8e0"
        },
        new()
        {
            Name = "Koboh",
            Slug = "koboh",
            Route = "planet/koboh",
            Region = "Outer Rim Territories",
            Description = "A frontier world of mesas and wetlands explored by Cal Kestis during the Imperial era.",
            X = 4900,
            Y = 1800,
            Color = "#7a9a5a"
        },
        new()
        {
            Name = "Korriban",
            Slug = "korriban",
            Route = "korriban",
            Region = "Outer Rim Territories",
            Description = "The ancient homeworld of the Sith — a desert world of tombs and dark history.",
            X = 6640,
            Y = 2170,
            Color = "#8b1a1a",
            ImagePath = "/images/korriban-space.webp"
        },
        new()
        {
            Name = "Lothal",
            Slug = "lothal",
            Route = "planet/lothal",
            Region = "Outer Rim Territories",
            Description = "An Outer Rim backwater of grassy plains and Imperial occupation, home to Ezra Bridger.",
            X = 2500,
            Y = 1900,
            Color = "#8ab86a"
        },
        new()
        {
            Name = "Malachor",
            Slug = "malachor",
            Route = "planet/malachor",
            Region = "Outer Rim Territories",
            Description = "A Sith wasteland scarred by a superweapon blast that petrified warriors mid-battle.",
            X = 5900,
            Y = 1900,
            Color = "#4a3a3a"
        },
        new()
        {
            Name = "Malachor V",
            Slug = "malachor-v",
            Route = "planet/malachor-v",
            Region = "Outer Rim Territories",
            Description = "A shattered world destroyed by the Mass Shadow Generator during the Mandalorian Wars.",
            X = 6000,
            Y = 4100,
            Color = "#3a2a2a"
        },
        new()
        {
            Name = "Manaan",
            Slug = "manaan",
            Route = "planet/manaan",
            Region = "Inner Rim",
            Description = "An ocean planet governed by the neutral Selkath, sole source of the healing kolto.",
            X = 3500,
            Y = 1700,
            Color = "#4a9ab8"
        },
        new()
        {
            Name = "Mandalore",
            Slug = "mandalore",
            Route = "planet/mandalore",
            Region = "Outer Rim Territories",
            Description = "The ancestral homeworld of the Mandalorians — a war-torn world of domed cities.",
            X = 4200,
            Y = 1700,
            Color = "#5a7a9a"
        },
        new()
        {
            Name = "Mon Cala",
            Slug = "mon-cala",
            Route = "planet/mon-cala",
            Region = "Outer Rim Territories",
            Description = "An ocean world of floating cities and the Mon Calamari, builders of the Rebel fleet.",
            X = 2600,
            Y = 2300,
            Color = "#3a7a9a"
        },
        new()
        {
            Name = "Mustafar",
            Slug = "mustafar",
            Route = "mustafar",
            Region = "Outer Rim Territories",
            Description = "A volcanic hellscape of lava rivers, ash storms, and treacherous mining operations.",
            X = 4720,
            Y = 3750,
            Color = "#c44a1a",
            ImagePath = "/images/mustafar-space.webp"
        },
        new()
        {
            Name = "Mygeeto",
            Slug = "mygeeto",
            Route = "planet/mygeeto",
            Region = "Outer Rim Territories",
            Description = "A crystalline ice world of elegant spires, ravaged during the Outer Rim Sieges.",
            X = 3600,
            Y = 1500,
            Color = "#8ab0c8"
        },
        new()
        {
            Name = "Naboo",
            Slug = "naboo",
            Route = "naboo",
            Region = "Mid Rim",
            Description = "A lush world of rolling plains, great lakes, and elegant cities ruled from Theed.",
            X = 3440,
            Y = 2250,
            Color = "#5a9e8f",
            ImagePath = "/images/naboo-space.webp"
        },
        new()
        {
            Name = "Nar Shaddaa",
            Slug = "nar-shaddaa",
            Route = "planet/nar-shaddaa",
            Region = "Hutt Space",
            Description = "The Smuggler's Moon — a vertical city-world of neon, crime, and endless vice.",
            X = 5100,
            Y = 2200,
            Color = "#c4a020"
        },
        new()
        {
            Name = "Nathema",
            Slug = "nathema",
            Route = "planet/nathema",
            Region = "Sith Space",
            Description = "A lifeless world drained of the Force by the Sith Emperor's ritual of mass extinction.",
            X = 7100,
            Y = 3200,
            Color = "#4a3a4a"
        },
        new()
        {
            Name = "Nevarro",
            Slug = "nevarro",
            Route = "planet/nevarro",
            Region = "Outer Rim Territories",
            Description = "A frontier world of lava rivers and cantinas that served as a Bounty Hunter Guild hub.",
            X = 4400,
            Y = 1400,
            Color = "#8a4a3a"
        },
        new()
        {
            Name = "Onderon",
            Slug = "onderon",
            Route = "planet/onderon",
            Region = "Inner Rim",
            Description = "A jungle world with a walled capital city, torn by civil war during the Clone Wars.",
            X = 3900,
            Y = 3100,
            Color = "#3a7a4a"
        },
        new()
        {
            Name = "Pasaana",
            Slug = "pasaana",
            Route = "planet/pasaana",
            Region = "Outer Rim Territories",
            Description = "A desert festival world of orange sands where the Resistance tracked a Sith wayfinder.",
            X = 4600,
            Y = 4000,
            Color = "#d4883a"
        },
        new()
        {
            Name = "Peridea",
            Slug = "peridea",
            Route = "planet/peridea",
            Region = "Unknown Regions",
            Description = "A distant extragalactic world of dead forests where Grand Admiral Thrawn was exiled.",
            X = 1000,
            Y = 1800,
            Color = "#6a5a4a"
        },
        new()
        {
            Name = "Polis Massa",
            Slug = "polis-massa",
            Route = "planet/polis-massa",
            Region = "Outer Rim Territories",
            Description = "An asteroid archipelago where Padmé Amidala gave birth to Luke and Leia before her death.",
            X = 3000,
            Y = 1200,
            Color = "#9a9aaa"
        },
        new()
        {
            Name = "Rakata Prime",
            Slug = "rakata-prime",
            Route = "planet/rakata-prime",
            Region = "Unknown Regions",
            Description = "The ruined homeworld of the Rakata Infinite Empire, overgrown by jungle and dark side ruins.",
            X = 1300,
            Y = 2400,
            Color = "#2a5a3a"
        },
        new()
        {
            Name = "Raxus",
            Slug = "raxus",
            Route = "planet/raxus",
            Region = "Outer Rim Territories",
            Description = "The capital of the Separatist Alliance, a temperate world of palaces and war councils.",
            X = 4700,
            Y = 2000,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Rishi",
            Slug = "rishi",
            Route = "planet/rishi",
            Region = "Outer Rim Territories",
            Description = "A tropical moon with a critical Republic listening post targeted by Separatist droids.",
            X = 2300,
            Y = 1500,
            Color = "#5a9a6a"
        },
        new()
        {
            Name = "Ryloth",
            Slug = "ryloth",
            Route = "planet/ryloth",
            Region = "Outer Rim Territories",
            Description = "The Twi'lek homeworld — a tidally locked planet of scorching dayside and frozen nightside.",
            X = 3400,
            Y = 2600,
            Color = "#9a6a8a"
        },
        new()
        {
            Name = "Serenno",
            Slug = "serenno",
            Route = "planet/serenno",
            Region = "Outer Rim Territories",
            Description = "An aristocratic world of great houses, seat of Count Dooku's power and wealth.",
            X = 5000,
            Y = 2500,
            Color = "#7a6a8a"
        },
        new()
        {
            Name = "Takodana",
            Slug = "takodana",
            Route = "planet/takodana",
            Region = "Mid Rim",
            Description = "A lake world home to Maz Kanata's ancient castle, a haven for smugglers and travelers.",
            X = 3800,
            Y = 2100,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Taris",
            Slug = "taris",
            Route = "planet/taris",
            Region = "Outer Rim Territories",
            Description = "Once a ecumenopolis rivaling Coruscant, now a ruin overrun by rakghouls after orbital bombardment.",
            X = 5400,
            Y = 1700,
            Color = "#5a6a7a"
        },
        new()
        {
            Name = "Tatooine",
            Slug = "tatooine",
            Route = "tatooine",
            Region = "Outer Rim Territories",
            Description = "A twin-sunned desert world of sand dunes, moisture farms, and frontier outposts.",
            X = 6380,
            Y = 3680,
            Color = "#c9a86c",
            ImagePath = "/images/tatooine-space.webp"
        },
        new()
        {
            Name = "Telos",
            Slug = "telos",
            Route = "planet/telos",
            Region = "Outer Rim Territories",
            Description = "A world devastated by the Sith then rebuilt as the Citadel Station orbital restoration project.",
            X = 5700,
            Y = 3300,
            Color = "#6a8aaa"
        },
        new()
        {
            Name = "Tython",
            Slug = "tython",
            Route = "planet/tython",
            Region = "Deep Core",
            Description = "The birthplace of the Jedi Order, a Force-soaked world of temples and ancient mysteries.",
            X = 4800,
            Y = 2600,
            Color = "#8a9a6a"
        },
        new()
        {
            Name = "Umbara",
            Slug = "umbara",
            Route = "planet/umbara",
            Region = "Expansion Region",
            Description = "The Shadow World — a perpetually dark planet of bioluminescent fungi and xenophobic natives.",
            X = 3300,
            Y = 3000,
            Color = "#4a3a6a"
        },
        new()
        {
            Name = "Utapau",
            Slug = "utapau",
            Route = "planet/utapau",
            Region = "Outer Rim Territories",
            Description = "A sinkhole world of wind-carved cities where General Grievous was tracked and destroyed.",
            X = 4100,
            Y = 3400,
            Color = "#a89070"
        },
        new()
        {
            Name = "Yavin 4",
            Slug = "yavin-4",
            Route = "planet/yavin-4",
            Region = "Outer Rim Territories",
            Description = "A jungle moon orbiting the gas giant Yavin Prime, site of the Rebel Alliance's great victory.",
            X = 2000,
            Y = 2600,
            Color = "#2a6a3a"
        },
        new()
        {
            Name = "Ziost",
            Slug = "ziost",
            Route = "planet/ziost",
            Region = "Sith Space",
            Description = "An ancient frozen Sith world and former capital of the Old Sith Empire before Dromund Kaas.",
            X = 6900,
            Y = 2800,
            Color = "#6a8ab0"
        }
    ];

    public static GalaxyPlanet? GetBySlug(string slug) =>
        Planets.FirstOrDefault(planet => planet.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
