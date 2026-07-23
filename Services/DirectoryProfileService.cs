using System.Net.Http.Json;
using StarWars.Models;

namespace StarWars.Services;

public sealed class DirectoryProfileService
{
    private readonly HttpClient httpClient;
    private readonly Dictionary<string, DirectoryProfile> cache = new(StringComparer.OrdinalIgnoreCase);

    public DirectoryProfileService(HttpClient httpClient)
    {
        this.httpClient = httpClient;
    }

    public async Task<DirectoryProfile?> GetProfileAsync(string category, string slug)
    {
        var key = $"{category}/{slug}";
        if (cache.TryGetValue(key, out var cached))
        {
            return cached;
        }

        try
        {
            var profile = await httpClient.GetFromJsonAsync<DirectoryProfile>($"data/profiles/{category}/{slug}.json");
            if (profile is not null)
            {
                cache[key] = profile;
            }

            return profile;
        }
        catch
        {
            return null;
        }
    }
}
