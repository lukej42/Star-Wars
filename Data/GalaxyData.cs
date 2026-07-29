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
,
        new()
        {
            Name = "A-Foroon",
            Slug = "a-foroon",
            Route = "planet/a-foroon",
            Region = "Mid Rim Territories",
            Description = "A-Foroon is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6104,
            Y = 3930,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aargau",
            Slug = "aargau",
            Route = "planet/aargau",
            Region = "Deep Core",
            Description = "Aargau is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3941,
            Y = 2617,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aargonar",
            Slug = "aargonar",
            Route = "planet/aargonar",
            Region = "Mid Rim Territories",
            Description = "Aargonar is a star system in the Mid Rim Territories, within the Perkell Sector, at galactic grid Q-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5776,
            Y = 1979,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Aaris III",
            Slug = "aaris-iii",
            Route = "planet/aaris-iii",
            Region = "Outer Rim Territories",
            Description = "Aaris III is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4143,
            Y = 559,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Abandoned planetoid",
            Slug = "abandoned-planetoid",
            Route = "planet/abandoned-planetoid",
            Region = "Wild Space",
            Description = "Abandoned planetoid is a star system in the Wild Space, within the Zuma Sector, at galactic grid @-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 320,
            Y = 4074,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Abeloth's planet",
            Slug = "abeloths-planet",
            Route = "planet/abeloths-planet",
            Region = "Expansion Region",
            Description = "Abeloth's planet is a star system in the Expansion Region, within the Zuma Sector, at galactic grid E-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2387,
            Y = 3324,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Abo Dreth",
            Slug = "abo-dreth",
            Route = "planet/abo-dreth",
            Region = "Outer Rim Territories",
            Description = "Abo Dreth is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6658,
            Y = 912,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Abraxin",
            Slug = "abraxin",
            Route = "planet/abraxin",
            Region = "Outer Rim Territories",
            Description = "Abraxin is a star system in the Outer Rim Territories, within the Tion Hegemony, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6649,
            Y = 1607,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Abregado debris field",
            Slug = "abregado-debris-field",
            Route = "planet/abregado-debris-field",
            Region = "Wild Space",
            Description = "Abregado debris field is a star system in the Wild Space, within the Zuma Sector, at galactic grid C-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1365,
            Y = 2466,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Abregado-rae",
            Slug = "abregado-rae",
            Route = "planet/abregado-rae",
            Region = "Core Worlds",
            Description = "Abregado-rae is a star system in the Core Worlds, within the Borderland Regions, at galactic grid K-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3603,
            Y = 3222,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Abridon",
            Slug = "abridon",
            Route = "planet/abridon",
            Region = "Outer Rim Territories",
            Description = "Abridon is a star system in the Outer Rim Territories, within the Koradin Sector, at galactic grid J-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3239,
            Y = 4468,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Absanz",
            Slug = "absanz",
            Route = "planet/absanz",
            Region = "Core Worlds",
            Description = "Absanz is a star system in the Core Worlds, within the Zuma Sector, at galactic grid H-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3368,
            Y = 2716,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Acilaris",
            Slug = "acilaris",
            Route = "planet/acilaris",
            Region = "Mid Rim Territories",
            Description = "Acilaris is a star system in the Mid Rim Territories, within the Thaere sector, at galactic grid P-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5169,
            Y = 3517,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Adari",
            Slug = "adari",
            Route = "planet/adari",
            Region = "Inner Rim Territories",
            Description = "Adari is a star system in the Inner Rim Territories, within the Adari Sector, at galactic grid M-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4043,
            Y = 2333,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Adega",
            Slug = "adega",
            Route = "planet/adega",
            Region = "Outer Rim Territories",
            Description = "Adega is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6762,
            Y = 4216,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Adriana",
            Slug = "adriana",
            Route = "planet/adriana",
            Region = "Outer Rim Territories",
            Description = "Adriana is a star system in the Outer Rim Territories, within the Arkanis Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6024,
            Y = 4055,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Aduba-3",
            Slug = "aduba-3",
            Route = "planet/aduba-3",
            Region = "Outer Rim Territories",
            Description = "Aduba-3 is a star system in the Outer Rim Territories, within the Bheriz Sector, at galactic grid U-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7167,
            Y = 2765,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aeten II",
            Slug = "aeten-ii",
            Route = "planet/aeten-ii",
            Region = "Outer Rim Territories",
            Description = "Aeten II is a star system in the Outer Rim Territories, within the Dreighton Nebula, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2981,
            Y = 1609,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Affa",
            Slug = "affa",
            Route = "planet/affa",
            Region = "Inner Rim Territories",
            Description = "Affa is a star system in the Inner Rim Territories, within the Testarr Sector, at galactic grid M-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4197,
            Y = 3370,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Affavan",
            Slug = "affavan",
            Route = "planet/affavan",
            Region = "Outer Rim Territories",
            Description = "Affavan is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6562,
            Y = 3112,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Agamar",
            Slug = "agamar",
            Route = "planet/agamar",
            Region = "Outer Rim Territories",
            Description = "Agamar is a star system in the Outer Rim Territories, within the Lahara Sector, at galactic grid M-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4169,
            Y = 1528,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Agaris",
            Slug = "agaris",
            Route = "planet/agaris",
            Region = "Outer Rim Territories",
            Description = "Agaris is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5039,
            Y = 1892,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Agriworld-2079",
            Slug = "agriworld-2079",
            Route = "planet/agriworld-2079",
            Region = "Mid Rim Territories",
            Description = "Agriworld-2079 is a star system in the Mid Rim Territories, within the M'shinni Sector, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3639,
            Y = 2026,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Aguarl 3",
            Slug = "aguarl-3",
            Route = "planet/aguarl-3",
            Region = "Expansion Region",
            Description = "Aguarl 3 is a star system in the Expansion Region, within the Zuma Sector, at galactic grid N-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4515,
            Y = 3832,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ahakista",
            Slug = "ahakista",
            Route = "planet/ahakista",
            Region = "Outer Rim Territories",
            Description = "Ahakista is a star system in the Outer Rim Territories, within the Myto Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3302,
            Y = 1108,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ailon",
            Slug = "ailon",
            Route = "planet/ailon",
            Region = "Colonies",
            Description = "Ailon is a star system in the Colonies, within the Zuma Sector, at galactic grid N-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4425,
            Y = 3098,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Akrit'tar",
            Slug = "akrittar",
            Route = "planet/akrittar",
            Region = "Outer Rim Territories",
            Description = "Akrit'tar is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6967,
            Y = 2348,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Akuria II",
            Slug = "akuria-ii",
            Route = "planet/akuria-ii",
            Region = "Outer Rim Territories",
            Description = "Akuria II is a star system in the Outer Rim Territories, within the Oplovis Sector, at galactic grid M-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4125,
            Y = 1380,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Alashan",
            Slug = "alashan",
            Route = "planet/alashan",
            Region = "Outer Rim Territories",
            Description = "Alashan is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3004,
            Y = 1504,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Alee",
            Slug = "alee",
            Route = "planet/alee",
            Region = "Mid Rim Territories",
            Description = "Alee is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6178,
            Y = 2408,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Aleen",
            Slug = "aleen",
            Route = "planet/aleen",
            Region = "Mid Rim Territories",
            Description = "Aleen is a star system in the Mid Rim Territories, within the Bright Jewel, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3639,
            Y = 1840,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Aleen Minor",
            Slug = "aleen-minor",
            Route = "planet/aleen-minor",
            Region = "Inner Rim Territories",
            Description = "Aleen Minor is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid M-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4167,
            Y = 3367,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Algara II",
            Slug = "algara-ii",
            Route = "planet/algara-ii",
            Region = "Mid Rim Territories",
            Description = "Algara II is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5326,
            Y = 3698,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Algarian",
            Slug = "algarian",
            Route = "planet/algarian",
            Region = "Mid Rim Territories",
            Description = "Algarian is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5745,
            Y = 3761,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Alk'Lellish III",
            Slug = "alklellish-iii",
            Route = "planet/alklellish-iii",
            Region = "Outer Rim Territories",
            Description = "Alk'Lellish III is a star system in the Outer Rim Territories, within the Sumitra Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4473,
            Y = 2026,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Alluuvia",
            Slug = "alluuvia",
            Route = "planet/alluuvia",
            Region = "Outer Rim Territories",
            Description = "Alluuvia is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4251,
            Y = 4693,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Allyuen",
            Slug = "allyuen",
            Route = "planet/allyuen",
            Region = "Outer Rim Territories",
            Description = "Allyuen is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3448,
            Y = 4531,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Almania",
            Slug = "almania",
            Route = "planet/almania",
            Region = "Outer Rim Territories",
            Description = "Almania is a star system in the Outer Rim Territories, within the Mortex Sector, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6323,
            Y = 1367,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Alsakan",
            Slug = "alsakan",
            Route = "planet/alsakan",
            Region = "Core Worlds",
            Description = "Alsakan is a star system in the Core Worlds, within the Alsaka Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3670,
            Y = 2469,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Altarrn",
            Slug = "altarrn",
            Route = "planet/altarrn",
            Region = "Mid Rim Territories",
            Description = "Altarrn is a star system in the Mid Rim Territories, within the Glythe Sector, at galactic grid J-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3076,
            Y = 2001,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Altyr V",
            Slug = "altyr-v",
            Route = "planet/altyr-v",
            Region = "Outer Rim Territories",
            Description = "Altyr V is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5108,
            Y = 1483,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Alvorine",
            Slug = "alvorine",
            Route = "planet/alvorine",
            Region = "Outer Rim Territories",
            Description = "Alvorine is a star system in the Outer Rim Territories, within the Yminis Sector, at galactic grid S-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6303,
            Y = 3637,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Alzar",
            Slug = "alzar",
            Route = "planet/alzar",
            Region = "Outer Rim Territories",
            Description = "Alzar is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6232,
            Y = 1615,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Alzoc III",
            Slug = "alzoc-iii",
            Route = "planet/alzoc-iii",
            Region = "Outer Rim Territories",
            Description = "Alzoc III is a star system in the Outer Rim Territories, within the Sarin Sector, at galactic grid P-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5302,
            Y = 4647,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Amaltanna",
            Slug = "amaltanna",
            Route = "planet/amaltanna",
            Region = "Outer Rim Territories",
            Description = "Amaltanna is a star system in the Outer Rim Territories, within the Kanz Sector, at galactic grid N-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4423,
            Y = 1245,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Amethia Prime",
            Slug = "amethia-prime",
            Route = "planet/amethia-prime",
            Region = "Wild Space",
            Description = "Amethia Prime is a star system in the Wild Space, within the Zuma Sector, at galactic grid P-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6389,
            Y = 4840,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ammuud",
            Slug = "ammuud",
            Route = "planet/ammuud",
            Region = "Outer Rim Territories",
            Description = "Ammuud is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6304,
            Y = 1308,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Amorris",
            Slug = "amorris",
            Route = "planet/amorris",
            Region = "Outer Rim Territories",
            Description = "Amorris is a star system in the Outer Rim Territories, within the Quelii Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4905,
            Y = 1692,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Anaxes asteroid belt",
            Slug = "anaxes-asteroid-belt",
            Route = "planet/anaxes-asteroid-belt",
            Region = "Core Worlds",
            Description = "Anaxes asteroid belt is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3934,
            Y = 2492,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Anchoron",
            Slug = "anchoron",
            Route = "planet/anchoron",
            Region = "Outer Rim Territories",
            Description = "Anchoron is a star system in the Outer Rim Territories, within the Mayagil Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4230,
            Y = 4549,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Andelm IV",
            Slug = "andelm-iv",
            Route = "planet/andelm-iv",
            Region = "Expansion Region",
            Description = "Andelm IV is a star system in the Expansion Region, within the Zuma Sector, at galactic grid H-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3509,
            Y = 2034,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ando Prime",
            Slug = "ando-prime",
            Route = "planet/ando-prime",
            Region = "Mid Rim Territories",
            Description = "Ando Prime is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5602,
            Y = 3867,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Andooweel",
            Slug = "andooweel",
            Route = "planet/andooweel",
            Region = "Outer Rim Territories",
            Description = "Andooweel is a star system in the Outer Rim Territories, within the Arkanis Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5964,
            Y = 4020,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Annaj",
            Slug = "annaj",
            Route = "planet/annaj",
            Region = "Outer Rim Territories",
            Description = "Annaj is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2391,
            Y = 3996,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Annamar",
            Slug = "annamar",
            Route = "planet/annamar",
            Region = "Expansion Region",
            Description = "Annamar is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3679,
            Y = 3669,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Annamar asteroid field",
            Slug = "annamar-asteroid-field",
            Route = "planet/annamar-asteroid-field",
            Region = "Expansion Region",
            Description = "Annamar asteroid field is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3625,
            Y = 3733,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Anoat",
            Slug = "anoat",
            Route = "planet/anoat",
            Region = "Outer Rim Territories",
            Description = "Anoat is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3427,
            Y = 4479,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Anobis",
            Slug = "anobis",
            Route = "planet/anobis",
            Region = "Mid Rim Territories",
            Description = "Anobis is a star system in the Mid Rim Territories, within the Bright Jewel, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3664,
            Y = 1932,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Anoth",
            Slug = "anoth",
            Route = "planet/anoth",
            Region = "Outer Rim Territories",
            Description = "Anoth is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3057,
            Y = 4880,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ansion",
            Slug = "ansion",
            Route = "planet/ansion",
            Region = "Mid Rim Territories",
            Description = "Ansion is a star system in the Mid Rim Territories, within the Churnis Sector, at galactic grid I-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2837,
            Y = 1580,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Antamont",
            Slug = "antamont",
            Route = "planet/antamont",
            Region = "Outer Rim Territories",
            Description = "Antamont is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5911,
            Y = 1734,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Anteevy",
            Slug = "anteevy",
            Route = "planet/anteevy",
            Region = "Mid Rim Territories",
            Description = "Anteevy is a star system in the Mid Rim Territories, within the Esuain Sector, at galactic grid P-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5335,
            Y = 1891,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Anthan Prime",
            Slug = "anthan-prime",
            Route = "planet/anthan-prime",
            Region = "Outer Rim Territories",
            Description = "Anthan Prime is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid A-1, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 775,
            Y = 485,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Antipose",
            Slug = "antipose",
            Route = "planet/antipose",
            Region = "Outer Rim Territories",
            Description = "Antipose is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7354,
            Y = 2227,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Antiquity",
            Slug = "antiquity",
            Route = "planet/antiquity",
            Region = "Mid Rim Territories",
            Description = "Antiquity is a star system in the Mid Rim Territories, within the Senex Sector, at galactic grid L-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3752,
            Y = 4392,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Antmuel VI",
            Slug = "antmuel-vi",
            Route = "planet/antmuel-vi",
            Region = "Outer Rim Territories",
            Description = "Antmuel VI is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4342,
            Y = 970,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Antolus I",
            Slug = "antolus-i",
            Route = "planet/antolus-i",
            Region = "Mid Rim Territories",
            Description = "Antolus I is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5681,
            Y = 2190,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Anx Minor",
            Slug = "anx-minor",
            Route = "planet/anx-minor",
            Region = "Outer Rim Territories",
            Description = "Anx Minor is a star system in the Outer Rim Territories, within the Raioballo Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3659,
            Y = 1234,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Aquaris",
            Slug = "aquaris",
            Route = "planet/aquaris",
            Region = "Expansion Region",
            Description = "Aquaris is a star system in the Expansion Region, within the Sumitra Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4747,
            Y = 1999,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Aquilaris",
            Slug = "aquilaris",
            Route = "planet/aquilaris",
            Region = "Outer Rim Territories",
            Description = "Aquilaris is a star system in the Outer Rim Territories, within the Sanbra Sector, at galactic grid O-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4797,
            Y = 4174,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aquilaris Minor",
            Slug = "aquilaris-minor",
            Route = "planet/aquilaris-minor",
            Region = "Mid Rim Territories",
            Description = "Aquilaris Minor is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4105,
            Y = 4128,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Arah asteroid belt",
            Slug = "arah-asteroid-belt",
            Route = "planet/arah-asteroid-belt",
            Region = "Mid Rim Territories",
            Description = "Arah asteroid belt is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3223,
            Y = 1698,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aram",
            Slug = "aram",
            Route = "planet/aram",
            Region = "Expansion Region",
            Description = "Aram is a star system in the Expansion Region, within the Brak Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5103,
            Y = 3476,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Arbooine",
            Slug = "arbooine",
            Route = "planet/arbooine",
            Region = "Outer Rim Territories",
            Description = "Arbooine is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3708,
            Y = 4879,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Arcan IV",
            Slug = "arcan-iv",
            Route = "planet/arcan-iv",
            Region = "Outer Rim Territories",
            Description = "Arcan IV is a star system in the Outer Rim Territories, within the Allied Tion Sector, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6533,
            Y = 1617,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Archenar asteroid field",
            Slug = "archenar-asteroid-field",
            Route = "planet/archenar-asteroid-field",
            Region = "Mid Rim Territories",
            Description = "Archenar asteroid field is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6017,
            Y = 2652,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Arda",
            Slug = "arda",
            Route = "planet/arda",
            Region = "Outer Rim Territories",
            Description = "Arda is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5675,
            Y = 1746,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Arda-1",
            Slug = "arda-1",
            Route = "planet/arda-1",
            Region = "Outer Rim Territories",
            Description = "Arda-1 is a star system in the Outer Rim Territories, within the Gordian Reach, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5724,
            Y = 1622,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Arda-2",
            Slug = "arda-2",
            Route = "planet/arda-2",
            Region = "Outer Rim Territories",
            Description = "Arda-2 is a star system in the Outer Rim Territories, within the Gordian Reach, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5724,
            Y = 1622,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Argavat",
            Slug = "argavat",
            Route = "planet/argavat",
            Region = "Colonies",
            Description = "Argavat is a star system in the Colonies, within the Bamula Sector, at galactic grid J-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3112,
            Y = 3241,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aridka",
            Slug = "aridka",
            Route = "planet/aridka",
            Region = "Mid Rim Territories",
            Description = "Aridka is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5896,
            Y = 3597,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Aridus",
            Slug = "aridus",
            Route = "planet/aridus",
            Region = "Expansion Region",
            Description = "Aridus is a star system in the Expansion Region, within the Narvath Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5013,
            Y = 3464,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Arkinnea",
            Slug = "arkinnea",
            Route = "planet/arkinnea",
            Region = "Mid Rim Territories",
            Description = "Arkinnea is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5284,
            Y = 2565,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Arorua",
            Slug = "arorua",
            Route = "planet/arorua",
            Region = "Outer Rim Territories",
            Description = "Arorua is a star system in the Outer Rim Territories, within the Sertar Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6165,
            Y = 1409,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Arrissa's Field",
            Slug = "arrissas-field",
            Route = "planet/arrissas-field",
            Region = "Expansion Region",
            Description = "Arrissa's Field is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4783,
            Y = 3249,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Arrochar",
            Slug = "arrochar",
            Route = "planet/arrochar",
            Region = "Outer Rim Territories",
            Description = "Arrochar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6524,
            Y = 2149,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Artesia",
            Slug = "artesia",
            Route = "planet/artesia",
            Region = "Expansion Region",
            Description = "Artesia is a star system in the Expansion Region, within the Zuma Sector, at galactic grid P-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5397,
            Y = 2759,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Artorias",
            Slug = "artorias",
            Route = "planet/artorias",
            Region = "Outer Rim Territories",
            Description = "Artorias is a star system in the Outer Rim Territories, within the Myto Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3327,
            Y = 921,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Artus Prime",
            Slug = "artus-prime",
            Route = "planet/artus-prime",
            Region = "Outer Rim Territories",
            Description = "Artus Prime is a star system in the Outer Rim Territories, within the Kwymar Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5762,
            Y = 1215,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Arzid",
            Slug = "arzid",
            Route = "planet/arzid",
            Region = "Outer Rim Territories",
            Description = "Arzid is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7016,
            Y = 2451,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Asation",
            Slug = "asation",
            Route = "planet/asation",
            Region = "Outer Rim Territories",
            Description = "Asation is a star system in the Outer Rim Territories, within the Veragi Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3425,
            Y = 1096,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Askaj",
            Slug = "askaj",
            Route = "planet/askaj",
            Region = "Outer Rim Territories",
            Description = "Askaj is a star system in the Outer Rim Territories, within the Cegul Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4080,
            Y = 4880,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Askaji",
            Slug = "askaji",
            Route = "planet/askaji",
            Region = "Outer Rim Territories",
            Description = "Askaji is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4141,
            Y = 4880,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Asuin",
            Slug = "asuin",
            Route = "planet/asuin",
            Region = "Mid Rim Territories",
            Description = "Asuin is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6609,
            Y = 2839,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Atchorb",
            Slug = "atchorb",
            Route = "planet/atchorb",
            Region = "Outer Rim Territories",
            Description = "Atchorb is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6513,
            Y = 1032,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Athulla",
            Slug = "athulla",
            Route = "planet/athulla",
            Region = "Core Worlds",
            Description = "Athulla is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3760,
            Y = 2483,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Atoa",
            Slug = "atoa",
            Route = "planet/atoa",
            Region = "Mid Rim Territories",
            Description = "Atoa is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5248,
            Y = 2580,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Atoan crystal planet",
            Slug = "atoan-crystal-planet",
            Route = "planet/atoan-crystal-planet",
            Region = "Expansion Region",
            Description = "Atoan crystal planet is a star system in the Expansion Region, within the Zuma Sector, at galactic grid P-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5202,
            Y = 2679,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Atoan tar-pit planet",
            Slug = "atoan-tar-pit-planet",
            Route = "planet/atoan-tar-pit-planet",
            Region = "Mid Rim Territories",
            Description = "Atoan tar-pit planet is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5358,
            Y = 2660,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Atorra",
            Slug = "atorra",
            Route = "planet/atorra",
            Region = "Outer Rim Territories",
            Description = "Atorra is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5605,
            Y = 1376,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Atraken",
            Slug = "atraken",
            Route = "planet/atraken",
            Region = "Outer Rim Territories",
            Description = "Atraken is a star system in the Outer Rim Territories, within the Rolion Sector, at galactic grid Q-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5544,
            Y = 2027,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Attahox",
            Slug = "attahox",
            Route = "planet/attahox",
            Region = "Expansion Region",
            Description = "Attahox is a star system in the Expansion Region, within the Hocatar Sector, at galactic grid P-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5402,
            Y = 2993,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Auratera",
            Slug = "auratera",
            Route = "planet/auratera",
            Region = "Outer Rim Territories",
            Description = "Auratera is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6055,
            Y = 1798,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Aurea",
            Slug = "aurea",
            Route = "planet/aurea",
            Region = "Core Worlds",
            Description = "Aurea is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4139,
            Y = 2864,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Averam",
            Slug = "averam",
            Route = "planet/averam",
            Region = "Outer Rim Territories",
            Description = "Averam is a star system in the Outer Rim Territories, within the Seswenna Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4077,
            Y = 4498,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Avidich",
            Slug = "avidich",
            Route = "planet/avidich",
            Region = "Wild Space",
            Description = "Avidich is a star system in the Wild Space, within the Zuma Sector, at galactic grid E-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1222,
            Y = 2241,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Axxila",
            Slug = "axxila",
            Route = "planet/axxila",
            Region = "Outer Rim Territories",
            Description = "Axxila is a star system in the Outer Rim Territories, within the D'astan Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4802,
            Y = 1542,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Aylayl",
            Slug = "aylayl",
            Route = "planet/aylayl",
            Region = "Outer Rim Territories",
            Description = "Aylayl is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6553,
            Y = 3165,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Azbrian",
            Slug = "azbrian",
            Route = "planet/azbrian",
            Region = "Colonies",
            Description = "Azbrian is a star system in the Colonies, within the Zuma Sector, at galactic grid L-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3871,
            Y = 3157,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Aztubek",
            Slug = "aztubek",
            Route = "planet/aztubek",
            Region = "Outer Rim Territories",
            Description = "Aztubek is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3375,
            Y = 4407,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "B-Foroon",
            Slug = "b-foroon",
            Route = "planet/b-foroon",
            Region = "Outer Rim Territories",
            Description = "B-Foroon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5965,
            Y = 3975,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Baarstal",
            Slug = "baarstal",
            Route = "planet/baarstal",
            Region = "Outer Rim Territories",
            Description = "Baarstal is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4476,
            Y = 4207,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Bacrana",
            Slug = "bacrana",
            Route = "planet/bacrana",
            Region = "Expansion Region",
            Description = "Bacrana is a star system in the Expansion Region, within the Brak Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5069,
            Y = 3558,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Bakkah",
            Slug = "bakkah",
            Route = "planet/bakkah",
            Region = "Outer Rim Territories",
            Description = "Bakkah is a star system in the Outer Rim Territories, within the Thrasybule Sector, at galactic grid P-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5378,
            Y = 1776,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Bal'demnic",
            Slug = "baldemnic",
            Route = "planet/baldemnic",
            Region = "Outer Rim Territories",
            Description = "Bal'demnic is a star system in the Outer Rim Territories, within the Auril Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6126,
            Y = 1896,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Balfron",
            Slug = "balfron",
            Route = "planet/balfron",
            Region = "Core Worlds",
            Description = "Balfron is a star system in the Core Worlds, within the Dolomar Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3422,
            Y = 2434,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Bandomeer",
            Slug = "bandomeer",
            Route = "planet/bandomeer",
            Region = "Outer Rim Territories",
            Description = "Bandomeer is a star system in the Outer Rim Territories, within the Meerian Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4824,
            Y = 1757,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Bannistar Station planetoid",
            Slug = "bannistar-station-planetoid",
            Route = "planet/bannistar-station-planetoid",
            Region = "Expansion Region",
            Description = "Bannistar Station planetoid is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5067,
            Y = 3703,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Banvhar Station",
            Slug = "banvhar-station",
            Route = "planet/banvhar-station",
            Region = "Outer Rim Territories",
            Description = "Banvhar Station is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3134,
            Y = 4490,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Bar Neth",
            Slug = "bar-neth",
            Route = "planet/bar-neth",
            Region = "Outer Rim Territories",
            Description = "Bar Neth is a star system in the Outer Rim Territories, within the Albarrio Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3289,
            Y = 1571,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Bar'leth",
            Slug = "barleth",
            Route = "planet/barleth",
            Region = "Colonies",
            Description = "Bar'leth is a star system in the Colonies, within the Zuma Sector, at galactic grid I-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3787,
            Y = 3212,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Baralou",
            Slug = "baralou",
            Route = "planet/baralou",
            Region = "Outer Rim Territories",
            Description = "Baralou is a star system in the Outer Rim Territories, within the Varada Sector, at galactic grid H-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2227,
            Y = 4880,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Baramorra",
            Slug = "baramorra",
            Route = "planet/baramorra",
            Region = "Outer Rim Territories",
            Description = "Baramorra is a star system in the Outer Rim Territories, within the Carrion Sector, at galactic grid J-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3027,
            Y = 1328,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Bardotta",
            Slug = "bardotta",
            Route = "planet/bardotta",
            Region = "Colonies",
            Description = "Bardotta is a star system in the Colonies, within the Bamula Sector, at galactic grid J-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2963,
            Y = 3198,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Barison",
            Slug = "barison",
            Route = "planet/barison",
            Region = "Outer Rim Territories",
            Description = "Barison is a star system in the Outer Rim Territories, within the Gordian Reach, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5899,
            Y = 1667,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Barkhesh",
            Slug = "barkhesh",
            Route = "planet/barkhesh",
            Region = "Outer Rim Territories",
            Description = "Barkhesh is a star system in the Outer Rim Territories, within the Seitia Sector, at galactic grid K-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3313,
            Y = 4576,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Barnaba",
            Slug = "barnaba",
            Route = "planet/barnaba",
            Region = "Colonies",
            Description = "Barnaba is a star system in the Colonies, within the Tapani Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3791,
            Y = 3199,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Baroonda",
            Slug = "baroonda",
            Route = "planet/baroonda",
            Region = "Outer Rim Territories",
            Description = "Baroonda is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6751,
            Y = 2277,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Baros",
            Slug = "baros",
            Route = "planet/baros",
            Region = "Outer Rim Territories",
            Description = "Baros is a star system in the Outer Rim Territories, within the Dominus Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7178,
            Y = 1918,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Bars Barka",
            Slug = "bars-barka",
            Route = "planet/bars-barka",
            Region = "Mid Rim Territories",
            Description = "Bars Barka is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2900,
            Y = 1626,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Basilisk",
            Slug = "basilisk",
            Route = "planet/basilisk",
            Region = "Core Worlds",
            Description = "Basilisk is a star system in the Core Worlds, within the Coruscant Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3809,
            Y = 2478,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Basteel",
            Slug = "basteel",
            Route = "planet/basteel",
            Region = "Outer Rim Territories",
            Description = "Basteel is a star system in the Outer Rim Territories, within the Corva Sector, at galactic grid P-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5346,
            Y = 911,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Bavva",
            Slug = "bavva",
            Route = "planet/bavva",
            Region = "Outer Rim Territories",
            Description = "Bavva is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3256,
            Y = 4344,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Be'ekk",
            Slug = "beekk",
            Route = "planet/beekk",
            Region = "Outer Rim Territories",
            Description = "Be'ekk is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6809,
            Y = 1489,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Bedlam",
            Slug = "bedlam",
            Route = "planet/bedlam",
            Region = "Mid Rim Territories",
            Description = "Bedlam is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid O-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4908,
            Y = 1830,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Beheboth",
            Slug = "beheboth",
            Route = "planet/beheboth",
            Region = "Outer Rim Territories",
            Description = "Beheboth is a star system in the Outer Rim Territories, within the Sanbra Sector, at galactic grid O-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4807,
            Y = 4166,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Behpour",
            Slug = "behpour",
            Route = "planet/behpour",
            Region = "Outer Rim Territories",
            Description = "Behpour is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4880,
            Y = 4122,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Belderone",
            Slug = "belderone",
            Route = "planet/belderone",
            Region = "Outer Rim Territories",
            Description = "Belderone is a star system in the Outer Rim Territories, within the Belderone Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6185,
            Y = 1777,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Belderone sector prison asteroid",
            Slug = "belderone-sector-prison-asteroid",
            Route = "planet/belderone-sector-prison-asteroid",
            Region = "Core Worlds",
            Description = "Belderone sector prison asteroid is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3883,
            Y = 3065,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Belgaroth",
            Slug = "belgaroth",
            Route = "planet/belgaroth",
            Region = "Core Worlds",
            Description = "Belgaroth is a star system in the Core Worlds, within the Juris Sector, at galactic grid K-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3315,
            Y = 3301,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Belkadan",
            Slug = "belkadan",
            Route = "planet/belkadan",
            Region = "Outer Rim Territories",
            Description = "Belkadan is a star system in the Outer Rim Territories, within the Dalonbian Sector, at galactic grid L-1, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3848,
            Y = 641,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bendii",
            Slug = "bendii",
            Route = "planet/bendii",
            Region = "Outer Rim Territories",
            Description = "Bendii is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3243,
            Y = 4604,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Benja-Rihn",
            Slug = "benja-rihn",
            Route = "planet/benja-rihn",
            Region = "Mid Rim Territories",
            Description = "Benja-Rihn is a star system in the Mid Rim Territories, within the Sevastol Sector, at galactic grid Q-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5597,
            Y = 3486,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Berchest",
            Slug = "berchest",
            Route = "planet/berchest",
            Region = "Inner Rim Territories",
            Description = "Berchest is a star system in the Inner Rim Territories, within the Anthos Sector, at galactic grid N-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4414,
            Y = 2200,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Berzite",
            Slug = "berzite",
            Route = "planet/berzite",
            Region = "Wild Space",
            Description = "Berzite is a star system in the Wild Space, within the Zuma Sector, at galactic grid @-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 353,
            Y = 2630,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bestine IV",
            Slug = "bestine-iv",
            Route = "planet/bestine-iv",
            Region = "Colonies",
            Description = "Bestine IV is a star system in the Colonies, within the Zuma Sector, at galactic grid M-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4093,
            Y = 3461,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Big One",
            Slug = "big-one",
            Route = "planet/big-one",
            Region = "Outer Rim Territories",
            Description = "Big One is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6459,
            Y = 4302,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Biitu",
            Slug = "biitu",
            Route = "planet/biitu",
            Region = "Outer Rim Territories",
            Description = "Biitu is a star system in the Outer Rim Territories, within the Cassander Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3468,
            Y = 1467,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bilbringi VII",
            Slug = "bilbringi-vii",
            Route = "planet/bilbringi-vii",
            Region = "Expansion Region",
            Description = "Bilbringi VII is a star system in the Expansion Region, within the Zuma Sector, at galactic grid J-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3020,
            Y = 2141,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Bimmisaari",
            Slug = "bimmisaari",
            Route = "planet/bimmisaari",
            Region = "Mid Rim Territories",
            Description = "Bimmisaari is a star system in the Mid Rim Territories, within the Halla Sector, at galactic grid R-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6190,
            Y = 2294,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Bith",
            Slug = "bith",
            Route = "planet/bith",
            Region = "Outer Rim Territories",
            Description = "Bith is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4187,
            Y = 4560,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Blackfel",
            Slug = "blackfel",
            Route = "planet/blackfel",
            Region = "Mid Rim Territories",
            Description = "Blackfel is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4327,
            Y = 1928,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Blenjeel",
            Slug = "blenjeel",
            Route = "planet/blenjeel",
            Region = "Mid Rim Territories",
            Description = "Blenjeel is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5534,
            Y = 3666,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Bogden",
            Slug = "bogden",
            Route = "planet/bogden",
            Region = "Expansion Region",
            Description = "Bogden is a star system in the Expansion Region, within the Zuma Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4253,
            Y = 2152,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Bogden 3",
            Slug = "bogden-3",
            Route = "planet/bogden-3",
            Region = "Inner Rim Territories",
            Description = "Bogden 3 is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4074,
            Y = 2153,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Bogoa",
            Slug = "bogoa",
            Route = "planet/bogoa",
            Region = "Expansion Region",
            Description = "Bogoa is a star system in the Expansion Region, within the Immerian Outback, at galactic grid N-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4589,
            Y = 3431,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Bomis Koori IV",
            Slug = "bomis-koori-iv",
            Route = "planet/bomis-koori-iv",
            Region = "Mid Rim Territories",
            Description = "Bomis Koori IV is a star system in the Mid Rim Territories, within the Wornal Sector, at galactic grid K-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3381,
            Y = 4069,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Bonadan",
            Slug = "bonadan",
            Route = "planet/bonadan",
            Region = "Outer Rim Territories",
            Description = "Bonadan is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6435,
            Y = 1112,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Boonta",
            Slug = "boonta",
            Route = "planet/boonta",
            Region = "Outer Rim Territories",
            Description = "Boonta is a star system in the Outer Rim Territories, within the Suolriep Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6457,
            Y = 2160,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Boordii",
            Slug = "boordii",
            Route = "planet/boordii",
            Region = "Expansion Region",
            Description = "Boordii is a star system in the Expansion Region, within the Sumitra Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4714,
            Y = 1851,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Boothi XII",
            Slug = "boothi-xii",
            Route = "planet/boothi-xii",
            Region = "Outer Rim Territories",
            Description = "Boothi XII is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3516,
            Y = 1519,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Boranall",
            Slug = "boranall",
            Route = "planet/boranall",
            Region = "Mid Rim Territories",
            Description = "Boranall is a star system in the Mid Rim Territories, within the Doldur Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5447,
            Y = 3757,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bormus",
            Slug = "bormus",
            Route = "planet/bormus",
            Region = "Expansion Region",
            Description = "Bormus is a star system in the Expansion Region, within the Zuma Sector, at galactic grid N-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4482,
            Y = 3931,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Borosk",
            Slug = "borosk",
            Route = "planet/borosk",
            Region = "Outer Rim Territories",
            Description = "Borosk is a star system in the Outer Rim Territories, within the Prefsbelt Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3259,
            Y = 1448,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Bortras",
            Slug = "bortras",
            Route = "planet/bortras",
            Region = "Outer Rim Territories",
            Description = "Bortras is a star system in the Outer Rim Territories, within the Brema Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4260,
            Y = 4555,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Botajef",
            Slug = "botajef",
            Route = "planet/botajef",
            Region = "Outer Rim Territories",
            Description = "Botajef is a star system in the Outer Rim Territories, within the Belsmuth Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4924,
            Y = 1689,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Bothawui asteroid field",
            Slug = "bothawui-asteroid-field",
            Route = "planet/bothawui-asteroid-field",
            Region = "Outer Rim Territories",
            Description = "Bothawui asteroid field is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6991,
            Y = 1609,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Bovo Yagen",
            Slug = "bovo-yagen",
            Route = "planet/bovo-yagen",
            Region = "Expansion Region",
            Description = "Bovo Yagen is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5046,
            Y = 3288,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Boz Pity",
            Slug = "boz-pity",
            Route = "planet/boz-pity",
            Region = "Mid Rim Territories",
            Description = "Boz Pity is a star system in the Mid Rim Territories, within the Halla Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6659,
            Y = 2362,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Bpfassh",
            Slug = "bpfassh",
            Route = "planet/bpfassh",
            Region = "Outer Rim Territories",
            Description = "Bpfassh is a star system in the Outer Rim Territories, within the Sluis Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4150,
            Y = 4594,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Branth",
            Slug = "branth",
            Route = "planet/branth",
            Region = "Wild Space",
            Description = "Branth is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2017,
            Y = 2611,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Brentaal IV",
            Slug = "brentaal-iv",
            Route = "planet/brentaal-iv",
            Region = "Core Worlds",
            Description = "Brentaal IV is a star system in the Core Worlds, within the Bormea Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3825,
            Y = 2402,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Breta Yaga",
            Slug = "breta-yaga",
            Route = "planet/breta-yaga",
            Region = "Outer Rim Territories",
            Description = "Breta Yaga is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5090,
            Y = 897,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Bri'ahl",
            Slug = "briahl",
            Route = "planet/briahl",
            Region = "Outer Rim Territories",
            Description = "Bri'ahl is a star system in the Outer Rim Territories, within the Bri'ahl Sector, at galactic grid I-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2675,
            Y = 4118,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Bridgeworld",
            Slug = "bridgeworld",
            Route = "planet/bridgeworld",
            Region = "Outer Rim Territories",
            Description = "Bridgeworld is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid A-1, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 626,
            Y = 559,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Bright Jewel asteroid field",
            Slug = "bright-jewel-asteroid-field",
            Route = "planet/bright-jewel-asteroid-field",
            Region = "Colonies",
            Description = "Bright Jewel asteroid field is a star system in the Colonies, within the Zuma Sector, at galactic grid I-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3758,
            Y = 3203,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Brint-wo",
            Slug = "brint-wo",
            Route = "planet/brint-wo",
            Region = "Outer Rim Territories",
            Description = "Brint-wo is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2780,
            Y = 4341,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Brolsam",
            Slug = "brolsam",
            Route = "planet/brolsam",
            Region = "Outer Rim Territories",
            Description = "Brolsam is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4161,
            Y = 555,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Brosi",
            Slug = "brosi",
            Route = "planet/brosi",
            Region = "Outer Rim Territories",
            Description = "Brosi is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6311,
            Y = 907,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Bryndar",
            Slug = "bryndar",
            Route = "planet/bryndar",
            Region = "Outer Rim Territories",
            Description = "Bryndar is a star system in the Outer Rim Territories, within the Dalicron Sector, at galactic grid K-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3290,
            Y = 4582,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Bundil",
            Slug = "bundil",
            Route = "planet/bundil",
            Region = "Outer Rim Territories",
            Description = "Bundil is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6637,
            Y = 4074,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Buoyant",
            Slug = "buoyant",
            Route = "planet/buoyant",
            Region = "Inner Rim Territories",
            Description = "Buoyant is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid J-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3152,
            Y = 3425,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Burska",
            Slug = "burska",
            Route = "planet/burska",
            Region = "Mid Rim Territories",
            Description = "Burska is a star system in the Mid Rim Territories, within the  Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2705,
            Y = 1909,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Butler's Cove",
            Slug = "butlers-cove",
            Route = "planet/butlers-cove",
            Region = "Mid Rim Territories",
            Description = "Butler's Cove is a star system in the Mid Rim Territories, within the Alderaan Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4326,
            Y = 2664,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Byblos",
            Slug = "byblos",
            Route = "planet/byblos",
            Region = "Colonies",
            Description = "Byblos is a star system in the Colonies, within the Parfadi Sector, at galactic grid M-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4347,
            Y = 3101,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "C-Foroon",
            Slug = "c-foroon",
            Route = "planet/c-foroon",
            Region = "Outer Rim Territories",
            Description = "C-Foroon is a star system in the Outer Rim Territories, within the Arkanis Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6271,
            Y = 3953,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Caamas",
            Slug = "caamas",
            Route = "planet/caamas",
            Region = "Core Worlds",
            Description = "Caamas is a star system in the Core Worlds, within the Shelsha Sector, at galactic grid M-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4047,
            Y = 2472,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Cademimu V",
            Slug = "cademimu-v",
            Route = "planet/cademimu-v",
            Region = "Outer Rim Territories",
            Description = "Cademimu V is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4367,
            Y = 1663,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Cadinth",
            Slug = "cadinth",
            Route = "planet/cadinth",
            Region = "Outer Rim Territories",
            Description = "Cadinth is a star system in the Outer Rim Territories, within the Allied Tion, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6379,
            Y = 1663,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Cal-Seti",
            Slug = "cal-seti",
            Route = "planet/cal-seti",
            Region = "Core Worlds",
            Description = "Cal-Seti is a star system in the Core Worlds, within the Torranix Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3460,
            Y = 2647,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Callos",
            Slug = "callos",
            Route = "planet/callos",
            Region = "Mid Rim Territories",
            Description = "Callos is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4352,
            Y = 4133,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Camson",
            Slug = "camson",
            Route = "planet/camson",
            Region = "Outer Rim Territories",
            Description = "Camson is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid F-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2681,
            Y = 2859,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Canyon",
            Slug = "canyon",
            Route = "planet/canyon",
            Region = "Expansion Region",
            Description = "Canyon is a star system in the Expansion Region, within the Montitian Grant, at galactic grid J-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3095,
            Y = 3781,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Caprioril",
            Slug = "caprioril",
            Route = "planet/caprioril",
            Region = "Core Worlds",
            Description = "Caprioril is a star system in the Core Worlds, within the Dolomar Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3426,
            Y = 2342,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Cardooine",
            Slug = "cardooine",
            Route = "planet/cardooine",
            Region = "Outer Rim Territories",
            Description = "Cardooine is a star system in the Outer Rim Territories, within the Jospro Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6026,
            Y = 1832,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Carlac",
            Slug = "carlac",
            Route = "planet/carlac",
            Region = "Outer Rim Territories",
            Description = "Carlac is a star system in the Outer Rim Territories, within the Prefsbelt Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3501,
            Y = 1445,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Carnelion IV",
            Slug = "carnelion-iv",
            Route = "planet/carnelion-iv",
            Region = "Wild Space",
            Description = "Carnelion IV is a star system in the Wild Space, within the Zuma Sector, at galactic grid C-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1620,
            Y = 2940,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Carratos",
            Slug = "carratos",
            Route = "planet/carratos",
            Region = "Expansion Region",
            Description = "Carratos is a star system in the Expansion Region, within the Zuma Sector, at galactic grid K-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3272,
            Y = 2132,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Carreras Major",
            Slug = "carreras-major",
            Route = "planet/carreras-major",
            Region = "Outer Rim Territories",
            Description = "Carreras Major is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3992,
            Y = 4647,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Carreras Minor",
            Slug = "carreras-minor",
            Route = "planet/carreras-minor",
            Region = "Outer Rim Territories",
            Description = "Carreras Minor is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3811,
            Y = 4707,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Cartao",
            Slug = "cartao",
            Route = "planet/cartao",
            Region = "Expansion Region",
            Description = "Cartao is a star system in the Expansion Region, within the Prackla Sector, at galactic grid O-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5046,
            Y = 2173,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Cataalda",
            Slug = "cataalda",
            Route = "planet/cataalda",
            Region = "Mid Rim Territories",
            Description = "Cataalda is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6093,
            Y = 3739,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Celanon",
            Slug = "celanon",
            Route = "planet/celanon",
            Region = "Outer Rim Territories",
            Description = "Celanon is a star system in the Outer Rim Territories, within the D'astan Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5024,
            Y = 1609,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Celwis",
            Slug = "celwis",
            Route = "planet/celwis",
            Region = "Wild Space",
            Description = "Celwis is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1416,
            Y = 2158,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ceriun",
            Slug = "ceriun",
            Route = "planet/ceriun",
            Region = "Outer Rim Territories",
            Description = "Ceriun is a star system in the Outer Rim Territories, within the Nuiri Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5528,
            Y = 1672,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Chad",
            Slug = "chad",
            Route = "planet/chad",
            Region = "Mid Rim Territories",
            Description = "Chad is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6059,
            Y = 1942,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Chalcedon",
            Slug = "chalcedon",
            Route = "planet/chalcedon",
            Region = "Mid Rim Territories",
            Description = "Chalcedon is a star system in the Mid Rim Territories, within the Tashtor Sector, at galactic grid I-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2826,
            Y = 3961,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Challon",
            Slug = "challon",
            Route = "planet/challon",
            Region = "Core Worlds",
            Description = "Challon is a star system in the Core Worlds, within the Challon System, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3876,
            Y = 2385,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Chandel",
            Slug = "chandel",
            Route = "planet/chandel",
            Region = "Outer Rim Territories",
            Description = "Chandel is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6931,
            Y = 4875,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Charis",
            Slug = "charis",
            Route = "planet/charis",
            Region = "Outer Rim Territories",
            Description = "Charis is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4107,
            Y = 504,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Charmath",
            Slug = "charmath",
            Route = "planet/charmath",
            Region = "Core Worlds",
            Description = "Charmath is a star system in the Core Worlds, within the Farrfin Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3437,
            Y = 2390,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Charros",
            Slug = "charros",
            Route = "planet/charros",
            Region = "Mid Rim Territories",
            Description = "Charros is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6222,
            Y = 2331,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Chazwa",
            Slug = "chazwa",
            Route = "planet/chazwa",
            Region = "Inner Rim Territories",
            Description = "Chazwa is a star system in the Inner Rim Territories, within the Orus Sector, at galactic grid N-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4380,
            Y = 2241,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Cheelit",
            Slug = "cheelit",
            Route = "planet/cheelit",
            Region = "Mid Rim Territories",
            Description = "Cheelit is a star system in the Mid Rim Territories, within the Semagi Sector, at galactic grid I-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2768,
            Y = 3916,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Chelloa",
            Slug = "chelloa",
            Route = "planet/chelloa",
            Region = "Mid Rim Territories",
            Description = "Chelloa is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4168,
            Y = 4217,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Chibias",
            Slug = "chibias",
            Route = "planet/chibias",
            Region = "Mid Rim Territories",
            Description = "Chibias is a star system in the Mid Rim Territories, within the Sombure Sector, at galactic grid K-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3340,
            Y = 4185,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Chol",
            Slug = "chol",
            Route = "planet/chol",
            Region = "Outer Rim Territories",
            Description = "Chol is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6956,
            Y = 1379,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Cholganna",
            Slug = "cholganna",
            Route = "planet/cholganna",
            Region = "Outer Rim Territories",
            Description = "Cholganna is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6956,
            Y = 1379,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Chorax",
            Slug = "chorax",
            Route = "planet/chorax",
            Region = "Colonies",
            Description = "Chorax is a star system in the Colonies, within the Rachuk Sector, at galactic grid N-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4450,
            Y = 2959,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Chule",
            Slug = "chule",
            Route = "planet/chule",
            Region = "Mid Rim Territories",
            Description = "Chule is a star system in the Mid Rim Territories, within the Trax Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5613,
            Y = 2533,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Churruma",
            Slug = "churruma",
            Route = "planet/churruma",
            Region = "Outer Rim Territories",
            Description = "Churruma is a star system in the Outer Rim Territories, within the Velcar Sector, at galactic grid J-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3201,
            Y = 1506,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Chuzalla",
            Slug = "chuzalla",
            Route = "planet/chuzalla",
            Region = "Outer Rim Territories",
            Description = "Chuzalla is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6920,
            Y = 3435,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Cilare",
            Slug = "cilare",
            Route = "planet/cilare",
            Region = "Outer Rim Territories",
            Description = "Cilare is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3493,
            Y = 964,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Cilpar",
            Slug = "cilpar",
            Route = "planet/cilpar",
            Region = "Colonies",
            Description = "Cilpar is a star system in the Colonies, within the Zuma Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3644,
            Y = 3354,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Cioral",
            Slug = "cioral",
            Route = "planet/cioral",
            Region = "Wild Space",
            Description = "Cioral is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1531,
            Y = 2110,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Circumtore",
            Slug = "circumtore",
            Route = "planet/circumtore",
            Region = "Outer Rim Territories",
            Description = "Circumtore is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6624,
            Y = 3186,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Cirus II",
            Slug = "cirus-ii",
            Route = "planet/cirus-ii",
            Region = "Outer Rim Territories",
            Description = "Cirus II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6131,
            Y = 4061,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ciutric",
            Slug = "ciutric",
            Route = "planet/ciutric",
            Region = "Outer Rim Territories",
            Description = "Ciutric is a star system in the Outer Rim Territories, within the Ciutric Sector, at galactic grid N-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4569,
            Y = 1407,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Ciutric IV",
            Slug = "ciutric-iv",
            Route = "planet/ciutric-iv",
            Region = "Outer Rim Territories",
            Description = "Ciutric IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4451,
            Y = 1522,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Codia",
            Slug = "codia",
            Route = "planet/codia",
            Region = "Mid Rim Territories",
            Description = "Codia is a star system in the Mid Rim Territories, within the  Sector, at galactic grid H-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2304,
            Y = 3679,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Commenor",
            Slug = "commenor",
            Route = "planet/commenor",
            Region = "Colonies",
            Description = "Commenor is a star system in the Colonies, within the Rachuk Sector, at galactic grid N-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4503,
            Y = 2711,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Constancia",
            Slug = "constancia",
            Route = "planet/constancia",
            Region = "Core Worlds",
            Description = "Constancia is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3309,
            Y = 3152,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Copero",
            Slug = "copero",
            Route = "planet/copero",
            Region = "Wild Space",
            Description = "Copero is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1645,
            Y = 2416,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Corfai",
            Slug = "corfai",
            Route = "planet/corfai",
            Region = "Core Worlds",
            Description = "Corfai is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4172,
            Y = 2933,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Corjain",
            Slug = "corjain",
            Route = "planet/corjain",
            Region = "Outer Rim Territories",
            Description = "Corjain is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4336,
            Y = 561,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Cormit",
            Slug = "cormit",
            Route = "planet/cormit",
            Region = "Wild Space",
            Description = "Cormit is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1695,
            Y = 2177,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Corsin",
            Slug = "corsin",
            Route = "planet/corsin",
            Region = "Expansion Region",
            Description = "Corsin is a star system in the Expansion Region, within the Greater Plooriod, at galactic grid M-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4336,
            Y = 1958,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Corstris",
            Slug = "corstris",
            Route = "planet/corstris",
            Region = "Outer Rim Territories",
            Description = "Corstris is a star system in the Outer Rim Territories, within the Quelii Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4988,
            Y = 1720,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Corulag",
            Slug = "corulag",
            Route = "planet/corulag",
            Region = "Core Worlds",
            Description = "Corulag is a star system in the Core Worlds, within the Bormea Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3880,
            Y = 2339,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Cotellier",
            Slug = "cotellier",
            Route = "planet/cotellier",
            Region = "Outer Rim Territories",
            Description = "Cotellier is a star system in the Outer Rim Territories, within the Rseik Sector, at galactic grid N-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4647,
            Y = 4875,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Council",
            Slug = "council",
            Route = "planet/council",
            Region = "Outer Rim Territories",
            Description = "Council is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3345,
            Y = 4519,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Courkrus",
            Slug = "courkrus",
            Route = "planet/courkrus",
            Region = "Outer Rim Territories",
            Description = "Courkrus is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4936,
            Y = 4414,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Coyn",
            Slug = "coyn",
            Route = "planet/coyn",
            Region = "Outer Rim Territories",
            Description = "Coyn is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4072,
            Y = 4880,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Crondre",
            Slug = "crondre",
            Route = "planet/crondre",
            Region = "Mid Rim Territories",
            Description = "Crondre is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6274,
            Y = 3743,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Csaus",
            Slug = "csaus",
            Route = "planet/csaus",
            Region = "Wild Space",
            Description = "Csaus is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1612,
            Y = 2430,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Culroon III",
            Slug = "culroon-iii",
            Route = "planet/culroon-iii",
            Region = "Outer Rim Territories",
            Description = "Culroon III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5208,
            Y = 4880,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Cyborrea",
            Slug = "cyborrea",
            Route = "planet/cyborrea",
            Region = "Mid Rim Territories",
            Description = "Cyborrea is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6606,
            Y = 2357,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Cyrkon",
            Slug = "cyrkon",
            Route = "planet/cyrkon",
            Region = "Outer Rim Territories",
            Description = "Cyrkon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4813,
            Y = 4318,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "D'ian",
            Slug = "dian",
            Route = "planet/dian",
            Region = "Outer Rim Territories",
            Description = "D'ian is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6380,
            Y = 1000,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "D'rinba IV",
            Slug = "drinba-iv",
            Route = "planet/drinba-iv",
            Region = "Mid Rim Territories",
            Description = "D'rinba IV is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid K-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3303,
            Y = 4153,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Da Soocha",
            Slug = "da-soocha",
            Route = "planet/da-soocha",
            Region = "Mid Rim Territories",
            Description = "Da Soocha is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6379,
            Y = 2739,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Dac",
            Slug = "dac",
            Route = "planet/dac",
            Region = "Outer Rim Territories",
            Description = "Dac is a star system in the Outer Rim Territories, within the Calamari Sector, at galactic grid U-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7056,
            Y = 1743,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Dagro",
            Slug = "dagro",
            Route = "planet/dagro",
            Region = "Mid Rim Territories",
            Description = "Dagro is a star system in the Mid Rim Territories, within the Esuain Sector, at galactic grid P-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5420,
            Y = 1866,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Dagu",
            Slug = "dagu",
            Route = "planet/dagu",
            Region = "Outer Rim Territories",
            Description = "Dagu is a star system in the Outer Rim Territories, within the Instrop Sector, at galactic grid S-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6320,
            Y = 4017,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Daltarra",
            Slug = "daltarra",
            Route = "planet/daltarra",
            Region = "Wild Space",
            Description = "Daltarra is a star system in the Wild Space, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6792,
            Y = 1356,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Daltarri",
            Slug = "daltarri",
            Route = "planet/daltarri",
            Region = "Mid Rim Territories",
            Description = "Daltarri is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5364,
            Y = 2051,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Dandelo",
            Slug = "dandelo",
            Route = "planet/dandelo",
            Region = "Outer Rim Territories",
            Description = "Dandelo is a star system in the Outer Rim Territories, within the Tammuz Sector, at galactic grid T-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6964,
            Y = 3445,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Dandoran",
            Slug = "dandoran",
            Route = "planet/dandoran",
            Region = "Wild Space",
            Description = "Dandoran is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1200,
            Y = 3737,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Danuta",
            Slug = "danuta",
            Route = "planet/danuta",
            Region = "Mid Rim Territories",
            Description = "Danuta is a star system in the Mid Rim Territories, within the Halla Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6293,
            Y = 2292,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Dar'Or",
            Slug = "daror",
            Route = "planet/daror",
            Region = "Mid Rim Territories",
            Description = "Dar'Or is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5915,
            Y = 1838,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Dargulli",
            Slug = "dargulli",
            Route = "planet/dargulli",
            Region = "Inner Rim Territories",
            Description = "Dargulli is a star system in the Inner Rim Territories, within the Pallis Sector, at galactic grid N-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4391,
            Y = 3504,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Darkknell",
            Slug = "darkknell",
            Route = "planet/darkknell",
            Region = "Outer Rim Territories",
            Description = "Darkknell is a star system in the Outer Rim Territories, within the Grumani Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4325,
            Y = 4216,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Darlyn Boda",
            Slug = "darlyn-boda",
            Route = "planet/darlyn-boda",
            Region = "Outer Rim Territories",
            Description = "Darlyn Boda is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3467,
            Y = 4556,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Darvannis",
            Slug = "darvannis",
            Route = "planet/darvannis",
            Region = "Expansion Region",
            Description = "Darvannis is a star system in the Expansion Region, within the Zuma Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5350,
            Y = 2727,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Davnar II",
            Slug = "davnar-ii",
            Route = "planet/davnar-ii",
            Region = "Core Worlds",
            Description = "Davnar II is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3283,
            Y = 2469,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Daxam IV",
            Slug = "daxam-iv",
            Route = "planet/daxam-iv",
            Region = "Wild Space",
            Description = "Daxam IV is a star system in the Wild Space, within the Zuma Sector, at galactic grid C-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1502,
            Y = 4472,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Delari Prime",
            Slug = "delari-prime",
            Route = "planet/delari-prime",
            Region = "Wild Space",
            Description = "Delari Prime is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1306,
            Y = 3331,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Delaya",
            Slug = "delaya",
            Route = "planet/delaya",
            Region = "Core Worlds",
            Description = "Delaya is a star system in the Core Worlds, within the Alderaan Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4103,
            Y = 2509,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Dellalt",
            Slug = "dellalt",
            Route = "planet/dellalt",
            Region = "Outer Rim Territories",
            Description = "Dellalt is a star system in the Outer Rim Territories, within the Tion Hegemony, at galactic grid T-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6734,
            Y = 1757,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Delrakkin",
            Slug = "delrakkin",
            Route = "planet/delrakkin",
            Region = "Outer Rim Territories",
            Description = "Delrakkin is a star system in the Outer Rim Territories, within the Kallea Sector, at galactic grid K-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3425,
            Y = 463,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Demar",
            Slug = "demar",
            Route = "planet/demar",
            Region = "Expansion Region",
            Description = "Demar is a star system in the Expansion Region, within the Brak Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5096,
            Y = 3453,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Demonsgate",
            Slug = "demonsgate",
            Route = "planet/demonsgate",
            Region = "Outer Rim Territories",
            Description = "Demonsgate is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4017,
            Y = 557,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Demophon",
            Slug = "demophon",
            Route = "planet/demophon",
            Region = "Core Worlds",
            Description = "Demophon is a star system in the Core Worlds, within the Demophon Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4164,
            Y = 2526,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Denab",
            Slug = "denab",
            Route = "planet/denab",
            Region = "Outer Rim Territories",
            Description = "Denab is a star system in the Outer Rim Territories, within the Sluis Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4170,
            Y = 4673,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Deneba",
            Slug = "deneba",
            Route = "planet/deneba",
            Region = "Mid Rim Territories",
            Description = "Deneba is a star system in the Mid Rim Territories, within the Maerdocian Sector, at galactic grid Q-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5703,
            Y = 3314,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Dennaskar",
            Slug = "dennaskar",
            Route = "planet/dennaskar",
            Region = "Mid Rim Territories",
            Description = "Dennaskar is a star system in the Mid Rim Territories, within the Manda Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6025,
            Y = 3835,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Dennogra",
            Slug = "dennogra",
            Route = "planet/dennogra",
            Region = "Outer Rim Territories",
            Description = "Dennogra is a star system in the Outer Rim Territories, within the Tharin Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6546,
            Y = 2052,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Denon",
            Slug = "denon",
            Route = "planet/denon",
            Region = "Inner Rim Territories",
            Description = "Denon is a star system in the Inner Rim Territories, within the Iseno Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4486,
            Y = 3212,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Denova",
            Slug = "denova",
            Route = "planet/denova",
            Region = "Outer Rim Territories",
            Description = "Denova is a star system in the Outer Rim Territories, within the Ojoster Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4614,
            Y = 1832,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Dentaal",
            Slug = "dentaal",
            Route = "planet/dentaal",
            Region = "Core Worlds",
            Description = "Dentaal is a star system in the Core Worlds, within the Barma Sector, at galactic grid K-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3614,
            Y = 3245,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Deralia",
            Slug = "deralia",
            Route = "planet/deralia",
            Region = "Outer Rim Territories",
            Description = "Deralia is a star system in the Outer Rim Territories, within the Tammuz Sector, at galactic grid T-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6888,
            Y = 3730,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Derilyn",
            Slug = "derilyn",
            Route = "planet/derilyn",
            Region = "Outer Rim Territories",
            Description = "Derilyn is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4349,
            Y = 4623,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Derra IV",
            Slug = "derra-iv",
            Route = "planet/derra-iv",
            Region = "Expansion Region",
            Description = "Derra IV is a star system in the Expansion Region, within the Kanchen Sector, at galactic grid N-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4391,
            Y = 3679,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Desevro",
            Slug = "desevro",
            Route = "planet/desevro",
            Region = "Outer Rim Territories",
            Description = "Desevro is a star system in the Outer Rim Territories, within the Tion Hegemony, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6335,
            Y = 1582,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Despayre",
            Slug = "despayre",
            Route = "planet/despayre",
            Region = "Outer Rim Territories",
            Description = "Despayre is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3881,
            Y = 1421,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Destreg II",
            Slug = "destreg-ii",
            Route = "planet/destreg-ii",
            Region = "Outer Rim Territories",
            Description = "Destreg II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4390,
            Y = 4358,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Destrillion",
            Slug = "destrillion",
            Route = "planet/destrillion",
            Region = "Outer Rim Territories",
            Description = "Destrillion is a star system in the Outer Rim Territories, within the Myto Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3490,
            Y = 1062,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Devil's Asteroid",
            Slug = "devils-asteroid",
            Route = "planet/devils-asteroid",
            Region = "Outer Rim Territories",
            Description = "Devil's Asteroid is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5070,
            Y = 745,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Deyer",
            Slug = "deyer",
            Route = "planet/deyer",
            Region = "Outer Rim Territories",
            Description = "Deyer is a star system in the Outer Rim Territories, within the Anoat Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3427,
            Y = 4479,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Diab",
            Slug = "diab",
            Route = "planet/diab",
            Region = "Mid Rim Territories",
            Description = "Diab is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2906,
            Y = 1772,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Diado",
            Slug = "diado",
            Route = "planet/diado",
            Region = "Mid Rim Territories",
            Description = "Diado is a star system in the Mid Rim Territories, within the Lifh Sector, at galactic grid R-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6129,
            Y = 2156,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Dibrook",
            Slug = "dibrook",
            Route = "planet/dibrook",
            Region = "Outer Rim Territories",
            Description = "Dibrook is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3534,
            Y = 1485,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Dirha",
            Slug = "dirha",
            Route = "planet/dirha",
            Region = "Mid Rim Territories",
            Description = "Dirha is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6523,
            Y = 2328,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Diyu",
            Slug = "diyu",
            Route = "planet/diyu",
            Region = "Outer Rim Territories",
            Description = "Diyu is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6523,
            Y = 3178,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Dodz",
            Slug = "dodz",
            Route = "planet/dodz",
            Region = "Outer Rim Territories",
            Description = "Dodz is a star system in the Outer Rim Territories, within the Zoraster Sector, at galactic grid U-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7051,
            Y = 3275,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Dolis 3",
            Slug = "dolis-3",
            Route = "planet/dolis-3",
            Region = "Outer Rim Territories",
            Description = "Dolis 3 is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2924,
            Y = 1018,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Dolva Prime",
            Slug = "dolva-prime",
            Route = "planet/dolva-prime",
            Region = "Mid Rim Territories",
            Description = "Dolva Prime is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2635,
            Y = 4020,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Dominus III",
            Slug = "dominus-iii",
            Route = "planet/dominus-iii",
            Region = "Wild Space",
            Description = "Dominus III is a star system in the Wild Space, within the Zuma Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7231,
            Y = 1823,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Doniphon",
            Slug = "doniphon",
            Route = "planet/doniphon",
            Region = "Outer Rim Territories",
            Description = "Doniphon is a star system in the Outer Rim Territories, within the Kwymar Sector, at galactic grid P-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5441,
            Y = 1191,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Dorlo",
            Slug = "dorlo",
            Route = "planet/dorlo",
            Region = "Outer Rim Territories",
            Description = "Dorlo is a star system in the Outer Rim Territories, within the Atravis Sector, at galactic grid L-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3699,
            Y = 4673,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Dorsis",
            Slug = "dorsis",
            Route = "planet/dorsis",
            Region = "Core Worlds",
            Description = "Dorsis is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4114,
            Y = 2834,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Dosuun",
            Slug = "dosuun",
            Route = "planet/dosuun",
            Region = "Outer Rim Territories",
            Description = "Dosuun is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2336,
            Y = 4880,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Douglas III",
            Slug = "douglas-iii",
            Route = "planet/douglas-iii",
            Region = "Outer Rim Territories",
            Description = "Douglas III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7217,
            Y = 2127,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Dractu",
            Slug = "dractu",
            Route = "planet/dractu",
            Region = "Mid Rim Territories",
            Description = "Dractu is a star system in the Mid Rim Territories, within the Lannik Space, at galactic grid Q-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5841,
            Y = 3271,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Draenell's Point",
            Slug = "draenells-point",
            Route = "planet/draenells-point",
            Region = "Mid Rim Territories",
            Description = "Draenell's Point is a star system in the Mid Rim Territories, within the Trax Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5623,
            Y = 2715,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Dragon's Spine",
            Slug = "dragons-spine",
            Route = "planet/dragons-spine",
            Region = "Mid Rim Territories",
            Description = "Dragon's Spine is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5901,
            Y = 3942,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Drall",
            Slug = "drall",
            Route = "planet/drall",
            Region = "Core Worlds",
            Description = "Drall is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4203,
            Y = 2926,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Dreighton",
            Slug = "dreighton",
            Route = "planet/dreighton",
            Region = "Outer Rim Territories",
            Description = "Dreighton is a star system in the Outer Rim Territories, within the Dantus Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3093,
            Y = 1701,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Dressel",
            Slug = "dressel",
            Route = "planet/dressel",
            Region = "Mid Rim Territories",
            Description = "Dressel is a star system in the Mid Rim Territories, within the Noolian Sector, at galactic grid Q-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5801,
            Y = 3359,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Drexel",
            Slug = "drexel",
            Route = "planet/drexel",
            Region = "Outer Rim Territories",
            Description = "Drexel is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5684,
            Y = 4384,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Drogheda",
            Slug = "drogheda",
            Route = "planet/drogheda",
            Region = "Mid Rim Territories",
            Description = "Drogheda is a star system in the Mid Rim Territories, within the Teraab Sector, at galactic grid Q-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5880,
            Y = 2909,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Drongar",
            Slug = "drongar",
            Route = "planet/drongar",
            Region = "Outer Rim Territories",
            Description = "Drongar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6921,
            Y = 1368,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Dubrava",
            Slug = "dubrava",
            Route = "planet/dubrava",
            Region = "Outer Rim Territories",
            Description = "Dubrava is a star system in the Outer Rim Territories, within the Albanin Sector, at galactic grid T-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6990,
            Y = 3235,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Dubrillion",
            Slug = "dubrillion",
            Route = "planet/dubrillion",
            Region = "Outer Rim Territories",
            Description = "Dubrillion is a star system in the Outer Rim Territories, within the Myto Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3481,
            Y = 1061,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Dur Sabon",
            Slug = "dur-sabon",
            Route = "planet/dur-sabon",
            Region = "Outer Rim Territories",
            Description = "Dur Sabon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4940,
            Y = 1439,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Durace",
            Slug = "durace",
            Route = "planet/durace",
            Region = "Wild Space",
            Description = "Durace is a star system in the Wild Space, within the Zuma Sector, at galactic grid H-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2272,
            Y = 1684,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Duroon",
            Slug = "duroon",
            Route = "planet/duroon",
            Region = "Outer Rim Territories",
            Description = "Duroon is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6459,
            Y = 1265,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Earth",
            Slug = "earth",
            Route = "planet/earth",
            Region = "Mid Rim Territories",
            Description = "Earth is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid K-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3536,
            Y = 1782,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Eiattu 6",
            Slug = "eiattu-6",
            Route = "planet/eiattu-6",
            Region = "Mid Rim Territories",
            Description = "Eiattu 6 is a star system in the Mid Rim Territories, within the Ado Sector, at galactic grid L-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3958,
            Y = 4216,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ejolus",
            Slug = "ejolus",
            Route = "planet/ejolus",
            Region = "Inner Rim Territories",
            Description = "Ejolus is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4253,
            Y = 2187,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Elerion",
            Slug = "elerion",
            Route = "planet/elerion",
            Region = "Outer Rim Territories",
            Description = "Elerion is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6170,
            Y = 1785,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Elgit",
            Slug = "elgit",
            Route = "planet/elgit",
            Region = "Outer Rim Territories",
            Description = "Elgit is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6875,
            Y = 2553,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Elrood",
            Slug = "elrood",
            Route = "planet/elrood",
            Region = "Outer Rim Territories",
            Description = "Elrood is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4191,
            Y = 4808,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Enarc",
            Slug = "enarc",
            Route = "planet/enarc",
            Region = "Outer Rim Territories",
            Description = "Enarc is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4824,
            Y = 4266,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Endymion",
            Slug = "endymion",
            Route = "planet/endymion",
            Region = "Outer Rim Territories",
            Description = "Endymion is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5223,
            Y = 1452,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Engira",
            Slug = "engira",
            Route = "planet/engira",
            Region = "Outer Rim Territories",
            Description = "Engira is a star system in the Outer Rim Territories, within the Jospro Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6273,
            Y = 2008,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Eos",
            Slug = "eos",
            Route = "planet/eos",
            Region = "Outer Rim Territories",
            Description = "Eos is a star system in the Outer Rim Territories, within the Cadavine Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5305,
            Y = 4315,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Er'stacia",
            Slug = "erstacia",
            Route = "planet/erstacia",
            Region = "Wild Space",
            Description = "Er'stacia is a star system in the Wild Space, within the Wild Space, at galactic grid V-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7622,
            Y = 2354,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Eredenn Prime",
            Slug = "eredenn-prime",
            Route = "planet/eredenn-prime",
            Region = "Outer Rim Territories",
            Description = "Eredenn Prime is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6410,
            Y = 1700,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Eriadu",
            Slug = "eriadu",
            Route = "planet/eriadu",
            Region = "Outer Rim Territories",
            Description = "Eriadu is a star system in the Outer Rim Territories, within the Seswenna Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4203,
            Y = 4405,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ertrax",
            Slug = "ertrax",
            Route = "planet/ertrax",
            Region = "Outer Rim Territories",
            Description = "Ertrax is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4693,
            Y = 523,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Espirion",
            Slug = "espirion",
            Route = "planet/espirion",
            Region = "Mid Rim Territories",
            Description = "Espirion is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid O-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6191,
            Y = 3890,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Esseles",
            Slug = "esseles",
            Route = "planet/esseles",
            Region = "Core Worlds",
            Description = "Esseles is a star system in the Core Worlds, within the Darpa Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3893,
            Y = 2356,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Essien",
            Slug = "essien",
            Route = "planet/essien",
            Region = "Outer Rim Territories",
            Description = "Essien is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4295,
            Y = 1648,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Essowyn",
            Slug = "essowyn",
            Route = "planet/essowyn",
            Region = "Mid Rim Territories",
            Description = "Essowyn is a star system in the Mid Rim Territories, within the Trax Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5667,
            Y = 2659,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Estaria",
            Slug = "estaria",
            Route = "planet/estaria",
            Region = "Outer Rim Territories",
            Description = "Estaria is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6500,
            Y = 1441,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Esyam",
            Slug = "esyam",
            Route = "planet/esyam",
            Region = "Outer Rim Territories",
            Description = "Esyam is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6624,
            Y = 3025,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Etorasp",
            Slug = "etorasp",
            Route = "planet/etorasp",
            Region = "Expansion Region",
            Description = "Etorasp is a star system in the Expansion Region, within the Hakartha Sector, at galactic grid K-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3326,
            Y = 3902,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Etti IV",
            Slug = "etti-iv",
            Route = "planet/etti-iv",
            Region = "Outer Rim Territories",
            Description = "Etti IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6611,
            Y = 1126,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Exodeen",
            Slug = "exodeen",
            Route = "planet/exodeen",
            Region = "Colonies",
            Description = "Exodeen is a star system in the Colonies, within the Parfadi Sector, at galactic grid M-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4369,
            Y = 2966,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "F'tral",
            Slug = "ftral",
            Route = "planet/ftral",
            Region = "Outer Rim Territories",
            Description = "F'tral is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6717,
            Y = 2360,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Fallowan",
            Slug = "fallowan",
            Route = "planet/fallowan",
            Region = "Outer Rim Territories",
            Description = "Fallowan is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5173,
            Y = 4782,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Far Pando",
            Slug = "far-pando",
            Route = "planet/far-pando",
            Region = "Outer Rim Territories",
            Description = "Far Pando is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6443,
            Y = 3383,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Farboon",
            Slug = "farboon",
            Route = "planet/farboon",
            Region = "Outer Rim Territories",
            Description = "Farboon is a star system in the Outer Rim Territories, within the Tantra Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4369,
            Y = 4593,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Farstine",
            Slug = "farstine",
            Route = "planet/farstine",
            Region = "Mid Rim Territories",
            Description = "Farstine is a star system in the Mid Rim Territories, within the Ryndellian Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5180,
            Y = 4122,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Fedje",
            Slug = "fedje",
            Route = "planet/fedje",
            Region = "Outer Rim Territories",
            Description = "Fedje is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3878,
            Y = 1421,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Fef",
            Slug = "fef",
            Route = "planet/fef",
            Region = "Mid Rim Territories",
            Description = "Fef is a star system in the Mid Rim Territories, within the Glythe Sector, at galactic grid J-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2962,
            Y = 1969,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Felacat",
            Slug = "felacat",
            Route = "planet/felacat",
            Region = "Outer Rim Territories",
            Description = "Felacat is a star system in the Outer Rim Territories, within the Grohl Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6012,
            Y = 3664,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Feriae Junction",
            Slug = "feriae-junction",
            Route = "planet/feriae-junction",
            Region = "Outer Rim Territories",
            Description = "Feriae Junction is a star system in the Outer Rim Territories, within the Thesme Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5069,
            Y = 1569,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Fest",
            Slug = "fest",
            Route = "planet/fest",
            Region = "Outer Rim Territories",
            Description = "Fest is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3800,
            Y = 1458,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Fiddanl",
            Slug = "fiddanl",
            Route = "planet/fiddanl",
            Region = "Outer Rim Territories",
            Description = "Fiddanl is a star system in the Outer Rim Territories, within the Gordian Reach, at galactic grid P-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5229,
            Y = 1759,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Filve",
            Slug = "filve",
            Route = "planet/filve",
            Region = "Mid Rim Territories",
            Description = "Filve is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5978,
            Y = 3807,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Firrerre",
            Slug = "firrerre",
            Route = "planet/firrerre",
            Region = "Outer Rim Territories",
            Description = "Firrerre is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2248,
            Y = 3988,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Firro",
            Slug = "firro",
            Route = "planet/firro",
            Region = "Core Worlds",
            Description = "Firro is a star system in the Core Worlds, within the Farrfin Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3306,
            Y = 2304,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Flashpoint",
            Slug = "flashpoint",
            Route = "planet/flashpoint",
            Region = "Mid Rim Territories",
            Description = "Flashpoint is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid O-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4877,
            Y = 1823,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Flax",
            Slug = "flax",
            Route = "planet/flax",
            Region = "Expansion Region",
            Description = "Flax is a star system in the Expansion Region, within the Sumitra Sector, at galactic grid O-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4986,
            Y = 1965,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Flesh Mongers planet",
            Slug = "flesh-mongers-planet",
            Route = "planet/flesh-mongers-planet",
            Region = "Outer Rim Territories",
            Description = "Flesh Mongers planet is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7225,
            Y = 3508,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Florn",
            Slug = "florn",
            Route = "planet/florn",
            Region = "Outer Rim Territories",
            Description = "Florn is a star system in the Outer Rim Territories, within the Pakuuni Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6679,
            Y = 1488,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Fluwhaka",
            Slug = "fluwhaka",
            Route = "planet/fluwhaka",
            Region = "Outer Rim Territories",
            Description = "Fluwhaka is a star system in the Outer Rim Territories, within the Mortex Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6191,
            Y = 1533,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Force planet",
            Slug = "force-planet",
            Route = "planet/force-planet",
            Region = "Outer Rim Territories",
            Description = "Force planet is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3486,
            Y = 1026,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Formos",
            Slug = "formos",
            Route = "planet/formos",
            Region = "Outer Rim Territories",
            Description = "Formos is a star system in the Outer Rim Territories, within the Kessel Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7012,
            Y = 2550,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Fornax",
            Slug = "fornax",
            Route = "planet/fornax",
            Region = "Mid Rim Territories",
            Description = "Fornax is a star system in the Mid Rim Territories, within the Glythe Sector, at galactic grid J-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2868,
            Y = 1891,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Foundry",
            Slug = "foundry",
            Route = "planet/foundry",
            Region = "Colonies",
            Description = "Foundry is a star system in the Colonies, within the Rachuk Sector, at galactic grid N-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4520,
            Y = 2619,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Fresia",
            Slug = "fresia",
            Route = "planet/fresia",
            Region = "Core Worlds",
            Description = "Fresia is a star system in the Core Worlds, within the Torranix Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3465,
            Y = 2528,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Froz",
            Slug = "froz",
            Route = "planet/froz",
            Region = "Core Worlds",
            Description = "Froz is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4109,
            Y = 2904,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Furies Gate",
            Slug = "furies-gate",
            Route = "planet/furies-gate",
            Region = "Deep Core",
            Description = "Furies Gate is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3813,
            Y = 2703,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Fwillsving",
            Slug = "fwillsving",
            Route = "planet/fwillsving",
            Region = "Outer Rim Territories",
            Description = "Fwillsving is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7017,
            Y = 2596,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "G'rho",
            Slug = "grho",
            Route = "planet/grho",
            Region = "Wild Space",
            Description = "G'rho is a star system in the Wild Space, within the Shiritoku Spur, at galactic grid G-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1879,
            Y = 4091,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "G'wenee",
            Slug = "gwenee",
            Route = "planet/gwenee",
            Region = "Outer Rim Territories",
            Description = "G'wenee is a star system in the Outer Rim Territories, within the Weneen Sector, at galactic grid N-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4558,
            Y = 1730,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Galantos",
            Slug = "galantos",
            Route = "planet/galantos",
            Region = "Core Worlds",
            Description = "Galantos is a star system in the Core Worlds, within the Farlax Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3500,
            Y = 2573,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Galidraan",
            Slug = "galidraan",
            Route = "planet/galidraan",
            Region = "Outer Rim Territories",
            Description = "Galidraan is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6190,
            Y = 1676,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Galpos II",
            Slug = "galpos-ii",
            Route = "planet/galpos-ii",
            Region = "Mid Rim Territories",
            Description = "Galpos II is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6293,
            Y = 3816,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Galtea",
            Slug = "galtea",
            Route = "planet/galtea",
            Region = "Outer Rim Territories",
            Description = "Galtea is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4336,
            Y = 626,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Galzez",
            Slug = "galzez",
            Route = "planet/galzez",
            Region = "Colonies",
            Description = "Galzez is a star system in the Colonies, within the Zuma Sector, at galactic grid F-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2542,
            Y = 2389,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Gamandar",
            Slug = "gamandar",
            Route = "planet/gamandar",
            Region = "Outer Rim Territories",
            Description = "Gamandar is a star system in the Outer Rim Territories, within the Iskalon System, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6077,
            Y = 3998,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ganath",
            Slug = "ganath",
            Route = "planet/ganath",
            Region = "Mid Rim Territories",
            Description = "Ganath is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6170,
            Y = 3092,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Gandle Ott",
            Slug = "gandle-ott",
            Route = "planet/gandle-ott",
            Region = "Outer Rim Territories",
            Description = "Gandle Ott is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4323,
            Y = 432,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ganlihk",
            Slug = "ganlihk",
            Route = "planet/ganlihk",
            Region = "Outer Rim Territories",
            Description = "Ganlihk is a star system in the Outer Rim Territories, within the Dantus Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3109,
            Y = 1623,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Garban",
            Slug = "garban",
            Route = "planet/garban",
            Region = "Outer Rim Territories",
            Description = "Garban is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6607,
            Y = 3801,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Garn",
            Slug = "garn",
            Route = "planet/garn",
            Region = "Outer Rim Territories",
            Description = "Garn is a star system in the Outer Rim Territories, within the Cadma Sector, at galactic grid T-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6986,
            Y = 2043,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Garnib",
            Slug = "garnib",
            Route = "planet/garnib",
            Region = "Outer Rim Territories",
            Description = "Garnib is a star system in the Outer Rim Territories, within the Bozhnee Sector, at galactic grid L-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3883,
            Y = 4421,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Garos IV",
            Slug = "garos-iv",
            Route = "planet/garos-iv",
            Region = "Mid Rim Territories",
            Description = "Garos IV is a star system in the Mid Rim Territories, within the Msst Sector, at galactic grid P-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5313,
            Y = 1931,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Garqi",
            Slug = "garqi",
            Route = "planet/garqi",
            Region = "Outer Rim Territories",
            Description = "Garqi is a star system in the Outer Rim Territories, within the Cassander Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3470,
            Y = 1474,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Gastrula",
            Slug = "gastrula",
            Route = "planet/gastrula",
            Region = "Outer Rim Territories",
            Description = "Gastrula is a star system in the Outer Rim Territories, within the Rayter Sector, at galactic grid J-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3104,
            Y = 4750,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Gavos",
            Slug = "gavos",
            Route = "planet/gavos",
            Region = "Mid Rim Territories",
            Description = "Gavos is a star system in the Mid Rim Territories, within the Kastolar Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5731,
            Y = 2706,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Geedon V",
            Slug = "geedon-v",
            Route = "planet/geedon-v",
            Region = "Outer Rim Territories",
            Description = "Geedon V is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4582,
            Y = 1876,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Gelgelar",
            Slug = "gelgelar",
            Route = "planet/gelgelar",
            Region = "Outer Rim Territories",
            Description = "Gelgelar is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4204,
            Y = 4880,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Genarius",
            Slug = "genarius",
            Route = "planet/genarius",
            Region = "Mid Rim Territories",
            Description = "Genarius is a star system in the Mid Rim Territories, within the Thaere sector, at galactic grid P-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5169,
            Y = 3517,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Gendius V",
            Slug = "gendius-v",
            Route = "planet/gendius-v",
            Region = "Mid Rim Territories",
            Description = "Gendius V is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3107,
            Y = 4268,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Generis",
            Slug = "generis",
            Route = "planet/generis",
            Region = "Outer Rim Territories",
            Description = "Generis is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3936,
            Y = 1461,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Genon",
            Slug = "genon",
            Route = "planet/genon",
            Region = "Inner Rim Territories",
            Description = "Genon is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4651,
            Y = 3245,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Gerrard V",
            Slug = "gerrard-v",
            Route = "planet/gerrard-v",
            Region = "Core Worlds",
            Description = "Gerrard V is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3340,
            Y = 3169,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Gertafuu VI",
            Slug = "gertafuu-vi",
            Route = "planet/gertafuu-vi",
            Region = "Outer Rim Territories",
            Description = "Gertafuu VI is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6580,
            Y = 4395,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ghorman",
            Slug = "ghorman",
            Route = "planet/ghorman",
            Region = "Colonies",
            Description = "Ghorman is a star system in the Colonies, within the Sern Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3725,
            Y = 3410,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Giaca",
            Slug = "giaca",
            Route = "planet/giaca",
            Region = "Outer Rim Territories",
            Description = "Giaca is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3449,
            Y = 4839,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Gibbela",
            Slug = "gibbela",
            Route = "planet/gibbela",
            Region = "Outer Rim Territories",
            Description = "Gibbela is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3694,
            Y = 1491,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Giju",
            Slug = "giju",
            Route = "planet/giju",
            Region = "Colonies",
            Description = "Giju is a star system in the Colonies, within the Herglic Space, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3625,
            Y = 3302,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Gilatter VIII",
            Slug = "gilatter-viii",
            Route = "planet/gilatter-viii",
            Region = "Mid Rim Territories",
            Description = "Gilatter VIII is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2627,
            Y = 1815,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Godo",
            Slug = "godo",
            Route = "planet/godo",
            Region = "Outer Rim Territories",
            Description = "Godo is a star system in the Outer Rim Territories, within the Quence Sector, at galactic grid O-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4875,
            Y = 4505,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Goelitz",
            Slug = "goelitz",
            Route = "planet/goelitz",
            Region = "Mid Rim Territories",
            Description = "Goelitz is a star system in the Mid Rim Territories, within the M'shinni Sector, at galactic grid M-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4377,
            Y = 1812,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Golm",
            Slug = "golm",
            Route = "planet/golm",
            Region = "Mid Rim Territories",
            Description = "Golm is a star system in the Mid Rim Territories, within the Bothan Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5961,
            Y = 3526,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Golm asteroid belt",
            Slug = "golm-asteroid-belt",
            Route = "planet/golm-asteroid-belt",
            Region = "Mid Rim Territories",
            Description = "Golm asteroid belt is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6029,
            Y = 3603,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Golrath",
            Slug = "golrath",
            Route = "planet/golrath",
            Region = "Outer Rim Territories",
            Description = "Golrath is a star system in the Outer Rim Territories, within the Sanbra Sector, at galactic grid O-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5075,
            Y = 4139,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Goroth Prime",
            Slug = "goroth-prime",
            Route = "planet/goroth-prime",
            Region = "Mid Rim Territories",
            Description = "Goroth Prime is a star system in the Mid Rim Territories, within the Trans-Nebular Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6252,
            Y = 3935,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Gorse",
            Slug = "gorse",
            Route = "planet/gorse",
            Region = "Expansion Region",
            Description = "Gorse is a star system in the Expansion Region, within the Zuma Sector, at galactic grid I-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3646,
            Y = 3690,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Gorsh",
            Slug = "gorsh",
            Route = "planet/gorsh",
            Region = "Outer Rim Territories",
            Description = "Gorsh is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5002,
            Y = 1047,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Graf-World",
            Slug = "graf-world",
            Route = "planet/graf-world",
            Region = "Outer Rim Territories",
            Description = "Graf-World is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid E-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2104,
            Y = 3545,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Graveyard of Lost Ships",
            Slug = "graveyard-of-lost-ships",
            Route = "planet/graveyard-of-lost-ships",
            Region = "Outer Rim Territories",
            Description = "Graveyard of Lost Ships is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4481,
            Y = 4386,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Gravlex Med",
            Slug = "gravlex-med",
            Route = "planet/gravlex-med",
            Region = "Outer Rim Territories",
            Description = "Gravlex Med is a star system in the Outer Rim Territories, within the Raioballo Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3870,
            Y = 1206,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Greater Marianas",
            Slug = "greater-marianas",
            Route = "planet/greater-marianas",
            Region = "Outer Rim Territories",
            Description = "Greater Marianas is a star system in the Outer Rim Territories, within the Sevetta Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6548,
            Y = 3835,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Gree",
            Slug = "gree",
            Route = "planet/gree",
            Region = "Outer Rim Territories",
            Description = "Gree is a star system in the Outer Rim Territories, within the Veragi Sector, at galactic grid L-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3637,
            Y = 870,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Gromas Belt",
            Slug = "gromas-belt",
            Route = "planet/gromas-belt",
            Region = "Mid Rim Territories",
            Description = "Gromas Belt is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5690,
            Y = 1878,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "GUHL-JO387O",
            Slug = "guhl-jo387o",
            Route = "planet/guhl-jo387o",
            Region = "Expansion Region",
            Description = "GUHL-JO387O is a star system in the Expansion Region, within the Zuma Sector, at galactic grid M-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5194,
            Y = 3130,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Gulma",
            Slug = "gulma",
            Route = "planet/gulma",
            Region = "Outer Rim Territories",
            Description = "Gulma is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5245,
            Y = 1097,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Gwori",
            Slug = "gwori",
            Route = "planet/gwori",
            Region = "Outer Rim Territories",
            Description = "Gwori is a star system in the Outer Rim Territories, within the Clacis Sector, at galactic grid K-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3500,
            Y = 1211,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Gymelo",
            Slug = "gymelo",
            Route = "planet/gymelo",
            Region = "Outer Rim Territories",
            Description = "Gymelo is a star system in the Outer Rim Territories, within the Bakura Sector, at galactic grid G-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2090,
            Y = 3893,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "H'nemthe",
            Slug = "hnemthe",
            Route = "planet/hnemthe",
            Region = "Outer Rim Territories",
            Description = "H'nemthe is a star system in the Outer Rim Territories, within the Mayagil Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4117,
            Y = 4496,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Haashimut",
            Slug = "haashimut",
            Route = "planet/haashimut",
            Region = "Outer Rim Territories",
            Description = "Haashimut is a star system in the Outer Rim Territories, within the Ash Worlds, at galactic grid S-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6565,
            Y = 1908,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Hakara",
            Slug = "hakara",
            Route = "planet/hakara",
            Region = "Outer Rim Territories",
            Description = "Hakara is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5472,
            Y = 982,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Halm",
            Slug = "halm",
            Route = "planet/halm",
            Region = "Mid Rim Territories",
            Description = "Halm is a star system in the Mid Rim Territories, within the Halm Sector, at galactic grid J-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3109,
            Y = 3885,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Halmad",
            Slug = "halmad",
            Route = "planet/halmad",
            Region = "Outer Rim Territories",
            Description = "Halmad is a star system in the Outer Rim Territories, within the Quelii Sector, at galactic grid N-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4714,
            Y = 1730,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Halowan",
            Slug = "halowan",
            Route = "planet/halowan",
            Region = "Colonies",
            Description = "Halowan is a star system in the Colonies, within the Fakir Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3601,
            Y = 2380,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Halthor",
            Slug = "halthor",
            Route = "planet/halthor",
            Region = "Outer Rim Territories",
            Description = "Halthor is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3805,
            Y = 1661,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Handooine",
            Slug = "handooine",
            Route = "planet/handooine",
            Region = "Outer Rim Territories",
            Description = "Handooine is a star system in the Outer Rim Territories, within the Phelleem Sector, at galactic grid S-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6353,
            Y = 1980,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Harix",
            Slug = "harix",
            Route = "planet/harix",
            Region = "Core Worlds",
            Description = "Harix is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3328,
            Y = 2389,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Haruun Kal",
            Slug = "haruun-kal",
            Route = "planet/haruun-kal",
            Region = "Mid Rim Territories",
            Description = "Haruun Kal is a star system in the Mid Rim Territories, within the Dustig Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4303,
            Y = 4339,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Hefi",
            Slug = "hefi",
            Route = "planet/hefi",
            Region = "Outer Rim Territories",
            Description = "Hefi is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6606,
            Y = 3676,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Helska IV",
            Slug = "helska-iv",
            Route = "planet/helska-iv",
            Region = "Outer Rim Territories",
            Description = "Helska IV is a star system in the Outer Rim Territories, within the Dalonbian Sector, at galactic grid L-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3803,
            Y = 816,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Heptooine",
            Slug = "heptooine",
            Route = "planet/heptooine",
            Region = "Wild Space",
            Description = "Heptooine is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1276,
            Y = 2445,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Herdessa",
            Slug = "herdessa",
            Route = "planet/herdessa",
            Region = "Mid Rim Territories",
            Description = "Herdessa is a star system in the Mid Rim Territories, within the Herdessa Sector, at galactic grid Q-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5635,
            Y = 3948,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "High Chunah",
            Slug = "high-chunah",
            Route = "planet/high-chunah",
            Region = "Outer Rim Territories",
            Description = "High Chunah is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3265,
            Y = 4354,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Hijarna",
            Slug = "hijarna",
            Route = "planet/hijarna",
            Region = "Inner Rim Territories",
            Description = "Hijarna is a star system in the Inner Rim Territories, within the Orus Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4088,
            Y = 2266,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Hishyim",
            Slug = "hishyim",
            Route = "planet/hishyim",
            Region = "Outer Rim Territories",
            Description = "Hishyim is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6565,
            Y = 3760,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Hissrich",
            Slug = "hissrich",
            Route = "planet/hissrich",
            Region = "Outer Rim Territories",
            Description = "Hissrich is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3737,
            Y = 1133,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Hitaka",
            Slug = "hitaka",
            Route = "planet/hitaka",
            Region = "Outer Rim Territories",
            Description = "Hitaka is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4124,
            Y = 1789,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Hockaleg",
            Slug = "hockaleg",
            Route = "planet/hockaleg",
            Region = "Outer Rim Territories",
            Description = "Hockaleg is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4271,
            Y = 4549,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Hollastin",
            Slug = "hollastin",
            Route = "planet/hollastin",
            Region = "Outer Rim Territories",
            Description = "Hollastin is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6462,
            Y = 3167,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Horn Station",
            Slug = "horn-station",
            Route = "planet/horn-station",
            Region = "Outer Rim Territories",
            Description = "Horn Station is a star system in the Outer Rim Territories, within the Lahara Sector, at galactic grid M-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4210,
            Y = 1351,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Horob",
            Slug = "horob",
            Route = "planet/horob",
            Region = "Expansion Region",
            Description = "Horob is a star system in the Expansion Region, within the Vardoss Sector, at galactic grid I-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2855,
            Y = 2225,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Hosra",
            Slug = "hosra",
            Route = "planet/hosra",
            Region = "Core Worlds",
            Description = "Hosra is a star system in the Core Worlds, within the Zuma Sector, at galactic grid G-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3222,
            Y = 2440,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Hosrel XI",
            Slug = "hosrel-xi",
            Route = "planet/hosrel-xi",
            Region = "Outer Rim Territories",
            Description = "Hosrel XI is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7362,
            Y = 2164,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Hoth asteroid belt",
            Slug = "hoth-asteroid-belt",
            Route = "planet/hoth-asteroid-belt",
            Region = "Outer Rim Territories",
            Description = "Hoth asteroid belt is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3259,
            Y = 4485,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Hoth asteroid field",
            Slug = "hoth-asteroid-field",
            Route = "planet/hoth-asteroid-field",
            Region = "Outer Rim Territories",
            Description = "Hoth asteroid field is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3259,
            Y = 4485,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Huloon",
            Slug = "huloon",
            Route = "planet/huloon",
            Region = "Mid Rim Territories",
            Description = "Huloon is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6295,
            Y = 2904,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Humbarine",
            Slug = "humbarine",
            Route = "planet/humbarine",
            Region = "Core Worlds",
            Description = "Humbarine is a star system in the Core Worlds, within the Humbarine Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4336,
            Y = 2718,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Hurikane",
            Slug = "hurikane",
            Route = "planet/hurikane",
            Region = "Wild Space",
            Description = "Hurikane is a star system in the Wild Space, within the Zuma Sector, at galactic grid V-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7596,
            Y = 2451,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Ibaar",
            Slug = "ibaar",
            Route = "planet/ibaar",
            Region = "Mid Rim Territories",
            Description = "Ibaar is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid G-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3127,
            Y = 4268,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Iceberg III",
            Slug = "iceberg-iii",
            Route = "planet/iceberg-iii",
            Region = "Outer Rim Territories",
            Description = "Iceberg III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7253,
            Y = 1679,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ifron",
            Slug = "ifron",
            Route = "planet/ifron",
            Region = "Outer Rim Territories",
            Description = "Ifron is a star system in the Outer Rim Territories, within the Thuris Sector, at galactic grid P-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5355,
            Y = 4480,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ilos",
            Slug = "ilos",
            Route = "planet/ilos",
            Region = "Mid Rim Territories",
            Description = "Ilos is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6022,
            Y = 2614,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ilos Minor",
            Slug = "ilos-minor",
            Route = "planet/ilos-minor",
            Region = "Mid Rim Territories",
            Description = "Ilos Minor is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6058,
            Y = 2664,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Imdaar",
            Slug = "imdaar",
            Route = "planet/imdaar",
            Region = "Outer Rim Territories",
            Description = "Imdaar is a star system in the Outer Rim Territories, within the Dantus Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3106,
            Y = 1737,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Imvur",
            Slug = "imvur",
            Route = "planet/imvur",
            Region = "Core Worlds",
            Description = "Imvur is a star system in the Core Worlds, within the Zuma Sector, at galactic grid H-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3550,
            Y = 2627,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Imynusoph",
            Slug = "imynusoph",
            Route = "planet/imynusoph",
            Region = "Wild Space",
            Description = "Imynusoph is a star system in the Wild Space, within the Zuma Sector, at galactic grid J-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3036,
            Y = 526,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Indoumodo",
            Slug = "indoumodo",
            Route = "planet/indoumodo",
            Region = "Outer Rim Territories",
            Description = "Indoumodo is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6531,
            Y = 4477,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ingo",
            Slug = "ingo",
            Route = "planet/ingo",
            Region = "Mid Rim Territories",
            Description = "Ingo is a star system in the Mid Rim Territories, within the Bortele Sector, at galactic grid R-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5919,
            Y = 2163,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Intuci",
            Slug = "intuci",
            Route = "planet/intuci",
            Region = "Outer Rim Territories",
            Description = "Intuci is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6402,
            Y = 3804,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Iokath",
            Slug = "iokath",
            Route = "planet/iokath",
            Region = "Wild Space",
            Description = "Iokath is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2747,
            Y = 2720,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Iol",
            Slug = "iol",
            Route = "planet/iol",
            Region = "Wild Space",
            Description = "Iol is a star system in the Wild Space, within the Zuma Sector, at galactic grid I-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2610,
            Y = 2636,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ione",
            Slug = "ione",
            Route = "planet/ione",
            Region = "Outer Rim Territories",
            Description = "Ione is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3318,
            Y = 4548,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Iridium",
            Slug = "iridium",
            Route = "planet/iridium",
            Region = "Outer Rim Territories",
            Description = "Iridium is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3653,
            Y = 1439,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Irith",
            Slug = "irith",
            Route = "planet/irith",
            Region = "Mid Rim Territories",
            Description = "Irith is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6397,
            Y = 2922,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Isis",
            Slug = "isis",
            Route = "planet/isis",
            Region = "Outer Rim Territories",
            Description = "Isis is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3529,
            Y = 4491,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Iskadrell",
            Slug = "iskadrell",
            Route = "planet/iskadrell",
            Region = "Outer Rim Territories",
            Description = "Iskadrell is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2116,
            Y = 3584,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Iskalon",
            Slug = "iskalon",
            Route = "planet/iskalon",
            Region = "Mid Rim Territories",
            Description = "Iskalon is a star system in the Mid Rim Territories, within the Trans-Nebular Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6046,
            Y = 3934,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ison",
            Slug = "ison",
            Route = "planet/ison",
            Region = "Outer Rim Territories",
            Description = "Ison is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3407,
            Y = 4441,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ithull",
            Slug = "ithull",
            Route = "planet/ithull",
            Region = "Inner Rim Territories",
            Description = "Ithull is a star system in the Inner Rim Territories, within the Airon Sector, at galactic grid O-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5066,
            Y = 2646,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ivatch",
            Slug = "ivatch",
            Route = "planet/ivatch",
            Region = "Outer Rim Territories",
            Description = "Ivatch is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4125,
            Y = 500,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "J't'p'tan",
            Slug = "jtptan",
            Route = "planet/jtptan",
            Region = "Core Worlds",
            Description = "J't'p'tan is a star system in the Core Worlds, within the Farlax Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3284,
            Y = 2505,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Jaelen",
            Slug = "jaelen",
            Route = "planet/jaelen",
            Region = "Expansion Region",
            Description = "Jaelen is a star system in the Expansion Region, within the Zuma Sector, at galactic grid F-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2676,
            Y = 2064,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Jagomir",
            Slug = "jagomir",
            Route = "planet/jagomir",
            Region = "Outer Rim Territories",
            Description = "Jagomir is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5769,
            Y = 1450,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Jalarren",
            Slug = "jalarren",
            Route = "planet/jalarren",
            Region = "Mid Rim Territories",
            Description = "Jalarren is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid L-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3651,
            Y = 4530,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Jalindi",
            Slug = "jalindi",
            Route = "planet/jalindi",
            Region = "Outer Rim Territories",
            Description = "Jalindi is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-1, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3789,
            Y = 609,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Jamiron",
            Slug = "jamiron",
            Route = "planet/jamiron",
            Region = "Wild Space",
            Description = "Jamiron is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1534,
            Y = 2120,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Janara III",
            Slug = "janara-iii",
            Route = "planet/janara-iii",
            Region = "Inner Rim Territories",
            Description = "Janara III is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid L-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3713,
            Y = 3612,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "JanFathal",
            Slug = "janfathal",
            Route = "planet/janfathal",
            Region = "Outer Rim Territories",
            Description = "JanFathal is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid F-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2636,
            Y = 911,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Jangelle",
            Slug = "jangelle",
            Route = "planet/jangelle",
            Region = "Outer Rim Territories",
            Description = "Jangelle is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4169,
            Y = 658,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Jarnollen",
            Slug = "jarnollen",
            Route = "planet/jarnollen",
            Region = "Mid Rim Territories",
            Description = "Jarnollen is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3728,
            Y = 1980,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Javaal",
            Slug = "javaal",
            Route = "planet/javaal",
            Region = "Core Worlds",
            Description = "Javaal is a star system in the Core Worlds, within the Bormea Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3825,
            Y = 2402,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Jazbina",
            Slug = "jazbina",
            Route = "planet/jazbina",
            Region = "Expansion Region",
            Description = "Jazbina is a star system in the Expansion Region, within the Lostar Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4180,
            Y = 2052,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Jebble",
            Slug = "jebble",
            Route = "planet/jebble",
            Region = "Outer Rim Territories",
            Description = "Jebble is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4602,
            Y = 1987,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Jelucan",
            Slug = "jelucan",
            Route = "planet/jelucan",
            Region = "Colonies",
            Description = "Jelucan is a star system in the Colonies, within the Zuma Sector, at galactic grid H-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3550,
            Y = 2337,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Jerijador",
            Slug = "jerijador",
            Route = "planet/jerijador",
            Region = "Outer Rim Territories",
            Description = "Jerijador is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6876,
            Y = 2385,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Jerne",
            Slug = "jerne",
            Route = "planet/jerne",
            Region = "Outer Rim Territories",
            Description = "Jerne is a star system in the Outer Rim Territories, within the Kanz Sector, at galactic grid N-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4713,
            Y = 1271,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Jestefad",
            Slug = "jestefad",
            Route = "planet/jestefad",
            Region = "Outer Rim Territories",
            Description = "Jestefad is a star system in the Outer Rim Territories, within the Atravis Sector, at galactic grid L-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3670,
            Y = 4754,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Jilrua",
            Slug = "jilrua",
            Route = "planet/jilrua",
            Region = "Mid Rim Territories",
            Description = "Jilrua is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6027,
            Y = 3025,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Joiol",
            Slug = "joiol",
            Route = "planet/joiol",
            Region = "Inner Rim Territories",
            Description = "Joiol is a star system in the Inner Rim Territories, within the Orus Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4103,
            Y = 2201,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Jomark",
            Slug = "jomark",
            Route = "planet/jomark",
            Region = "Outer Rim Territories",
            Description = "Jomark is a star system in the Outer Rim Territories, within the Jospro Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6190,
            Y = 1878,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Joralla",
            Slug = "joralla",
            Route = "planet/joralla",
            Region = "Mid Rim Territories",
            Description = "Joralla is a star system in the Mid Rim Territories, within the Mektrun Sector, at galactic grid L-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3933,
            Y = 4275,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Jovan III",
            Slug = "jovan-iii",
            Route = "planet/jovan-iii",
            Region = "Outer Rim Territories",
            Description = "Jovan III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5322,
            Y = 1610,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Jubalene",
            Slug = "jubalene",
            Route = "planet/jubalene",
            Region = "Outer Rim Territories",
            Description = "Jubalene is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4622,
            Y = 4229,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Jubilar",
            Slug = "jubilar",
            Route = "planet/jubilar",
            Region = "Outer Rim Territories",
            Description = "Jubilar is a star system in the Outer Rim Territories, within the Jubilar Sector, at galactic grid T-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6912,
            Y = 1840,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Kaal",
            Slug = "kaal",
            Route = "planet/kaal",
            Region = "Mid Rim Territories",
            Description = "Kaal is a star system in the Mid Rim Territories, within the Yushan Sector, at galactic grid K-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3348,
            Y = 4169,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kabal",
            Slug = "kabal",
            Route = "planet/kabal",
            Region = "Outer Rim Territories",
            Description = "Kabal is a star system in the Outer Rim Territories, within the Mayagil Sector, at galactic grid N-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4491,
            Y = 4445,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kabray",
            Slug = "kabray",
            Route = "planet/kabray",
            Region = "Mid Rim Territories",
            Description = "Kabray is a star system in the Mid Rim Territories, within the Corweillian Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5477,
            Y = 3669,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kadavo",
            Slug = "kadavo",
            Route = "planet/kadavo",
            Region = "Wild Space",
            Description = "Kadavo is a star system in the Wild Space, within the Chorlian Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6521,
            Y = 1337,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kaddak",
            Slug = "kaddak",
            Route = "planet/kaddak",
            Region = "Deep Core",
            Description = "Kaddak is a star system in the Deep Core, within the Zuma Sector, at galactic grid I-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3672,
            Y = 2685,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kadril",
            Slug = "kadril",
            Route = "planet/kadril",
            Region = "Outer Rim Territories",
            Description = "Kadril is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6120,
            Y = 1793,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kaer",
            Slug = "kaer",
            Route = "planet/kaer",
            Region = "Outer Rim Territories",
            Description = "Kaer is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6267,
            Y = 4223,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kafane",
            Slug = "kafane",
            Route = "planet/kafane",
            Region = "Outer Rim Territories",
            Description = "Kafane is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6603,
            Y = 2301,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kafrene asteroid belt",
            Slug = "kafrene-asteroid-belt",
            Route = "planet/kafrene-asteroid-belt",
            Region = "Expansion Region",
            Description = "Kafrene asteroid belt is a star system in the Expansion Region, within the Zuma Sector, at galactic grid H-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3335,
            Y = 2269,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kal'Shebbol",
            Slug = "kalshebbol",
            Route = "planet/kalshebbol",
            Region = "Outer Rim Territories",
            Description = "Kal'Shebbol is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4236,
            Y = 477,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kalaan",
            Slug = "kalaan",
            Route = "planet/kalaan",
            Region = "Mid Rim Territories",
            Description = "Kalaan is a star system in the Mid Rim Territories, within the Churnis Sector, at galactic grid J-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3115,
            Y = 1962,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kalandis Seven",
            Slug = "kalandis-seven",
            Route = "planet/kalandis-seven",
            Region = "Expansion Region",
            Description = "Kalandis Seven is a star system in the Expansion Region, within the Zuma Sector, at galactic grid N-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4484,
            Y = 3608,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Kalarba",
            Slug = "kalarba",
            Route = "planet/kalarba",
            Region = "Mid Rim Territories",
            Description = "Kalarba is a star system in the Mid Rim Territories, within the Hevvrol Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5157,
            Y = 3679,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kalimahr",
            Slug = "kalimahr",
            Route = "planet/kalimahr",
            Region = "Deep Core",
            Description = "Kalimahr is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3668,
            Y = 2682,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Kalist VI",
            Slug = "kalist-vi",
            Route = "planet/kalist-vi",
            Region = "Deep Core",
            Description = "Kalist VI is a star system in the Deep Core, within the Deep Core Security Zone, at galactic grid K-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3570,
            Y = 3183,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kalkovak",
            Slug = "kalkovak",
            Route = "planet/kalkovak",
            Region = "Mid Rim Territories",
            Description = "Kalkovak is a star system in the Mid Rim Territories, within the Bortele Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6650,
            Y = 2079,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kaller",
            Slug = "kaller",
            Route = "planet/kaller",
            Region = "Core Worlds",
            Description = "Kaller is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3985,
            Y = 2479,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kammia",
            Slug = "kammia",
            Route = "planet/kammia",
            Region = "Wild Space",
            Description = "Kammia is a star system in the Wild Space, within the Shiritoku Spur, at galactic grid G-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1984,
            Y = 3978,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kamparas",
            Slug = "kamparas",
            Route = "planet/kamparas",
            Region = "Core Worlds",
            Description = "Kamparas is a star system in the Core Worlds, within the Dolomar Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3541,
            Y = 2476,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kampe",
            Slug = "kampe",
            Route = "planet/kampe",
            Region = "Deep Core",
            Description = "Kampe is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3678,
            Y = 2925,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kardoa",
            Slug = "kardoa",
            Route = "planet/kardoa",
            Region = "Wild Space",
            Description = "Kardoa is a star system in the Wild Space, within the Zuma Sector, at galactic grid @-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 297,
            Y = 2576,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Katalla",
            Slug = "katalla",
            Route = "planet/katalla",
            Region = "Mid Rim Territories",
            Description = "Katalla is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6129,
            Y = 2681,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Katanos VII",
            Slug = "katanos-vii",
            Route = "planet/katanos-vii",
            Region = "Mid Rim Territories",
            Description = "Katanos VII is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5834,
            Y = 3746,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Katarr",
            Slug = "katarr",
            Route = "planet/katarr",
            Region = "Mid Rim Territories",
            Description = "Katarr is a star system in the Mid Rim Territories, within the Vensori Sector, at galactic grid O-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4781,
            Y = 2218,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Katraasii",
            Slug = "katraasii",
            Route = "planet/katraasii",
            Region = "Outer Rim Territories",
            Description = "Katraasii is a star system in the Outer Rim Territories, within the Belsmuth Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4973,
            Y = 1601,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kattada",
            Slug = "kattada",
            Route = "planet/kattada",
            Region = "Colonies",
            Description = "Kattada is a star system in the Colonies, within the Darpa Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4347,
            Y = 2550,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Keeper's World",
            Slug = "keepers-world",
            Route = "planet/keepers-world",
            Region = "Outer Rim Territories",
            Description = "Keeper's World is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4765,
            Y = 1456,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kejim",
            Slug = "kejim",
            Route = "planet/kejim",
            Region = "Outer Rim Territories",
            Description = "Kejim is a star system in the Outer Rim Territories, within the Sertar Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5993,
            Y = 1475,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Keldooine",
            Slug = "keldooine",
            Route = "planet/keldooine",
            Region = "Mid Rim Territories",
            Description = "Keldooine is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6029,
            Y = 2577,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kellux",
            Slug = "kellux",
            Route = "planet/kellux",
            Region = "Expansion Region",
            Description = "Kellux is a star system in the Expansion Region, within the Zuma Sector, at galactic grid G-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2983,
            Y = 2275,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Keresia",
            Slug = "keresia",
            Route = "planet/keresia",
            Region = "Mid Rim Territories",
            Description = "Keresia is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5448,
            Y = 1813,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kerev Doi",
            Slug = "kerev-doi",
            Route = "planet/kerev-doi",
            Region = "Core Worlds",
            Description = "Kerev Doi is a star system in the Core Worlds, within the Zuma Sector, at galactic grid H-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3395,
            Y = 2550,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kerilt",
            Slug = "kerilt",
            Route = "planet/kerilt",
            Region = "Mid Rim Territories",
            Description = "Kerilt is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5470,
            Y = 3652,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Keskin",
            Slug = "keskin",
            Route = "planet/keskin",
            Region = "Outer Rim Territories",
            Description = "Keskin is a star system in the Outer Rim Territories, within the Koradin Sector, at galactic grid J-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2977,
            Y = 4503,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Kestavel",
            Slug = "kestavel",
            Route = "planet/kestavel",
            Region = "Mid Rim Territories",
            Description = "Kestavel is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4330,
            Y = 2689,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ketaris",
            Slug = "ketaris",
            Route = "planet/ketaris",
            Region = "Outer Rim Territories",
            Description = "Ketaris is a star system in the Outer Rim Territories, within the Oplovis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3980,
            Y = 1555,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Keyorin",
            Slug = "keyorin",
            Route = "planet/keyorin",
            Region = "Outer Rim Territories",
            Description = "Keyorin is a star system in the Outer Rim Territories, within the Belderone Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6178,
            Y = 1591,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Kharzet III",
            Slug = "kharzet-iii",
            Route = "planet/kharzet-iii",
            Region = "Outer Rim Territories",
            Description = "Kharzet III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6046,
            Y = 1285,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kholes",
            Slug = "kholes",
            Route = "planet/kholes",
            Region = "Mid Rim Territories",
            Description = "Kholes is a star system in the Mid Rim Territories, within the Elbaran Sector, at galactic grid J-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2908,
            Y = 4178,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Khorm",
            Slug = "khorm",
            Route = "planet/khorm",
            Region = "Mid Rim Territories",
            Description = "Khorm is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5239,
            Y = 2054,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Khubeaie",
            Slug = "khubeaie",
            Route = "planet/khubeaie",
            Region = "Outer Rim Territories",
            Description = "Khubeaie is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5972,
            Y = 4298,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kiara's Comet Cluster",
            Slug = "kiaras-comet-cluster",
            Route = "planet/kiaras-comet-cluster",
            Region = "Outer Rim Territories",
            Description = "Kiara's Comet Cluster is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid @-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 363,
            Y = 964,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kidriff 5",
            Slug = "kidriff-5",
            Route = "planet/kidriff-5",
            Region = "Inner Rim Territories",
            Description = "Kidriff 5 is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4061,
            Y = 2194,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kidron",
            Slug = "kidron",
            Route = "planet/kidron",
            Region = "Outer Rim Territories",
            Description = "Kidron is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4182,
            Y = 4834,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kiffu",
            Slug = "kiffu",
            Route = "planet/kiffu",
            Region = "Inner Rim Territories",
            Description = "Kiffu is a star system in the Inner Rim Territories, within the Jaso Sector, at galactic grid L-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3725,
            Y = 3477,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kile II",
            Slug = "kile-ii",
            Route = "planet/kile-ii",
            Region = "Outer Rim Territories",
            Description = "Kile II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6402,
            Y = 1894,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kimanan",
            Slug = "kimanan",
            Route = "planet/kimanan",
            Region = "Inner Rim Territories",
            Description = "Kimanan is a star system in the Inner Rim Territories, within the Orus Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4102,
            Y = 2239,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kinooine",
            Slug = "kinooine",
            Route = "planet/kinooine",
            Region = "Wild Space",
            Description = "Kinooine is a star system in the Wild Space, within the Kallea Sector, at galactic grid J-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2893,
            Y = 517,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kinoss",
            Slug = "kinoss",
            Route = "planet/kinoss",
            Region = "Wild Space",
            Description = "Kinoss is a star system in the Wild Space, within the Zuma Sector, at galactic grid E-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1104,
            Y = 2106,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kinrah",
            Slug = "kinrah",
            Route = "planet/kinrah",
            Region = "Mid Rim Territories",
            Description = "Kinrah is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3814,
            Y = 3951,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kintoni",
            Slug = "kintoni",
            Route = "planet/kintoni",
            Region = "Outer Rim Territories",
            Description = "Kintoni is a star system in the Outer Rim Territories, within the Ash Worlds, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6424,
            Y = 1662,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kirdo III",
            Slug = "kirdo-iii",
            Route = "planet/kirdo-iii",
            Region = "Outer Rim Territories",
            Description = "Kirdo III is a star system in the Outer Rim Territories, within the Xappyh Sector, at galactic grid N-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4625,
            Y = 4647,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kiros",
            Slug = "kiros",
            Route = "planet/kiros",
            Region = "Expansion Region",
            Description = "Kiros is a star system in the Expansion Region, within the Ehosiq Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3761,
            Y = 2116,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kirrek",
            Slug = "kirrek",
            Route = "planet/kirrek",
            Region = "Deep Core",
            Description = "Kirrek is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3690,
            Y = 2642,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kirtarkin",
            Slug = "kirtarkin",
            Route = "planet/kirtarkin",
            Region = "Outer Rim Territories",
            Description = "Kirtarkin is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3538,
            Y = 4467,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kishpaugh",
            Slug = "kishpaugh",
            Route = "planet/kishpaugh",
            Region = "Expansion Region",
            Description = "Kishpaugh is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5048,
            Y = 3889,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kiskua",
            Slug = "kiskua",
            Route = "planet/kiskua",
            Region = "Mid Rim Territories",
            Description = "Kiskua is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6456,
            Y = 3077,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Koba",
            Slug = "koba",
            Route = "planet/koba",
            Region = "Mid Rim Territories",
            Description = "Koba is a star system in the Mid Rim Territories, within the Narrant Sector, at galactic grid J-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3002,
            Y = 3970,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kolaador",
            Slug = "kolaador",
            Route = "planet/kolaador",
            Region = "Outer Rim Territories",
            Description = "Kolaador is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5911,
            Y = 4148,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Kolatill",
            Slug = "kolatill",
            Route = "planet/kolatill",
            Region = "Outer Rim Territories",
            Description = "Kolatill is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4176,
            Y = 652,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Koltine",
            Slug = "koltine",
            Route = "planet/koltine",
            Region = "Outer Rim Territories",
            Description = "Koltine is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3808,
            Y = 644,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Konkiv",
            Slug = "konkiv",
            Route = "planet/konkiv",
            Region = "Wild Space",
            Description = "Konkiv is a star system in the Wild Space, within the Zuma Sector, at galactic grid A-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 726,
            Y = 2088,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kooriva",
            Slug = "kooriva",
            Route = "planet/kooriva",
            Region = "Inner Rim Territories",
            Description = "Kooriva is a star system in the Inner Rim Territories, within the Fakir Sector, at galactic grid M-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4225,
            Y = 3464,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Korad",
            Slug = "korad",
            Route = "planet/korad",
            Region = "Outer Rim Territories",
            Description = "Korad is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4176,
            Y = 4594,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Korda Six",
            Slug = "korda-six",
            Route = "planet/korda-six",
            Region = "Expansion Region",
            Description = "Korda Six is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5054,
            Y = 2115,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Korteen asteroid belt",
            Slug = "korteen-asteroid-belt",
            Route = "planet/korteen-asteroid-belt",
            Region = "Outer Rim Territories",
            Description = "Korteen asteroid belt is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5565,
            Y = 4286,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kothlis",
            Slug = "kothlis",
            Route = "planet/kothlis",
            Region = "Mid Rim Territories",
            Description = "Kothlis is a star system in the Mid Rim Territories, within the Bothan Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5990,
            Y = 3544,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kothlis asteroid field",
            Slug = "kothlis-asteroid-field",
            Route = "planet/kothlis-asteroid-field",
            Region = "Mid Rim Territories",
            Description = "Kothlis asteroid field is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6056,
            Y = 3523,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kovor",
            Slug = "kovor",
            Route = "planet/kovor",
            Region = "Outer Rim Territories",
            Description = "Kovor is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2859,
            Y = 4464,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kowak",
            Slug = "kowak",
            Route = "planet/kowak",
            Region = "Outer Rim Territories",
            Description = "Kowak is a star system in the Outer Rim Territories, within the Sevetta Sector, at galactic grid S-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6612,
            Y = 3880,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Krake's Planet",
            Slug = "krakes-planet",
            Route = "planet/krakes-planet",
            Region = "Outer Rim Territories",
            Description = "Krake's Planet is a star system in the Outer Rim Territories, within the Demetras Sector, at galactic grid P-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5362,
            Y = 2014,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Krant",
            Slug = "krant",
            Route = "planet/krant",
            Region = "Mid Rim Territories",
            Description = "Krant is a star system in the Mid Rim Territories, within the Bothan Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6100,
            Y = 3427,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Krayiss Two",
            Slug = "krayiss-two",
            Route = "planet/krayiss-two",
            Region = "Outer Rim Territories",
            Description = "Krayiss Two is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6104,
            Y = 1536,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Krev Coeur",
            Slug = "krev-coeur",
            Route = "planet/krev-coeur",
            Region = "Core Worlds",
            Description = "Krev Coeur is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3700,
            Y = 2502,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Kril'Dor",
            Slug = "krildor",
            Route = "planet/krildor",
            Region = "Mid Rim Territories",
            Description = "Kril'Dor is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2652,
            Y = 1951,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Krykas asteroid field",
            Slug = "krykas-asteroid-field",
            Route = "planet/krykas-asteroid-field",
            Region = "Expansion Region",
            Description = "Krykas asteroid field is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3743,
            Y = 4064,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ktath'atn",
            Slug = "ktathatn",
            Route = "planet/ktathatn",
            Region = "Expansion Region",
            Description = "Ktath'atn is a star system in the Expansion Region, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5379,
            Y = 2776,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Kuan",
            Slug = "kuan",
            Route = "planet/kuan",
            Region = "Outer Rim Territories",
            Description = "Kuan is a star system in the Outer Rim Territories, within the Imperial Space, at galactic grid N-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4480,
            Y = 4880,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Kumru",
            Slug = "kumru",
            Route = "planet/kumru",
            Region = "Outer Rim Territories",
            Description = "Kumru is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3284,
            Y = 4475,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Kuras III",
            Slug = "kuras-iii",
            Route = "planet/kuras-iii",
            Region = "Outer Rim Territories",
            Description = "Kuras III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4258,
            Y = 4734,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kuratooine",
            Slug = "kuratooine",
            Route = "planet/kuratooine",
            Region = "Mid Rim Territories",
            Description = "Kuratooine is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2890,
            Y = 1569,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Kwenn",
            Slug = "kwenn",
            Route = "planet/kwenn",
            Region = "Mid Rim Territories",
            Description = "Kwenn is a star system in the Mid Rim Territories, within the Bright Jewel Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6079,
            Y = 2684,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Laakteen",
            Slug = "laakteen",
            Route = "planet/laakteen",
            Region = "Core Worlds",
            Description = "Laakteen is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3673,
            Y = 3278,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ladro",
            Slug = "ladro",
            Route = "planet/ladro",
            Region = "Colonies",
            Description = "Ladro is a star system in the Colonies, within the Zuma Sector, at galactic grid J-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2931,
            Y = 3233,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Lafra",
            Slug = "lafra",
            Route = "planet/lafra",
            Region = "Outer Rim Territories",
            Description = "Lafra is a star system in the Outer Rim Territories, within the Wyl Sector, at galactic grid R-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6015,
            Y = 1282,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Lahn",
            Slug = "lahn",
            Route = "planet/lahn",
            Region = "Wild Space",
            Description = "Lahn is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2011,
            Y = 2712,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lahsbane",
            Slug = "lahsbane",
            Route = "planet/lahsbane",
            Region = "Mid Rim Territories",
            Description = "Lahsbane is a star system in the Mid Rim Territories, within the Onatos Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6024,
            Y = 3746,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Lamaredd",
            Slug = "lamaredd",
            Route = "planet/lamaredd",
            Region = "Outer Rim Territories",
            Description = "Lamaredd is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6466,
            Y = 4438,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lan Barell",
            Slug = "lan-barell",
            Route = "planet/lan-barell",
            Region = "Outer Rim Territories",
            Description = "Lan Barell is a star system in the Outer Rim Territories, within the Hook Nebula, at galactic grid O-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5095,
            Y = 4515,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lanteeb",
            Slug = "lanteeb",
            Route = "planet/lanteeb",
            Region = "Outer Rim Territories",
            Description = "Lanteeb is a star system in the Outer Rim Territories, within the Bri'ahl Sector, at galactic grid I-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2527,
            Y = 4135,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Lantillies",
            Slug = "lantillies",
            Route = "planet/lantillies",
            Region = "Mid Rim Territories",
            Description = "Lantillies is a star system in the Mid Rim Territories, within the Lantillian Sector, at galactic grid P-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5269,
            Y = 2214,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Lao-mon",
            Slug = "lao-mon",
            Route = "planet/lao-mon",
            Region = "Core Worlds",
            Description = "Lao-mon is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3758,
            Y = 3082,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lapez 3",
            Slug = "lapez-3",
            Route = "planet/lapez-3",
            Region = "Outer Rim Territories",
            Description = "Lapez 3 is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5665,
            Y = 1462,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lazerian IV",
            Slug = "lazerian-iv",
            Route = "planet/lazerian-iv",
            Region = "Expansion Region",
            Description = "Lazerian IV is a star system in the Expansion Region, within the Kira Sector, at galactic grid N-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4481,
            Y = 3829,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Lefrani",
            Slug = "lefrani",
            Route = "planet/lefrani",
            Region = "Outer Rim Territories",
            Description = "Lefrani is a star system in the Outer Rim Territories, within the Atravis Sector, at galactic grid L-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3670,
            Y = 4754,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Lelmra",
            Slug = "lelmra",
            Route = "planet/lelmra",
            Region = "Mid Rim Territories",
            Description = "Lelmra is a star system in the Mid Rim Territories, within the Churba Sector, at galactic grid P-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5400,
            Y = 3528,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lenico Belt",
            Slug = "lenico-belt",
            Route = "planet/lenico-belt",
            Region = "Outer Rim Territories",
            Description = "Lenico Belt is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3728,
            Y = 1586,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lenico IV",
            Slug = "lenico-iv",
            Route = "planet/lenico-iv",
            Region = "Outer Rim Territories",
            Description = "Lenico IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3712,
            Y = 1712,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Leria Kerlsil",
            Slug = "leria-kerlsil",
            Route = "planet/leria-kerlsil",
            Region = "Core Worlds",
            Description = "Leria Kerlsil is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4127,
            Y = 2509,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Leritor",
            Slug = "leritor",
            Route = "planet/leritor",
            Region = "Mid Rim Territories",
            Description = "Leritor is a star system in the Mid Rim Territories, within the Yucrales Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5824,
            Y = 3706,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lettow",
            Slug = "lettow",
            Route = "planet/lettow",
            Region = "Core Worlds",
            Description = "Lettow is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4247,
            Y = 2906,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lew'el",
            Slug = "lewel",
            Route = "planet/lewel",
            Region = "Outer Rim Territories",
            Description = "Lew'el is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5064,
            Y = 1106,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Liinade III",
            Slug = "liinade-iii",
            Route = "planet/liinade-iii",
            Region = "Outer Rim Territories",
            Description = "Liinade III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4626,
            Y = 1565,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Linuri",
            Slug = "linuri",
            Route = "planet/linuri",
            Region = "Mid Rim Territories",
            Description = "Linuri is a star system in the Mid Rim Territories, within the Doldur Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5378,
            Y = 3804,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Lirra",
            Slug = "lirra",
            Route = "planet/lirra",
            Region = "Outer Rim Territories",
            Description = "Lirra is a star system in the Outer Rim Territories, within the Baxel Sector, at galactic grid U-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7407,
            Y = 2999,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Llanic",
            Slug = "llanic",
            Route = "planet/llanic",
            Region = "Outer Rim Territories",
            Description = "Llanic is a star system in the Outer Rim Territories, within the Karthakk Sector, at galactic grid Q-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5613,
            Y = 4095,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lok",
            Slug = "lok",
            Route = "planet/lok",
            Region = "Outer Rim Territories",
            Description = "Lok is a star system in the Outer Rim Territories, within the Karthakk Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5702,
            Y = 4149,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lokondo",
            Slug = "lokondo",
            Route = "planet/lokondo",
            Region = "Outer Rim Territories",
            Description = "Lokondo is a star system in the Outer Rim Territories, within the Braxant Sector, at galactic grid J-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3012,
            Y = 1069,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Lola Sayu",
            Slug = "lola-sayu",
            Route = "planet/lola-sayu",
            Region = "Outer Rim Territories",
            Description = "Lola Sayu is a star system in the Outer Rim Territories, within the Belderone Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6202,
            Y = 1643,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lolnar",
            Slug = "lolnar",
            Route = "planet/lolnar",
            Region = "Colonies",
            Description = "Lolnar is a star system in the Colonies, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4340,
            Y = 2954,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Loovria",
            Slug = "loovria",
            Route = "planet/loovria",
            Region = "Mid Rim Territories",
            Description = "Loovria is a star system in the Mid Rim Territories, within the Juvex Sector, at galactic grid L-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3960,
            Y = 4469,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Loronar",
            Slug = "loronar",
            Route = "planet/loronar",
            Region = "Colonies",
            Description = "Loronar is a star system in the Colonies, within the Parfadi Sector, at galactic grid M-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4325,
            Y = 3060,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Lorta",
            Slug = "lorta",
            Route = "planet/lorta",
            Region = "Mid Rim Territories",
            Description = "Lorta is a star system in the Mid Rim Territories, within the Gendius Sector, at galactic grid J-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3214,
            Y = 4270,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lotho Minor",
            Slug = "lotho-minor",
            Route = "planet/lotho-minor",
            Region = "Outer Rim Territories",
            Description = "Lotho Minor is a star system in the Outer Rim Territories, within the Wazta Sector, at galactic grid I-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2678,
            Y = 4189,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lubang Minor",
            Slug = "lubang-minor",
            Route = "planet/lubang-minor",
            Region = "Outer Rim Territories",
            Description = "Lubang Minor is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5676,
            Y = 1245,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Luprora",
            Slug = "luprora",
            Route = "planet/luprora",
            Region = "Outer Rim Territories",
            Description = "Luprora is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3913,
            Y = 1324,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Lutrillia",
            Slug = "lutrillia",
            Route = "planet/lutrillia",
            Region = "Outer Rim Territories",
            Description = "Lutrillia is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid J-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3192,
            Y = 4418,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "M'Bardi",
            Slug = "mbardi",
            Route = "planet/mbardi",
            Region = "Outer Rim Territories",
            Description = "M'Bardi is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5468,
            Y = 1386,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "M'haeli",
            Slug = "mhaeli",
            Route = "planet/mhaeli",
            Region = "Expansion Region",
            Description = "M'haeli is a star system in the Expansion Region, within the Majoor Sector, at galactic grid N-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4436,
            Y = 3813,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "M'Hanna",
            Slug = "mhanna",
            Route = "planet/mhanna",
            Region = "Outer Rim Territories",
            Description = "M'Hanna is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6674,
            Y = 2900,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "M4-78",
            Slug = "m4-78",
            Route = "planet/m4-78",
            Region = "Inner Rim Territories",
            Description = "M4-78 is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid O-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5024,
            Y = 2421,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ma'ar Shaddam",
            Slug = "maar-shaddam",
            Route = "planet/maar-shaddam",
            Region = "Outer Rim Territories",
            Description = "Ma'ar Shaddam is a star system in the Outer Rim Territories, within the Rseik Sector, at galactic grid N-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4692,
            Y = 4880,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Maicombe",
            Slug = "maicombe",
            Route = "planet/maicombe",
            Region = "Mid Rim Territories",
            Description = "Maicombe is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid K-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3440,
            Y = 1830,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Mairne",
            Slug = "mairne",
            Route = "planet/mairne",
            Region = "Outer Rim Territories",
            Description = "Mairne is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4357,
            Y = 489,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Makem Te",
            Slug = "makem-te",
            Route = "planet/makem-te",
            Region = "Outer Rim Territories",
            Description = "Makem Te is a star system in the Outer Rim Territories, within the Nilgaard Sector, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6457,
            Y = 1473,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Mala",
            Slug = "mala",
            Route = "planet/mala",
            Region = "Outer Rim Territories",
            Description = "Mala is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3637,
            Y = 4699,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Malicar 3",
            Slug = "malicar-3",
            Route = "planet/malicar-3",
            Region = "Outer Rim Territories",
            Description = "Malicar 3 is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4690,
            Y = 1235,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Malrev IV",
            Slug = "malrev-iv",
            Route = "planet/malrev-iv",
            Region = "Outer Rim Territories",
            Description = "Malrev IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5305,
            Y = 1696,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Malterra",
            Slug = "malterra",
            Route = "planet/malterra",
            Region = "Deep Core",
            Description = "Malterra is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3823,
            Y = 2612,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Manda",
            Slug = "manda",
            Route = "planet/manda",
            Region = "Mid Rim Territories",
            Description = "Manda is a star system in the Mid Rim Territories, within the Manda Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6201,
            Y = 3652,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Manpha",
            Slug = "manpha",
            Route = "planet/manpha",
            Region = "Outer Rim Territories",
            Description = "Manpha is a star system in the Outer Rim Territories, within the Seitia Sector, at galactic grid K-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3314,
            Y = 4808,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Mantessa",
            Slug = "mantessa",
            Route = "planet/mantessa",
            Region = "Inner Rim Territories",
            Description = "Mantessa is a star system in the Inner Rim Territories, within the Orus Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4260,
            Y = 2241,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Mantooine",
            Slug = "mantooine",
            Route = "planet/mantooine",
            Region = "Outer Rim Territories",
            Description = "Mantooine is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3900,
            Y = 1534,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Maramere",
            Slug = "maramere",
            Route = "planet/maramere",
            Region = "Outer Rim Territories",
            Description = "Maramere is a star system in the Outer Rim Territories, within the Karthakk Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5702,
            Y = 4149,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Maryx Minor",
            Slug = "maryx-minor",
            Route = "planet/maryx-minor",
            Region = "Outer Rim Territories",
            Description = "Maryx Minor is a star system in the Outer Rim Territories, within the Sujimis Sector, at galactic grid O-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5002,
            Y = 4687,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Mathas",
            Slug = "mathas",
            Route = "planet/mathas",
            Region = "Outer Rim Territories",
            Description = "Mathas is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7191,
            Y = 3364,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Mawan",
            Slug = "mawan",
            Route = "planet/mawan",
            Region = "Core Worlds",
            Description = "Mawan is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4060,
            Y = 2958,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Mawr",
            Slug = "mawr",
            Route = "planet/mawr",
            Region = "Deep Core",
            Description = "Mawr is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3951,
            Y = 2562,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Megalox Beta",
            Slug = "megalox-beta",
            Route = "planet/megalox-beta",
            Region = "Core Worlds",
            Description = "Megalox Beta is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3999,
            Y = 2400,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Merisee",
            Slug = "merisee",
            Route = "planet/merisee",
            Region = "Outer Rim Territories",
            Description = "Merisee is a star system in the Outer Rim Territories, within the Elrood Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4158,
            Y = 4793,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Merson",
            Slug = "merson",
            Route = "planet/merson",
            Region = "Inner Rim Territories",
            Description = "Merson is a star system in the Inner Rim Territories, within the Stenness Node, at galactic grid O-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4892,
            Y = 2547,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Merson asteroid belt",
            Slug = "merson-asteroid-belt",
            Route = "planet/merson-asteroid-belt",
            Region = "Inner Rim Territories",
            Description = "Merson asteroid belt is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid O-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4918,
            Y = 2552,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Metalorn",
            Slug = "metalorn",
            Route = "planet/metalorn",
            Region = "Mid Rim Territories",
            Description = "Metalorn is a star system in the Mid Rim Territories, within the Talcene Sector, at galactic grid R-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5924,
            Y = 2093,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Metellos",
            Slug = "metellos",
            Route = "planet/metellos",
            Region = "Core Worlds",
            Description = "Metellos is a star system in the Core Worlds, within the Coruscant Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3383,
            Y = 2596,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Mexeluine",
            Slug = "mexeluine",
            Route = "planet/mexeluine",
            Region = "Outer Rim Territories",
            Description = "Mexeluine is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3568,
            Y = 4395,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Mijos",
            Slug = "mijos",
            Route = "planet/mijos",
            Region = "Outer Rim Territories",
            Description = "Mijos is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3467,
            Y = 4448,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Mika",
            Slug = "mika",
            Route = "planet/mika",
            Region = "Outer Rim Territories",
            Description = "Mika is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5933,
            Y = 4158,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Mindor",
            Slug = "mindor",
            Route = "planet/mindor",
            Region = "Mid Rim Territories",
            Description = "Mindor is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4199,
            Y = 2249,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Mining Worlds",
            Slug = "mining-worlds",
            Route = "planet/mining-worlds",
            Region = "Outer Rim Territories",
            Description = "Mining Worlds is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3267,
            Y = 4543,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Molavar",
            Slug = "molavar",
            Route = "planet/molavar",
            Region = "Outer Rim Territories",
            Description = "Molavar is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6390,
            Y = 3773,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Moltok",
            Slug = "moltok",
            Route = "planet/moltok",
            Region = "Outer Rim Territories",
            Description = "Moltok is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3648,
            Y = 1448,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Mon Gazza",
            Slug = "mon-gazza",
            Route = "planet/mon-gazza",
            Region = "Mid Rim Territories",
            Description = "Mon Gazza is a star system in the Mid Rim Territories, within the Lambda Sector, at galactic grid Q-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5569,
            Y = 3907,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Monastery",
            Slug = "monastery",
            Route = "planet/monastery",
            Region = "Mid Rim Territories",
            Description = "Monastery is a star system in the Mid Rim Territories, within the Haserian Sector, at galactic grid Q-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5557,
            Y = 3625,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Montross",
            Slug = "montross",
            Route = "planet/montross",
            Region = "Wild Space",
            Description = "Montross is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2783,
            Y = 2647,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Moog Mot VI",
            Slug = "moog-mot-vi",
            Route = "planet/moog-mot-vi",
            Region = "Outer Rim Territories",
            Description = "Moog Mot VI is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6413,
            Y = 2251,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Moorja",
            Slug = "moorja",
            Route = "planet/moorja",
            Region = "Expansion Region",
            Description = "Moorja is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3780,
            Y = 3877,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Moorjhone",
            Slug = "moorjhone",
            Route = "planet/moorjhone",
            Region = "Outer Rim Territories",
            Description = "Moorjhone is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6070,
            Y = 1977,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Moraga",
            Slug = "moraga",
            Route = "planet/moraga",
            Region = "Mid Rim Territories",
            Description = "Moraga is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3827,
            Y = 1918,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Morjakar",
            Slug = "morjakar",
            Route = "planet/morjakar",
            Region = "Mid Rim Territories",
            Description = "Morjakar is a star system in the Mid Rim Territories, within the Thaere sector, at galactic grid P-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5169,
            Y = 3517,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Morvogodine",
            Slug = "morvogodine",
            Route = "planet/morvogodine",
            Region = "Outer Rim Territories",
            Description = "Morvogodine is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7034,
            Y = 2495,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Mrisst",
            Slug = "mrisst",
            Route = "planet/mrisst",
            Region = "Colonies",
            Description = "Mrisst is a star system in the Colonies, within the Fakir Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3425,
            Y = 2335,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Mrlsst",
            Slug = "mrlsst",
            Route = "planet/mrlsst",
            Region = "Colonies",
            Description = "Mrlsst is a star system in the Colonies, within the Tapani Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3923,
            Y = 3275,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Mugaar",
            Slug = "mugaar",
            Route = "planet/mugaar",
            Region = "Mid Rim Territories",
            Description = "Mugaar is a star system in the Mid Rim Territories, within the Bruanii Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3292,
            Y = 4351,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Munto Codru",
            Slug = "munto-codru",
            Route = "planet/munto-codru",
            Region = "Outer Rim Territories",
            Description = "Munto Codru is a star system in the Outer Rim Territories, within the Pakuuni Sector, at galactic grid T-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7001,
            Y = 1649,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Murkhana",
            Slug = "murkhana",
            Route = "planet/murkhana",
            Region = "Outer Rim Territories",
            Description = "Murkhana is a star system in the Outer Rim Territories, within the Auril Sector, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6379,
            Y = 1743,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Murninkam",
            Slug = "murninkam",
            Route = "planet/murninkam",
            Region = "Outer Rim Territories",
            Description = "Murninkam is a star system in the Outer Rim Territories, within the Corva Sector, at galactic grid O-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5030,
            Y = 1021,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Mykapo",
            Slug = "mykapo",
            Route = "planet/mykapo",
            Region = "Deep Core",
            Description = "Mykapo is a star system in the Deep Core, within the Zuma Sector, at galactic grid I-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3708,
            Y = 2773,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Mytus VII",
            Slug = "mytus-vii",
            Route = "planet/mytus-vii",
            Region = "Outer Rim Territories",
            Description = "Mytus VII is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6357,
            Y = 950,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "N'ildwab",
            Slug = "nildwab",
            Route = "planet/nildwab",
            Region = "Outer Rim Territories",
            Description = "N'ildwab is a star system in the Outer Rim Territories, within the Tynquay Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5576,
            Y = 1166,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "N'zoth",
            Slug = "nzoth",
            Route = "planet/nzoth",
            Region = "Core Worlds",
            Description = "N'zoth is a star system in the Core Worlds, within the Farlax Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3248,
            Y = 2630,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Naalol",
            Slug = "naalol",
            Route = "planet/naalol",
            Region = "Mid Rim Territories",
            Description = "Naalol is a star system in the Mid Rim Territories, within the Spirva Sector, at galactic grid L-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3975,
            Y = 4209,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Nadiem",
            Slug = "nadiem",
            Route = "planet/nadiem",
            Region = "Outer Rim Territories",
            Description = "Nadiem is a star system in the Outer Rim Territories, within the Baxel Sector, at galactic grid U-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7180,
            Y = 2936,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Nagi",
            Slug = "nagi",
            Route = "planet/nagi",
            Region = "Wild Space",
            Description = "Nagi is a star system in the Wild Space, within the Zuma Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7489,
            Y = 2305,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "NaJedha",
            Slug = "najedha",
            Route = "planet/najedha",
            Region = "Wild Space",
            Description = "NaJedha is a star system in the Wild Space, within the Zuma Sector, at galactic grid H-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2235,
            Y = 2706,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nal Kapok",
            Slug = "nal-kapok",
            Route = "planet/nal-kapok",
            Region = "Outer Rim Territories",
            Description = "Nal Kapok is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid @-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 544,
            Y = 1374,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nal Koska",
            Slug = "nal-koska",
            Route = "planet/nal-koska",
            Region = "Outer Rim Territories",
            Description = "Nal Koska is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6577,
            Y = 3086,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Nal Yeshu",
            Slug = "nal-yeshu",
            Route = "planet/nal-yeshu",
            Region = "Outer Rim Territories",
            Description = "Nal Yeshu is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6494,
            Y = 3001,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Naldar",
            Slug = "naldar",
            Route = "planet/naldar",
            Region = "Outer Rim Territories",
            Description = "Naldar is a star system in the Outer Rim Territories, within the Phelleem Sector, at galactic grid S-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6493,
            Y = 1897,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nalyd",
            Slug = "nalyd",
            Route = "planet/nalyd",
            Region = "Outer Rim Territories",
            Description = "Nalyd is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6562,
            Y = 1923,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Nam Chorios",
            Slug = "nam-chorios",
            Route = "planet/nam-chorios",
            Region = "Outer Rim Territories",
            Description = "Nam Chorios is a star system in the Outer Rim Territories, within the Meridian Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6024,
            Y = 1797,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nam'ta",
            Slug = "namta",
            Route = "planet/namta",
            Region = "Outer Rim Territories",
            Description = "Nam'ta is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3771,
            Y = 1423,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Nar Haaska",
            Slug = "nar-haaska",
            Route = "planet/nar-haaska",
            Region = "Outer Rim Territories",
            Description = "Nar Haaska is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6921,
            Y = 2763,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Nar Hekka",
            Slug = "nar-hekka",
            Route = "planet/nar-hekka",
            Region = "Outer Rim Territories",
            Description = "Nar Hekka is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6624,
            Y = 2960,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Nar Kreeta",
            Slug = "nar-kreeta",
            Route = "planet/nar-kreeta",
            Region = "Mid Rim Territories",
            Description = "Nar Kreeta is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6321,
            Y = 2568,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Naraka",
            Slug = "naraka",
            Route = "planet/naraka",
            Region = "Expansion Region",
            Description = "Naraka is a star system in the Expansion Region, within the Zuma Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5161,
            Y = 2584,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Near Pando",
            Slug = "near-pando",
            Route = "planet/near-pando",
            Region = "Outer Rim Territories",
            Description = "Near Pando is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6327,
            Y = 3474,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Necropolis",
            Slug = "necropolis",
            Route = "planet/necropolis",
            Region = "Colonies",
            Description = "Necropolis is a star system in the Colonies, within the Zuma Sector, at galactic grid J-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3030,
            Y = 3202,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Neelgaimon",
            Slug = "neelgaimon",
            Route = "planet/neelgaimon",
            Region = "Outer Rim Territories",
            Description = "Neelgaimon is a star system in the Outer Rim Territories, within the Xappyh Sector, at galactic grid Q-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5559,
            Y = 908,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Neftali",
            Slug = "neftali",
            Route = "planet/neftali",
            Region = "Outer Rim Territories",
            Description = "Neftali is a star system in the Outer Rim Territories, within the Kibilini Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5752,
            Y = 4250,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Nelvaan",
            Slug = "nelvaan",
            Route = "planet/nelvaan",
            Region = "Outer Rim Territories",
            Description = "Nelvaan is a star system in the Outer Rim Territories, within the Savareen Sector, at galactic grid Q-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5824,
            Y = 4095,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Nentan",
            Slug = "nentan",
            Route = "planet/nentan",
            Region = "Mid Rim Territories",
            Description = "Nentan is a star system in the Mid Rim Territories, within the Glythe Sector, at galactic grid K-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3293,
            Y = 2039,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Neshtab",
            Slug = "neshtab",
            Route = "planet/neshtab",
            Region = "Expansion Region",
            Description = "Neshtab is a star system in the Expansion Region, within the Zuma Sector, at galactic grid K-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3279,
            Y = 2253,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "New Alderaan",
            Slug = "new-alderaan",
            Route = "planet/new-alderaan",
            Region = "Outer Rim Territories",
            Description = "New Alderaan is a star system in the Outer Rim Territories, within the Ash Worlds, at galactic grid T-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6991,
            Y = 1600,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "New Bakstre",
            Slug = "new-bakstre",
            Route = "planet/new-bakstre",
            Region = "Outer Rim Territories",
            Description = "New Bakstre is a star system in the Outer Rim Territories, within the Cassander Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3494,
            Y = 1498,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "New Cov",
            Slug = "new-cov",
            Route = "planet/new-cov",
            Region = "Mid Rim Territories",
            Description = "New Cov is a star system in the Mid Rim Territories, within the Churba Sector, at galactic grid P-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5146,
            Y = 3625,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "New Holstice",
            Slug = "new-holstice",
            Route = "planet/new-holstice",
            Region = "Mid Rim Territories",
            Description = "New Holstice is a star system in the Mid Rim Territories, within the Maldrood Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6096,
            Y = 1827,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "New Plympto",
            Slug = "new-plympto",
            Route = "planet/new-plympto",
            Region = "Core Worlds",
            Description = "New Plympto is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4308,
            Y = 2889,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nexus Ortai",
            Slug = "nexus-ortai",
            Route = "planet/nexus-ortai",
            Region = "Mid Rim Territories",
            Description = "Nexus Ortai is a star system in the Mid Rim Territories, within the Hertae Sector, at galactic grid Q-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5690,
            Y = 3531,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Nez Peron",
            Slug = "nez-peron",
            Route = "planet/nez-peron",
            Region = "Outer Rim Territories",
            Description = "Nez Peron is a star system in the Outer Rim Territories, within the D'astan Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4924,
            Y = 1542,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Nibiru",
            Slug = "nibiru",
            Route = "planet/nibiru",
            Region = "Outer Rim Territories",
            Description = "Nibiru is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2170,
            Y = 3881,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Nichen",
            Slug = "nichen",
            Route = "planet/nichen",
            Region = "Outer Rim Territories",
            Description = "Nichen is a star system in the Outer Rim Territories, within the Morshdine Sector, at galactic grid N-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4495,
            Y = 1120,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nilash III",
            Slug = "nilash-iii",
            Route = "planet/nilash-iii",
            Region = "Outer Rim Territories",
            Description = "Nilash III is a star system in the Outer Rim Territories, within the Spumani Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4004,
            Y = 4138,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Nimba Five",
            Slug = "nimba-five",
            Route = "planet/nimba-five",
            Region = "Outer Rim Territories",
            Description = "Nimba Five is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6960,
            Y = 4184,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ningoth",
            Slug = "ningoth",
            Route = "planet/ningoth",
            Region = "Outer Rim Territories",
            Description = "Ningoth is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3628,
            Y = 901,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ninn",
            Slug = "ninn",
            Route = "planet/ninn",
            Region = "Outer Rim Territories",
            Description = "Ninn is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid R-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6188,
            Y = 907,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Nivek",
            Slug = "nivek",
            Route = "planet/nivek",
            Region = "Expansion Region",
            Description = "Nivek is a star system in the Expansion Region, within the Citlik Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5062,
            Y = 3587,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Nixus",
            Slug = "nixus",
            Route = "planet/nixus",
            Region = "Outer Rim Territories",
            Description = "Nixus is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3813,
            Y = 1353,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Nkllon",
            Slug = "nkllon",
            Route = "planet/nkllon",
            Region = "Expansion Region",
            Description = "Nkllon is a star system in the Expansion Region, within the Alchenaut Sector, at galactic grid L-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3836,
            Y = 3907,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Noctralis",
            Slug = "noctralis",
            Route = "planet/noctralis",
            Region = "Core Worlds",
            Description = "Noctralis is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3975,
            Y = 2246,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Noctu",
            Slug = "noctu",
            Route = "planet/noctu",
            Region = "Wild Space",
            Description = "Noctu is a star system in the Wild Space, within the Zuma Sector, at galactic grid Q-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6724,
            Y = 732,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Nod Kartha",
            Slug = "nod-kartha",
            Route = "planet/nod-kartha",
            Region = "Outer Rim Territories",
            Description = "Nod Kartha is a star system in the Outer Rim Territories, within the Karthakk Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5702,
            Y = 4149,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Noe'ha'on",
            Slug = "noehaon",
            Route = "planet/noehaon",
            Region = "Expansion Region",
            Description = "Noe'ha'on is a star system in the Expansion Region, within the Piryn Shar, at galactic grid K-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3303,
            Y = 3921,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Noris",
            Slug = "noris",
            Route = "planet/noris",
            Region = "Wild Space",
            Description = "Noris is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1647,
            Y = 2241,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Norulac",
            Slug = "norulac",
            Route = "planet/norulac",
            Region = "Inner Rim Territories",
            Description = "Norulac is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid O-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5075,
            Y = 2373,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Norval II",
            Slug = "norval-ii",
            Route = "planet/norval-ii",
            Region = "Outer Rim Territories",
            Description = "Norval II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6893,
            Y = 2409,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nothoiin",
            Slug = "nothoiin",
            Route = "planet/nothoiin",
            Region = "Outer Rim Territories",
            Description = "Nothoiin is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3337,
            Y = 4418,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Nox",
            Slug = "nox",
            Route = "planet/nox",
            Region = "Core Worlds",
            Description = "Nox is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3924,
            Y = 2547,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Nubia",
            Slug = "nubia",
            Route = "planet/nubia",
            Region = "Core Worlds",
            Description = "Nubia is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4108,
            Y = 2945,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Null",
            Slug = "null",
            Route = "planet/null",
            Region = "Mid Rim Territories",
            Description = "Null is a star system in the Mid Rim Territories, within the Trans-Vulta Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4469,
            Y = 1878,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Nurstin",
            Slug = "nurstin",
            Route = "planet/nurstin",
            Region = "Mid Rim Territories",
            Description = "Nurstin is a star system in the Mid Rim Territories, within the Trax Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5830,
            Y = 2657,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Nyara",
            Slug = "nyara",
            Route = "planet/nyara",
            Region = "Core Worlds",
            Description = "Nyara is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3887,
            Y = 2241,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Nyriaan",
            Slug = "nyriaan",
            Route = "planet/nyriaan",
            Region = "Outer Rim Territories",
            Description = "Nyriaan is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4599,
            Y = 1870,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "O'reen",
            Slug = "oreen",
            Route = "planet/oreen",
            Region = "Expansion Region",
            Description = "O'reen is a star system in the Expansion Region, within the Zuma Sector, at galactic grid H-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2170,
            Y = 3274,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Oaka Prime",
            Slug = "oaka-prime",
            Route = "planet/oaka-prime",
            Region = "Expansion Region",
            Description = "Oaka Prime is a star system in the Expansion Region, within the Zuma Sector, at galactic grid J-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3091,
            Y = 2245,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Obas",
            Slug = "obas",
            Route = "planet/obas",
            Region = "Expansion Region",
            Description = "Obas is a star system in the Expansion Region, within the Andirma Sector, at galactic grid L-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3769,
            Y = 3749,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Obri",
            Slug = "obri",
            Route = "planet/obri",
            Region = "Deep Core",
            Description = "Obri is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3674,
            Y = 2696,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Obroa-skai",
            Slug = "obroa-skai",
            Route = "planet/obroa-skai",
            Region = "Inner Rim Territories",
            Description = "Obroa-skai is a star system in the Inner Rim Territories, within the Borderland Regions, at galactic grid N-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4736,
            Y = 2093,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Obus VI",
            Slug = "obus-vi",
            Route = "planet/obus-vi",
            Region = "Outer Rim Territories",
            Description = "Obus VI is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7647,
            Y = 4669,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Odacer-Faustin",
            Slug = "odacer-faustin",
            Route = "planet/odacer-faustin",
            Region = "Outer Rim Territories",
            Description = "Odacer-Faustin is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5852,
            Y = 1439,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Odik II",
            Slug = "odik-ii",
            Route = "planet/odik-ii",
            Region = "Core Worlds",
            Description = "Odik II is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3421,
            Y = 2768,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Odona",
            Slug = "odona",
            Route = "planet/odona",
            Region = "Wild Space",
            Description = "Odona is a star system in the Wild Space, within the Zuma Sector, at galactic grid @-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 543,
            Y = 2972,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Odryn",
            Slug = "odryn",
            Route = "planet/odryn",
            Region = "Outer Rim Territories",
            Description = "Odryn is a star system in the Outer Rim Territories, within the Noonian Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4591,
            Y = 1836,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Olanet",
            Slug = "olanet",
            Route = "planet/olanet",
            Region = "Outer Rim Territories",
            Description = "Olanet is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6060,
            Y = 4181,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Old Barag",
            Slug = "old-barag",
            Route = "planet/old-barag",
            Region = "Expansion Region",
            Description = "Old Barag is a star system in the Expansion Region, within the Epsi Collective, at galactic grid M-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4029,
            Y = 3741,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Omar",
            Slug = "omar",
            Route = "planet/omar",
            Region = "Core Worlds",
            Description = "Omar is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3357,
            Y = 3319,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Omphalos",
            Slug = "omphalos",
            Route = "planet/omphalos",
            Region = "Colonies",
            Description = "Omphalos is a star system in the Colonies, within the Zuma Sector, at galactic grid F-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2728,
            Y = 2442,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Omwat",
            Slug = "omwat",
            Route = "planet/omwat",
            Region = "Outer Rim Territories",
            Description = "Omwat is a star system in the Outer Rim Territories, within the Garis Sector, at galactic grid N-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4480,
            Y = 4567,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Oon",
            Slug = "oon",
            Route = "planet/oon",
            Region = "Deep Core",
            Description = "Oon is a star system in the Deep Core, within the Zuma Sector, at galactic grid I-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3650,
            Y = 2794,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Oon Tien",
            Slug = "oon-tien",
            Route = "planet/oon-tien",
            Region = "Outer Rim Territories",
            Description = "Oon Tien is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4128,
            Y = 469,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Ooo-temiuk",
            Slug = "ooo-temiuk",
            Route = "planet/ooo-temiuk",
            Region = "Core Worlds",
            Description = "Ooo-temiuk is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3683,
            Y = 3004,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Oosalon",
            Slug = "oosalon",
            Route = "planet/oosalon",
            Region = "Wild Space",
            Description = "Oosalon is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2505,
            Y = 2522,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ootoola",
            Slug = "ootoola",
            Route = "planet/ootoola",
            Region = "Outer Rim Territories",
            Description = "Ootoola is a star system in the Outer Rim Territories, within the Morshdine Sector, at galactic grid O-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5132,
            Y = 1350,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Oovo",
            Slug = "oovo",
            Route = "planet/oovo",
            Region = "Outer Rim Territories",
            Description = "Oovo is a star system in the Outer Rim Territories, within the Tharin Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6439,
            Y = 2116,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ophideraan",
            Slug = "ophideraan",
            Route = "planet/ophideraan",
            Region = "Core Worlds",
            Description = "Ophideraan is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3547,
            Y = 3255,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ord Antalaha",
            Slug = "ord-antalaha",
            Route = "planet/ord-antalaha",
            Region = "Expansion Region",
            Description = "Ord Antalaha is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3727,
            Y = 2089,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Ord Biniir",
            Slug = "ord-biniir",
            Route = "planet/ord-biniir",
            Region = "Outer Rim Territories",
            Description = "Ord Biniir is a star system in the Outer Rim Territories, within the Relgim Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3614,
            Y = 1424,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ord Cantrell",
            Slug = "ord-cantrell",
            Route = "planet/ord-cantrell",
            Region = "Outer Rim Territories",
            Description = "Ord Cantrell is a star system in the Outer Rim Territories, within the Fath Sector, at galactic grid K-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3559,
            Y = 1636,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ord Cestus",
            Slug = "ord-cestus",
            Route = "planet/ord-cestus",
            Region = "Outer Rim Territories",
            Description = "Ord Cestus is a star system in the Outer Rim Territories, within the D'astan Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4869,
            Y = 1582,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ord Ibanna",
            Slug = "ord-ibanna",
            Route = "planet/ord-ibanna",
            Region = "Outer Rim Territories",
            Description = "Ord Ibanna is a star system in the Outer Rim Territories, within the Brema Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4176,
            Y = 4118,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ord Janon",
            Slug = "ord-janon",
            Route = "planet/ord-janon",
            Region = "Outer Rim Territories",
            Description = "Ord Janon is a star system in the Outer Rim Territories, within the Spinward Sector, at galactic grid N-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4389,
            Y = 739,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ord Lithone",
            Slug = "ord-lithone",
            Route = "planet/ord-lithone",
            Region = "Colonies",
            Description = "Ord Lithone is a star system in the Colonies, within the Zuma Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3913,
            Y = 2119,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ord Pardron",
            Slug = "ord-pardron",
            Route = "planet/ord-pardron",
            Region = "Mid Rim Territories",
            Description = "Ord Pardron is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6079,
            Y = 3867,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ord Radama",
            Slug = "ord-radama",
            Route = "planet/ord-radama",
            Region = "Outer Rim Territories",
            Description = "Ord Radama is a star system in the Outer Rim Territories, within the Esstran Sector, at galactic grid Q-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5524,
            Y = 1367,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ord Sedra",
            Slug = "ord-sedra",
            Route = "planet/ord-sedra",
            Region = "Outer Rim Territories",
            Description = "Ord Sedra is a star system in the Outer Rim Territories, within the Clacis Sector, at galactic grid K-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3422,
            Y = 1132,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ord Tiddell",
            Slug = "ord-tiddell",
            Route = "planet/ord-tiddell",
            Region = "Mid Rim Territories",
            Description = "Ord Tiddell is a star system in the Mid Rim Territories, within the Tennuutta Sector, at galactic grid Q-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5554,
            Y = 2024,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Ord Trasi",
            Slug = "ord-trasi",
            Route = "planet/ord-trasi",
            Region = "Outer Rim Territories",
            Description = "Ord Trasi is a star system in the Outer Rim Territories, within the Relgim Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3670,
            Y = 1327,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ord Vaug",
            Slug = "ord-vaug",
            Route = "planet/ord-vaug",
            Region = "Expansion Region",
            Description = "Ord Vaug is a star system in the Expansion Region, within the Rocantor Sector, at galactic grid L-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3878,
            Y = 3770,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ord Vaxal",
            Slug = "ord-vaxal",
            Route = "planet/ord-vaxal",
            Region = "Inner Rim Territories",
            Description = "Ord Vaxal is a star system in the Inner Rim Territories, within the Callia Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4634,
            Y = 3320,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Orinackra",
            Slug = "orinackra",
            Route = "planet/orinackra",
            Region = "Outer Rim Territories",
            Description = "Orinackra is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2868,
            Y = 947,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Orinda",
            Slug = "orinda",
            Route = "planet/orinda",
            Region = "Mid Rim Territories",
            Description = "Orinda is a star system in the Mid Rim Territories, within the Irishi Sector, at galactic grid K-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3525,
            Y = 1703,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Orion IV",
            Slug = "orion-iv",
            Route = "planet/orion-iv",
            Region = "Outer Rim Territories",
            Description = "Orion IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6907,
            Y = 1671,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Orkana",
            Slug = "orkana",
            Route = "planet/orkana",
            Region = "Core Worlds",
            Description = "Orkana is a star system in the Core Worlds, within the Zuma Sector, at galactic grid H-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3403,
            Y = 2663,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Orleon",
            Slug = "orleon",
            Route = "planet/orleon",
            Region = "Mid Rim Territories",
            Description = "Orleon is a star system in the Mid Rim Territories, within the Talcene Sector, at galactic grid Q-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5681,
            Y = 2127,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Orocco",
            Slug = "orocco",
            Route = "planet/orocco",
            Region = "Outer Rim Territories",
            Description = "Orocco is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4198,
            Y = 1812,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Orondia",
            Slug = "orondia",
            Route = "planet/orondia",
            Region = "Mid Rim Territories",
            Description = "Orondia is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6552,
            Y = 2750,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Orroman",
            Slug = "orroman",
            Route = "planet/orroman",
            Region = "Inner Rim Territories",
            Description = "Orroman is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid I-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2842,
            Y = 3605,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Orron III",
            Slug = "orron-iii",
            Route = "planet/orron-iii",
            Region = "Outer Rim Territories",
            Description = "Orron III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6414,
            Y = 1121,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Orvax IV",
            Slug = "orvax-iv",
            Route = "planet/orvax-iv",
            Region = "Outer Rim Territories",
            Description = "Orvax IV is a star system in the Outer Rim Territories, within the Savareen Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5901,
            Y = 4190,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Osadia",
            Slug = "osadia",
            Route = "planet/osadia",
            Region = "Core Worlds",
            Description = "Osadia is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3515,
            Y = 2571,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Osarian",
            Slug = "osarian",
            Route = "planet/osarian",
            Region = "Inner Rim Territories",
            Description = "Osarian is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4693,
            Y = 3291,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Oseon",
            Slug = "oseon",
            Route = "planet/oseon",
            Region = "Outer Rim Territories",
            Description = "Oseon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6740,
            Y = 2166,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ostor",
            Slug = "ostor",
            Route = "planet/ostor",
            Region = "Outer Rim Territories",
            Description = "Ostor is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2689,
            Y = 4530,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ota",
            Slug = "ota",
            Route = "planet/ota",
            Region = "Mid Rim Territories",
            Description = "Ota is a star system in the Mid Rim Territories, within the Mytaranor Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5781,
            Y = 2699,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Otavon XII",
            Slug = "otavon-xii",
            Route = "planet/otavon-xii",
            Region = "Mid Rim Territories",
            Description = "Otavon XII is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4340,
            Y = 1913,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Otherworld",
            Slug = "otherworld",
            Route = "planet/otherworld",
            Region = "Wild Space",
            Description = "Otherworld is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1298,
            Y = 1498,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ottethan",
            Slug = "ottethan",
            Route = "planet/ottethan",
            Region = "Outer Rim Territories",
            Description = "Ottethan is a star system in the Outer Rim Territories, within the Halthor Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4379,
            Y = 1604,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Otunia",
            Slug = "otunia",
            Route = "planet/otunia",
            Region = "Outer Rim Territories",
            Description = "Otunia is a star system in the Outer Rim Territories, within the Bosph Sector, at galactic grid Q-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5617,
            Y = 1116,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Outpost",
            Slug = "outpost",
            Route = "planet/outpost",
            Region = "Mid Rim Territories",
            Description = "Outpost is a star system in the Mid Rim Territories, within the Trax Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5755,
            Y = 2514,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ova",
            Slug = "ova",
            Route = "planet/ova",
            Region = "Outer Rim Territories",
            Description = "Ova is a star system in the Outer Rim Territories, within the Quelii Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4766,
            Y = 1771,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ovanis",
            Slug = "ovanis",
            Route = "planet/ovanis",
            Region = "Wild Space",
            Description = "Ovanis is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1279,
            Y = 4753,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Oznek",
            Slug = "oznek",
            Route = "planet/oznek",
            Region = "Outer Rim Territories",
            Description = "Oznek is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4057,
            Y = 1587,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Paarin Minor",
            Slug = "paarin-minor",
            Route = "planet/paarin-minor",
            Region = "Outer Rim Territories",
            Description = "Paarin Minor is a star system in the Outer Rim Territories, within the Cademimu Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4348,
            Y = 1604,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Paklan",
            Slug = "paklan",
            Route = "planet/paklan",
            Region = "Outer Rim Territories",
            Description = "Paklan is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5834,
            Y = 1732,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Pakuuni",
            Slug = "pakuuni",
            Route = "planet/pakuuni",
            Region = "Outer Rim Territories",
            Description = "Pakuuni is a star system in the Outer Rim Territories, within the Pakuuni Sector, at galactic grid T-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6823,
            Y = 1609,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Palanhi",
            Slug = "palanhi",
            Route = "planet/palanhi",
            Region = "Colonies",
            Description = "Palanhi is a star system in the Colonies, within the Fakir Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3370,
            Y = 2497,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Pallaxides",
            Slug = "pallaxides",
            Route = "planet/pallaxides",
            Region = "Outer Rim Territories",
            Description = "Pallaxides is a star system in the Outer Rim Territories, within the Ojoster Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4547,
            Y = 1833,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Panna",
            Slug = "panna",
            Route = "planet/panna",
            Region = "Outer Rim Territories",
            Description = "Panna is a star system in the Outer Rim Territories, within the Cronese Mandate, at galactic grid S-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6656,
            Y = 1745,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Pantolomin",
            Slug = "pantolomin",
            Route = "planet/pantolomin",
            Region = "Core Worlds",
            Description = "Pantolomin is a star system in the Core Worlds, within the Dolomar Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3487,
            Y = 2395,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Paqualis III",
            Slug = "paqualis-iii",
            Route = "planet/paqualis-iii",
            Region = "Inner Rim Territories",
            Description = "Paqualis III is a star system in the Inner Rim Territories, within the Immalia Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3980,
            Y = 2120,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Parcellus Minor",
            Slug = "parcellus-minor",
            Route = "planet/parcellus-minor",
            Region = "Expansion Region",
            Description = "Parcellus Minor is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5085,
            Y = 3097,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Parnassos",
            Slug = "parnassos",
            Route = "planet/parnassos",
            Region = "Expansion Region",
            Description = "Parnassos is a star system in the Expansion Region, within the Zuma Sector, at galactic grid I-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3703,
            Y = 3762,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Pashvi",
            Slug = "pashvi",
            Route = "planet/pashvi",
            Region = "Wild Space",
            Description = "Pashvi is a star system in the Wild Space, within the Zuma Sector, at galactic grid I-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2617,
            Y = 1543,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Pastil",
            Slug = "pastil",
            Route = "planet/pastil",
            Region = "Outer Rim Territories",
            Description = "Pastil is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6420,
            Y = 3766,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Patch-4",
            Slug = "patch-4",
            Route = "planet/patch-4",
            Region = "Wild Space",
            Description = "Patch-4 is a star system in the Wild Space, within the Zuma Sector, at galactic grid C-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1709,
            Y = 2667,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Patitite Pattuna",
            Slug = "patitite-pattuna",
            Route = "planet/patitite-pattuna",
            Region = "Mid Rim Territories",
            Description = "Patitite Pattuna is a star system in the Mid Rim Territories, within the Bright Jewel, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3863,
            Y = 1894,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Peirs",
            Slug = "peirs",
            Route = "planet/peirs",
            Region = "Outer Rim Territories",
            Description = "Peirs is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4027,
            Y = 632,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Pelagon",
            Slug = "pelagon",
            Route = "planet/pelagon",
            Region = "Colonies",
            Description = "Pelagon is a star system in the Colonies, within the Tapani Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3757,
            Y = 3200,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Pembric II",
            Slug = "pembric-ii",
            Route = "planet/pembric-ii",
            Region = "Outer Rim Territories",
            Description = "Pembric II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4260,
            Y = 432,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Pengalan IV",
            Slug = "pengalan-iv",
            Route = "planet/pengalan-iv",
            Region = "Inner Rim Territories",
            Description = "Pengalan IV is a star system in the Inner Rim Territories, within the The Veil, at galactic grid O-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4880,
            Y = 2187,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Per Lupelo",
            Slug = "per-lupelo",
            Route = "planet/per-lupelo",
            Region = "Colonies",
            Description = "Per Lupelo is a star system in the Colonies, within the Zuma Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3714,
            Y = 2235,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Peragus asteroid field",
            Slug = "peragus-asteroid-field",
            Route = "planet/peragus-asteroid-field",
            Region = "Expansion Region",
            Description = "Peragus asteroid field is a star system in the Expansion Region, within the Zuma Sector, at galactic grid G-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2953,
            Y = 3864,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Peragus II",
            Slug = "peragus-ii",
            Route = "planet/peragus-ii",
            Region = "Outer Rim Territories",
            Description = "Peragus II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5663,
            Y = 1133,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Perma",
            Slug = "perma",
            Route = "planet/perma",
            Region = "Core Worlds",
            Description = "Perma is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4183,
            Y = 2933,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Phaeda",
            Slug = "phaeda",
            Route = "planet/phaeda",
            Region = "Outer Rim Territories",
            Description = "Phaeda is a star system in the Outer Rim Territories, within the Cademimu Sector, at galactic grid L-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3825,
            Y = 1649,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Phaseera",
            Slug = "phaseera",
            Route = "planet/phaseera",
            Region = "Mid Rim Territories",
            Description = "Phaseera is a star system in the Mid Rim Territories, within the Lantillian Sector, at galactic grid P-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5424,
            Y = 2125,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Phaylenn",
            Slug = "phaylenn",
            Route = "planet/phaylenn",
            Region = "Core Worlds",
            Description = "Phaylenn is a star system in the Core Worlds, within the Zuma Sector, at galactic grid G-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3002,
            Y = 3028,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Phelarion",
            Slug = "phelarion",
            Route = "planet/phelarion",
            Region = "Outer Rim Territories",
            Description = "Phelarion is a star system in the Outer Rim Territories, within the Seswenna Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4282,
            Y = 4502,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Phemis",
            Slug = "phemis",
            Route = "planet/phemis",
            Region = "Core Worlds",
            Description = "Phemis is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4080,
            Y = 2839,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Pheryon",
            Slug = "pheryon",
            Route = "planet/pheryon",
            Region = "Outer Rim Territories",
            Description = "Pheryon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4186,
            Y = 1281,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Phorliss",
            Slug = "phorliss",
            Route = "planet/phorliss",
            Region = "Core Worlds",
            Description = "Phorliss is a star system in the Core Worlds, within the Dolomar Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3541,
            Y = 2358,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Phorose",
            Slug = "phorose",
            Route = "planet/phorose",
            Region = "Colonies",
            Description = "Phorose is a star system in the Colonies, within the Zuma Sector, at galactic grid M-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4142,
            Y = 3402,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Phraetiss",
            Slug = "phraetiss",
            Route = "planet/phraetiss",
            Region = "Core Worlds",
            Description = "Phraetiss is a star system in the Core Worlds, within the Farrfin Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3365,
            Y = 2359,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Pil Diller",
            Slug = "pil-diller",
            Route = "planet/pil-diller",
            Region = "Outer Rim Territories",
            Description = "Pil Diller is a star system in the Outer Rim Territories, within the Quelii Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4773,
            Y = 1620,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Pillio",
            Slug = "pillio",
            Route = "planet/pillio",
            Region = "Outer Rim Territories",
            Description = "Pillio is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7573,
            Y = 2823,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Pizilis",
            Slug = "pizilis",
            Route = "planet/pizilis",
            Region = "Mid Rim Territories",
            Description = "Pizilis is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5380,
            Y = 2665,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Pizkoss",
            Slug = "pizkoss",
            Route = "planet/pizkoss",
            Region = "Core Worlds",
            Description = "Pizkoss is a star system in the Core Worlds, within the Core Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3466,
            Y = 2597,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Planet of the Red Nebula",
            Slug = "planet-of-the-red-nebula",
            Route = "planet/planet-of-the-red-nebula",
            Region = "Outer Rim Territories",
            Description = "Planet of the Red Nebula is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid G-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1933,
            Y = 529,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Pleem's Nexus",
            Slug = "pleems-nexus",
            Route = "planet/pleems-nexus",
            Region = "Inner Rim Territories",
            Description = "Pleem's Nexus is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4681,
            Y = 1997,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Plooriod III",
            Slug = "plooriod-iii",
            Route = "planet/plooriod-iii",
            Region = "Outer Rim Territories",
            Description = "Plooriod III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4534,
            Y = 1870,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "PM-1203",
            Slug = "pm-1203",
            Route = "planet/pm-1203",
            Region = "Core Worlds",
            Description = "PM-1203 is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3626,
            Y = 2463,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Poderis",
            Slug = "poderis",
            Route = "planet/poderis",
            Region = "Inner Rim Territories",
            Description = "Poderis is a star system in the Inner Rim Territories, within the Orus Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4193,
            Y = 2157,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Poison Moon",
            Slug = "poison-moon",
            Route = "planet/poison-moon",
            Region = "Outer Rim Territories",
            Description = "Poison Moon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3259,
            Y = 4485,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Polith Belt",
            Slug = "polith-belt",
            Route = "planet/polith-belt",
            Region = "Inner Rim Territories",
            Description = "Polith Belt is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid L-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3940,
            Y = 3511,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Pollillus",
            Slug = "pollillus",
            Route = "planet/pollillus",
            Region = "Core Worlds",
            Description = "Pollillus is a star system in the Core Worlds, within the Vannell Sector, at galactic grid J-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2882,
            Y = 2608,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Poln Major",
            Slug = "poln-major",
            Route = "planet/poln-major",
            Region = "Outer Rim Territories",
            Description = "Poln Major is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3055,
            Y = 1539,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Polus",
            Slug = "polus",
            Route = "planet/polus",
            Region = "Outer Rim Territories",
            Description = "Polus is a star system in the Outer Rim Territories, within the Oricho Sector, at galactic grid M-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4137,
            Y = 1582,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Port Haven",
            Slug = "port-haven",
            Route = "planet/port-haven",
            Region = "Outer Rim Territories",
            Description = "Port Haven is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3870,
            Y = 1638,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Praya",
            Slug = "praya",
            Route = "planet/praya",
            Region = "Outer Rim Territories",
            Description = "Praya is a star system in the Outer Rim Territories, within the Clacis Sector, at galactic grid K-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3448,
            Y = 1230,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Prefsbelt IV",
            Slug = "prefsbelt-iv",
            Route = "planet/prefsbelt-iv",
            Region = "Outer Rim Territories",
            Description = "Prefsbelt IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3508,
            Y = 1426,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Prine",
            Slug = "prine",
            Route = "planet/prine",
            Region = "Mid Rim Territories",
            Description = "Prine is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid O-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5062,
            Y = 3929,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Procopia",
            Slug = "procopia",
            Route = "planet/procopia",
            Region = "Colonies",
            Description = "Procopia is a star system in the Colonies, within the Tapani Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3757,
            Y = 3251,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Purple planet",
            Slug = "purple-planet",
            Route = "planet/purple-planet",
            Region = "Wild Space",
            Description = "Purple planet is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1936,
            Y = 2769,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Pybus",
            Slug = "pybus",
            Route = "planet/pybus",
            Region = "Mid Rim Territories",
            Description = "Pybus is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6560,
            Y = 2848,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Pzob",
            Slug = "pzob",
            Route = "planet/pzob",
            Region = "Outer Rim Territories",
            Description = "Pzob is a star system in the Outer Rim Territories, within the Herios Sector, at galactic grid T-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6923,
            Y = 3840,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Q'Maere",
            Slug = "qmaere",
            Route = "planet/qmaere",
            Region = "Outer Rim Territories",
            Description = "Q'Maere is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4358,
            Y = 466,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Qat Chrystac",
            Slug = "qat-chrystac",
            Route = "planet/qat-chrystac",
            Region = "Expansion Region",
            Description = "Qat Chrystac is a star system in the Expansion Region, within the Parnabe Sector, at galactic grid L-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3836,
            Y = 3907,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Qiaxx",
            Slug = "qiaxx",
            Route = "planet/qiaxx",
            Region = "Outer Rim Territories",
            Description = "Qiaxx is a star system in the Outer Rim Territories, within the Cor'ric Sector, at galactic grid P-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5353,
            Y = 4395,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Qiilura",
            Slug = "qiilura",
            Route = "planet/qiilura",
            Region = "Mid Rim Territories",
            Description = "Qiilura is a star system in the Mid Rim Territories, within the Qiilura Sector, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3871,
            Y = 1991,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Queel",
            Slug = "queel",
            Route = "planet/queel",
            Region = "Mid Rim Territories",
            Description = "Queel is a star system in the Mid Rim Territories, within the Doldur Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5514,
            Y = 3675,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Quell",
            Slug = "quell",
            Route = "planet/quell",
            Region = "Outer Rim Territories",
            Description = "Quell is a star system in the Outer Rim Territories, within the Nuiri Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5521,
            Y = 1751,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Queyta",
            Slug = "queyta",
            Route = "planet/queyta",
            Region = "Outer Rim Territories",
            Description = "Queyta is a star system in the Outer Rim Territories, within the Danjar Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4291,
            Y = 4620,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Quila",
            Slug = "quila",
            Route = "planet/quila",
            Region = "Core Worlds",
            Description = "Quila is a star system in the Core Worlds, within the Zuma Sector, at galactic grid F-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2765,
            Y = 2500,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "R-Duba",
            Slug = "r-duba",
            Route = "planet/r-duba",
            Region = "Outer Rim Territories",
            Description = "R-Duba is a star system in the Outer Rim Territories, within the Quiberon Sector, at galactic grid T-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6686,
            Y = 3825,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Rabaan",
            Slug = "rabaan",
            Route = "planet/rabaan",
            Region = "Expansion Region",
            Description = "Rabaan is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5004,
            Y = 3131,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Radhii",
            Slug = "radhii",
            Route = "planet/radhii",
            Region = "Outer Rim Territories",
            Description = "Radhii is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3664,
            Y = 4684,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Radix",
            Slug = "radix",
            Route = "planet/radix",
            Region = "Mid Rim Territories",
            Description = "Radix is a star system in the Mid Rim Territories, within the Yushan Sector, at galactic grid K-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3475,
            Y = 4248,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Rafa IV",
            Slug = "rafa-iv",
            Route = "planet/rafa-iv",
            Region = "Mid Rim Territories",
            Description = "Rafa IV is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid T-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6695,
            Y = 2095,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ragmar V",
            Slug = "ragmar-v",
            Route = "planet/ragmar-v",
            Region = "Outer Rim Territories",
            Description = "Ragmar V is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5724,
            Y = 4252,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Rago",
            Slug = "rago",
            Route = "planet/rago",
            Region = "Wild Space",
            Description = "Rago is a star system in the Wild Space, within the Rago Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2659,
            Y = 1904,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Ragoon VI",
            Slug = "ragoon-vi",
            Route = "planet/ragoon-vi",
            Region = "Colonies",
            Description = "Ragoon VI is a star system in the Colonies, within the Zuma Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3496,
            Y = 2361,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Rainboh",
            Slug = "rainboh",
            Route = "planet/rainboh",
            Region = "Inner Rim Territories",
            Description = "Rainboh is a star system in the Inner Rim Territories, within the Hapes Cluster, at galactic grid O-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5022,
            Y = 2462,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Raithal",
            Slug = "raithal",
            Route = "planet/raithal",
            Region = "Colonies",
            Description = "Raithal is a star system in the Colonies, within the Zuma Sector, at galactic grid M-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4268,
            Y = 2390,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Rakhuuun",
            Slug = "rakhuuun",
            Route = "planet/rakhuuun",
            Region = "Mid Rim Territories",
            Description = "Rakhuuun is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5626,
            Y = 2516,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Ralltiir",
            Slug = "ralltiir",
            Route = "planet/ralltiir",
            Region = "Core Worlds",
            Description = "Ralltiir is a star system in the Core Worlds, within the Darpa Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3651,
            Y = 2362,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Randa",
            Slug = "randa",
            Route = "planet/randa",
            Region = "Outer Rim Territories",
            Description = "Randa is a star system in the Outer Rim Territories, within the Kessel Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6941,
            Y = 2690,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Rangorah",
            Slug = "rangorah",
            Route = "planet/rangorah",
            Region = "Outer Rim Territories",
            Description = "Rangorah is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6790,
            Y = 2352,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Rannon",
            Slug = "rannon",
            Route = "planet/rannon",
            Region = "Outer Rim Territories",
            Description = "Rannon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6810,
            Y = 4120,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Raxus II",
            Slug = "raxus-ii",
            Route = "planet/raxus-ii",
            Region = "Outer Rim Territories",
            Description = "Raxus II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6519,
            Y = 1500,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Raxus Prime",
            Slug = "raxus-prime",
            Route = "planet/raxus-prime",
            Region = "Outer Rim Territories",
            Description = "Raxus Prime is a star system in the Outer Rim Territories, within the Tion Hegemony, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6519,
            Y = 1500,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Raydonia",
            Slug = "raydonia",
            Route = "planet/raydonia",
            Region = "Outer Rim Territories",
            Description = "Raydonia is a star system in the Outer Rim Territories, within the Belsmuth Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5066,
            Y = 1593,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Reamma",
            Slug = "reamma",
            Route = "planet/reamma",
            Region = "Wild Space",
            Description = "Reamma is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1946,
            Y = 1723,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Recopia",
            Slug = "recopia",
            Route = "planet/recopia",
            Region = "Core Worlds",
            Description = "Recopia is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4127,
            Y = 2759,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Reecee",
            Slug = "reecee",
            Route = "planet/reecee",
            Region = "Expansion Region",
            Description = "Reecee is a star system in the Expansion Region, within the Zuma Sector, at galactic grid J-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3056,
            Y = 2173,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Rehemsa",
            Slug = "rehemsa",
            Route = "planet/rehemsa",
            Region = "Core Worlds",
            Description = "Rehemsa is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4071,
            Y = 2895,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Reltooine",
            Slug = "reltooine",
            Route = "planet/reltooine",
            Region = "Outer Rim Territories",
            Description = "Reltooine is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid R-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6122,
            Y = 1098,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Remduba II",
            Slug = "remduba-ii",
            Route = "planet/remduba-ii",
            Region = "Wild Space",
            Description = "Remduba II is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1311,
            Y = 2738,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Renatasia",
            Slug = "renatasia",
            Route = "planet/renatasia",
            Region = "Outer Rim Territories",
            Description = "Renatasia is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7100,
            Y = 2261,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Rendili",
            Slug = "rendili",
            Route = "planet/rendili",
            Region = "Core Worlds",
            Description = "Rendili is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4236,
            Y = 2819,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Reuss VIII",
            Slug = "reuss-viii",
            Route = "planet/reuss-viii",
            Region = "Outer Rim Territories",
            Description = "Reuss VIII is a star system in the Outer Rim Territories, within the Portmoak Sector, at galactic grid P-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5369,
            Y = 4445,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Reytha",
            Slug = "reytha",
            Route = "planet/reytha",
            Region = "Expansion Region",
            Description = "Reytha is a star system in the Expansion Region, within the Harron Sector, at galactic grid O-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4982,
            Y = 3063,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Rhinnal",
            Slug = "rhinnal",
            Route = "planet/rhinnal",
            Region = "Core Worlds",
            Description = "Rhinnal is a star system in the Core Worlds, within the Darpa Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3811,
            Y = 2302,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Rhommamool",
            Slug = "rhommamool",
            Route = "planet/rhommamool",
            Region = "Expansion Region",
            Description = "Rhommamool is a star system in the Expansion Region, within the Merthian Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4658,
            Y = 3329,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Riflor",
            Slug = "riflor",
            Route = "planet/riflor",
            Region = "Mid Rim Territories",
            Description = "Riflor is a star system in the Mid Rim Territories, within the Narrant Sector, at galactic grid J-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2926,
            Y = 4095,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Rinn",
            Slug = "rinn",
            Route = "planet/rinn",
            Region = "Outer Rim Territories",
            Description = "Rinn is a star system in the Outer Rim Territories, within the Baxel Sector, at galactic grid U-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7051,
            Y = 3097,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Rintonne",
            Slug = "rintonne",
            Route = "planet/rintonne",
            Region = "Mid Rim Territories",
            Description = "Rintonne is a star system in the Mid Rim Territories, within the Lambda Sector, at galactic grid P-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5302,
            Y = 3961,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Rion",
            Slug = "rion",
            Route = "planet/rion",
            Region = "Outer Rim Territories",
            Description = "Rion is a star system in the Outer Rim Territories, within the Kessel Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6700,
            Y = 2637,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Roccus",
            Slug = "roccus",
            Route = "planet/roccus",
            Region = "Outer Rim Territories",
            Description = "Roccus is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4538,
            Y = 4182,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Roche asteroid field",
            Slug = "roche-asteroid-field",
            Route = "planet/roche-asteroid-field",
            Region = "Mid Rim Territories",
            Description = "Roche asteroid field is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid Q-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5785,
            Y = 2224,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ronika",
            Slug = "ronika",
            Route = "planet/ronika",
            Region = "Deep Core",
            Description = "Ronika is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3672,
            Y = 2600,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ronyards",
            Slug = "ronyards",
            Route = "planet/ronyards",
            Region = "Inner Rim Territories",
            Description = "Ronyards is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4385,
            Y = 3401,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Roon",
            Slug = "roon",
            Route = "planet/roon",
            Region = "Outer Rim Territories",
            Description = "Roon is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6659,
            Y = 3827,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ropagi II",
            Slug = "ropagi-ii",
            Route = "planet/ropagi-ii",
            Region = "Mid Rim Territories",
            Description = "Ropagi II is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid N-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4624,
            Y = 3913,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Rorak 4",
            Slug = "rorak-4",
            Route = "planet/rorak-4",
            Region = "Mid Rim Territories",
            Description = "Rorak 4 is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6373,
            Y = 3115,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Rothana",
            Slug = "rothana",
            Route = "planet/rothana",
            Region = "Outer Rim Territories",
            Description = "Rothana is a star system in the Outer Rim Territories, within the Quiberon Sector, at galactic grid T-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6856,
            Y = 3759,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Ruhe",
            Slug = "ruhe",
            Route = "planet/ruhe",
            Region = "Outer Rim Territories",
            Description = "Ruhe is a star system in the Outer Rim Territories, within the Savareen Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5689,
            Y = 4158,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Rutan",
            Slug = "rutan",
            Route = "planet/rutan",
            Region = "Outer Rim Territories",
            Description = "Rutan is a star system in the Outer Rim Territories, within the Atravis Sector, at galactic grid L-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3659,
            Y = 4821,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ruul",
            Slug = "ruul",
            Route = "planet/ruul",
            Region = "Deep Core",
            Description = "Ruul is a star system in the Deep Core, within the Zuma Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4000,
            Y = 2685,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ruuria",
            Slug = "ruuria",
            Route = "planet/ruuria",
            Region = "Outer Rim Territories",
            Description = "Ruuria is a star system in the Outer Rim Territories, within the Xappyh Sector, at galactic grid Q-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5801,
            Y = 1098,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Rychel",
            Slug = "rychel",
            Route = "planet/rychel",
            Region = "Outer Rim Territories",
            Description = "Rychel is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3978,
            Y = 732,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Ryien",
            Slug = "ryien",
            Route = "planet/ryien",
            Region = "Wild Space",
            Description = "Ryien is a star system in the Wild Space, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6734,
            Y = 1370,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "RZ7-6113-23",
            Slug = "rz7-6113-23",
            Route = "planet/rz7-6113-23",
            Region = "Outer Rim Territories",
            Description = "RZ7-6113-23 is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3945,
            Y = 1343,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Sacorria",
            Slug = "sacorria",
            Route = "planet/sacorria",
            Region = "Core Worlds",
            Description = "Sacorria is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4040,
            Y = 2926,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Saijo",
            Slug = "saijo",
            Route = "planet/saijo",
            Region = "Outer Rim Territories",
            Description = "Saijo is a star system in the Outer Rim Territories, within the Saijo Sector, at galactic grid K-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3248,
            Y = 4880,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Sakifwanna",
            Slug = "sakifwanna",
            Route = "planet/sakifwanna",
            Region = "Outer Rim Territories",
            Description = "Sakifwanna is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6898,
            Y = 2787,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Sakiya",
            Slug = "sakiya",
            Route = "planet/sakiya",
            Region = "Mid Rim Territories",
            Description = "Sakiya is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6354,
            Y = 2815,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Sanctuary",
            Slug = "sanctuary",
            Route = "planet/sanctuary",
            Region = "Outer Rim Territories",
            Description = "Sanctuary is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7054,
            Y = 1997,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Saqqar",
            Slug = "saqqar",
            Route = "planet/saqqar",
            Region = "Outer Rim Territories",
            Description = "Saqqar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7032,
            Y = 2851,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Sarapin",
            Slug = "sarapin",
            Route = "planet/sarapin",
            Region = "Core Worlds",
            Description = "Sarapin is a star system in the Core Worlds, within the Alderaan Sector, at galactic grid M-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4158,
            Y = 2711,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Sarapin Four",
            Slug = "sarapin-four",
            Route = "planet/sarapin-four",
            Region = "Core Worlds",
            Description = "Sarapin Four is a star system in the Core Worlds, within the Zuma Sector, at galactic grid H-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3567,
            Y = 2607,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Sarka",
            Slug = "sarka",
            Route = "planet/sarka",
            Region = "Mid Rim Territories",
            Description = "Sarka is a star system in the Mid Rim Territories, within the Sarka Sector, at galactic grid Q-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5846,
            Y = 2146,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Sarlucif",
            Slug = "sarlucif",
            Route = "planet/sarlucif",
            Region = "Wild Space",
            Description = "Sarlucif is a star system in the Wild Space, within the Zuma Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6332,
            Y = 1266,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Sarrassia",
            Slug = "sarrassia",
            Route = "planet/sarrassia",
            Region = "Outer Rim Territories",
            Description = "Sarrassia is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4629,
            Y = 4317,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Sarrish",
            Slug = "sarrish",
            Route = "planet/sarrish",
            Region = "Expansion Region",
            Description = "Sarrish is a star system in the Expansion Region, within the Vensensor Sector, at galactic grid K-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3371,
            Y = 3996,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Sathiemon",
            Slug = "sathiemon",
            Route = "planet/sathiemon",
            Region = "Outer Rim Territories",
            Description = "Sathiemon is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5587,
            Y = 1163,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Sebaddon",
            Slug = "sebaddon",
            Route = "planet/sebaddon",
            Region = "Mid Rim Territories",
            Description = "Sebaddon is a star system in the Mid Rim Territories, within the  Sector, at galactic grid Q-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5760,
            Y = 2940,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Sebiris",
            Slug = "sebiris",
            Route = "planet/sebiris",
            Region = "Outer Rim Territories",
            Description = "Sebiris is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4135,
            Y = 480,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Sedratis",
            Slug = "sedratis",
            Route = "planet/sedratis",
            Region = "Core Worlds",
            Description = "Sedratis is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4310,
            Y = 2757,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Sedri",
            Slug = "sedri",
            Route = "planet/sedri",
            Region = "Outer Rim Territories",
            Description = "Sedri is a star system in the Outer Rim Territories, within the Tharin Sector, at galactic grid S-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6562,
            Y = 2128,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Seelos",
            Slug = "seelos",
            Route = "planet/seelos",
            Region = "Wild Space",
            Description = "Seelos is a star system in the Wild Space, within the Zuma Sector, at galactic grid E-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2302,
            Y = 2280,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Seidhkona",
            Slug = "seidhkona",
            Route = "planet/seidhkona",
            Region = "Outer Rim Territories",
            Description = "Seidhkona is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6898,
            Y = 1460,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Seline",
            Slug = "seline",
            Route = "planet/seline",
            Region = "Outer Rim Territories",
            Description = "Seline is a star system in the Outer Rim Territories, within the Dalonbian Sector, at galactic grid M-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4070,
            Y = 988,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Selvaris",
            Slug = "selvaris",
            Route = "planet/selvaris",
            Region = "Colonies",
            Description = "Selvaris is a star system in the Colonies, within the Zuma Sector, at galactic grid I-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2854,
            Y = 2403,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Seoul 5",
            Slug = "seoul-5",
            Route = "planet/seoul-5",
            Region = "Wild Space",
            Description = "Seoul 5 is a star system in the Wild Space, within the Varada Sector, at galactic grid H-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2126,
            Y = 4880,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Sepan 8",
            Slug = "sepan-8",
            Route = "planet/sepan-8",
            Region = "Expansion Region",
            Description = "Sepan 8 is a star system in the Expansion Region, within the Zuma Sector, at galactic grid P-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5346,
            Y = 3332,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Seregar",
            Slug = "seregar",
            Route = "planet/seregar",
            Region = "Outer Rim Territories",
            Description = "Seregar is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid U-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7132,
            Y = 2375,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Serphidi",
            Slug = "serphidi",
            Route = "planet/serphidi",
            Region = "Outer Rim Territories",
            Description = "Serphidi is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4709,
            Y = 4309,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Serroco",
            Slug = "serroco",
            Route = "planet/serroco",
            Region = "Expansion Region",
            Description = "Serroco is a star system in the Expansion Region, within the Ploo Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4717,
            Y = 1980,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Sesid",
            Slug = "sesid",
            Route = "planet/sesid",
            Region = "Outer Rim Territories",
            Description = "Sesid is a star system in the Outer Rim Territories, within the Corva Sector, at galactic grid P-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5389,
            Y = 1128,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Sevarcos",
            Slug = "sevarcos",
            Route = "planet/sevarcos",
            Region = "Outer Rim Territories",
            Description = "Sevarcos is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4410,
            Y = 4737,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Seylott",
            Slug = "seylott",
            Route = "planet/seylott",
            Region = "Outer Rim Territories",
            Description = "Seylott is a star system in the Outer Rim Territories, within the Sarin Sector, at galactic grid P-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5333,
            Y = 4385,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Sha Qarot",
            Slug = "sha-qarot",
            Route = "planet/sha-qarot",
            Region = "Wild Space",
            Description = "Sha Qarot is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1770,
            Y = 1571,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Shadda-Bi-Boran",
            Slug = "shadda-bi-boran",
            Route = "planet/shadda-bi-boran",
            Region = "Outer Rim Territories",
            Description = "Shadda-Bi-Boran is a star system in the Outer Rim Territories, within the Toblain Sector, at galactic grid O-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4836,
            Y = 4351,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Shador",
            Slug = "shador",
            Route = "planet/shador",
            Region = "Mid Rim Territories",
            Description = "Shador is a star system in the Mid Rim Territories, within the Maerdocian Sector, at galactic grid Q-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5693,
            Y = 3375,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Shalyvane",
            Slug = "shalyvane",
            Route = "planet/shalyvane",
            Region = "Outer Rim Territories",
            Description = "Shalyvane is a star system in the Outer Rim Territories, within the Indrexu Sector, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6523,
            Y = 1407,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Shantipole",
            Slug = "shantipole",
            Route = "planet/shantipole",
            Region = "Core Worlds",
            Description = "Shantipole is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3658,
            Y = 3288,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Shawken",
            Slug = "shawken",
            Route = "planet/shawken",
            Region = "Core Worlds",
            Description = "Shawken is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3939,
            Y = 2427,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Shelkonwa",
            Slug = "shelkonwa",
            Route = "planet/shelkonwa",
            Region = "Colonies",
            Description = "Shelkonwa is a star system in the Colonies, within the Zuma Sector, at galactic grid M-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4308,
            Y = 2414,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Shi'kar homeworld",
            Slug = "shikar-homeworld",
            Route = "planet/shikar-homeworld",
            Region = "Wild Space",
            Description = "Shi'kar homeworld is a star system in the Wild Space, within the Zuma Sector, at galactic grid G-1, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2888,
            Y = 494,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Shi'kar Straits",
            Slug = "shikar-straits",
            Route = "planet/shikar-straits",
            Region = "Outer Rim Territories",
            Description = "Shi'kar Straits is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5471,
            Y = 1175,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Shikaakwa",
            Slug = "shikaakwa",
            Route = "planet/shikaakwa",
            Region = "Deep Core",
            Description = "Shikaakwa is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3805,
            Y = 2722,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Shimia",
            Slug = "shimia",
            Route = "planet/shimia",
            Region = "Outer Rim Territories",
            Description = "Shimia is a star system in the Outer Rim Territories, within the Dalchon Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6046,
            Y = 4216,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Shinbone",
            Slug = "shinbone",
            Route = "planet/shinbone",
            Region = "Outer Rim Territories",
            Description = "Shinbone is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6873,
            Y = 4180,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Shintel",
            Slug = "shintel",
            Route = "planet/shintel",
            Region = "Outer Rim Territories",
            Description = "Shintel is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4334,
            Y = 618,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Shiva IV",
            Slug = "shiva-iv",
            Route = "planet/shiva-iv",
            Region = "Outer Rim Territories",
            Description = "Shiva IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3804,
            Y = 500,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Shola",
            Slug = "shola",
            Route = "planet/shola",
            Region = "Outer Rim Territories",
            Description = "Shola is a star system in the Outer Rim Territories, within the Tammuz Sector, at galactic grid U-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7089,
            Y = 3450,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Shownar",
            Slug = "shownar",
            Route = "planet/shownar",
            Region = "Outer Rim Territories",
            Description = "Shownar is a star system in the Outer Rim Territories, within the Parmic Sector, at galactic grid P-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5368,
            Y = 4594,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Shramar",
            Slug = "shramar",
            Route = "planet/shramar",
            Region = "Outer Rim Territories",
            Description = "Shramar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3296,
            Y = 1288,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Shu-Torun",
            Slug = "shu-torun",
            Route = "planet/shu-torun",
            Region = "Mid Rim Territories",
            Description = "Shu-Torun is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid N-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5719,
            Y = 2512,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Shuldene",
            Slug = "shuldene",
            Route = "planet/shuldene",
            Region = "Outer Rim Territories",
            Description = "Shuldene is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid J-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2894,
            Y = 4390,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Shumari",
            Slug = "shumari",
            Route = "planet/shumari",
            Region = "Outer Rim Territories",
            Description = "Shumari is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5003,
            Y = 4482,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Shusugaunt",
            Slug = "shusugaunt",
            Route = "planet/shusugaunt",
            Region = "Wild Space",
            Description = "Shusugaunt is a star system in the Wild Space, within the Zuma Sector, at galactic grid A-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 626,
            Y = 3900,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Sicemon",
            Slug = "sicemon",
            Route = "planet/sicemon",
            Region = "Wild Space",
            Description = "Sicemon is a star system in the Wild Space, within the Zuma Sector, at galactic grid C-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1352,
            Y = 2453,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Sif-Uwana",
            Slug = "sif-uwana",
            Route = "planet/sif-uwana",
            Region = "Expansion Region",
            Description = "Sif-Uwana is a star system in the Expansion Region, within the Zuma Sector, at galactic grid K-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3457,
            Y = 2222,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Silken Asteroids",
            Slug = "silken-asteroids",
            Route = "planet/silken-asteroids",
            Region = "Outer Rim Territories",
            Description = "Silken Asteroids is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid O-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4996,
            Y = 4850,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Simbarc",
            Slug = "simbarc",
            Route = "planet/simbarc",
            Region = "Outer Rim Territories",
            Description = "Simbarc is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7038,
            Y = 2205,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Simocadia",
            Slug = "simocadia",
            Route = "planet/simocadia",
            Region = "Colonies",
            Description = "Simocadia is a star system in the Colonies, within the Zuma Sector, at galactic grid J-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2865,
            Y = 3224,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Simoom",
            Slug = "simoom",
            Route = "planet/simoom",
            Region = "Mid Rim Territories",
            Description = "Simoom is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid L-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3678,
            Y = 4381,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Sinsang",
            Slug = "sinsang",
            Route = "planet/sinsang",
            Region = "Outer Rim Territories",
            Description = "Sinsang is a star system in the Outer Rim Territories, within the Raioballo Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3804,
            Y = 1235,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Sinton",
            Slug = "sinton",
            Route = "planet/sinton",
            Region = "Mid Rim Territories",
            Description = "Sinton is a star system in the Mid Rim Territories, within the Rago Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2615,
            Y = 1948,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ska Gora",
            Slug = "ska-gora",
            Route = "planet/ska-gora",
            Region = "Deep Core",
            Description = "Ska Gora is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3774,
            Y = 2697,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Skako Minor",
            Slug = "skako-minor",
            Route = "planet/skako-minor",
            Region = "Colonies",
            Description = "Skako Minor is a star system in the Colonies, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3721,
            Y = 2439,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Skaradosh",
            Slug = "skaradosh",
            Route = "planet/skaradosh",
            Region = "Wild Space",
            Description = "Skaradosh is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1983,
            Y = 2527,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Skarpos",
            Slug = "skarpos",
            Route = "planet/skarpos",
            Region = "Mid Rim Territories",
            Description = "Skarpos is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid O-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6252,
            Y = 2605,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Skeebo",
            Slug = "skeebo",
            Route = "planet/skeebo",
            Region = "Outer Rim Territories",
            Description = "Skeebo is a star system in the Outer Rim Territories, within the Shadola Sector, at galactic grid U-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7323,
            Y = 2182,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Skor II",
            Slug = "skor-ii",
            Route = "planet/skor-ii",
            Region = "Outer Rim Territories",
            Description = "Skor II is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4162,
            Y = 4880,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Skorii-Lei",
            Slug = "skorii-lei",
            Route = "planet/skorii-lei",
            Region = "Outer Rim Territories",
            Description = "Skorii-Lei is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid @-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 309,
            Y = 963,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Skorrupon",
            Slug = "skorrupon",
            Route = "planet/skorrupon",
            Region = "Mid Rim Territories",
            Description = "Skorrupon is a star system in the Mid Rim Territories, within the Trans-Vulta Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4571,
            Y = 1839,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Skye",
            Slug = "skye",
            Route = "planet/skye",
            Region = "Outer Rim Territories",
            Description = "Skye is a star system in the Outer Rim Territories, within the Varada Sector, at galactic grid H-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2399,
            Y = 4757,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Sluis Van",
            Slug = "sluis-van",
            Route = "planet/sluis-van",
            Region = "Outer Rim Territories",
            Description = "Sluis Van is a star system in the Outer Rim Territories, within the Sluis Sector, at galactic grid M-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4231,
            Y = 4586,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Smarck",
            Slug = "smarck",
            Route = "planet/smarck",
            Region = "Outer Rim Territories",
            Description = "Smarck is a star system in the Outer Rim Territories, within the Cademimu Sector, at galactic grid K-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3597,
            Y = 1590,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Smarteel",
            Slug = "smarteel",
            Route = "planet/smarteel",
            Region = "Outer Rim Territories",
            Description = "Smarteel is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7162,
            Y = 3425,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Socorro",
            Slug = "socorro",
            Route = "planet/socorro",
            Region = "Outer Rim Territories",
            Description = "Socorro is a star system in the Outer Rim Territories, within the Kibilini Sector, at galactic grid Q-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5569,
            Y = 4247,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Solay",
            Slug = "solay",
            Route = "planet/solay",
            Region = "Outer Rim Territories",
            Description = "Solay is a star system in the Outer Rim Territories, within the Dominus Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7216,
            Y = 1999,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Solem",
            Slug = "solem",
            Route = "planet/solem",
            Region = "Outer Rim Territories",
            Description = "Solem is a star system in the Outer Rim Territories, within the Rayter Sector, at galactic grid J-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3018,
            Y = 4623,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Solibus IV",
            Slug = "solibus-iv",
            Route = "planet/solibus-iv",
            Region = "Expansion Region",
            Description = "Solibus IV is a star system in the Expansion Region, within the Zuma Sector, at galactic grid K-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3413,
            Y = 3878,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Somov Rit",
            Slug = "somov-rit",
            Route = "planet/somov-rit",
            Region = "Mid Rim Territories",
            Description = "Somov Rit is a star system in the Mid Rim Territories, within the Onatos Sector, at galactic grid R-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6246,
            Y = 3718,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Son-tuul",
            Slug = "son-tuul",
            Route = "planet/son-tuul",
            Region = "Mid Rim Territories",
            Description = "Son-tuul is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid H-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3436,
            Y = 1956,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Sooma",
            Slug = "sooma",
            Route = "planet/sooma",
            Region = "Outer Rim Territories",
            Description = "Sooma is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6028,
            Y = 1612,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Spalex",
            Slug = "spalex",
            Route = "planet/spalex",
            Region = "Mid Rim Territories",
            Description = "Spalex is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3950,
            Y = 1888,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Spefik",
            Slug = "spefik",
            Route = "planet/spefik",
            Region = "Outer Rim Territories",
            Description = "Spefik is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3930,
            Y = 1505,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Spindrift",
            Slug = "spindrift",
            Route = "planet/spindrift",
            Region = "Outer Rim Territories",
            Description = "Spindrift is a star system in the Outer Rim Territories, within the Rseik Sector, at galactic grid N-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4746,
            Y = 4880,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Spintir",
            Slug = "spintir",
            Route = "planet/spintir",
            Region = "Outer Rim Territories",
            Description = "Spintir is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5742,
            Y = 1653,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Spira",
            Slug = "spira",
            Route = "planet/spira",
            Region = "Core Worlds",
            Description = "Spira is a star system in the Core Worlds, within the Lytton Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3798,
            Y = 2503,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Spuma",
            Slug = "spuma",
            Route = "planet/spuma",
            Region = "Outer Rim Territories",
            Description = "Spuma is a star system in the Outer Rim Territories, within the Seswenna Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4289,
            Y = 4483,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Stend IV",
            Slug = "stend-iv",
            Route = "planet/stend-iv",
            Region = "Outer Rim Territories",
            Description = "Stend IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5393,
            Y = 4298,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Stend VI",
            Slug = "stend-vi",
            Route = "planet/stend-vi",
            Region = "Outer Rim Territories",
            Description = "Stend VI is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5209,
            Y = 4333,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Stenos",
            Slug = "stenos",
            Route = "planet/stenos",
            Region = "Outer Rim Territories",
            Description = "Stenos is a star system in the Outer Rim Territories, within the Spadja Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5968,
            Y = 1559,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Sterdic IV",
            Slug = "sterdic-iv",
            Route = "planet/sterdic-iv",
            Region = "Outer Rim Territories",
            Description = "Sterdic IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid B-1, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1176,
            Y = 588,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Stic",
            Slug = "stic",
            Route = "planet/stic",
            Region = "Outer Rim Territories",
            Description = "Stic is a star system in the Outer Rim Territories, within the Xappyh Sector, at galactic grid Q-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5647,
            Y = 1116,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Stobar",
            Slug = "stobar",
            Route = "planet/stobar",
            Region = "Expansion Region",
            Description = "Stobar is a star system in the Expansion Region, within the Boeus Sector, at galactic grid M-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4303,
            Y = 3858,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Stoga",
            Slug = "stoga",
            Route = "planet/stoga",
            Region = "Outer Rim Territories",
            Description = "Stoga is a star system in the Outer Rim Territories, within the Bitrose Sector, at galactic grid T-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6668,
            Y = 4228,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Storthus",
            Slug = "storthus",
            Route = "planet/storthus",
            Region = "Mid Rim Territories",
            Description = "Storthus is a star system in the Mid Rim Territories, within the Churba Sector, at galactic grid P-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5300,
            Y = 3694,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Stroiketcy",
            Slug = "stroiketcy",
            Route = "planet/stroiketcy",
            Region = "Outer Rim Territories",
            Description = "Stroiketcy is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5229,
            Y = 1759,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Strokill Prime",
            Slug = "strokill-prime",
            Route = "planet/strokill-prime",
            Region = "Outer Rim Territories",
            Description = "Strokill Prime is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid G-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3228,
            Y = 4485,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Su Exposs",
            Slug = "su-exposs",
            Route = "planet/su-exposs",
            Region = "Mid Rim Territories",
            Description = "Su Exposs is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid L-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3814,
            Y = 1981,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Sululluub",
            Slug = "sululluub",
            Route = "planet/sululluub",
            Region = "Mid Rim Territories",
            Description = "Sululluub is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4203,
            Y = 4297,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Sump",
            Slug = "sump",
            Route = "planet/sump",
            Region = "Outer Rim Territories",
            Description = "Sump is a star system in the Outer Rim Territories, within the Koradin Sector, at galactic grid I-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2826,
            Y = 4539,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Sunspot",
            Slug = "sunspot",
            Route = "planet/sunspot",
            Region = "Core Worlds",
            Description = "Sunspot is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3765,
            Y = 2548,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Suurja",
            Slug = "suurja",
            Route = "planet/suurja",
            Region = "Outer Rim Territories",
            Description = "Suurja is a star system in the Outer Rim Territories, within the Ojoster Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4654,
            Y = 1842,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Svivren",
            Slug = "svivren",
            Route = "planet/svivren",
            Region = "Outer Rim Territories",
            Description = "Svivren is a star system in the Outer Rim Territories, within the Svivreni Sector, at galactic grid O-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4980,
            Y = 4660,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Syned",
            Slug = "syned",
            Route = "planet/syned",
            Region = "Outer Rim Territories",
            Description = "Syned is a star system in the Outer Rim Territories, within the Grumani Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4511,
            Y = 4153,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Taanab",
            Slug = "taanab",
            Route = "planet/taanab",
            Region = "Inner Rim Territories",
            Description = "Taanab is a star system in the Inner Rim Territories, within the The Veil, at galactic grid O-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4946,
            Y = 2241,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tahlboor",
            Slug = "tahlboor",
            Route = "planet/tahlboor",
            Region = "Outer Rim Territories",
            Description = "Tahlboor is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6257,
            Y = 1446,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Taivas",
            Slug = "taivas",
            Route = "planet/taivas",
            Region = "Mid Rim Territories",
            Description = "Taivas is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5144,
            Y = 4117,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Takobo",
            Slug = "takobo",
            Route = "planet/takobo",
            Region = "Wild Space",
            Description = "Takobo is a star system in the Wild Space, within the Zuma Sector, at galactic grid R-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7174,
            Y = 871,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Talas",
            Slug = "talas",
            Route = "planet/talas",
            Region = "Outer Rim Territories",
            Description = "Talas is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7391,
            Y = 1906,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Talasea",
            Slug = "talasea",
            Route = "planet/talasea",
            Region = "Colonies",
            Description = "Talasea is a star system in the Colonies, within the Morobe Sector, at galactic grid N-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4568,
            Y = 2730,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Talay",
            Slug = "talay",
            Route = "planet/talay",
            Region = "Mid Rim Territories",
            Description = "Talay is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid Q-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5785,
            Y = 3991,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Tallaan",
            Slug = "tallaan",
            Route = "planet/tallaan",
            Region = "Colonies",
            Description = "Tallaan is a star system in the Colonies, within the Tapani Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3778,
            Y = 3356,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Taloraan",
            Slug = "taloraan",
            Route = "planet/taloraan",
            Region = "Expansion Region",
            Description = "Taloraan is a star system in the Expansion Region, within the  Sector, at galactic grid I-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2830,
            Y = 3797,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Talus",
            Slug = "talus",
            Route = "planet/talus",
            Region = "Core Worlds",
            Description = "Talus is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4203,
            Y = 2926,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Tamban",
            Slug = "tamban",
            Route = "planet/tamban",
            Region = "Core Worlds",
            Description = "Tamban is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3391,
            Y = 2595,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Tammuz-an",
            Slug = "tammuz-an",
            Route = "planet/tammuz-an",
            Region = "Outer Rim Territories",
            Description = "Tammuz-an is a star system in the Outer Rim Territories, within the Galov Sector, at galactic grid T-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6878,
            Y = 3517,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Tamsye Prime",
            Slug = "tamsye-prime",
            Route = "planet/tamsye-prime",
            Region = "Outer Rim Territories",
            Description = "Tamsye Prime is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid E-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2283,
            Y = 3499,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Tandankin",
            Slug = "tandankin",
            Route = "planet/tandankin",
            Region = "Outer Rim Territories",
            Description = "Tandankin is a star system in the Outer Rim Territories, within the Spadja Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6144,
            Y = 1630,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tangrene",
            Slug = "tangrene",
            Route = "planet/tangrene",
            Region = "Outer Rim Territories",
            Description = "Tangrene is a star system in the Outer Rim Territories, within the Morshdine Sector, at galactic grid O-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4946,
            Y = 1327,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Tantajoc V",
            Slug = "tantajoc-v",
            Route = "planet/tantajoc-v",
            Region = "Mid Rim Territories",
            Description = "Tantajoc V is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid P-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5234,
            Y = 1962,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Taral V",
            Slug = "taral-v",
            Route = "planet/taral-v",
            Region = "Outer Rim Territories",
            Description = "Taral V is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7337,
            Y = 2024,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Targonn",
            Slug = "targonn",
            Route = "planet/targonn",
            Region = "Outer Rim Territories",
            Description = "Targonn is a star system in the Outer Rim Territories, within the Dominus Sector, at galactic grid U-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7245,
            Y = 2012,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Taris asteroid belt",
            Slug = "taris-asteroid-belt",
            Route = "planet/taris-asteroid-belt",
            Region = "Outer Rim Territories",
            Description = "Taris asteroid belt is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4641,
            Y = 1824,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tarnoonga",
            Slug = "tarnoonga",
            Route = "planet/tarnoonga",
            Region = "Outer Rim Territories",
            Description = "Tarnoonga is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6174,
            Y = 4118,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Taronda",
            Slug = "taronda",
            Route = "planet/taronda",
            Region = "Outer Rim Territories",
            Description = "Taronda is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2775,
            Y = 4132,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Tarsa",
            Slug = "tarsa",
            Route = "planet/tarsa",
            Region = "Mid Rim Territories",
            Description = "Tarsa is a star system in the Mid Rim Territories, within the D'aelgoth Sector, at galactic grid L-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3884,
            Y = 4155,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Taspir III",
            Slug = "taspir-iii",
            Route = "planet/taspir-iii",
            Region = "Wild Space",
            Description = "Taspir III is a star system in the Wild Space, within the Zuma Sector, at galactic grid J-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3008,
            Y = 1188,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Tay'ah'loo",
            Slug = "tayahloo",
            Route = "planet/tayahloo",
            Region = "Mid Rim Territories",
            Description = "Tay'ah'loo is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid J-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3136,
            Y = 4203,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Te Hasa",
            Slug = "te-hasa",
            Route = "planet/te-hasa",
            Region = "Outer Rim Territories",
            Description = "Te Hasa is a star system in the Outer Rim Territories, within the Veragi Sector, at galactic grid K-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3583,
            Y = 777,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Tebru",
            Slug = "tebru",
            Route = "planet/tebru",
            Region = "Outer Rim Territories",
            Description = "Tebru is a star system in the Outer Rim Territories, within the Juris Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5266,
            Y = 4333,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Telerath",
            Slug = "telerath",
            Route = "planet/telerath",
            Region = "Mid Rim Territories",
            Description = "Telerath is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid N-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4396,
            Y = 1911,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Telfrey",
            Slug = "telfrey",
            Route = "planet/telfrey",
            Region = "Outer Rim Territories",
            Description = "Telfrey is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5981,
            Y = 4001,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Telos IV",
            Slug = "telos-iv",
            Route = "planet/telos-iv",
            Region = "Outer Rim Territories",
            Description = "Telos IV is a star system in the Outer Rim Territories, within the Tynquay Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5535,
            Y = 1192,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Tenara",
            Slug = "tenara",
            Route = "planet/tenara",
            Region = "Outer Rim Territories",
            Description = "Tenara is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5699,
            Y = 1757,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Tenupe",
            Slug = "tenupe",
            Route = "planet/tenupe",
            Region = "Wild Space",
            Description = "Tenupe is a star system in the Wild Space, within the Utegetu Nebula, at galactic grid I-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2834,
            Y = 2136,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Terephon",
            Slug = "terephon",
            Route = "planet/terephon",
            Region = "Inner Rim Territories",
            Description = "Terephon is a star system in the Inner Rim Territories, within the Hapes Cluster, at galactic grid O-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4889,
            Y = 2309,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Tergamenion",
            Slug = "tergamenion",
            Route = "planet/tergamenion",
            Region = "Mid Rim Territories",
            Description = "Tergamenion is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4005,
            Y = 4161,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Terminus",
            Slug = "terminus",
            Route = "planet/terminus",
            Region = "Outer Rim Territories",
            Description = "Terminus is a star system in the Outer Rim Territories, within the Kallea Sector, at galactic grid K-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3337,
            Y = 4880,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Terra Sool",
            Slug = "terra-sool",
            Route = "planet/terra-sool",
            Region = "Expansion Region",
            Description = "Terra Sool is a star system in the Expansion Region, within the Immeria Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4870,
            Y = 3470,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Tertiary Kesmere",
            Slug = "tertiary-kesmere",
            Route = "planet/tertiary-kesmere",
            Region = "Outer Rim Territories",
            Description = "Tertiary Kesmere is a star system in the Outer Rim Territories, within the Raioballo Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3642,
            Y = 1137,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Teth",
            Slug = "teth",
            Route = "planet/teth",
            Region = "Outer Rim Territories",
            Description = "Teth is a star system in the Outer Rim Territories, within the Baxel Sector, at galactic grid U-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7067,
            Y = 2980,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Teyr",
            Slug = "teyr",
            Route = "planet/teyr",
            Region = "Colonies",
            Description = "Teyr is a star system in the Colonies, within the Tapani Sector, at galactic grid L-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3925,
            Y = 3383,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Thaldo",
            Slug = "thaldo",
            Route = "planet/thaldo",
            Region = "Mid Rim Territories",
            Description = "Thaldo is a star system in the Mid Rim Territories, within the Graador Sector, at galactic grid J-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2909,
            Y = 4202,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Thanta Zilbra",
            Slug = "thanta-zilbra",
            Route = "planet/thanta-zilbra",
            Region = "Outer Rim Territories",
            Description = "Thanta Zilbra is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5589,
            Y = 1090,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tharkos",
            Slug = "tharkos",
            Route = "planet/tharkos",
            Region = "Outer Rim Territories",
            Description = "Tharkos is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5974,
            Y = 1750,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "The Clar",
            Slug = "the-clar",
            Route = "planet/the-clar",
            Region = "Outer Rim Territories",
            Description = "The Clar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2519,
            Y = 4880,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "The Deep",
            Slug = "the-deep",
            Route = "planet/the-deep",
            Region = "Wild Space",
            Description = "The Deep is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2533,
            Y = 1503,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Themis",
            Slug = "themis",
            Route = "planet/themis",
            Region = "Expansion Region",
            Description = "Themis is a star system in the Expansion Region, within the Zuma Sector, at galactic grid L-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3715,
            Y = 3821,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Thila",
            Slug = "thila",
            Route = "planet/thila",
            Region = "Outer Rim Territories",
            Description = "Thila is a star system in the Outer Rim Territories, within the I-Sector, at galactic grid Q-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5602,
            Y = 1273,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Thorgeld I",
            Slug = "thorgeld-i",
            Route = "planet/thorgeld-i",
            Region = "Core Worlds",
            Description = "Thorgeld I is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3668,
            Y = 2379,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Thrad",
            Slug = "thrad",
            Route = "planet/thrad",
            Region = "Wild Space",
            Description = "Thrad is a star system in the Wild Space, within the Zuma Sector, at galactic grid D-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1861,
            Y = 2518,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Thrakia",
            Slug = "thrakia",
            Route = "planet/thrakia",
            Region = "Inner Rim Territories",
            Description = "Thrakia is a star system in the Inner Rim Territories, within the Hapes Cluster, at galactic grid O-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4951,
            Y = 2306,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Thuna III",
            Slug = "thuna-iii",
            Route = "planet/thuna-iii",
            Region = "Mid Rim Territories",
            Description = "Thuna III is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2812,
            Y = 1614,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Thustra",
            Slug = "thustra",
            Route = "planet/thustra",
            Region = "Expansion Region",
            Description = "Thustra is a star system in the Expansion Region, within the Sumitra Sector, at galactic grid O-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4769,
            Y = 1972,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Thyferra",
            Slug = "thyferra",
            Route = "planet/thyferra",
            Region = "Inner Rim Territories",
            Description = "Thyferra is a star system in the Inner Rim Territories, within the Jaso Sector, at galactic grid L-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3859,
            Y = 3517,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Tieos",
            Slug = "tieos",
            Route = "planet/tieos",
            Region = "Outer Rim Territories",
            Description = "Tieos is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6393,
            Y = 3792,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Tierfon",
            Slug = "tierfon",
            Route = "planet/tierfon",
            Region = "Expansion Region",
            Description = "Tierfon is a star system in the Expansion Region, within the Sumitra Sector, at galactic grid O-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4827,
            Y = 1928,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Tirahnn",
            Slug = "tirahnn",
            Route = "planet/tirahnn",
            Region = "Inner Rim Territories",
            Description = "Tirahnn is a star system in the Inner Rim Territories, within the Zeemacht Cluster, at galactic grid N-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4591,
            Y = 2217,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Tisht",
            Slug = "tisht",
            Route = "planet/tisht",
            Region = "Outer Rim Territories",
            Description = "Tisht is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6778,
            Y = 2793,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Tiss'sharl",
            Slug = "tisssharl",
            Route = "planet/tisssharl",
            Region = "Outer Rim Territories",
            Description = "Tiss'sharl is a star system in the Outer Rim Territories, within the Xappyh Sector, at galactic grid R-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5957,
            Y = 1125,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Togoria",
            Slug = "togoria",
            Route = "planet/togoria",
            Region = "Mid Rim Territories",
            Description = "Togoria is a star system in the Mid Rim Territories, within the Taldot Sector, at galactic grid P-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5356,
            Y = 2293,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Tokmia",
            Slug = "tokmia",
            Route = "planet/tokmia",
            Region = "Outer Rim Territories",
            Description = "Tokmia is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3428,
            Y = 4440,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Tol Amn",
            Slug = "tol-amn",
            Route = "planet/tol-amn",
            Region = "Mid Rim Territories",
            Description = "Tol Amn is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5941,
            Y = 2820,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Toprawa",
            Slug = "toprawa",
            Route = "planet/toprawa",
            Region = "Outer Rim Territories",
            Description = "Toprawa is a star system in the Outer Rim Territories, within the Kalamith Sector, at galactic grid P-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5157,
            Y = 1474,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Torize",
            Slug = "torize",
            Route = "planet/torize",
            Region = "Outer Rim Territories",
            Description = "Torize is a star system in the Outer Rim Territories, within the Kathol Sector, at galactic grid M-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4066,
            Y = 461,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Tozeer",
            Slug = "tozeer",
            Route = "planet/tozeer",
            Region = "Outer Rim Territories",
            Description = "Tozeer is a star system in the Outer Rim Territories, within the Hunnoverrs Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6153,
            Y = 4066,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tralus",
            Slug = "tralus",
            Route = "planet/tralus",
            Region = "Core Worlds",
            Description = "Tralus is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4201,
            Y = 2919,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Trammis III",
            Slug = "trammis-iii",
            Route = "planet/trammis-iii",
            Region = "Outer Rim Territories",
            Description = "Trammis III is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7325,
            Y = 2135,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Trasse",
            Slug = "trasse",
            Route = "planet/trasse",
            Region = "Mid Rim Territories",
            Description = "Trasse is a star system in the Mid Rim Territories, within the Sarka Sector, at galactic grid Q-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5834,
            Y = 2267,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Trellar Yagen",
            Slug = "trellar-yagen",
            Route = "planet/trellar-yagen",
            Region = "Expansion Region",
            Description = "Trellar Yagen is a star system in the Expansion Region, within the Zuma Sector, at galactic grid O-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4889,
            Y = 3370,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Trenwyth",
            Slug = "trenwyth",
            Route = "planet/trenwyth",
            Region = "Outer Rim Territories",
            Description = "Trenwyth is a star system in the Outer Rim Territories, within the Stensen Sector, at galactic grid I-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2504,
            Y = 4082,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Trigalis",
            Slug = "trigalis",
            Route = "planet/trigalis",
            Region = "Outer Rim Territories",
            Description = "Trigalis is a star system in the Outer Rim Territories, within the Juris Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5169,
            Y = 4203,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Triton",
            Slug = "triton",
            Route = "planet/triton",
            Region = "Outer Rim Territories",
            Description = "Triton is a star system in the Outer Rim Territories, within the Mayagil Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4203,
            Y = 4526,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Trogan",
            Slug = "trogan",
            Route = "planet/trogan",
            Region = "Outer Rim Territories",
            Description = "Trogan is a star system in the Outer Rim Territories, within the Jospro Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6168,
            Y = 1837,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Troska",
            Slug = "troska",
            Route = "planet/troska",
            Region = "Outer Rim Territories",
            Description = "Troska is a star system in the Outer Rim Territories, within the Dantus Sector, at galactic grid J-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3126,
            Y = 1660,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tshindral III",
            Slug = "tshindral-iii",
            Route = "planet/tshindral-iii",
            Region = "Mid Rim Territories",
            Description = "Tshindral III is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4129,
            Y = 4302,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Tsoss Beacon",
            Slug = "tsoss-beacon",
            Route = "planet/tsoss-beacon",
            Region = "Deep Core",
            Description = "Tsoss Beacon is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3724,
            Y = 2855,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Tsyk",
            Slug = "tsyk",
            Route = "planet/tsyk",
            Region = "Outer Rim Territories",
            Description = "Tsyk is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6709,
            Y = 3236,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Tulatharri Junction",
            Slug = "tulatharri-junction",
            Route = "planet/tulatharri-junction",
            Region = "Outer Rim Territories",
            Description = "Tulatharri Junction is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid K-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3575,
            Y = 983,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Tureen VII",
            Slug = "tureen-vii",
            Route = "planet/tureen-vii",
            Region = "Outer Rim Territories",
            Description = "Tureen VII is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5820,
            Y = 1528,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Turkana",
            Slug = "turkana",
            Route = "planet/turkana",
            Region = "Outer Rim Territories",
            Description = "Turkana is a star system in the Outer Rim Territories, within the Pakuuni Sector, at galactic grid T-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6883,
            Y = 1767,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Twon Ketee",
            Slug = "twon-ketee",
            Route = "planet/twon-ketee",
            Region = "Outer Rim Territories",
            Description = "Twon Ketee is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7167,
            Y = 2588,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tyed Kant",
            Slug = "tyed-kant",
            Route = "planet/tyed-kant",
            Region = "Core Worlds",
            Description = "Tyed Kant is a star system in the Core Worlds, within the Zuma Sector, at galactic grid R-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5917,
            Y = 3638,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Tyegin",
            Slug = "tyegin",
            Route = "planet/tyegin",
            Region = "Outer Rim Territories",
            Description = "Tyegin is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid C-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1672,
            Y = 3864,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Tyne's Horky",
            Slug = "tynes-horky",
            Route = "planet/tynes-horky",
            Region = "Mid Rim Territories",
            Description = "Tyne's Horky is a star system in the Mid Rim Territories, within the Teraab Sector, at galactic grid Q-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5837,
            Y = 2944,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Uhanayih",
            Slug = "uhanayih",
            Route = "planet/uhanayih",
            Region = "Expansion Region",
            Description = "Uhanayih is a star system in the Expansion Region, within the Immalia Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3748,
            Y = 2093,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Ukio",
            Slug = "ukio",
            Route = "planet/ukio",
            Region = "Outer Rim Territories",
            Description = "Ukio is a star system in the Outer Rim Territories, within the Abrion Sector, at galactic grid S-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6390,
            Y = 3719,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ulmatra",
            Slug = "ulmatra",
            Route = "planet/ulmatra",
            Region = "Mid Rim Territories",
            Description = "Ulmatra is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6454,
            Y = 2706,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Ultaar",
            Slug = "ultaar",
            Route = "planet/ultaar",
            Region = "Mid Rim Territories",
            Description = "Ultaar is a star system in the Mid Rim Territories, within the Bortele Sector, at galactic grid R-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6101,
            Y = 2146,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Umgul",
            Slug = "umgul",
            Route = "planet/umgul",
            Region = "Mid Rim Territories",
            Description = "Umgul is a star system in the Mid Rim Territories, within the Mulgard Sector, at galactic grid N-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4758,
            Y = 4032,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Unagin",
            Slug = "unagin",
            Route = "planet/unagin",
            Region = "Outer Rim Territories",
            Description = "Unagin is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6831,
            Y = 3281,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Uninhabited planetoid",
            Slug = "uninhabited-planetoid",
            Route = "planet/uninhabited-planetoid",
            Region = "Wild Space",
            Description = "Uninhabited planetoid is a star system in the Wild Space, within the Zuma Sector, at galactic grid B-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1144,
            Y = 2650,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Uphrades",
            Slug = "uphrades",
            Route = "planet/uphrades",
            Region = "Inner Rim Territories",
            Description = "Uphrades is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid M-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4077,
            Y = 2182,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Urdur",
            Slug = "urdur",
            Route = "planet/urdur",
            Region = "Outer Rim Territories",
            Description = "Urdur is a star system in the Outer Rim Territories, within the Corporate Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6433,
            Y = 1252,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Usk",
            Slug = "usk",
            Route = "planet/usk",
            Region = "Hutt Space",
            Description = "Usk is a star system in the Hutt Space, within the Zuma Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6660,
            Y = 2511,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Uthtara",
            Slug = "uthtara",
            Route = "planet/uthtara",
            Region = "Mid Rim Territories",
            Description = "Uthtara is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6112,
            Y = 1934,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "V'shar",
            Slug = "vshar",
            Route = "planet/vshar",
            Region = "Outer Rim Territories",
            Description = "V'shar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid U-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7387,
            Y = 3864,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Vaal",
            Slug = "vaal",
            Route = "planet/vaal",
            Region = "Outer Rim Territories",
            Description = "Vaal is a star system in the Outer Rim Territories, within the Gordian Reach, at galactic grid P-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5436,
            Y = 1393,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Vaal asteroid field",
            Slug = "vaal-asteroid-field",
            Route = "planet/vaal-asteroid-field",
            Region = "Outer Rim Territories",
            Description = "Vaal asteroid field is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5281,
            Y = 1390,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vagran",
            Slug = "vagran",
            Route = "planet/vagran",
            Region = "Core Worlds",
            Description = "Vagran is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4305,
            Y = 2883,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Vaklin",
            Slug = "vaklin",
            Route = "planet/vaklin",
            Region = "Colonies",
            Description = "Vaklin is a star system in the Colonies, within the Zuma Sector, at galactic grid M-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4166,
            Y = 3527,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Valahari",
            Slug = "valahari",
            Route = "planet/valahari",
            Region = "Outer Rim Territories",
            Description = "Valahari is a star system in the Outer Rim Territories, within the D'astan Sector, at galactic grid N-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4611,
            Y = 1427,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Vallt",
            Slug = "vallt",
            Route = "planet/vallt",
            Region = "Outer Rim Territories",
            Description = "Vallt is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6891,
            Y = 3682,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Valrar",
            Slug = "valrar",
            Route = "planet/valrar",
            Region = "Mid Rim Territories",
            Description = "Valrar is a star system in the Mid Rim Territories, within the Glythe Sector, at galactic grid J-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2905,
            Y = 1895,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Valsedian asteroid belt",
            Slug = "valsedian-asteroid-belt",
            Route = "planet/valsedian-asteroid-belt",
            Region = "Outer Rim Territories",
            Description = "Valsedian asteroid belt is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6560,
            Y = 2958,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Vandelhelm",
            Slug = "vandelhelm",
            Route = "planet/vandelhelm",
            Region = "Expansion Region",
            Description = "Vandelhelm is a star system in the Expansion Region, within the Epsi Collective, at galactic grid M-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4069,
            Y = 3840,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Vandelhelm Cloud",
            Slug = "vandelhelm-cloud",
            Route = "planet/vandelhelm-cloud",
            Region = "Expansion Region",
            Description = "Vandelhelm Cloud is a star system in the Expansion Region, within the Zuma Sector, at galactic grid M-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4069,
            Y = 3840,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vandin",
            Slug = "vandin",
            Route = "planet/vandin",
            Region = "Core Worlds",
            Description = "Vandin is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3987,
            Y = 2462,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Vandos",
            Slug = "vandos",
            Route = "planet/vandos",
            Region = "Outer Rim Territories",
            Description = "Vandos is a star system in the Outer Rim Territories, within the Nuiri Sector, at galactic grid Q-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5808,
            Y = 2014,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vanqor",
            Slug = "vanqor",
            Route = "planet/vanqor",
            Region = "Outer Rim Territories",
            Description = "Vanqor is a star system in the Outer Rim Territories, within the Sertar Sector, at galactic grid R-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6198,
            Y = 1527,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Vanquo",
            Slug = "vanquo",
            Route = "planet/vanquo",
            Region = "Outer Rim Territories",
            Description = "Vanquo is a star system in the Outer Rim Territories, within the Meerian Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4762,
            Y = 1615,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vardos",
            Slug = "vardos",
            Route = "planet/vardos",
            Region = "Wild Space",
            Description = "Vardos is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2840,
            Y = 2694,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Varl",
            Slug = "varl",
            Route = "planet/varl",
            Region = "Mid Rim Territories",
            Description = "Varl is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6313,
            Y = 2958,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Varn",
            Slug = "varn",
            Route = "planet/varn",
            Region = "Outer Rim Territories",
            Description = "Varn is a star system in the Outer Rim Territories, within the Quelii Sector, at galactic grid O-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5131,
            Y = 1586,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Varonat",
            Slug = "varonat",
            Route = "planet/varonat",
            Region = "Outer Rim Territories",
            Description = "Varonat is a star system in the Outer Rim Territories, within the Javin Sector, at galactic grid K-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3327,
            Y = 4387,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vashka",
            Slug = "vashka",
            Route = "planet/vashka",
            Region = "Core Worlds",
            Description = "Vashka is a star system in the Core Worlds, within the Zuma Sector, at galactic grid I-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3928,
            Y = 2517,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Vassek",
            Slug = "vassek",
            Route = "planet/vassek",
            Region = "Outer Rim Territories",
            Description = "Vassek is a star system in the Outer Rim Territories, within the Wazta Sector, at galactic grid I-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2631,
            Y = 4337,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Vatleria",
            Slug = "vatleria",
            Route = "planet/vatleria",
            Region = "Outer Rim Territories",
            Description = "Vatleria is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid T-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7025,
            Y = 2321,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vaynai",
            Slug = "vaynai",
            Route = "planet/vaynai",
            Region = "Outer Rim Territories",
            Description = "Vaynai is a star system in the Outer Rim Territories, within the Chorlian Sector, at galactic grid S-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6446,
            Y = 1286,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Veccacopia",
            Slug = "veccacopia",
            Route = "planet/veccacopia",
            Region = "Outer Rim Territories",
            Description = "Veccacopia is a star system in the Outer Rim Territories, within the Tunka Sector, at galactic grid I-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2667,
            Y = 4703,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Vellas Pavo",
            Slug = "vellas-pavo",
            Route = "planet/vellas-pavo",
            Region = "Outer Rim Territories",
            Description = "Vellas Pavo is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid M-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4213,
            Y = 4291,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Velusia",
            Slug = "velusia",
            Route = "planet/velusia",
            Region = "Core Worlds",
            Description = "Velusia is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3949,
            Y = 2443,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vendaxa",
            Slug = "vendaxa",
            Route = "planet/vendaxa",
            Region = "Expansion Region",
            Description = "Vendaxa is a star system in the Expansion Region, within the Chaykin Sector, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4836,
            Y = 3544,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vendred",
            Slug = "vendred",
            Route = "planet/vendred",
            Region = "Mid Rim Territories",
            Description = "Vendred is a star system in the Mid Rim Territories, within the Trax Sector, at galactic grid Q-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5569,
            Y = 2584,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Ventooine",
            Slug = "ventooine",
            Route = "planet/ventooine",
            Region = "Outer Rim Territories",
            Description = "Ventooine is a star system in the Outer Rim Territories, within the Corva Sector, at galactic grid P-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5391,
            Y = 1058,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Verdanth",
            Slug = "verdanth",
            Route = "planet/verdanth",
            Region = "Outer Rim Territories",
            Description = "Verdanth is a star system in the Outer Rim Territories, within the Bon'nyuw-Luq Sector, at galactic grid N-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4660,
            Y = 4171,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Vergesso Asteroids",
            Slug = "vergesso-asteroids",
            Route = "planet/vergesso-asteroids",
            Region = "Outer Rim Territories",
            Description = "Vergesso Asteroids is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5207,
            Y = 4535,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Veroleem",
            Slug = "veroleem",
            Route = "planet/veroleem",
            Region = "Wild Space",
            Description = "Veroleem is a star system in the Wild Space, within the Zuma Sector, at galactic grid I-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2753,
            Y = 1689,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Veron",
            Slug = "veron",
            Route = "planet/veron",
            Region = "Mid Rim Territories",
            Description = "Veron is a star system in the Mid Rim Territories, within the Senex Sector, at galactic grid L-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3844,
            Y = 4153,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Vesla Three",
            Slug = "vesla-three",
            Route = "planet/vesla-three",
            Region = "Outer Rim Territories",
            Description = "Vesla Three is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4406,
            Y = 1622,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Vesla Two",
            Slug = "vesla-two",
            Route = "planet/vesla-two",
            Region = "Outer Rim Territories",
            Description = "Vesla Two is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid N-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4735,
            Y = 1737,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Vestar",
            Slug = "vestar",
            Route = "planet/vestar",
            Region = "Outer Rim Territories",
            Description = "Vestar is a star system in the Outer Rim Territories, within the Rseik Sector, at galactic grid N-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4603,
            Y = 4880,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Vetine",
            Slug = "vetine",
            Route = "planet/vetine",
            Region = "Core Worlds",
            Description = "Vetine is a star system in the Core Worlds, within the Zuma Sector, at galactic grid G-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3236,
            Y = 2531,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Viidaav",
            Slug = "viidaav",
            Route = "planet/viidaav",
            Region = "Mid Rim Territories",
            Description = "Viidaav is a star system in the Mid Rim Territories, within the Bryx Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6229,
            Y = 1870,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Vlemoth Port",
            Slug = "vlemoth-port",
            Route = "planet/vlemoth-port",
            Region = "Outer Rim Territories",
            Description = "Vlemoth Port is a star system in the Outer Rim Territories, within the Instrop Sector, at galactic grid S-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6373,
            Y = 3965,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Vodran",
            Slug = "vodran",
            Route = "planet/vodran",
            Region = "Hutt Space",
            Description = "Vodran is a star system in the Hutt Space, within the Si'klaata Cluster, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6616,
            Y = 2498,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Voktunma",
            Slug = "voktunma",
            Route = "planet/voktunma",
            Region = "Core Worlds",
            Description = "Voktunma is a star system in the Core Worlds, within the Zuma Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4076,
            Y = 2820,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Volgax",
            Slug = "volgax",
            Route = "planet/volgax",
            Region = "Core Worlds",
            Description = "Volgax is a star system in the Core Worlds, within the Zuma Sector, at galactic grid K-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3580,
            Y = 2511,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vonak",
            Slug = "vonak",
            Route = "planet/vonak",
            Region = "Outer Rim Territories",
            Description = "Vonak is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3748,
            Y = 1049,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vondarc",
            Slug = "vondarc",
            Route = "planet/vondarc",
            Region = "Mid Rim Territories",
            Description = "Vondarc is a star system in the Mid Rim Territories, within the Var Hagen, at galactic grid M-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4169,
            Y = 4082,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Vondoru",
            Slug = "vondoru",
            Route = "planet/vondoru",
            Region = "Mid Rim Territories",
            Description = "Vondoru is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid O-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6269,
            Y = 2956,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Vornax",
            Slug = "vornax",
            Route = "planet/vornax",
            Region = "Outer Rim Territories",
            Description = "Vornax is a star system in the Outer Rim Territories, within the Thanium Sector, at galactic grid S-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6477,
            Y = 1484,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vortex",
            Slug = "vortex",
            Route = "planet/vortex",
            Region = "Mid Rim Territories",
            Description = "Vortex is a star system in the Mid Rim Territories, within the Glythe Sector, at galactic grid K-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3270,
            Y = 1985,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vorusku",
            Slug = "vorusku",
            Route = "planet/vorusku",
            Region = "Outer Rim Territories",
            Description = "Vorusku is a star system in the Outer Rim Territories, within the Juris Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5231,
            Y = 4311,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vorzyd IV",
            Slug = "vorzyd-iv",
            Route = "planet/vorzyd-iv",
            Region = "Outer Rim Territories",
            Description = "Vorzyd IV is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5984,
            Y = 1776,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Vorzyd V",
            Slug = "vorzyd-v",
            Route = "planet/vorzyd-v",
            Region = "Outer Rim Territories",
            Description = "Vorzyd V is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6081,
            Y = 1606,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Vrogas Vas",
            Slug = "vrogas-vas",
            Route = "planet/vrogas-vas",
            Region = "Mid Rim Territories",
            Description = "Vrogas Vas is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid G-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3037,
            Y = 1901,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vuchelle",
            Slug = "vuchelle",
            Route = "planet/vuchelle",
            Region = "Outer Rim Territories",
            Description = "Vuchelle is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3884,
            Y = 1562,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Vulcar",
            Slug = "vulcar",
            Route = "planet/vulcar",
            Region = "Mid Rim Territories",
            Description = "Vulcar is a star system in the Mid Rim Territories, within the Juvex Sector, at galactic grid L-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3918,
            Y = 4455,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Vulpter",
            Slug = "vulpter",
            Route = "planet/vulpter",
            Region = "Deep Core",
            Description = "Vulpter is a star system in the Deep Core, within the Zuma Sector, at galactic grid L-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3658,
            Y = 2671,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Vvaw",
            Slug = "vvaw",
            Route = "planet/vvaw",
            Region = "Outer Rim Territories",
            Description = "Vvaw is a star system in the Outer Rim Territories, within the Calaron Sector, at galactic grid U-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7154,
            Y = 2452,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Vyndal",
            Slug = "vyndal",
            Route = "planet/vyndal",
            Region = "Wild Space",
            Description = "Vyndal is a star system in the Wild Space, within the Zuma Sector, at galactic grid C-20, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1569,
            Y = 4871,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Wakeelmui",
            Slug = "wakeelmui",
            Route = "planet/wakeelmui",
            Region = "Core Worlds",
            Description = "Wakeelmui is a star system in the Core Worlds, within the Zuma Sector, at galactic grid L-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3866,
            Y = 2327,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Wall of Dantooine",
            Slug = "wall-of-dantooine",
            Route = "planet/wall-of-dantooine",
            Region = "Outer Rim Territories",
            Description = "Wall of Dantooine is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid L-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3707,
            Y = 1242,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Waskiro",
            Slug = "waskiro",
            Route = "planet/waskiro",
            Region = "Outer Rim Territories",
            Description = "Waskiro is a star system in the Outer Rim Territories, within the Jospro Sector, at galactic grid R-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6116,
            Y = 1950,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Wecacoe",
            Slug = "wecacoe",
            Route = "planet/wecacoe",
            Region = "Mid Rim Territories",
            Description = "Wecacoe is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3867,
            Y = 1977,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Weik",
            Slug = "weik",
            Route = "planet/weik",
            Region = "Colonies",
            Description = "Weik is a star system in the Colonies, within the Zuma Sector, at galactic grid G-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3161,
            Y = 2233,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Wellspring of Life",
            Slug = "wellspring-of-life",
            Route = "planet/wellspring-of-life",
            Region = "Wild Space",
            Description = "Wellspring of Life is a star system in the Wild Space, within the Zuma Sector, at galactic grid E-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2110,
            Y = 2973,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Whiforla II",
            Slug = "whiforla-ii",
            Route = "planet/whiforla-ii",
            Region = "Colonies",
            Description = "Whiforla II is a star system in the Colonies, within the Zuma Sector, at galactic grid H-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3515,
            Y = 2424,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Wielu",
            Slug = "wielu",
            Route = "planet/wielu",
            Region = "Inner Rim Territories",
            Description = "Wielu is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid N-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4412,
            Y = 3364,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Wistril",
            Slug = "wistril",
            Route = "planet/wistril",
            Region = "Outer Rim Territories",
            Description = "Wistril is a star system in the Outer Rim Territories, within the Fath Sector, at galactic grid K-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3275,
            Y = 1594,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Womrik",
            Slug = "womrik",
            Route = "planet/womrik",
            Region = "Mid Rim Territories",
            Description = "Womrik is a star system in the Mid Rim Territories, within the Dufilvian Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5754,
            Y = 3838,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Woostri",
            Slug = "woostri",
            Route = "planet/woostri",
            Region = "Expansion Region",
            Description = "Woostri is a star system in the Expansion Region, within the Woostri Sector, at galactic grid M-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4103,
            Y = 3907,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Wor Tandell",
            Slug = "wor-tandell",
            Route = "planet/wor-tandell",
            Region = "Core Worlds",
            Description = "Wor Tandell is a star system in the Core Worlds, within the Dolomar Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3466,
            Y = 2345,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Wrea",
            Slug = "wrea",
            Route = "planet/wrea",
            Region = "Outer Rim Territories",
            Description = "Wrea is a star system in the Outer Rim Territories, within the Gaulus Sector, at galactic grid S-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6427,
            Y = 4439,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Wynkahthu",
            Slug = "wynkahthu",
            Route = "planet/wynkahthu",
            Region = "Inner Rim Territories",
            Description = "Wynkahthu is a star system in the Inner Rim Territories, within the Zuma Sector, at galactic grid J-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4028,
            Y = 3520,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Xa Fel",
            Slug = "xa-fel",
            Route = "planet/xa-fel",
            Region = "Core Worlds",
            Description = "Xa Fel is a star system in the Core Worlds, within the Kanchen Sector, at galactic grid K-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3417,
            Y = 2404,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Xagobah",
            Slug = "xagobah",
            Route = "planet/xagobah",
            Region = "Outer Rim Territories",
            Description = "Xagobah is a star system in the Outer Rim Territories, within the Mayagil Sector, at galactic grid M-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4336,
            Y = 4485,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Xantar",
            Slug = "xantar",
            Route = "planet/xantar",
            Region = "Outer Rim Territories",
            Description = "Xantar is a star system in the Outer Rim Territories, within the Corva Sector, at galactic grid P-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5359,
            Y = 1187,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Xendek",
            Slug = "xendek",
            Route = "planet/xendek",
            Region = "Outer Rim Territories",
            Description = "Xendek is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid Q-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6908,
            Y = 3806,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Xerton Nine",
            Slug = "xerton-nine",
            Route = "planet/xerton-nine",
            Region = "Outer Rim Territories",
            Description = "Xerton Nine is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid J-3, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2938,
            Y = 1058,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Xo",
            Slug = "xo",
            Route = "planet/xo",
            Region = "Outer Rim Territories",
            Description = "Xo is a star system in the Outer Rim Territories, within the Spinward Sector, at galactic grid N-2, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4591,
            Y = 750,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Xolu",
            Slug = "xolu",
            Route = "planet/xolu",
            Region = "Mid Rim Territories",
            Description = "Xolu is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-13, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6296,
            Y = 3284,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Xoman Three",
            Slug = "xoman-three",
            Route = "planet/xoman-three",
            Region = "Mid Rim Territories",
            Description = "Xoman Three is a star system in the Mid Rim Territories, within the Halla Sector, at galactic grid S-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6632,
            Y = 2479,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Xorrn",
            Slug = "xorrn",
            Route = "planet/xorrn",
            Region = "Wild Space",
            Description = "Xorrn is a star system in the Wild Space, within the Zuma Sector, at galactic grid E-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2343,
            Y = 2507,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Xyquine II",
            Slug = "xyquine-ii",
            Route = "planet/xyquine-ii",
            Region = "Core Worlds",
            Description = "Xyquine II is a star system in the Core Worlds, within the Corellian Sector, at galactic grid M-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4087,
            Y = 2950,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Yaga Minor",
            Slug = "yaga-minor",
            Route = "planet/yaga-minor",
            Region = "Outer Rim Territories",
            Description = "Yaga Minor is a star system in the Outer Rim Territories, within the Prefsbelt Sector, at galactic grid K-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3259,
            Y = 1394,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Yalara",
            Slug = "yalara",
            Route = "planet/yalara",
            Region = "Outer Rim Territories",
            Description = "Yalara is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid I-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2486,
            Y = 534,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Yanibar",
            Slug = "yanibar",
            Route = "planet/yanibar",
            Region = "Wild Space",
            Description = "Yanibar is a star system in the Wild Space, within the Wild Space, at galactic grid R-19, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6250,
            Y = 4668,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Yarma",
            Slug = "yarma",
            Route = "planet/yarma",
            Region = "Deep Core",
            Description = "Yarma is a star system in the Deep Core, within the Zuma Sector, at galactic grid I-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3842,
            Y = 2557,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Yashuvhu",
            Slug = "yashuvhu",
            Route = "planet/yashuvhu",
            Region = "Wild Space",
            Description = "Yashuvhu is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1443,
            Y = 2358,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Yavin",
            Slug = "yavin",
            Route = "planet/yavin",
            Region = "Outer Rim Territories",
            Description = "Yavin is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid P-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5229,
            Y = 1759,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Yellowblade's Landing",
            Slug = "yellowblades-landing",
            Route = "planet/yellowblades-landing",
            Region = "Wild Space",
            Description = "Yellowblade's Landing is a star system in the Wild Space, within the Zuma Sector, at galactic grid E-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2287,
            Y = 2059,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Yeshocq",
            Slug = "yeshocq",
            Route = "planet/yeshocq",
            Region = "Mid Rim Territories",
            Description = "Yeshocq is a star system in the Mid Rim Territories, within the Mulgard Sector, at galactic grid N-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4639,
            Y = 4011,
            Color = "#8a6a4a"
        },
        new()
        {
            Name = "Yibikkoror",
            Slug = "yibikkoror",
            Route = "planet/yibikkoror",
            Region = "Expansion Region",
            Description = "Yibikkoror is a star system in the Expansion Region, within the Immalia Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3748,
            Y = 2093,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Yinchorr",
            Slug = "yinchorr",
            Route = "planet/yinchorr",
            Region = "Expansion Region",
            Description = "Yinchorr is a star system in the Expansion Region, within the Fellwe Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3748,
            Y = 2093,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Yitheeth",
            Slug = "yitheeth",
            Route = "planet/yitheeth",
            Region = "Expansion Region",
            Description = "Yitheeth is a star system in the Expansion Region, within the Immalia Sector, at galactic grid L-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3748,
            Y = 2093,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Ylesia",
            Slug = "ylesia",
            Route = "planet/ylesia",
            Region = "Outer Rim Territories",
            Description = "Ylesia is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6837,
            Y = 3000,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Ylix",
            Slug = "ylix",
            Route = "planet/ylix",
            Region = "Mid Rim Territories",
            Description = "Ylix is a star system in the Mid Rim Territories, within the M'shinni Sector, at galactic grid M-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4000,
            Y = 1904,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Yorn Skot",
            Slug = "yorn-skot",
            Route = "planet/yorn-skot",
            Region = "Expansion Region",
            Description = "Yorn Skot is a star system in the Expansion Region, within the Zuma Sector, at galactic grid N-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4664,
            Y = 3508,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Yuuzhan'tar",
            Slug = "yuuzhantar",
            Route = "planet/yuuzhantar",
            Region = "Mid Rim Territories",
            Description = "Yuuzhan'tar is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid I-7, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3766,
            Y = 1910,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Z'trop",
            Slug = "ztrop",
            Route = "planet/ztrop",
            Region = "Outer Rim Territories",
            Description = "Z'trop is a star system in the Outer Rim Territories, within the Tamarin Sector, at galactic grid N-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 4416,
            Y = 4370,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Zaadja",
            Slug = "zaadja",
            Route = "planet/zaadja",
            Region = "Outer Rim Territories",
            Description = "Zaadja is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid R-16, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6157,
            Y = 4082,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Zaddja",
            Slug = "zaddja",
            Route = "planet/zaddja",
            Region = "Outer Rim Territories",
            Description = "Zaddja is a star system in the Outer Rim Territories, within the Trilon Sector, at galactic grid H-15, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2171,
            Y = 3679,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Zakuul",
            Slug = "zakuul",
            Route = "planet/zakuul",
            Region = "Core Worlds",
            Description = "Zakuul is a star system in the Core Worlds, within the Zuma Sector, at galactic grid H-11, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3449,
            Y = 2824,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Zaloriis",
            Slug = "zaloriis",
            Route = "planet/zaloriis",
            Region = "Expansion Region",
            Description = "Zaloriis is a star system in the Expansion Region, within the Askarian Sector, at galactic grid P-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5414,
            Y = 3164,
            Color = "#4a7a5a"
        },
        new()
        {
            Name = "Zebitrope IV",
            Slug = "zebitrope-iv",
            Route = "planet/zebitrope-iv",
            Region = "Outer Rim Territories",
            Description = "Zebitrope IV is a star system in the Outer Rim Territories, within the Centrality Sector, at galactic grid T-8, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6712,
            Y = 2230,
            Color = "#8a7a5a"
        },
        new()
        {
            Name = "Zeenada",
            Slug = "zeenada",
            Route = "planet/zeenada",
            Region = "Expansion Region",
            Description = "Zeenada is a star system in the Expansion Region, within the Immerian Outback, at galactic grid O-14, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5077,
            Y = 3449,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Zeffliffl",
            Slug = "zeffliffl",
            Route = "planet/zeffliffl",
            Region = "Outer Rim Territories",
            Description = "Zeffliffl is a star system in the Outer Rim Territories, within the Atrivis Sector, at galactic grid L-5, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3777,
            Y = 1465,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Zerm",
            Slug = "zerm",
            Route = "planet/zerm",
            Region = "Outer Rim Territories",
            Description = "Zerm is a star system in the Outer Rim Territories, within the Kessel Sector, at galactic grid T-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6868,
            Y = 2502,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Zhar",
            Slug = "zhar",
            Route = "planet/zhar",
            Region = "Outer Rim Territories",
            Description = "Zhar is a star system in the Outer Rim Territories, within the Cadavine Sector, at galactic grid P-17, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 5480,
            Y = 4136,
            Color = "#6a8a5a"
        },
        new()
        {
            Name = "Zigoola",
            Slug = "zigoola",
            Route = "planet/zigoola",
            Region = "Wild Space",
            Description = "Zigoola is a star system in the Wild Space, within the Calamari Sector, at galactic grid U-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7196,
            Y = 1674,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Zisia",
            Slug = "zisia",
            Route = "planet/zisia",
            Region = "Mid Rim Territories",
            Description = "Zisia is a star system in the Mid Rim Territories, within the Zuma Sector, at galactic grid S-10, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 6397,
            Y = 2717,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Ziugen",
            Slug = "ziugen",
            Route = "planet/ziugen",
            Region = "Outer Rim Territories",
            Description = "Ziugen is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid T-12, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 7025,
            Y = 2981,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Zoh",
            Slug = "zoh",
            Route = "planet/zoh",
            Region = "Outer Rim Territories",
            Description = "Zoh is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid F-18, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2734,
            Y = 4401,
            Color = "#4a6a8a"
        },
        new()
        {
            Name = "Zonama Sekot",
            Slug = "zonama-sekot",
            Route = "planet/zonama-sekot",
            Region = "Wild Space",
            Description = "Zonama Sekot is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-9, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1476,
            Y = 2357,
            Color = "#9a6a4a"
        },
        new()
        {
            Name = "Zonju V",
            Slug = "zonju-v",
            Route = "planet/zonju-v",
            Region = "Outer Rim Territories",
            Description = "Zonju V is a star system in the Outer Rim Territories, within the Kallea Sector, at galactic grid J-21, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 2863,
            Y = 442,
            Color = "#5a8a9a"
        },
        new()
        {
            Name = "Zosha",
            Slug = "zosha",
            Route = "planet/zosha",
            Region = "Wild Space",
            Description = "Zosha is a star system in the Wild Space, within the Zuma Sector, at galactic grid F-6, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 1667,
            Y = 1801,
            Color = "#7a5a8a"
        },
        new()
        {
            Name = "Zyzar",
            Slug = "zyzar",
            Route = "planet/zyzar",
            Region = "Outer Rim Territories",
            Description = "Zyzar is a star system in the Outer Rim Territories, within the Zuma Sector, at galactic grid H-4, Documented in the Essential Atlas and StarWars.com galaxy map appendix.",
            X = 3339,
            Y = 1313,
            Color = "#8a6a4a"
        }
    ];

    public static GalaxyPlanet? GetBySlug(string slug) =>
        Planets.FirstOrDefault(planet => planet.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
