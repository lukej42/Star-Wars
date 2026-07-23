using StarWars.Models;

namespace StarWars.Data;

public static class SithData
{
    public static IReadOnlyList<SithMember> Members { get; } =
    [
        // Prequel and original trilogy Sith Lords
        new()
        {
            Name = "Darth Sidious",
            Slug = "darth-sidious",
            Route = "sith/darth-sidious",
            Title = "Dark Lord of the Sith",
            Description = "Sheev Palpatine, the Sith mastermind who orchestrated the fall of the Republic and ruled the Galactic Empire as Emperor.",
            Color = "#450a0a"
        },
        new()
        {
            Name = "Darth Maul",
            Slug = "darth-maul",
            Route = "sith/darth-maul",
            Title = "Sith Lord",
            Description = "A Zabrak warrior trained by Sidious who survived his defeat to become a feared crime lord and dark-side zealot.",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Darth Tyranus",
            Slug = "darth-tyranus",
            Route = "sith/darth-tyranus",
            Title = "Sith Lord",
            Description = "Count Dooku, a former Jedi Master who became Sidious's apprentice and led the Separatist Alliance during the Clone Wars.",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Darth Vader",
            Slug = "darth-vader",
            Route = "sith/darth-vader",
            Title = "Dark Lord of the Sith",
            Description = "Anakin Skywalker fallen to the dark side, encased in black armor and serving as the Emperor's enforcer.",
            Color = "#7f1d1d"
        },
        new()
        {
            Name = "Darth Plagueis",
            Slug = "darth-plagueis",
            Route = "sith/darth-plagueis",
            Title = "Dark Lord of the Sith",
            Description = "A Muun Sith Lord who mastered the manipulation of midichlorians and trained Sheev Palpatine before being betrayed.",
            Color = "#b91c1c"
        },

        // Clone Wars era
        new()
        {
            Name = "Savage Opress",
            Slug = "savage-opress",
            Route = "sith/savage-opress",
            Title = "Dark Side Warrior",
            Description = "A Nightbrother transformed by Mother Talzin and Count Dooku into a hulking dark-side enforcer and Maul's brother.",
            Color = "#ea580c"
        },
        new()
        {
            Name = "Asajj Ventress",
            Slug = "asajj-ventress",
            Route = "sith/asajj-ventress",
            Title = "Dark Acolyte",
            Description = "A Dathomirian assassin trained by Dooku who walked the line between Sith acolyte and independent bounty hunter.",
            Color = "#dc2626"
        },

        // Rebels Inquisitors
        new()
        {
            Name = "Grand Inquisitor",
            Slug = "grand-inquisitor",
            Route = "sith/grand-inquisitor",
            Title = "Grand Inquisitor",
            Description = "A Pau'an former Jedi Temple Guard who led the Inquisitorius in hunting surviving Jedi for the Empire.",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Second Sister",
            Slug = "second-sister",
            Route = "sith/second-sister",
            Title = "Inquisitor",
            Description = "Trilla Suduri, a former Jedi Padawan turned Inquisitor who relentlessly hunted her old master, Cere Junda.",
            Color = "#7f1d1d"
        },
        new()
        {
            Name = "Fifth Brother",
            Slug = "fifth-brother",
            Route = "sith/fifth-brother",
            Title = "Inquisitor",
            Description = "A hulking gray-skinned Inquisitor who served the Empire alongside the Seventh Sister in hunting Force-sensitive fugitives.",
            Color = "#450a0a"
        },
        new()
        {
            Name = "Seventh Sister",
            Slug = "seventh-sister",
            Route = "sith/seventh-sister",
            Title = "Inquisitor",
            Description = "A Mirialan Inquisitor known for her agile fighting style and relentless pursuit of Kanan Jarrus and Ezra Bridger.",
            Color = "#b91c1c"
        },
        new()
        {
            Name = "Eighth Brother",
            Slug = "eighth-brother",
            Route = "sith/eighth-brother",
            Title = "Inquisitor",
            Description = "A Terrellian Jango Jumper Inquisitor dispatched to Malachor to eliminate Maul, the Jedi, and any other threats.",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Ninth Sister",
            Slug = "ninth-sister",
            Route = "sith/ninth-sister",
            Title = "Inquisitor",
            Description = "A Dowutin former Jedi who became an Inquisitor, distinguished by her imposing size and cruel interrogation methods.",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Sixth Brother",
            Slug = "sixth-brother",
            Route = "sith/sixth-brother",
            Title = "Inquisitor",
            Description = "A blue-skinned Inquisitor who confronted Ahsoka Tano on Raada before being defeated by the former Jedi.",
            Color = "#ea580c"
        },

        // Fallen Jedi
        new()
        {
            Name = "Barriss Offee",
            Slug = "barriss-offee",
            Route = "sith/barriss-offee",
            Title = "Fallen Jedi",
            Description = "A Mirialan Jedi Padawan who bombed the Jedi Temple and framed Ahsoka Tano, believing the Order had become corrupt.",
            Color = "#7f1d1d"
        },
        new()
        {
            Name = "Pong Krell",
            Slug = "pong-krell",
            Route = "sith/pong-krell",
            Title = "Fallen Jedi General",
            Description = "A Besalisk Jedi General who secretly foresaw the Jedi's defeat and turned on his clone troopers during the Clone Wars.",
            Color = "#450a0a"
        },

        // Knights of the Old Republic
        new()
        {
            Name = "Darth Revan",
            Slug = "darth-revan",
            Route = "sith/darth-revan",
            Title = "Dark Lord of the Sith",
            Description = "A legendary Jedi Knight who fell to the dark side, conquered the galaxy, and was later redeemed before disappearing.",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Darth Malak",
            Slug = "darth-malak",
            Route = "sith/darth-malak",
            Title = "Dark Lord of the Sith",
            Description = "Revan's apprentice who seized control of the Sith Empire and waged war against the Republic with brutal efficiency.",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Darth Bandon",
            Slug = "darth-bandon",
            Route = "sith/darth-bandon",
            Title = "Sith Apprentice",
            Description = "Malak's cruel apprentice who hunted the amnesiac Revan across the galaxy during the Jedi Civil War.",
            Color = "#b91c1c"
        },

        // Knights of the Old Republic II
        new()
        {
            Name = "Darth Traya",
            Slug = "darth-traya",
            Route = "sith/darth-traya",
            Title = "Dark Lord of the Sith",
            Description = "Kreia, a former Jedi Master who became a Sith Lord and sought to destroy the Force itself through manipulation.",
            Color = "#450a0a"
        },
        new()
        {
            Name = "Darth Sion",
            Slug = "darth-sion",
            Route = "sith/darth-sion",
            Title = "Lord of Pain",
            Description = "A Sith Lord held together by sheer hatred and the dark side, enduring endless agony as he hunted the Jedi Exile.",
            Color = "#7f1d1d"
        },
        new()
        {
            Name = "Darth Nihilus",
            Slug = "darth-nihilus",
            Route = "sith/darth-nihilus",
            Title = "Lord of Hunger",
            Description = "A wound in the Force who consumed entire worlds to feed his insatiable hunger for living energy.",
            Color = "#dc2626"
        },

        // Ancient Sith Empire
        new()
        {
            Name = "Marka Ragnos",
            Slug = "marka-ragnos",
            Route = "sith/marka-ragnos",
            Title = "Dark Lord of the Sith",
            Description = "An ancient Sith ruler whose spirit haunted the Valley of the Dark Lords long after his golden age ended.",
            Color = "#ea580c"
        },
        new()
        {
            Name = "Naga Sadow",
            Slug = "naga-sadow",
            Route = "sith/naga-sadow",
            Title = "Dark Lord of the Sith",
            Description = "A Sith Lord who launched the Great Hyperspace War against the Republic and fled into exile on Yavin 4.",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Ludo Kressh",
            Slug = "ludo-kressh",
            Route = "sith/ludo-kressh",
            Title = "Dark Lord of the Sith",
            Description = "A rival Sith Lord who opposed Naga Sadow's ambitions and fought for control of the Sith Empire after Marka Ragnos.",
            Color = "#7f1d1d"
        },
        new()
        {
            Name = "Tulak Hord",
            Slug = "tulak-hord",
            Route = "sith/tulak-hord",
            Title = "Dark Lord of the Sith",
            Description = "An ancient Sith warrior-king renowned as the greatest lightsaber duelist of his era and master of the Force.",
            Color = "#450a0a"
        },
        new()
        {
            Name = "Exar Kun",
            Slug = "exar-kun",
            Route = "sith/exar-kun",
            Title = "Dark Lord of the Sith",
            Description = "A fallen Jedi who discovered Sith secrets on Yavin 4 and unleashed the Great Sith War upon the galaxy.",
            Color = "#b91c1c"
        },
        new()
        {
            Name = "Ulic Qel-Droma",
            Slug = "ulic-qel-droma",
            Route = "sith/ulic-qel-droma",
            Title = "Sith Lord",
            Description = "A Jedi Knight who infiltrated the Krath cult and fell to the dark side alongside Exar Kun during the Sith War.",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Darth Vitiate",
            Slug = "darth-vitiate",
            Route = "sith/darth-vitiate",
            Title = "Sith Emperor",
            Description = "Tenebrae, an immortal Sith who consumed his homeworld's life force and ruled the reconstituted Sith Empire for centuries.",
            Color = "#450a0a"
        },
        new()
        {
            Name = "Darth Malgus",
            Slug = "darth-malgus",
            Route = "sith/darth-malgus",
            Title = "Sith Lord",
            Description = "A fierce Sith warrior who led the assault on the Jedi Temple during the Sacking of Coruscant.",
            Color = "#991b1b"
        },
        new()
        {
            Name = "Darth Bane",
            Slug = "darth-bane",
            Route = "sith/darth-bane",
            Title = "Dark Lord of the Sith",
            Description = "The Sith Lord who survived the Brotherhood of Darkness and established the Rule of Two that shaped Sith doctrine for a millennium.",
            Color = "#7f1d1d"
        },
        new()
        {
            Name = "Darth Zannah",
            Slug = "darth-zannah",
            Route = "sith/darth-zannah",
            Title = "Dark Lord of the Sith",
            Description = "Bane's apprentice who mastered Sith sorcery and carried forward the Rule of Two after defeating her master.",
            Color = "#b91c1c"
        },
        new()
        {
            Name = "Ajunta Pall",
            Slug = "ajunta-pall",
            Route = "sith/ajunta-pall",
            Title = "Dark Lord of the Sith",
            Description = "One of the first Dark Jedi exiled to Korriban who became a founding Sith Lord and ruler of the early Sith Empire.",
            Color = "#dc2626"
        },
        new()
        {
            Name = "Freedon Nadd",
            Slug = "freedon-nadd",
            Route = "sith/freedon-nadd",
            Title = "Dark Lord of the Sith",
            Description = "A fallen Jedi who discovered Sith tombs on Dxun and Onderon, whose spirit corrupted generations of dark-side rulers.",
            Color = "#ea580c"
        }
    ];

    public static SithMember? GetBySlug(string slug) =>
        Members.FirstOrDefault(member => member.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
