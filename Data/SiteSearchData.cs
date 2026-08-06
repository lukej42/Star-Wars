using StarWars.Models;

namespace StarWars.Data;

public static class SiteSearchData
{
    public static IReadOnlyList<SiteSearchEntry> Entries { get; } = BuildEntries();

    public static IReadOnlyList<SiteSearchEntry> Search(string query, int limit = 12)
    {
        if (string.IsNullOrWhiteSpace(query))
        {
            return [];
        }

        var trimmed = query.Trim();

        return Entries
            .Where(entry =>
                entry.Name.Contains(trimmed, StringComparison.OrdinalIgnoreCase) ||
                entry.Route.Contains(trimmed, StringComparison.OrdinalIgnoreCase) ||
                entry.Category.Contains(trimmed, StringComparison.OrdinalIgnoreCase))
            .OrderBy(entry => entry.Name.StartsWith(trimmed, StringComparison.OrdinalIgnoreCase) ? 0 : 1)
            .ThenBy(entry => entry.Name.IndexOf(trimmed, StringComparison.OrdinalIgnoreCase))
            .ThenBy(entry => entry.Name)
            .Take(limit)
            .ToList();
    }

    private static List<SiteSearchEntry> BuildEntries()
    {
        var entries = new List<SiteSearchEntry>();

        Add(entries, CharacterData.Characters, "Character");
        Add(entries, JediData.Members, "Jedi");
        Add(entries, SithData.Members, "Sith");
        Add(entries, GalaxyData.Planets, "Planet");
        Add(entries, ShipData.Ships, "Ship");
        Add(entries, SpeciesData.SpeciesList, "Species");
        Add(entries, FactionData.Factions, "Faction");
        Add(entries, ForcePowerData.Powers, "Force Power");
        Add(entries, DroidData.Droids, "Droid");
        Add(entries, BountyHunterData.BountyHunters, "Bounty Hunter");
        Add(entries, SettlementData.Settlements, "Settlement");
        Add(entries, OrganizationData.Organizations, "Organization");
        Add(entries, CreatureData.Creatures, "Creature");
        Add(entries, TimelineData.Eras, "Timeline");

        return entries
            .GroupBy(entry => entry.Route, StringComparer.OrdinalIgnoreCase)
            .Select(group => group.First())
            .OrderBy(entry => entry.Name)
            .ToList();
    }

    private static void Add<T>(List<SiteSearchEntry> entries, IEnumerable<T> items, string category)
        where T : class
    {
        foreach (var item in items)
        {
            var name = GetProperty<string>(item, "Name");
            var route = GetProperty<string>(item, "Route");

            if (string.IsNullOrWhiteSpace(name) || string.IsNullOrWhiteSpace(route))
            {
                continue;
            }

            entries.Add(new SiteSearchEntry
            {
                Name = name,
                Route = route,
                Category = category
            });
        }
    }

    private static T? GetProperty<T>(object item, string propertyName)
    {
        var property = item.GetType().GetProperty(propertyName);
        if (property?.GetValue(item) is T value)
        {
            return value;
        }

        return default;
    }
}
