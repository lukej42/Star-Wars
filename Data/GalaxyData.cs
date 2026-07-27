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
,
        new()
        {
            Name = "Abednedo",
            Slug = "abednedo",
            Route = "planet/abednedo",
            Region = "Outer Rim Territories",
            Description = "Abednedo is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2522,
            Y = 2416,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Aldhani",
            Slug = "aldhani",
            Route = "planet/aldhani",
            Region = "Outer Rim Territories",
            Description = "A rugged alpine world of Rebel heist operations against Imperial payroll shipments.",
            X = 2799,
            Y = 2387,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Aleena",
            Slug = "aleena",
            Route = "planet/aleena",
            Region = "Outer Rim Territories",
            Description = "Aleena is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1529,
            Y = 1631,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Alpheridies",
            Slug = "alpheridies",
            Route = "planet/alpheridies",
            Region = "Outer Rim Territories",
            Description = "Alpheridies is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2247,
            Y = 3786,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Althir",
            Slug = "althir",
            Route = "planet/althir",
            Region = "Outer Rim Territories",
            Description = "An Outer Rim world contested during the Mandalorian Wars between Neo-Crusaders and Republic.",
            X = 1709,
            Y = 2143,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ando",
            Slug = "ando",
            Route = "planet/ando",
            Region = "Outer Rim Territories",
            Description = "Ando is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 3136,
            Y = 1907,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Anzat",
            Slug = "anzat",
            Route = "planet/anzat",
            Region = "Outer Rim Territories",
            Description = "Anzat is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2634,
            Y = 1889,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Atzerri",
            Slug = "atzerri",
            Route = "planet/atzerri",
            Region = "Outer Rim Territories",
            Description = "A trade world of sprawling markets and black-market technology stalls.",
            X = 2630,
            Y = 3950,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Bakura",
            Slug = "bakura",
            Route = "planet/bakura",
            Region = "Outer Rim Territories",
            Description = "An Outer Rim world invaded by the Ssi-ruuk during the Imperial era.",
            X = 1215,
            Y = 3945,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Balmorra",
            Slug = "balmorra",
            Route = "planet/balmorra",
            Region = "Outer Rim Territories",
            Description = "An industrial factory world of foundries and war forges contested across the Great Galactic War.",
            X = 2286,
            Y = 4148,
            Color = "#7a8a9a"
        },
        new()
        {
            Name = "Balosar",
            Slug = "balosar",
            Route = "planet/balosar",
            Region = "Outer Rim Territories",
            Description = "Balosar is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1614,
            Y = 3339,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Barab I",
            Slug = "barab-i",
            Route = "planet/barab-i",
            Region = "Outer Rim Territories",
            Description = "Barab I is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1028,
            Y = 3592,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bastion",
            Slug = "bastion",
            Route = "planet/bastion",
            Region = "Outer Rim Territories",
            Description = "Bastion is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2929,
            Y = 2781,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Batuu",
            Slug = "batuu",
            Route = "planet/batuu",
            Region = "Outer Rim Territories",
            Description = "A remote Outer Rim trading outpost on the edge of Wild Space, home to Black Spire Outpost.",
            X = 1380,
            Y = 2952,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Bestoon",
            Slug = "bestoon",
            Route = "planet/bestoon",
            Region = "Outer Rim Territories",
            Description = "Bestoon is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1493,
            Y = 3527,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Bilbringi",
            Slug = "bilbringi",
            Route = "planet/bilbringi",
            Region = "Core Worlds",
            Description = "A shipyard world near Bothawui that became a New Republic strategic prize after Endor.",
            X = 4456,
            Y = 2416,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bothawui",
            Slug = "bothawui",
            Route = "planet/bothawui",
            Region = "Mid Rim Territories",
            Description = "A Mid Rim intelligence hub homeworld of the Bothan spynet that tracked the second Death Star.",
            X = 2293,
            Y = 2202,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Byss",
            Slug = "byss",
            Route = "planet/byss",
            Region = "Deep Core",
            Description = "Byss is a deep core world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 5166,
            Y = 2710,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Cadomai",
            Slug = "cadomai",
            Route = "planet/cadomai",
            Region = "Outer Rim Territories",
            Description = "Cadomai is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2591,
            Y = 4038,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Cadomai Prime",
            Slug = "cadomai-prime",
            Route = "planet/cadomai-prime",
            Region = "Outer Rim Territories",
            Description = "Cadomai Prime is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2751,
            Y = 1740,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Castell",
            Slug = "castell",
            Route = "planet/castell",
            Region = "Outer Rim Territories",
            Description = "A urban colony world of the Colicoid species and droid manufacturing.",
            X = 1844,
            Y = 3160,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Cathar",
            Slug = "cathar",
            Route = "planet/cathar",
            Region = "Outer Rim Territories",
            Description = "The homeworld of the Cathar species, scarred by Mandalorian orbital bombardment in ancient wars.",
            X = 1806,
            Y = 2292,
            Color = "#c87840"
        },
        new()
        {
            Name = "Cerea",
            Slug = "cerea",
            Route = "planet/cerea",
            Region = "Outer Rim Territories",
            Description = "Cerea is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2759,
            Y = 2656,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Chaasadai",
            Slug = "chaasadai",
            Route = "planet/chaasadai",
            Region = "Outer Rim Territories",
            Description = "Chaasadai is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1147,
            Y = 2420,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Chalacta",
            Slug = "chalacta",
            Route = "planet/chalacta",
            Region = "Outer Rim Territories",
            Description = "Chalacta is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1299,
            Y = 3850,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Champala",
            Slug = "champala",
            Route = "planet/champala",
            Region = "Outer Rim Territories",
            Description = "Champala is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1272,
            Y = 2035,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Chandrila",
            Slug = "chandrila",
            Route = "planet/chandrila",
            Region = "Core Worlds",
            Description = "A green Core world of rolling hills and coastal cities that hosted the first restored Galactic Senate after Endor.",
            X = 4997,
            Y = 2188,
            Color = "#5a9a6a"
        },
        new()
        {
            Name = "Chorin",
            Slug = "chorin",
            Route = "planet/chorin",
            Region = "Outer Rim Territories",
            Description = "Chorin is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1065,
            Y = 1399,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Clak'dor VII",
            Slug = "clakdor-vii",
            Route = "planet/clakdor-vii",
            Region = "Outer Rim Territories",
            Description = "Clak'dor VII is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1059,
            Y = 3107,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Colla IV",
            Slug = "colla-iv",
            Route = "planet/colla-iv",
            Region = "Outer Rim Territories",
            Description = "Colla IV is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2885,
            Y = 1330,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Cona",
            Slug = "cona",
            Route = "planet/cona",
            Region = "Outer Rim Territories",
            Description = "Cona is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2012,
            Y = 3517,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Concord Dawn",
            Slug = "concord-dawn",
            Route = "planet/concord-dawn",
            Region = "Outer Rim Territories",
            Description = "A Mandalorian colony world of Journeyman Protectors and beskar traditions.",
            X = 2317,
            Y = 2556,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Corbos",
            Slug = "corbos",
            Route = "planet/corbos",
            Region = "Outer Rim Territories",
            Description = "A mining colony world where lost Jedi children were discovered in ancient ruins.",
            X = 3044,
            Y = 3610,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Corellia",
            Slug = "corellia",
            Route = "planet/corellia",
            Region = "Core Worlds",
            Description = "A Core shipyard world famed for Corellian Engineering Corporation freighters, fighters, and smuggler culture.",
            X = 4554,
            Y = 2086,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Csilla",
            Slug = "csilla",
            Route = "planet/csilla",
            Region = "Unknown Regions",
            Description = "A frozen Chiss Ascendancy homeworld in the Unknown Regions with underground hive cities.",
            X = 1290,
            Y = 741,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Devaron",
            Slug = "devaron",
            Route = "planet/devaron",
            Region = "Outer Rim Territories",
            Description = "Devaron is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1637,
            Y = 1355,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Dorin",
            Slug = "dorin",
            Route = "planet/dorin",
            Region = "Outer Rim Territories",
            Description = "Dorin is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1105,
            Y = 3854,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Duro",
            Slug = "duro",
            Route = "planet/duro",
            Region = "Outer Rim Territories",
            Description = "Duro is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1889,
            Y = 3834,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Dxun",
            Slug = "dxun",
            Route = "planet/dxun",
            Region = "Outer Rim Territories",
            Description = "A jungle moon of Onderon infested with vicious beasts and used as a Mandalorian staging ground.",
            X = 2022,
            Y = 2210,
            Color = "#4a6a3a"
        },
        new()
        {
            Name = "Eadu",
            Slug = "eadu",
            Route = "planet/eadu",
            Region = "Outer Rim Territories",
            Description = "A storm-lashed research world housing Imperial kyber weapon research facilities.",
            X = 2023,
            Y = 3296,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Elom",
            Slug = "elom",
            Route = "planet/elom",
            Region = "Outer Rim Territories",
            Description = "Elom is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1415,
            Y = 3929,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Eshan",
            Slug = "eshan",
            Route = "planet/eshan",
            Region = "Outer Rim Territories",
            Description = "Eshan is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2796,
            Y = 2814,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Falleen",
            Slug = "falleen",
            Route = "planet/falleen",
            Region = "Outer Rim Territories",
            Description = "Falleen is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1692,
            Y = 3252,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Fondor",
            Slug = "fondor",
            Route = "planet/fondor",
            Region = "Core Worlds",
            Description = "A Core engineering world of massive orbital shipyards and supercarrier construction docks.",
            X = 4683,
            Y = 2243,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Gamorr",
            Slug = "gamorr",
            Route = "planet/gamorr",
            Region = "Outer Rim Territories",
            Description = "Gamorr is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2873,
            Y = 1914,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Gand",
            Slug = "gand",
            Route = "planet/gand",
            Region = "Outer Rim Territories",
            Description = "Gand is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1873,
            Y = 1907,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Garel",
            Slug = "garel",
            Route = "planet/garel",
            Region = "Outer Rim Territories",
            Description = "A rocky Outer Rim world with multiple moons used as a Rebel supply hub in the early rebellion.",
            X = 1993,
            Y = 1756,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Gentes",
            Slug = "gentes",
            Route = "planet/gentes",
            Region = "Outer Rim Territories",
            Description = "Gentes is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2802,
            Y = 2190,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Glee Anselm",
            Slug = "glee-anselm",
            Route = "planet/glee-anselm",
            Region = "Outer Rim Territories",
            Description = "Glee Anselm is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1956,
            Y = 2079,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Honoghr",
            Slug = "honoghr",
            Route = "planet/honoghr",
            Region = "Outer Rim Territories",
            Description = "A devastated homeworld of the Noghri, poisoned by Imperial chemical warfare.",
            X = 2315,
            Y = 1657,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Hosnian Prime",
            Slug = "hosnian-prime",
            Route = "planet/hosnian-prime",
            Region = "Core Worlds",
            Description = "The Core capital of the New Republic Senate, destroyed by Starkiller Base's superlaser in 34 ABY.",
            X = 4874,
            Y = 2034,
            Color = "#4a8ab8"
        },
        new()
        {
            Name = "Iktotch",
            Slug = "iktotch",
            Route = "planet/iktotch",
            Region = "Outer Rim Territories",
            Description = "Iktotch is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1615,
            Y = 1220,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Iridonia",
            Slug = "iridonia",
            Route = "planet/iridonia",
            Region = "Outer Rim Territories",
            Description = "Iridonia is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2439,
            Y = 3633,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Ithor",
            Slug = "ithor",
            Route = "planet/ithor",
            Region = "Outer Rim Territories",
            Description = "Ithor is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1802,
            Y = 3225,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kafrene",
            Slug = "kafrene",
            Route = "planet/kafrene",
            Region = "Outer Rim Territories",
            Description = "A mining colony in the Ring of Kafrene where Bodhi Rook met Galen Erso's messenger.",
            X = 2914,
            Y = 3966,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kalee",
            Slug = "kalee",
            Route = "planet/kalee",
            Region = "Outer Rim Territories",
            Description = "Kalee is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2390,
            Y = 1581,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kalevala",
            Slug = "kalevala",
            Route = "planet/kalevala",
            Region = "Outer Rim Territories",
            Description = "An ocean moon of Mandalore famed for Kryze royal estates and shipyards.",
            X = 2934,
            Y = 3921,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kamino (clone origin)",
            Slug = "kamino-clone-origin",
            Route = "planet/kamino-clone-origin",
            Region = "Outer Rim Territories",
            Description = "Kamino (clone origin) is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1377,
            Y = 1227,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kaon",
            Slug = "kaon",
            Route = "planet/kaon",
            Region = "Outer Rim Territories",
            Description = "A Sith industrial world of weapons factories and siege lines during the Great Galactic War.",
            X = 1010,
            Y = 3257,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kemplex IX",
            Slug = "kemplex-nine",
            Route = "planet/kemplex-nine",
            Region = "Sith Space",
            Description = "A Deep Core astronomical anomaly destroyed when ancient Sith superweapons detonated during the Great Sith War.",
            X = 7030,
            Y = 3709,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kessel",
            Slug = "kessel",
            Route = "planet/kessel",
            Region = "Outer Rim Territories",
            Description = "An Outer Rim spice-mining world of harsh conditions, glimmering maelstrom approaches, and Pyke syndicate control.",
            X = 1455,
            Y = 1447,
            Color = "#c45a20"
        },
        new()
        {
            Name = "Kiffex",
            Slug = "kiffex",
            Route = "planet/kiffex",
            Region = "Outer Rim Territories",
            Description = "Kiffex is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2719,
            Y = 3846,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kintan",
            Slug = "kintan",
            Route = "planet/kintan",
            Region = "Outer Rim Territories",
            Description = "Kintan is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2135,
            Y = 2465,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kinyen",
            Slug = "kinyen",
            Route = "planet/kinyen",
            Region = "Outer Rim Territories",
            Description = "Kinyen is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2511,
            Y = 2435,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Klatooine",
            Slug = "klatooine",
            Route = "planet/klatooine",
            Region = "Outer Rim Territories",
            Description = "Klatooine is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1583,
            Y = 2435,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Krownest",
            Slug = "krownest",
            Route = "planet/krownest",
            Region = "Outer Rim Territories",
            Description = "A snowy Mandalorian world of Clan Wren fortresses and beskar mines.",
            X = 1618,
            Y = 2950,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kuat",
            Slug = "kuat",
            Route = "planet/kuat",
            Region = "Core Worlds",
            Description = "A Core shipyard world whose orbital rings built Star Destroyers for every galactic regime.",
            X = 4943,
            Y = 2719,
            Color = "#7a8aaa"
        },
        new()
        {
            Name = "Kubindi",
            Slug = "kubindi",
            Route = "planet/kubindi",
            Region = "Outer Rim Territories",
            Description = "Kubindi is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1794,
            Y = 3297,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Lah'mu",
            Slug = "lahmu",
            Route = "planet/lahmu",
            Region = "Outer Rim Territories",
            Description = "A remote ocean-edged world where the Erso family hid from the Empire before Rogue One.",
            X = 2402,
            Y = 2609,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Lannik",
            Slug = "lannik",
            Route = "planet/lannik",
            Region = "Outer Rim Territories",
            Description = "Lannik is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1598,
            Y = 1775,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Lehon",
            Slug = "lehon",
            Route = "planet/lehon",
            Region = "Unknown Regions",
            Description = "The Rakata homeworld of the Infinite Empire, known as the Unknown World in KOTOR.",
            X = 855,
            Y = 1002,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "L'huguen'ok",
            Slug = "lhuguenok",
            Route = "planet/lhuguenok",
            Region = "Outer Rim Territories",
            Description = "L'huguen'ok is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1908,
            Y = 1686,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Lianna",
            Slug = "lianna",
            Route = "planet/lianna",
            Region = "Outer Rim Territories",
            Description = "Lianna is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2792,
            Y = 1604,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lira San",
            Slug = "lira-san",
            Route = "planet/lira-san",
            Region = "Outer Rim Territories",
            Description = "Lira San is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1467,
            Y = 3208,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Lorrd",
            Slug = "lorrd",
            Route = "planet/lorrd",
            Region = "Outer Rim Territories",
            Description = "Lorrd is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1556,
            Y = 3251,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Lowick",
            Slug = "lowick",
            Route = "planet/lowick",
            Region = "Outer Rim Territories",
            Description = "Lowick is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1955,
            Y = 2542,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Makeb",
            Slug = "makeb",
            Route = "planet/makeb",
            Region = "Outer Rim Territories",
            Description = "A resort world lifted from destruction on colossal repulsorlift pylons during the Old Republic era.",
            X = 2788,
            Y = 2493,
            Color = "#4a9aaa"
        },
        new()
        {
            Name = "Malastare",
            Slug = "malastare",
            Route = "planet/malastare",
            Region = "Mid Rim Territories",
            Description = "A fuel-rich world of podracing plains and Dug–Gran political tensions.",
            X = 2258,
            Y = 3505,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Maridun",
            Slug = "maridun",
            Route = "planet/maridun",
            Region = "Outer Rim Territories",
            Description = "A grassland world where Lurmen colonies faced Separatist superweapon tests.",
            X = 1511,
            Y = 2414,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Mimban",
            Slug = "mimban",
            Route = "planet/mimban",
            Region = "Outer Rim Territories",
            Description = "A muddy war-torn world of misty swamps where Imperial ground forces clashed with native Mimbanese resistance.",
            X = 1337,
            Y = 3310,
            Color = "#5a6a4a"
        },
        new()
        {
            Name = "Mirial",
            Slug = "mirial",
            Route = "planet/mirial",
            Region = "Outer Rim Territories",
            Description = "Mirial is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1296,
            Y = 3021,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Moraband",
            Slug = "moraband",
            Route = "planet/moraband",
            Region = "Outer Rim Territories",
            Description = "The ancient Sith homeworld of barren red wastes, tomb valleys, and dark side sanctuaries predating Korriban records.",
            X = 1146,
            Y = 1379,
            Color = "#8a3030"
        },
        new()
        {
            Name = "Muunilinst",
            Slug = "muunilinst",
            Route = "planet/muunilinst",
            Region = "Outer Rim Territories",
            Description = "A Muun banking colony of towering spires and InterGalactic Banking Clan vaults.",
            X = 2271,
            Y = 1429,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Mygeeto colony",
            Slug = "mygeeto-colony",
            Route = "planet/mygeeto-colony",
            Region = "Outer Rim Territories",
            Description = "Mygeeto colony is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 3040,
            Y = 2607,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Nal Hutta",
            Slug = "nal-hutta",
            Route = "planet/nal-hutta",
            Region = "Hutt Space",
            Description = "The Hutt homeworld — a polluted swamp planet orbited by the smuggler moon Nar Shaddaa.",
            X = 2713,
            Y = 3743,
            Color = "#6a7a3a"
        },
        new()
        {
            Name = "Narkina 5",
            Slug = "narkina-5",
            Route = "planet/narkina-5",
            Region = "Outer Rim Territories",
            Description = "An Imperial factory moon of assembly lines where Cassian Andor was imprisoned.",
            X = 1998,
            Y = 1429,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Neimoidia",
            Slug = "neimoidia",
            Route = "planet/neimoidia",
            Region = "Colonies",
            Description = "A fog-shrouded Trade Federation homeworld of bridge cities and Neimoidian merchant councils.",
            X = 4881,
            Y = 3189,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Oba Diah",
            Slug = "oba-diah",
            Route = "planet/oba-diah",
            Region = "Outer Rim Territories",
            Description = "A volcanic world where the Pyke Syndicate mined spice and hid Sifo-Dyas's crashed shuttle.",
            X = 2177,
            Y = 2920,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Odessen",
            Slug = "odessen",
            Route = "planet/odessen",
            Region = "Wild Space",
            Description = "A remote sanctuary world that became the Eternal Alliance base in the Old Republic era.",
            X = 1043,
            Y = 1857,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ojom",
            Slug = "ojom",
            Route = "planet/ojom",
            Region = "Outer Rim Territories",
            Description = "Ojom is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1579,
            Y = 2437,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Olega",
            Slug = "olega",
            Route = "planet/olega",
            Region = "Outer Rim Territories",
            Description = "Olega is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2291,
            Y = 3474,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ord Mantell",
            Slug = "ord-mantell",
            Route = "planet/ord-mantell",
            Region = "Outer Rim Territories",
            Description = "A scrapyard port world on the Corellian Run famous for bounty hunters and salvage yards.",
            X = 2700,
            Y = 3095,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Orto",
            Slug = "orto",
            Route = "planet/orto",
            Region = "Outer Rim Territories",
            Description = "Orto is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2660,
            Y = 2654,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Orto Plutonia",
            Slug = "orto-plutonia",
            Route = "planet/orto-plutonia",
            Region = "Outer Rim Territories",
            Description = "Orto Plutonia is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 3112,
            Y = 2235,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ossus",
            Slug = "ossus",
            Route = "planet/ossus",
            Region = "Outer Rim Territories",
            Description = "A Jedi library world of giant trees and ruined archives, devastated during the Great Sith War.",
            X = 1882,
            Y = 2450,
            Color = "#9a8a50"
        },
        new()
        {
            Name = "Pantora",
            Slug = "pantora",
            Route = "planet/pantora",
            Region = "Outer Rim Territories",
            Description = "Pantora is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2755,
            Y = 1361,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Parwan",
            Slug = "parwan",
            Route = "planet/parwan",
            Region = "Outer Rim Territories",
            Description = "Parwan is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2065,
            Y = 1804,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Patrolia",
            Slug = "patrolia",
            Route = "planet/patrolia",
            Region = "Outer Rim Territories",
            Description = "Patrolia is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2643,
            Y = 2291,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Peragus",
            Slug = "peragus",
            Route = "planet/peragus",
            Region = "Outer Rim Territories",
            Description = "A mining asteroid field station supplying fuel to Telos restoration efforts in the KOTOR era.",
            X = 2805,
            Y = 1252,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Phatrong",
            Slug = "phatrong",
            Route = "planet/phatrong",
            Region = "Outer Rim Territories",
            Description = "Phatrong is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2947,
            Y = 2658,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Phindar",
            Slug = "phindar",
            Route = "planet/phindar",
            Region = "Outer Rim Territories",
            Description = "Phindar is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1750,
            Y = 1235,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Plazir-17",
            Slug = "plazir-17",
            Route = "planet/plazir-17",
            Region = "Outer Rim Territories",
            Description = "A domed pleasure world governed by the Duchess of Plazir-15 in the New Republic era.",
            X = 2095,
            Y = 2780,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Primus Goluud",
            Slug = "primus-goluud",
            Route = "planet/primus-goluud",
            Region = "Outer Rim Territories",
            Description = "A red supergiant system used as a Sith staging point during the Great Hyperspace War.",
            X = 2514,
            Y = 2406,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Qika",
            Slug = "qika",
            Route = "planet/qika",
            Region = "Outer Rim Territories",
            Description = "A contested world in the New Sith Wars where Brotherhood forces clashed with Republic armies.",
            X = 1392,
            Y = 1758,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Quarzite",
            Slug = "quarzite",
            Route = "planet/quarzite",
            Region = "Outer Rim Territories",
            Description = "Quarzite is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2096,
            Y = 3181,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Quermia",
            Slug = "quermia",
            Route = "planet/quermia",
            Region = "Outer Rim Territories",
            Description = "Quermia is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 3141,
            Y = 2871,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Rattatak",
            Slug = "rattatak",
            Route = "planet/rattatak",
            Region = "Outer Rim Territories",
            Description = "Rattatak is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2151,
            Y = 1440,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Rhen Var",
            Slug = "rhen-var",
            Route = "planet/rhen-var",
            Region = "Outer Rim Territories",
            Description = "An ice moon with Jedi sanctuaries and ancient Force monuments.",
            X = 1154,
            Y = 1392,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Roche",
            Slug = "roche",
            Route = "planet/roche",
            Region = "Outer Rim Territories",
            Description = "Roche is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1505,
            Y = 2190,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Rodia",
            Slug = "rodia",
            Route = "planet/rodia",
            Region = "Outer Rim Territories",
            Description = "A humid jungle hunter world homeworld of the Rodian species and Grand Hunt traditions.",
            X = 2426,
            Y = 2067,
            Color = "#3a8a4a"
        },
        new()
        {
            Name = "Ruusan",
            Slug = "ruusan",
            Route = "planet/ruusan",
            Region = "Outer Rim Territories",
            Description = "A Mid Rim world of barren valleys where the Brotherhood of Darkness met final defeat and the Rule of Two began.",
            X = 2354,
            Y = 1893,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Saleucami",
            Slug = "saleucami",
            Route = "planet/saleucami",
            Region = "Outer Rim Territories",
            Description = "A mosaic grassland world of clone medic camps and Separatist enclaves during the Clone Wars.",
            X = 1350,
            Y = 4119,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Scarif",
            Slug = "scarif",
            Route = "planet/scarif",
            Region = "Outer Rim Territories",
            Description = "A tropical Outer Rim world housing the Imperial Citadel and the data vault targeted during the Death Star plans raid.",
            X = 2436,
            Y = 1833,
            Color = "#2a8a6a"
        },
        new()
        {
            Name = "Selonia",
            Slug = "selonia",
            Route = "planet/selonia",
            Region = "Outer Rim Territories",
            Description = "Selonia is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2095,
            Y = 1955,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Sembla",
            Slug = "sembla",
            Route = "planet/sembla",
            Region = "Outer Rim Territories",
            Description = "Sembla is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1192,
            Y = 2994,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Shili",
            Slug = "shili",
            Route = "planet/shili",
            Region = "Outer Rim Territories",
            Description = "Shili is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1885,
            Y = 3719,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Shukut",
            Slug = "shukut",
            Route = "planet/shukut",
            Region = "Outer Rim Territories",
            Description = "Shukut is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1083,
            Y = 3758,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Siniteen",
            Slug = "siniteen",
            Route = "planet/siniteen",
            Region = "Outer Rim Territories",
            Description = "Siniteen is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2176,
            Y = 2905,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Skako",
            Slug = "skako",
            Route = "planet/skako",
            Region = "Outer Rim Territories",
            Description = "Skako is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 3102,
            Y = 3496,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Skustell",
            Slug = "skustell",
            Route = "planet/skustell",
            Region = "Outer Rim Territories",
            Description = "Skustell is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2507,
            Y = 4179,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Sorgan",
            Slug = "sorgan",
            Route = "planet/sorgan",
            Region = "Outer Rim Territories",
            Description = "A remote forest world where Mandalorian warriors protected a vulnerable village.",
            X = 2689,
            Y = 1837,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Sriluur",
            Slug = "sriluur",
            Route = "planet/sriluur",
            Region = "Outer Rim Territories",
            Description = "Sriluur is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 3084,
            Y = 3332,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Starkiller Base",
            Slug = "starkiller-base",
            Route = "planet/starkiller-base",
            Region = "Unknown Regions",
            Description = "Ilum converted into a mobile ice planet superweapon that annihilated the Hosnian system.",
            X = 632,
            Y = 883,
            Color = "#3a4a6a"
        },
        new()
        {
            Name = "Stygeon Prime",
            Slug = "stygeon-prime",
            Route = "planet/stygeon-prime",
            Region = "Outer Rim Territories",
            Description = "A mountainous world housing the Spire, a Separatist prison for Jedi captives.",
            X = 2951,
            Y = 3519,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Sullust",
            Slug = "sullust",
            Route = "planet/sullust",
            Region = "Outer Rim Territories",
            Description = "A volcanic industrial world of Sullustan shipyards and underground cities glowing with factory light.",
            X = 2414,
            Y = 3672,
            Color = "#b85a30"
        },
        new()
        {
            Name = "Thisspias",
            Slug = "thisspias",
            Route = "planet/thisspias",
            Region = "Outer Rim Territories",
            Description = "Thisspias is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2682,
            Y = 1227,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Tholoth",
            Slug = "tholoth",
            Route = "planet/tholoth",
            Region = "Outer Rim Territories",
            Description = "Tholoth is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2319,
            Y = 1760,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Tibrin",
            Slug = "tibrin",
            Route = "planet/tibrin",
            Region = "Outer Rim Territories",
            Description = "Tibrin is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2889,
            Y = 2063,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Toola",
            Slug = "toola",
            Route = "planet/toola",
            Region = "Outer Rim Territories",
            Description = "Toola is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2051,
            Y = 1636,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Toydaria",
            Slug = "toydaria",
            Route = "planet/toydaria",
            Region = "Outer Rim Territories",
            Description = "Toydaria is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2548,
            Y = 3298,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Trandosha",
            Slug = "trandosha",
            Route = "planet/trandosha",
            Region = "Outer Rim Territories",
            Description = "Trandosha is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1849,
            Y = 4067,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Troiken",
            Slug = "troiken",
            Route = "planet/troiken",
            Region = "Outer Rim Territories",
            Description = "An ice world where the Stark Commercial Combine made its last stand against Republic forces.",
            X = 2974,
            Y = 4151,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Uba IV",
            Slug = "uba-iv",
            Route = "planet/uba-iv",
            Region = "Outer Rim Territories",
            Description = "Uba IV is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2331,
            Y = 3048,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Uvena Prime",
            Slug = "uvena-prime",
            Route = "planet/uvena-prime",
            Region = "Outer Rim Territories",
            Description = "Uvena Prime is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1300,
            Y = 2408,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vinsoth",
            Slug = "vinsoth",
            Route = "planet/vinsoth",
            Region = "Outer Rim Territories",
            Description = "Vinsoth is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2512,
            Y = 2869,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Wayland",
            Slug = "wayland",
            Route = "planet/wayland",
            Region = "Wild Space",
            Description = "A Wild Space jungle world hiding Emperor Palpatine's secret storehouse and Mount Tantiss.",
            X = 1233,
            Y = 1570,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Wobani",
            Slug = "wobani",
            Route = "planet/wobani",
            Region = "Outer Rim Territories",
            Description = "An Imperial prison world of harsh work camps where Jyn Erso was held before liberation.",
            X = 2965,
            Y = 1775,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Wroona",
            Slug = "wroona",
            Route = "planet/wroona",
            Region = "Outer Rim Territories",
            Description = "Wroona is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2763,
            Y = 3711,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Yablari",
            Slug = "yablari",
            Route = "planet/yablari",
            Region = "Outer Rim Territories",
            Description = "Yablari is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1811,
            Y = 2741,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Yag'Dhul",
            Slug = "yagdhul",
            Route = "planet/yagdhul",
            Region = "Outer Rim Territories",
            Description = "Yag'Dhul is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1024,
            Y = 2784,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Yar Togna",
            Slug = "yar-togna",
            Route = "planet/yar-togna",
            Region = "Outer Rim Territories",
            Description = "Yar Togna is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1555,
            Y = 1558,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Zeltros",
            Slug = "zeltros",
            Route = "planet/zeltros",
            Region = "Outer Rim Territories",
            Description = "Zeltros is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 1219,
            Y = 1875,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Zolan",
            Slug = "zolan",
            Route = "planet/zolan",
            Region = "Outer Rim Territories",
            Description = "Zolan is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2559,
            Y = 1360,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Zygerria",
            Slug = "zygerria",
            Route = "planet/zygerria",
            Region = "Outer Rim Territories",
            Description = "Zygerria is a outer rim territories world documented across the nine saga films, live-action and animated series, Knights of the Old Republic, and Old Sith Empire records.",
            X = 2348,
            Y = 2081,
            Color = "#4a6a8a"
        }
