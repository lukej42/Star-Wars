using System.Net.Http.Json;
using StarWars.Models;
using StarWars.Services;

namespace StarWars.Data;

public sealed class EntityLocationService
{
    private readonly HttpClient httpClient;
    private Dictionary<string, EntityLocationRecord>? cache;

    public EntityLocationService(HttpClient httpClient)
    {
        this.httpClient = httpClient;
    }

    public async Task<ProfileLinkItem?> GetHomePlanetAsync(string category, string slug)
    {
        if (category.Equals("settlements", StringComparison.OrdinalIgnoreCase))
        {
            return null;
        }

        var record = await GetRecordAsync(category, slug);
        return record is null ? null : ToHomePlanetLink(record);
    }

    public ProfileLinkItem? GetLocationFromPlanetName(string? planetName)
    {
        var link = PlanetLinks.FromName(planetName);
        if (link is null)
        {
            return null;
        }

        return new ProfileLinkItem
        {
            Label = "Location",
            Value = link.Value,
            Route = link.Route
        };
    }

    public ProfileLinkItem? GetHomePlanetFromName(string? planetName)
    {
        var link = PlanetLinks.FromName(planetName);
        if (link is null)
        {
            return null;
        }

        return ToHomePlanetLink(new EntityLocationRecord
        {
            PlanetName = link.Value,
            Route = link.Route
        });
    }

    public static ProfileLinkItem ToHomePlanetLink(EntityLocationRecord record) =>
        new()
        {
            Label = "Home planet",
            Value = record.PlanetName,
            Route = record.Route
        };

    public static ProfileLinkItem ToLocationLink(EntityLocationRecord record) =>
        new()
        {
            Label = "Location",
            Value = record.PlanetName,
            Route = record.Route
        };

    private async Task<EntityLocationRecord?> GetRecordAsync(string category, string slug)
    {
        await EnsureLoadedAsync();
        return cache!.TryGetValue($"{category}/{slug}", out var record) ? record : null;
    }

    private async Task EnsureLoadedAsync()
    {
        if (cache is not null)
        {
            return;
        }

        try
        {
            cache = await httpClient.GetFromJsonAsync<Dictionary<string, EntityLocationRecord>>("data/entity-locations.json")
                ?? new Dictionary<string, EntityLocationRecord>(StringComparer.OrdinalIgnoreCase);
        }
        catch
        {
            cache = new Dictionary<string, EntityLocationRecord>(StringComparer.OrdinalIgnoreCase);
        }
    }
}

public sealed class EntityLocationRecord
{
    public string PlanetName { get; init; } = string.Empty;
    public string Route { get; init; } = string.Empty;
}
