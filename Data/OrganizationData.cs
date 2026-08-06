using StarWars.Models;

namespace StarWars.Data;

public static class OrganizationData
{
    public static IReadOnlyList<Organization> Organizations { get; } =
    [
        new()
        {
            Name = "Techno Union",
            Slug = "techno-union",
            Route = "organizations/techno-union",
            Group = "Separatist Corporations",
            Description = "Skakoan-led manufacturing combine that supplied battle droids, foundries, and research contracts to the Confederacy while maintaining Senate seats on Muunilinst.",
            Color = "#6366f1",
            ParentFactionSlug = "confederacy",
            ParentFactionLabel = "Member of the Confederacy of Independent Systems",
        },
        new()
        {
            Name = "InterGalactic Banking Clan",
            Slug = "intergalactic-banking-clan",
            Route = "organizations/intergalactic-banking-clan",
            Group = "Separatist Corporations",
            Description = "Muun financiers whose Hego Damask holdings and IGBC vaults underwrote Separatist war bonds and droid army payroll across the Outer Rim.",
            Color = "#0891b2",
            ParentFactionSlug = "confederacy",
            ParentFactionLabel = "Member of the Confederacy of Independent Systems",
        },
        new()
        {
            Name = "Commerce Guild",
            Slug = "commerce-guild",
            Route = "organizations/commerce-guild",
            Group = "Separatist Corporations",
            Description = "Gossam-run trade guild whose private security fleets and procurement networks backed Count Dooku's secessionist bloc on Castell.",
            Color = "#059669",
            ParentFactionSlug = "confederacy",
            ParentFactionLabel = "Member of the Confederacy of Independent Systems",
        },
        new()
        {
            Name = "Corporate Alliance",
            Slug = "corporate-alliance",
            Route = "organizations/corporate-alliance",
            Group = "Separatist Corporations",
            Description = "Magistrate Passel Argente's corporate militia that fielded NR-N99 Persuader tanks and droid enforcers for Separatist ground campaigns.",
            Color = "#ca8a04",
            ParentFactionSlug = "confederacy",
            ParentFactionLabel = "Member of the Confederacy of Independent Systems",
        },
        new()
        {
            Name = "Retail Caucus",
            Slug = "retail-caucus",
            Route = "organizations/retail-caucus",
            Group = "Separatist Corporations",
            Description = "Retail megacorp bloc whose logistics hubs and consumer-goods monopolies quietly bankrolled Separatist supply lines during the Clone Wars.",
            Color = "#db2777",
            ParentFactionSlug = "confederacy",
            ParentFactionLabel = "Member of the Confederacy of Independent Systems",
        },
        new()
        {
            Name = "Pyke Syndicate",
            Slug = "pyke-syndicate",
            Route = "organizations/pyke-syndicate",
            Group = "Syndicates & Guilds",
            Description = "Pyke spice cartel from Oba Diah whose refineries and assassin cadres dominated Kessel slave-labor routes for centuries.",
            Color = "#7c3aed",
        },
        new()
        {
            Name = "Black Sun",
            Slug = "black-sun",
            Route = "organizations/black-sun",
            Group = "Syndicates & Guilds",
            Description = "Galaxy-spanning crime syndicate headquartered on Mustafar whose Vigos controlled smuggling, slavery, and assassination markets from the Clone Wars onward.",
            Color = "#1e293b",
        },
        new()
        {
            Name = "Crimson Dawn",
            Slug = "crimson-dawn",
            Route = "organizations/crimson-dawn",
            Group = "Syndicates & Guilds",
            Description = "Maul's shadow syndicate that exploited Imperial chaos through Dryden Vos's refineries and Qi'ra's covert operations on Corellia and Savareen.",
            Color = "#dc2626",
        },
        new()
        {
            Name = "Inquisitorius",
            Slug = "inquisitorius",
            Route = "organizations/inquisitorius",
            Group = "Syndicates & Guilds",
            Description = "Palpatine's dark-side hunters who tracked Jedi survivors with spinning double-bladed lightsabers and Imperial intelligence backing.",
            Color = "#991b1b",
            ParentFactionSlug = "empire",
            ParentFactionLabel = "Imperial dark-side order",
        },
        new()
        {
            Name = "Mining Guild",
            Slug = "mining-guild",
            Route = "organizations/mining-guild",
            Group = "Syndicates & Guilds",
            Description = "Industrial guild whose ore freighters, claim rights, and guild security fleets extract resources from asteroids and toxic worlds under Imperial charter.",
            Color = "#78716c",
        },
        new()
        {
            Name = "Smuggler Guilds",
            Slug = "smuggler-guilds",
            Route = "organizations/smuggler-guilds",
            Group = "Category Hub",
            Description = "Umbrella directory of guild charters, shadow ports, and convoy networks that move contraband between Hutt space and the Outer Rim.",
            Color = "#0284c7",
            IsCategoryHub = true,
        },
        new()
        {
            Name = "Corporate Blocs",
            Slug = "corporate-blocs",
            Route = "organizations/corporate-blocs",
            Group = "Category Hub",
            Description = "Megacorporate holding structures whose boardrooms and private armies shape galactic trade beyond any single government tariff code.",
            Color = "#4f46e5",
            IsCategoryHub = true,
        },
        new()
        {
            Name = "Crime Families",
            Slug = "crime-families",
            Route = "organizations/crime-families",
            Group = "Category Hub",
            Description = "Kajidic clans and syndicate councils whose blood oaths, spice routes, and bounty ledgers govern the galactic underworld.",
            Color = "#b45309",
            IsCategoryHub = true,
        },
        new()
        {
            Name = "Spice Runners' Guild",
            Slug = "spice-runners-guild",
            Route = "organizations/spice-runners-guild",
            Group = "Smuggler Guilds",
            Description = "Guild of Kessel-route pilots who move glitterstim and coaxium under Pyke contracts while evading Imperial customs patrols.",
            Color = "#0d9488",
            ParentOrganizationSlug = "smuggler-guilds",
        },
        new()
        {
            Name = "Corellian Smuggler Guild",
            Slug = "corellian-smuggler-guild",
            Route = "organizations/corellian-smuggler-guild",
            Group = "Smuggler Guilds",
            Description = "Corellian charter guild whose YT-series freighter captains and shadow-dock foremen dominate the Corellian Run black market.",
            Color = "#2563eb",
            ParentOrganizationSlug = "smuggler-guilds",
        },
        new()
        {
            Name = "Hutt Smuggling Rings",
            Slug = "hutt-smuggling-rings",
            Route = "organizations/hutt-smuggling-rings",
            Group = "Smuggler Guilds",
            Description = "Loose kajidic-backed convoy rings that ferry spice, slaves, and weapons through Nal Hutta's protected shipping lanes.",
            Color = "#65a30d",
            ParentOrganizationSlug = "smuggler-guilds",
        },
        new()
        {
            Name = "Desilijic Kajidic",
            Slug = "desilijic-kajidic",
            Route = "organizations/desilijic-kajidic",
            Group = "Crime Families",
            Description = "Jabba the Hutt's kajidic clan whose palace on Tatooine anchored spice, bounty, and slave trade across Hutt Space for generations.",
            Color = "#84cc16",
            ParentOrganizationSlug = "crime-families",
        },
        new()
        {
            Name = "Besadii Kajidic",
            Slug = "besadii-kajidic",
            Route = "organizations/besadii-kajidic",
            Group = "Crime Families",
            Description = "Rival Hutt clan led by Durga Besadii that contested Desilijic spice monopolies and Kessel labor contracts through the New Republic era.",
            Color = "#a3e635",
            ParentOrganizationSlug = "crime-families",
        },
        new()
        {
            Name = "Black Sun Vigo Council",
            Slug = "black-sun-vigo-council",
            Route = "organizations/black-sun-vigo-council",
            Group = "Crime Families",
            Description = "Regional Vigo council that coordinates Black Sun sector bosses, assassin retainer contracts, and syndicate succession disputes from secret fortresses.",
            Color = "#334155",
            ParentOrganizationSlug = "crime-families",
        },
        new()
        {
            Name = "Trade Federation Directorate",
            Slug = "trade-federation-directorate",
            Route = "organizations/trade-federation-directorate",
            Group = "Corporate Blocs",
            Description = "Neimoidian directorate board that commanded Trade Federation blockades and battle droid armies; see also the Trade Federation faction profile for wartime history.",
            Color = "#7c3aed",
            ParentOrganizationSlug = "corporate-blocs",
        },
        new()
        {
            Name = "InterGalactic Banking Holding",
            Slug = "intergalactic-banking-holding",
            Route = "organizations/intergalactic-banking-holding",
            Group = "Corporate Blocs",
            Description = "Parent holding company whose Muun executives and vault networks consolidate IGBC assets, war loans, and corporate charter stakes across the galaxy.",
            Color = "#0369a1",
            ParentOrganizationSlug = "corporate-blocs",
        },
    ];

    public static Organization? GetBySlug(string slug) =>
        Organizations.FirstOrDefault(org => org.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));

    public static IReadOnlyList<Organization> GetByGroup(string group) =>
        Organizations.Where(org => org.Group.Equals(group, StringComparison.OrdinalIgnoreCase))
            .OrderBy(org => org.Name)
            .ToList();

    public static IReadOnlyList<Organization> GetByParentFaction(string factionSlug) =>
        Organizations.Where(org =>
                org.ParentFactionSlug != null &&
                org.ParentFactionSlug.Equals(factionSlug, StringComparison.OrdinalIgnoreCase))
            .OrderBy(org => org.Name)
            .ToList();

    public static IReadOnlyList<Organization> GetChildren(string hubSlug) =>
        Organizations.Where(org =>
                org.ParentOrganizationSlug != null &&
                org.ParentOrganizationSlug.Equals(hubSlug, StringComparison.OrdinalIgnoreCase))
            .OrderBy(org => org.Name)
            .ToList();

    public static IReadOnlyList<Organization> GetCategoryHubs() =>
        Organizations.Where(org => org.IsCategoryHub)
            .OrderBy(org => org.Name)
            .ToList();
}