,
        new()
        {
            Name = "Ambria",
            Slug = "ambria",
            Route = "planet/ambria",
            Region = "Outer Rim Territories",
            Description = "A desolate wasteland poisoned by Sith alchemy, later home to Master Thon's Jedi enclave.",
            X = 2567,
            Y = 2349,
            Color = "#6a5040"
        },
        new()
        {
            Name = "Thule",
            Slug = "thule",
            Route = "planet/thule",
            Region = "Sith Space",
            Description = "A secret Sith stronghold world used by the Brotherhood of Darkness and later Imperial cultists.",
            X = 6571,
            Y = 3019,
            Color = "#4a3030"
        },
        new()
        {
            Name = "Krayiss II",
            Slug = "krayiss-ii",
            Route = "planet/krayiss-ii",
            Region = "Sith Space",
            Description = "A dark side nexus world of Sith temples haunted by trapped spirits and ancient holocrons.",
            X = 6464,
            Y = 3618,
            Color = "#5a3545"
        },
        new()
        {
            Name = "Khar Delba",
            Slug = "khar-delba",
            Route = "planet/khar-delba",
            Region = "Sith Space",
            Description = "An icy Sith world and fortress moon of Naga Sadow's empire during the Great Hyperspace War.",
            X = 6867,
            Y = 3815,
            Color = "#7a9ab0"
        },
        new()
        {
            Name = "Khar Shian",
            Slug = "khar-shian",
            Route = "planet/khar-shian",
            Region = "Sith Space",
            Description = "The rocky moon fortress companion to Khar Delba, anchoring Sadow's ancient invasion fleets.",
            X = 7069,
            Y = 3688,
            Color = "#6a8090"
        },
        new()
        {
            Name = "Rhelg",
            Slug = "rhelg",
            Route = "planet/rhelg",
            Region = "Sith Space",
            Description = "One of the five sacred Sith worlds of the Sith Empire, ruled by the Sith Lord Kalimash Persada.",
            X = 6434,
            Y = 3682,
            Color = "#8a4040"
        },
        new()
        {
            Name = "Ch'hodos",
            Slug = "ch-hodos",
            Route = "planet/ch-hodos",
            Region = "Sith Space",
            Description = "A volcanic Sith world among the five sacred domains of the Old Sith Empire.",
            X = 6456,
            Y = 3054,
            Color = "#9a4530"
        },
        new()
        {
            Name = "Jaguada",
            Slug = "jaguada",
            Route = "planet/jaguada",
            Region = "Sith Space",
            Description = "A red desert Sith world with temple complexes tied to the Great Hyperspace War era.",
            X = 6850,
            Y = 3601,
            Color = "#a05030"
        },
        new()
        {
            Name = "Tund",
            Slug = "tund",
            Route = "planet/tund",
            Region = "Outer Rim Territories",
            Description = "A gas-shrouded world of pureblood Sith sorcerers and strange Force traditions.",
            X = 3132,
            Y = 4075,
            Color = "#7a6a50"
        },
        new()
        {
            Name = "Vjun",
            Slug = "vjun",
            Route = "planet/vjun",
            Region = "Outer Rim Territories",
            Description = "A acid-rain world where Count Dooku built Bast Castle amid ruins of Force-worshipping nobility.",
            X = 2473,
            Y = 3112,
            Color = "#6a7a40"
        },
        new()
        {
            Name = "Athiss",
            Slug = "atthiss",
            Route = "planet/atthiss",
            Region = "Outer Rim Territories",
            Description = "A jungle tomb world of the ancient Sith species, overrun by corrupted beasts and dark side relics.",
            X = 2715,
            Y = 4099,
            Color = "#3a6a3a"
        },
        new()
        {
            Name = "Voss",
            Slug = "voss",
            Route = "planet/voss",
            Region = "Unknown Regions",
            Description = "A mist-shrouded world of prophetic Voss Mystics contested by Jedi, Sith, and the Eternal Empire.",
            X = 988,
            Y = 1365,
            Color = "#5a8a7a"
        },
        new()
        {
            Name = "Belsavis",
            Slug = "belsavis",
            Route = "planet/belsavis",
            Region = "Outer Rim Territories",
            Description = "An ice world hiding a vast Republic prison vault containing ancient Sith superweapons and warlords.",
            X = 1204,
            Y = 1887,
            Color = "#8ab0d0"
        },
        new()
        {
            Name = "Quesh",
            Slug = "quesh",
            Route = "planet/quesh",
            Region = "Outer Rim Territories",
            Description = "A toxic jungle world rich in 'adrenal' chemicals, fought over by Republic and Empire in the Old Republic era.",
            X = 1012,
            Y = 2715,
            Color = "#7a9a30"
        },
        new()
        {
            Name = "Empress Teta",
            Slug = "empress-teta",
            Route = "planet/empress-teta",
            Region = "Deep Core",
            Description = "A Deep Core industrial world and capital of the Tetan monarchy, central to the Great Sith War.",
            X = 5118,
            Y = 2768,
            Color = "#6a5a8a"
        },
        new()
        {
            Name = "Prakith",
            Slug = "prakith",
            Route = "planet/prakith",
            Region = "Deep Core",
            Description = "A fortress world of the Imperial Inquisitorius and ancient Sith catacombs beneath its citadels.",
            X = 5133,
            Y = 2431,
            Color = "#5a5a6a"
        },
        new()
        {
            Name = "Koros Major",
            Slug = "koros-major",
            Route = "planet/koros-major",
            Region = "Deep Core",
            Description = "The carbonite-rich founding world of the Empress Teta system and early Unification Wars.",
            X = 5314,
            Y = 2466,
            Color = "#7a6a9a"
        },
        new()
        {
            Name = "Kesh",
            Slug = "kesh",
            Route = "planet/kesh",
            Region = "Wild Space",
            Description = "An isolated continent world where the Lost Tribe of Sith survived for millennia after a crash landing.",
            X = 981,
            Y = 1235,
            Color = "#4a7a8a"
        },
        new()
        {
            Name = "Almas",
            Slug = "almas",
            Route = "planet/almas",
            Region = "Cularin System",
            Description = "A desert world in the Cularin system housing a Jedi academy built over an ancient Sith fortress.",
            X = 2444,
            Y = 3006,
            Color = "#c4a060"
        },
        new()
        {
            Name = "Cularin",
            Slug = "cularin",
            Route = "planet/cularin",
            Region = "Cularin System",
            Description = "A binary-star system world of dense jungles and Force anomalies tied to Sith experimentation.",
            X = 2576,
            Y = 3514,
            Color = "#3a7a4a"
        },
        new()
        {
            Name = "Foerost",
            Slug = "foerost",
            Route = "planet/foerost",
            Region = "Deep Core",
            Description = "An ancient shipyard world seized by the Sith during the Great Sith War for dreadnought construction.",
            X = 5205,
            Y = 2685,
            Color = "#6a7080"
        },
        new()
        {
            Name = "Koros",
            Slug = "koros",
            Route = "planet/koros",
            Region = "Deep Core",
            Description = "A Deep Core system anchor world linked to Empress Teta's unification campaigns and Sith incursions.",
            X = 5360,
            Y = 2476,
            Color = "#706090"
        },
        new()
        {
            Name = "Myrkr",
            Slug = "myrkr",
            Route = "planet/myrkr",
            Region = "Wild Space",
            Description = "A forest world of ysalamir Force-null zones, used as a base by smugglers and later Imperial factions.",
            X = 1102,
            Y = 2417,
            Color = "#2a6a3a"
        },
        new()
        {
            Name = "Nirauan",
            Slug = "nirauan",
            Route = "planet/nirauan",
            Region = "Unknown Regions",
            Description = "A remote jungle world with a Chiss hand of Thrawn's hidden fortress and ysalamir groves.",
            X = 816,
            Y = 1376,
            Color = "#3a6a5a"
        },
        new()
        {
            Name = "Hypori",
            Slug = "hypori",
            Route = "planet/hypori",
            Region = "Outer Rim Territories",
            Description = "A factory moon of droid foundries where General Grievous was first revealed to the Jedi.",
            X = 3164,
            Y = 3317,
            Color = "#7a8070"
        },
        new()
        {
            Name = "Sleheyron",
            Slug = "sleheyron",
            Route = "planet/sleheyron",
            Region = "Outer Rim Territories",
            Description = "A Hutt-linked trade world referenced in KOTOR as a rival hub to Nar Shaddaa's shadow economy.",
            X = 1422,
            Y = 1589,
            Color = "#8a6840"
        },
        new()
        {
            Name = "Rekkiad",
            Slug = "rekkiad",
            Route = "planet/rekkiad",
            Region = "Unknown Regions",
            Description = "An ice world where Sith Emperor Vitiate's mask was hidden among tribal Mandalorian graves.",
            X = 885,
            Y = 980,
            Color = "#a0c0d0"
        },
        new()
        {
            Name = "Yavin 8",
            Slug = "yavin-8",
            Route = "planet/yavin-8",
            Region = "Outer Rim Territories",
            Description = "An ocean moon of Yavin Prime with Massassi ruins and Jedi Exile training sites.",
            X = 2550,
            Y = 2982,
            Color = "#2a5a6a"
        },
        new()
        {
            Name = "Yavin 13",
            Slug = "yavin-13",
            Route = "planet/yavin-13",
            Region = "Outer Rim Territories",
            Description = "A remote moon in the Yavin system tied to Sithspawn experiments and exile colonies.",
            X = 1171,
            Y = 2831,
            Color = "#3a5a5a"
        },
        new()
        {
            Name = "Had Abbadon",
            Slug = "had-abbadon",
            Route = "planet/had-abbadon",
            Region = "Deep Core",
            Description = "A legendary Deep Core throne world concept tied to dark side imperial ambitions in early drafts.",
            X = 5298,
            Y = 2769,
            Color = "#5a4060"
        },
        new()
        {
            Name = "Khomm",
            Slug = "khomm",
            Route = "planet/khomm",
            Region = "Deep Core",
            Description = "A Deep Core cloning world of uniform Arkanian Offshoot communities and genetic laboratories.",
            X = 5238,
            Y = 2675,
            Color = "#8a9aaa"
        },
        new()
        {
            Name = "Columus",
            Slug = "columus",
            Route = "planet/columus",
            Region = "Core Worlds",
            Description = "A low-gravity Core world of floating cities and Columi observers during galactic conflicts.",
            X = 4632,
            Y = 2201,
            Color = "#7a9a8a"
        },
        new()
        {
            Name = "Centares",
            Slug = "centares",
            Route = "planet/centares",
            Region = "Mid Rim Territories",
            Description = "A Mid Rim battleground world where art and war collided under Imperial occupation.",
            X = 3986,
            Y = 2420,
            Color = "#8a7060"
        },
        new()
        {
            Name = "Kuar",
            Slug = "kuar",
            Route = "planet/kuar",
            Region = "Sith Space",
            Description = "A Sith world used for dark side training and Brotherhood of Darkness trials.",
            X = 6523,
            Y = 3239,
            Color = "#704040"
        },
        new()
        {
            Name = "Sanbra",
            Slug = "sanbra",
            Route = "planet/sanbra",
            Region = "Outer Rim Territories",
            Description = "A scholarly world and holonet hub near the Outer Rim trade lanes.",
            X = 2737,
            Y = 3276,
            Color = "#6a8a9a"
        },
        new()
        {
            Name = "Ubrikkia",
            Slug = "ubrikkia",
            Route = "planet/ubrikkia",
            Region = "Mid Rim Territories",
            Description = "A Mid Rim industrial world known for Ubrikkian Industries repulsorcraft and shipyards.",
            X = 2453,
            Y = 3651,
            Color = "#708090"
        },
        new()
        {
            Name = "Volik",
            Slug = "volik",
            Route = "planet/volik",
            Region = "Unknown Regions",
            Description = "A Unknown Regions world linked to Sith Empire exile routes and hidden fleet movements.",
            X = 1321,
            Y = 1296,
            Color = "#506070"
        },
        new()
        {
            Name = "Arbra",
            Slug = "arbra",
            Route = "planet/arbra",
            Region = "Wild Space",
            Description = "A jungle world with extensive cave networks used as a Rebel base in Legends continuity.",
            X = 1436,
            Y = 2580,
            Color = "#3a7a4a"
        },
        new()
        {
            Name = "Daluuj",
            Slug = "daluuj",
            Route = "planet/daluuj",
            Region = "Outer Rim Territories",
            Description = "An ocean world of island chains and wrecked starships from ancient Sith skirmishes.",
            X = 1669,
            Y = 2313,
            Color = "#4a8090"
        },
        new()
        {
            Name = "Iego",
            Slug = "iego",
            Route = "planet/iego",
            Region = "Outer Rim Territories",
            Description = "The World of a Thousand Moons, a remote world trapped by a Separatist laser web during the Clone Wars.",
            X = 1330,
            Y = 3509,
            Color = "#6a5080"
        },
        new()
        {
            Name = "Susevfi",
            Slug = "susevfi",
            Route = "planet/susevfi",
            Region = "Outer Rim Territories",
            Description = "A volcanic retreat world of SoroSuub executives and later Jedi refuge sites.",
            X = 1205,
            Y = 1361,
            Color = "#9a5030"
        },
        new()
        {
            Name = "Tund Minor",
            Slug = "tund-minor",
            Route = "planet/tund-minor",
            Region = "Outer Rim Territories",
            Description = "A companion world to Tund associated with Sith sorcerer enclaves and dark side sects.",
            X = 2682,
            Y = 2037,
            Color = "#7a7050"
        },
        new()
        {
            Name = "Ziost II",
            Slug = "ziost-ii",
            Route = "planet/ziost-ii",
            Region = "Sith Space",
            Description = "A chart label for secondary Ziost orbit facilities during Old Sith Empire logistics records.",
            X = 6956,
            Y = 3993,
            Color = "#6a8090"
        },
        new()
        {
            Name = "Stygium Caldera",
            Slug = "stygium-caldera",
            Route = "planet/stygium-caldera",
            Region = "Sith Space",
            Description = "An asteroid caldera rich in stygium crystals used for cloaking devices and Sith artifacts.",
            X = 6968,
            Y = 3689,
            Color = "#3a3040"
        },
        new()
        {
            Name = "Nicht Ka",
            Slug = "nicht-ka",
            Route = "planet/nicht-ka",
            Region = "Sith Space",
            Description = "A barren Sith world with tomb cities from the era before the Great Hyperspace War.",
            X = 6861,
            Y = 2810,
            Color = "#5a3535"
        },
        new()
        {
            Name = "XoXaan's Tomb World",
            Slug = "xoxaan-tomb",
            Route = "planet/xoxaan-tomb",
            Region = "Sith Space",
            Description = "A forgotten Sith mausoleum world tied to one of the first Sith Lords after the Hundred-Year Darkness.",
            X = 7011,
            Y = 2632,
            Color = "#4a2830"
        },
        new()
        {
            Name = "Bogo Rai",
            Slug = "bogo-rai",
            Route = "planet/bogo-rai",
            Region = "Unknown Regions",
            Description = "A Unknown Regions world referenced in Sith Empire exile charts and Chiss border surveys.",
            X = 1226,
            Y = 1411,
            Color = "#506858"
        },
        new()
        {
            Name = "Sorzus Ne",
            Slug = "sorzus-ne",
            Route = "planet/sorzus-ne",
            Region = "Sith Space",
            Description = "A Sith world associated with Sorzus Syn's alchemical texts and early Sith pureblood colonies.",
            X = 6514,
            Y = 3425,
            Color = "#6a3848"
        },
        new()
        {
            Name = "Korriban's Moon",
            Slug = "korriban-moon",
            Route = "planet/korriban-moon",
            Region = "Sith Space",
            Description = "An ash-dark moon orbiting Korriban with orbital tombs and Sith academy staging platforms.",
            X = 6919,
            Y = 3626,
            Color = "#504038"
        },
        new()
        {
            Name = "Yavin Prime",
            Slug = "yavin-prime",
            Route = "planet/yavin-prime",
            Region = "Outer Rim Territories",
            Description = "The gas giant anchoring the Yavin system, orbited by Yavin 4 and other Massassi-touched moons.",
            X = 1919,
            Y = 1739,
            Color = "#c87830"
        },
        new()
        {
            Name = "Tatoo I",
            Slug = "tatoo-i",
            Route = "planet/tatoo-i",
            Region = "Outer Rim Territories",
            Description = "The primary star of the Tatoo system, whose intense heat shaped Tatooine's desert ecology.",
            X = 3149,
            Y = 1661,
            Color = "#e8a030"
        },
        new()
        {
            Name = "Tatoo II",
            Slug = "tatoo-ii",
            Route = "planet/tatoo-ii",
            Region = "Outer Rim Territories",
            Description = "The twin sun of Tatooine's binary system, defining the iconic double-sunset horizon.",
            X = 2954,
            Y = 1410,
            Color = "#f0b040"
        },
        new()
        {
            Name = "Subterrel",
            Slug = "subterrel",
            Route = "planet/subterrel",
            Region = "Outer Rim Territories",
            Description = "A mining world of underground cities and podracing circuits on hostile surface terrain.",
            X = 3113,
            Y = 3067,
            Color = "#806850"
        },
        new()
        {
            Name = "Praesitlyn",
            Slug = "praesitlyn",
            Route = "planet/praesitlyn",
            Region = "Outer Rim Territories",
            Description = "A communications hub world fought over during Clone Wars campaigns for its HoloNet relay nodes.",
            X = 2271,
            Y = 3037,
            Color = "#6a9080"
        },
        new()
        {
            Name = "Druckenwell",
            Slug = "druckenwell",
            Route = "planet/druckenwell",
            Region = "Mid Rim Territories",
            Description = "A Mid Rim factory world supplying components to galactic shipwrights across multiple eras.",
            X = 2318,
            Y = 3735,
            Color = "#708070"
        },
        new()
        {
            Name = "Hapes",
            Slug = "hapes",
            Route = "planet/hapes",
            Region = "Hapes Consortium",
            Description = "The crown world of the Hapes Consortium, isolated by transitory mists and royal matriarchy.",
            X = 3746,
            Y = 2189,
            Color = "#9a7ab0"
        },
        new()
        {
            Name = "Dathomir Sister Moon",
            Slug = "dathomir-sister-moon",
            Route = "planet/dathomir-sister-moon",
            Region = "Outer Rim Territories",
            Description = "A companion moon in the Dathomir system tied to Nightsister orbital rituals.",
            X = 2768,
            Y = 1254,
            Color = "#6a3040"
        },
        new()
        {
            Name = "Gorog",
            Slug = "gorog",
            Route = "planet/gorog",
            Region = "Unknown Regions",
            Description = "A dark side world of the Gorog assassin cult within the Killik hive mind expansions.",
            X = 747,
            Y = 1095,
            Color = "#404838"
        },
        new()
        {
            Name = "Yoggoy",
            Slug = "yoggoy",
            Route = "planet/yoggoy",
            Region = "Unknown Regions",
            Description = "A Killik nest world on the fringes of the Unknown Regions hive collective.",
            X = 1229,
            Y = 1496,
            Color = "#5a6840"
        },
        new()
        {
            Name = "Tatooine's Sister",
            Slug = "ghomrassen",
            Route = "planet/ghomrassen",
            Region = "Outer Rim Territories",
            Description = "Ghomrassen, a rocky Tatooine region moon and mining settlement in Legends surveys.",
            X = 1975,
            Y = 3489,
            Color = "#9a8060"
        },
        new()
        {
            Name = "Adumar",
            Slug = "adumar",
            Route = "planet/adumar",
            Region = "Wild Space",
            Description = "A Wild Space world obsessed with starfighter dueling culture, courted by New Republic and Empire.",
            X = 912,
            Y = 2114,
            Color = "#5a8ab0"
        },
        new()
        {
            Name = "Borleias",
            Slug = "borleias",
            Route = "planet/borleias",
            Region = "Colonies",
            Description = "A Colonies world with a vital planetary shield generator, contested in the New Republic era.",
            X = 4838,
            Y = 2940,
            Color = "#6a8090"
        },
        new()
        {
            Name = "Ebaq 9",
            Slug = "ebaq-9",
            Route = "planet/ebaq-9",
            Region = "Deep Core",
            Description = "An asteroid fortress in the Deep Core used by the New Republic against Yuuzhan Vong incursions.",
            X = 5057,
            Y = 2662,
            Color = "#707880"
        },
        new()
        {
            Name = "Mortis",
            Slug = "mortis",
            Route = "planet/mortis",
            Region = "Wild Space",
            Description = "A ethereal Force nexus realm manifesting as a planetoid with the Father, Son, and Daughter.",
            X = 1747,
            Y = 1358,
            Color = "#6a5080"
        },
        new()
        {
            Name = "Abafar",
            Slug = "abafar",
            Route = "planet/abafar",
            Region = "Outer Rim Territories",
            Description = "A desert world with a sunken municipal landfill and Clone Wars fuel depot.",
            X = 1492,
            Y = 1519,
            Color = "#c4a060"
        },
        new()
        {
            Name = "Raxus Secundus",
            Slug = "raxus-secundus",
            Route = "planet/raxus-secundus",
            Region = "Outer Rim Territories",
            Description = "The official capital world of the Confederacy of Independent Systems during the Clone Wars.",
            X = 2439,
            Y = 3632,
            Color = "#5a9a7a"
        },
        new()
        {
            Name = "Christophsis Moon",
            Slug = "leesis",
            Route = "planet/leesis",
            Region = "Outer Rim Territories",
            Description = "Leesis, a moon in the Christoph system used for forward clone staging areas.",
            X = 2390,
            Y = 2460,
            Color = "#7a9080"
        },
        new()
        {
            Name = "Anaxes",
            Slug = "anaxes",
            Route = "planet/anaxes",
            Region = "Core Worlds",
            Description = "A Core fortress world of the Republic Navy, reduced to an asteroid field during the Clone Wars.",
            X = 4381,
            Y = 2106,
            Color = "#8090a0"
        },
        new()
        {
            Name = "Ringo Vinda",
            Slug = "ringo-vinda",
            Route = "planet/ringo-vinda",
            Region = "Mid Rim Territories",
            Description = "A Mid Rim orbital station world blockaded during the Clone Wars biochip crisis.",
            X = 3566,
            Y = 2617,
            Color = "#8090a8"
        },
        new()
        {
            Name = "Scipio",
            Slug = "scipio",
            Route = "planet/scipio",
            Region = "Outer Rim Territories",
            Description = "The headquarters world of the InterGalactic Banking Clan on a crystalline alpine plateau.",
            X = 1429,
            Y = 2321,
            Color = "#a0b8d0"
        },
        new()
        {
            Name = "Lwhekk",
            Slug = "lwhekk",
            Route = "planet/lwhekk",
            Region = "Unknown Regions",
            Description = "The Ssi-ruuvi homeworld of humid jungles and entechment weapon factories.",
            X = 1345,
            Y = 1578,
            Color = "#4a6850"
        },
        new()
        {
            Name = "Bakura-Prime",
            Slug = "bakura-prime",
            Route = "planet/bakura-prime",
            Region = "Outer Rim Territories",
            Description = "The primary inhabited world of the Bakura system invaded during the Ssi-ruuvi incursion.",
            X = 1120,
            Y = 2861,
            Color = "#6a9080"
        },
        new()
        {
            Name = "Dantooine Moon",
            Slug = "dantooine-moon",
            Route = "planet/dantooine-moon",
            Region = "Outer Rim Territories",
            Description = "A sparsely settled moon used for Rebel listening posts near Dantooine.",
            X = 1656,
            Y = 2234,
            Color = "#7a9a70"
        },
        new()
        {
            Name = "Taris Undercity",
            Slug = "taris-undercity",
            Route = "planet/taris-undercity",
            Region = "Outer Rim Territories",
            Description = "The rakghoul-infested foundation levels of Taris before and after planetary bombardment.",
            X = 2436,
            Y = 3749,
            Color = "#505860"
        },
        new()
        {
            Name = "Manaan Kolto City",
            Slug = "ahahta",
            Route = "planet/ahahta",
            Region = "Inner Rim Territories",
            Description = "Ahto City on Manaan, the floating kolto harvesting capital of the Selkath.",
            X = 4514,
            Y = 3111,
            Color = "#60a0c0"
        },
        new()
        {
            Name = "Sernpidal",
            Slug = "sernpidal",
            Route = "planet/sernpidal",
            Region = "Outer Rim Territories",
            Description = "An Outer Rim world destroyed when its moon was pulled into the planet by Yuuzhan Vong dovin basals.",
            X = 2413,
            Y = 2007,
            Color = "#8090a0"
        },
        new()
        {
            Name = "Hapes Cluster",
            Slug = "hapes-cluster",
            Route = "planet/hapes-cluster",
            Region = "Hapes Consortium",
            Description = "The navigational heart of the Hapes Consortium's ninety-three-world isolationist realm.",
            X = 3801,
            Y = 1850,
            Color = "#9070a0"
        },
        new()
        {
            Name = "Kamino Prime",
            Slug = "kamino-prime",
            Route = "planet/kamino-prime",
            Region = "Wild Space",
            Description = "The storm planet Kamino, homeworld of clone template production for the Grand Army.",
            X = 941,
            Y = 2008,
            Color = "#6090b0"
        },
        new()
        {
            Name = "Rishi Moon",
            Slug = "rishi-moon",
            Route = "planet/rishi-moon",
            Region = "Outer Rim Territories",
            Description = "The tropical Rishi moon housing a Republic listening post above the Rishi Maze approach.",
            X = 1761,
            Y = 3187,
            Color = "#4a9070"
        }
