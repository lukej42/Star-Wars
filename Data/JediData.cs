using StarWars.Models;

namespace StarWars.Data;

public static class JediData
{
    public static IReadOnlyList<JediMember> Members { get; } =
    [
        new()
        {
            Name = "Aayla Secura",
            Slug = "aayla-secura",
            Route = "jedi/aayla-secura",
            Rank = "Jedi Master",
            Description = "A Twi'lek Jedi Master who served on the front lines of the Clone Wars with grace and courage.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Adi Gallia",
            Slug = "adi-gallia",
            Route = "jedi/adi-gallia",
            Rank = "Jedi Master",
            Description = "A Tholothian Jedi Council member known for her diplomatic skill and mastery of Form V.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Agen Kolar",
            Slug = "agen-kolar",
            Route = "jedi/agen-kolar",
            Rank = "Jedi Master",
            Description = "A Zabrak Jedi Master and Council member who joined Mace Windu in confronting Chancellor Palpatine.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Ahsoka Tano",
            Slug = "ahsoka-tano",
            Route = "jedi/ahsoka-tano",
            Rank = "Former Padawan",
            Description = "Anakin Skywalker's former apprentice who left the Order and later wielded white lightsabers as a free agent.",
            Color = "#e2e8f0"
        },
        new()
        {
            Name = "Anakin Skywalker",
            Slug = "anakin-skywalker",
            Route = "jedi/anakin-skywalker",
            Rank = "Jedi Knight",
            Description = "The Chosen One whose unmatched piloting and power made him a hero of the Clone Wars before his fall.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Barriss Offee",
            Slug = "barriss-offee",
            Route = "jedi/barriss-offee",
            Rank = "Jedi Padawan",
            Description = "Luminara Unduli's Mirialan padawan who grew disillusioned with the Jedi Order during the war.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Bolla Ropal",
            Slug = "bolla-ropal",
            Route = "jedi/bolla-ropal",
            Rank = "Jedi Master",
            Description = "A Rodian Jedi Master who guarded the Kyber memory crystal before his capture by Cad Bane.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Cin Drallig",
            Slug = "cin-drallig",
            Route = "jedi/cin-drallig",
            Rank = "Jedi Battlemaster",
            Description = "The Temple's lightsaber combat instructor who valiantly defended the Jedi Temple during Order 66.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Coleman Kcaj",
            Slug = "coleman-kcaj",
            Route = "jedi/coleman-kcaj",
            Rank = "Jedi Master",
            Description = "An Ongree Jedi Council member who served during the final years of the Republic.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Coleman Trebor",
            Slug = "coleman-trebor",
            Route = "jedi/coleman-trebor",
            Rank = "Jedi Master",
            Description = "A Vurk Jedi Council member who fell defending the arena on Geonosis during the opening battle of the Clone Wars.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Depa Billaba",
            Slug = "depa-billaba",
            Route = "jedi/depa-billaba",
            Rank = "Jedi Master",
            Description = "A Chalactan Jedi Council member and former padawan of Mace Windu who trained Caleb Dume.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Eeth Koth",
            Slug = "eeth-koth",
            Route = "jedi/eeth-koth",
            Rank = "Jedi Master",
            Description = "A Zabrak Jedi Council member who survived captivity by General Grievous and continued serving the Order.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Even Piell",
            Slug = "even-piell",
            Route = "jedi/even-piell",
            Rank = "Jedi Master",
            Description = "A diminutive Lannik Jedi Master who held vital intelligence about the Nexus Route before his death on Lola Sayu.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Ezra Bridger",
            Slug = "ezra-bridger",
            Route = "jedi/ezra-bridger",
            Rank = "Jedi Padawan",
            Description = "A Lothal orphan who became Kanan Jarrus's apprentice and a key leader of the early rebellion.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Grogu",
            Slug = "grogu",
            Route = "jedi/grogu",
            Rank = "Jedi Initiate",
            Description = "A Force-sensitive foundling of Yoda's species who survived the Purge and was trained briefly by Luke Skywalker.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Gungi",
            Slug = "gungi",
            Route = "jedi/gungi",
            Rank = "Jedi Padawan",
            Description = "A Wookiee youngling who crafted a unique wooden-hilted green lightsaber during the Clone Wars era.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Ima-Gun Di",
            Slug = "ima-gun-di",
            Route = "jedi/ima-gun-di",
            Rank = "Jedi Master",
            Description = "A Nikto Jedi Master who sacrificed himself on Ryloth to buy time for Twi'lek refugees to escape.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Jocasta Nu",
            Slug = "jocasta-nu",
            Route = "jedi/jocasta-nu",
            Rank = "Jedi Chief Librarian",
            Description = "The keeper of the Jedi Archives who guarded the Temple's vast repository of knowledge for decades.",
            Color = "#eab308"
        },
        new()
        {
            Name = "Kanan Jarrus",
            Slug = "kanan-jarrus",
            Route = "jedi/kanan-jarrus",
            Rank = "Jedi Knight",
            Description = "Former padawan Caleb Dume who survived Order 66 and secretly trained Ezra Bridger as a rebel leader.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Katooni",
            Slug = "katooni",
            Route = "jedi/katooni",
            Rank = "Jedi Initiate",
            Description = "A Tholothian youngling who overcame doubt to forge her lightsaber during the Gathering on Ilum.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Kelleran Beq",
            Slug = "kelleran-beq",
            Route = "jedi/kelleran-beq",
            Rank = "Jedi Master",
            Description = "A Jedi Master who helped rescue Grogu from the Temple during Order 66 and later crossed paths with Din Djarin.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Ki-Adi-Mundi",
            Slug = "ki-adi-mundi",
            Route = "jedi/ki-adi-mundi",
            Rank = "Jedi Master",
            Description = "A Cerean Jedi Council member who commanded clone forces across multiple fronts of the Clone Wars.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Kit Fisto",
            Slug = "kit-fisto",
            Route = "jedi/kit-fisto",
            Rank = "Jedi Master",
            Description = "A Nautolan Jedi Council member celebrated for his cheerful demeanor and mastery of Form I underwater.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Luminara Unduli",
            Slug = "luminara-unduli",
            Route = "jedi/luminara-unduli",
            Rank = "Jedi Master",
            Description = "A Mirialan Jedi Master who fought alongside her padawan Barriss Offee on Geonosis and across the galaxy.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Luke Skywalker",
            Slug = "luke-skywalker",
            Route = "jedi/luke-skywalker",
            Rank = "Jedi Master",
            Description = "The son of Anakin Skywalker who destroyed the Death Star and restored balance to the Force.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Mace Windu",
            Slug = "mace-windu",
            Route = "jedi/mace-windu",
            Rank = "Jedi Master",
            Description = "A senior Jedi Council member and master of Vaapad who wielded a distinctive purple lightsaber.",
            Color = "#7c3aed"
        },
        new()
        {
            Name = "Nahdar Vebb",
            Slug = "nahdar-vebb",
            Route = "jedi/nahdar-vebb",
            Rank = "Jedi Knight",
            Description = "Kit Fisto's Mon Calamari former padawan who confronted General Grievous on the moon of Vassek.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Obi-Wan Kenobi",
            Slug = "obi-wan-kenobi",
            Route = "jedi/obi-wan-kenobi",
            Rank = "Jedi Master",
            Description = "Qui-Gon Jinn's apprentice who became a legendary general and mentor to both Anakin and Luke Skywalker.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Oppo Rancisis",
            Slug = "oppo-rancisis",
            Route = "jedi/oppo-rancisis",
            Rank = "Jedi Master",
            Description = "A Thisspiasian Jedi Council member and strategic mastermind who rarely left the Temple.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Petro",
            Slug = "petro",
            Route = "jedi/petro",
            Rank = "Jedi Initiate",
            Description = "A bold youngling who struggled with patience during the Gathering but ultimately completed his lightsaber.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Plo Koon",
            Slug = "plo-koon",
            Route = "jedi/plo-koon",
            Rank = "Jedi Master",
            Description = "A Kel Dor Jedi Council member who discovered Ahsoka Tano and commanded the Wolfpack clone battalion.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Quinlan Vos",
            Slug = "quinlan-vos",
            Route = "jedi/quinlan-vos",
            Rank = "Jedi Master",
            Description = "A Kiffar Jedi Master whose psychometric abilities made him an expert tracker and undercover operative.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Qui-Gon Jinn",
            Slug = "qui-gon-jinn",
            Route = "jedi/qui-gon-jinn",
            Rank = "Jedi Master",
            Description = "A maverick Jedi who discovered Anakin Skywalker on Tatooine and learned the secrets of life after death.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Saesee Tiin",
            Slug = "saesee-tiin",
            Route = "jedi/saesee-tiin",
            Rank = "Jedi Master",
            Description = "An Iktotchi Jedi Council member and ace starfighter pilot who served throughout the Clone Wars.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Shaak Ti",
            Slug = "shaak-ti",
            Route = "jedi/shaak-ti",
            Rank = "Jedi Master",
            Description = "A Togruta Jedi Council member who oversaw clone trooper training on Kamino during the war.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Sifo-Dyas",
            Slug = "sifo-dyas",
            Route = "jedi/sifo-dyas",
            Rank = "Jedi Master",
            Description = "A Jedi Master whose foresight led him to secretly commission the clone army before his mysterious death.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Stass Allie",
            Slug = "stass-allie",
            Route = "jedi/stass-allie",
            Rank = "Jedi Master",
            Description = "A Tholothian Jedi Master who replaced Adi Gallia on the Council and served on Saleucami.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Tera Sinube",
            Slug = "tera-sinube",
            Route = "jedi/tera-sinube",
            Rank = "Jedi Master",
            Description = "An elderly Cosian investigator who aided Ahsoka Tano with his cane-mounted lightsaber on Coruscant.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Tiplee",
            Slug = "tiplee",
            Route = "jedi/tiplee",
            Rank = "Jedi Master",
            Description = "A red-skinned Mikkian Jedi Master who partnered with her twin Tiplar during the Clone Wars.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Tiplar",
            Slug = "tiplar",
            Route = "jedi/tiplar",
            Rank = "Jedi Master",
            Description = "A red-skinned Mikkian Jedi Master who fought alongside her sister Tiplee until her death on Ringo Vinda.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Yaddle",
            Slug = "yaddle",
            Route = "jedi/yaddle",
            Rank = "Jedi Master",
            Description = "A member of Yoda's species who served on the Jedi Council before the Clone Wars.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Yoda",
            Slug = "yoda",
            Route = "jedi/yoda",
            Rank = "Jedi Grand Master",
            Description = "The oldest and wisest Jedi Master, whose centuries of teaching shaped the Order and the fate of the galaxy.",
            Color = "#22c55e"
        }
    ];

    public static JediMember? GetBySlug(string slug) =>
        Members.FirstOrDefault(member => member.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
