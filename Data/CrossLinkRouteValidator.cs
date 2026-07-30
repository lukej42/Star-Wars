using StarWars.Models;
using StarWars.Services;

namespace StarWars.Data;

public static class CrossLinkRouteValidator
{
    private static readonly HashSet<string> ValidRoutes = BuildValidRoutes();

    private static readonly Dictionary<string, string> RouteAliases = new(StringComparer.OrdinalIgnoreCase)
    {
        ["factions/galactic-empire"] = "factions/empire",
        ["factions/galactic-republic"] = "factions/republic",
        ["factions/confederacy-of-independent-systems"] = "factions/confederacy",
        ["factions/jedi-order"] = "all-jedi",
        ["factions/sith-order"] = "all-sith",
        ["factions/mandalorian"] = "factions/mandalorians",
        ["factions/bounty-hunters-guild"] = "all-bounty-hunters",
        ["planets/tatooine"] = "planet/tatooine",
        ["planets/coruscant"] = "planet/coruscant",
        ["planets/naboo"] = "planet/naboo",
        ["planets/mustafar"] = "planet/mustafar",
        ["planets/dagobah"] = "planet/dagobah",
        ["planets/hoth"] = "planet/hoth",
        ["planets/endor"] = "planet/endor",
        ["planets/kamino"] = "planet/kamino",
        ["planets/bespin"] = "bespin",
        ["planets/kashyyyk"] = "planet/kashyyyk",
        ["ships/executor"] = "ships/executor-class",
        ["ships/t-65-x-wing"] = "ships/x-wing",
        ["force-powers/telekinesis"] = "force-powers/force-throw",
        ["wars-conflicts/battles/battle-of-geonosis"] = "wars-conflicts/battles/first-battle-of-geonosis",
        ["species/yodas-species"] = "species/yoda-species"
    };

    public static string? NormalizeRoute(string route)
    {
        if (string.IsNullOrWhiteSpace(route))
        {
            return null;
        }

        var normalized = route.Trim().TrimStart('/');

        if (RouteAliases.TryGetValue(normalized, out var alias))
        {
            normalized = alias;
        }

        return ValidRoutes.Contains(normalized) ? normalized : null;
    }

    public static IReadOnlyList<EntityCrossLink> ValidateLinks(IReadOnlyList<EntityCrossLink> links)
    {
        var validated = new List<EntityCrossLink>();

        foreach (var link in links)
        {
            var route = NormalizeRoute(link.Route);
            if (route is null)
            {
                continue;
            }

            validated.Add(new EntityCrossLink
            {
                Label = link.Label,
                Value = link.Value,
                Route = route,
                Image = ImageUrls.Resolve(CrossLinkImageResolver.Resolve(route) ?? link.Image)
            });
        }

        return validated;
    }

    private static HashSet<string> BuildValidRoutes()
    {
        var routes = new HashSet<string>(StringComparer.OrdinalIgnoreCase)
        {
            "all-planets", "all-characters", "all-jedi", "all-sith", "all-ships",
            "all-species", "all-factions", "all-cities-settlements", "all-droids",
            "all-bounty-hunters", "all-military-units", "all-force-powers",
            "all-light-side-powers", "all-dark-side-powers", "galaxy-map", "timelines"
        };

        foreach (var planet in GalaxyData.Planets)
        {
            routes.Add(planet.Route);
        }

        foreach (var faction in FactionData.Factions)
        {
            routes.Add(faction.Route);
        }

        foreach (var character in CharacterData.Characters)
        {
            routes.Add(character.Route);
        }

        foreach (var jedi in JediData.Members)
        {
            routes.Add(jedi.Route);
        }

        foreach (var sith in SithData.Members)
        {
            routes.Add(sith.Route);
        }

        foreach (var ship in ShipData.Ships)
        {
            routes.Add(ship.Route);
        }

        foreach (var species in SpeciesData.SpeciesList)
        {
            routes.Add(species.Route);
        }

        foreach (var power in ForcePowerData.Powers)
        {
            routes.Add(power.Route);
        }

        foreach (var droid in DroidData.Droids)
        {
            routes.Add(droid.Route);
        }

        foreach (var hunter in BountyHunterData.BountyHunters)
        {
            routes.Add(hunter.Route);
        }

        foreach (var settlement in SettlementData.Settlements)
        {
            routes.Add(settlement.Route);
        }

        foreach (var faction in MilitaryUnitData.Factions)
        {
            routes.Add(faction.Route);
        }

        foreach (var unit in MilitaryUnitData.Units)
        {
            routes.Add(unit.Route);
        }

        foreach (var conflict in WarConflictData.Conflicts)
        {
            routes.Add(conflict.Route);
        }

        foreach (var battle in BattleData.All())
        {
            routes.Add(battle.Route);
        }

        foreach (var form in LightsaberFormData.Forms)
        {
            routes.Add(form.Route);
        }

        routes.Add(TheForceTopicData.ConflictBetweenLightAndDark.Route);

        foreach (var topic in TheForceTopicData.Topics)
        {
            routes.Add(topic.Route);
        }

        foreach (var era in TimelineData.Eras)
        {
            routes.Add(era.Route);
        }

        foreach (var chronicle in ChroniclesData.Entries)
        {
            routes.Add(chronicle.Route);
        }

        foreach (var government in GovernmentData.Governments)
        {
            routes.Add(government.Route);
        }

        return routes;
    }
}