,
        new()
        {
            Name = "Begeren",
            Slug = "begeren",
            Route = "planet/begeren",
            Region = "Sith Space",
            Description = "A Sith industrial world of tomb-cities and ore refineries that supplied the Old Sith Empire's war forges.",
            X = 7004,
            Y = 3951,
            Color = "#6a4038"
        },
        new()
        {
            Name = "Bosthirda",
            Slug = "bosthirda",
            Route = "planet/bosthirda",
            Region = "Sith Space",
            Description = "A remote Sith Space world of fortress monasteries used during the Golden Age of the Sith.",
            X = 6745,
            Y = 3038,
            Color = "#5a3530"
        },
        new()
        {
            Name = "Dromund Fels",
            Slug = "dromund-fels",
            Route = "planet/dromund-fels",
            Region = "Sith Space",
            Description = "A moon in the Dromund system orbiting Dromund Kaas, used for Sith training trials and dark side rituals.",
            X = 6890,
            Y = 3093,
            Color = "#4a5048"
        },
        new()
        {
            Name = "Dromund Ixin",
            Slug = "dromund-ixin",
            Route = "planet/dromund-ixin",
            Region = "Sith Space",
            Description = "A storm-wracked moon of the Dromund Kaas system housing Sith academies and exile colonies.",
            X = 6484,
            Y = 3155,
            Color = "#5a5850"
        },
        new()
        {
            Name = "Dromund Kalakar",
            Slug = "dromund-kalakar",
            Route = "planet/dromund-kalakar",
            Region = "Sith Space",
            Description = "Kalakar Six — a volcanic moon in the Dromund system where Sith alchemists forged weapons and relics.",
            X = 6551,
            Y = 3060,
            Color = "#7a4030"
        },
        new()
        {
            Name = "Dromund Tyne",
            Slug = "dromund-tyne",
            Route = "planet/dromund-tyne",
            Region = "Sith Space",
            Description = "A mist-shrouded moon of Dromund Kaas used as a retreat for Sith sorcerers and assassin initiates.",
            X = 6874,
            Y = 2672,
            Color = "#505848"
        },
        new()
        {
            Name = "Jaguada's Moon",
            Slug = "jaguada-moon",
            Route = "planet/jaguada-moon",
            Region = "Sith Space",
            Description = "The ash-gray moon of Jaguada, site of Sith beacon towers and invasion fleet staging yards.",
            X = 7045,
            Y = 3102,
            Color = "#6a5040"
        },
        new()
        {
            Name = "Kalsunor",
            Slug = "kalsunor",
            Route = "planet/kalsunor",
            Region = "Sith Space",
            Description = "A barren Sith world of obsidian plains where ancient Dark Lords buried war trophies and holocrons.",
            X = 6426,
            Y = 3469,
            Color = "#4a3838"
        },
        new()
        {
            Name = "Korriz",
            Slug = "korriz",
            Route = "planet/korriz",
            Region = "Sith Space",
            Description = "A Korriban sister world of red deserts and satellite tomb complexes tied to the Valley of the Dark Lords.",
            X = 6596,
            Y = 3382,
            Color = "#8a5030"
        },
        new()
        {
            Name = "Nfolgai",
            Slug = "nfolgai",
            Route = "planet/nfolgai",
            Region = "Sith Space",
            Description = "A forgotten Sith tomb world of crumbling pyramids and sealed mausoleums from the Old Sith Wars.",
            X = 6907,
            Y = 3864,
            Color = "#5a4040"
        },
        new()
        {
            Name = "Arkania",
            Slug = "arkania",
            Route = "planet/arkania",
            Region = "Colonies",
            Description = "An icy Colonies world famed for genetic laboratories and Arkanian Offshoot communities with Sith-era ties.",
            X = 3974,
            Y = 2945,
            Color = "#a0c0d8"
        },
        new()
        {
            Name = "Korriban Outpost",
            Slug = "korriban-outpost",
            Route = "planet/korriban-outpost",
            Region = "Sith Space",
            Description = "An orbital logistics station serving Korriban's academy complexes and tomb excavations.",
            X = 6739,
            Y = 2864,
            Color = "#605040"
        }
    ];

    public static GalaxyPlanet? GetBySlug(string slug) =>
        Planets.FirstOrDefault(planet => planet.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
