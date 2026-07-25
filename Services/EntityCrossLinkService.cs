using System.Net.Http.Json;
using StarWars.Data;
using StarWars.Models;

namespace StarWars.Services;

public sealed class EntityCrossLinkService
{
    private readonly HttpClient httpClient;
    private Dictionary<string, IReadOnlyList<EntityCrossLink>>? cache;

    public EntityCrossLinkService(HttpClient httpClient)
    {
        this.httpClient = httpClient;
    }

    public async Task<IReadOnlyList<EntityCrossLink>> GetLinksAsync(string category, string slug)
    {
        await EnsureLoadedAsync();
        var key = $"{category}/{slug}";
        return cache!.TryGetValue(key, out var links) ? links : Array.Empty<EntityCrossLink>();
    }

    private async Task EnsureLoadedAsync()
    {
        if (cache is not null)
        {
            return;
        }

        try
        {
            var entries = await httpClient.GetFromJsonAsync<List<ProfileCrossLinkEntry>>("data/cross-links.json");
            cache = entries?.ToDictionary(
                entry => $"{entry.Category}/{entry.Slug}",
                entry => CrossLinkRouteValidator.ValidateLinks(entry.Links),
                StringComparer.OrdinalIgnoreCase) ?? new Dictionary<string, IReadOnlyList<EntityCrossLink>>(StringComparer.OrdinalIgnoreCase);
        }
        catch
        {
            cache = new Dictionary<string, IReadOnlyList<EntityCrossLink>>(StringComparer.OrdinalIgnoreCase);
        }
    }
}
