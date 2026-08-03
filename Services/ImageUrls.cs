namespace StarWars.Services;

/// <summary>
/// Resolves app-relative /images/... paths to Azure Blob URLs when ImageBaseUrl is configured.
/// </summary>
public static class ImageUrls
{
    private const string ImagesPrefix = "/images/";

    public static string BaseUrl { get; private set; } = string.Empty;

    public static string CacheVersion { get; private set; } = string.Empty;

    public static void Configure(string? baseUrl, string? cacheVersion = null)
    {
        BaseUrl = baseUrl?.Trim().TrimEnd('/') ?? string.Empty;
        CacheVersion = cacheVersion?.Trim() ?? string.Empty;
    }

    public static string Resolve(string? path)
    {
        if (string.IsNullOrWhiteSpace(path))
        {
            return string.Empty;
        }

        if (path.StartsWith("http://", StringComparison.OrdinalIgnoreCase)
            || path.StartsWith("https://", StringComparison.OrdinalIgnoreCase))
        {
            return AppendCacheVersion(path);
        }

        if (string.IsNullOrEmpty(BaseUrl))
        {
            return path.StartsWith('/') ? path : $"/{path}";
        }

        string resolved;
        if (path.StartsWith(ImagesPrefix, StringComparison.OrdinalIgnoreCase))
        {
            resolved = $"{BaseUrl}/{path[ImagesPrefix.Length..].TrimStart('/')}";
        }
        else if (path.StartsWith("images/", StringComparison.OrdinalIgnoreCase))
        {
            resolved = $"{BaseUrl}/{path["images/".Length..]}";
        }
        else
        {
            resolved = path.StartsWith('/') ? $"{BaseUrl}{path}" : $"{BaseUrl}/{path}";
        }

        return AppendCacheVersion(resolved);
    }

    private static string AppendCacheVersion(string url)
    {
        if (string.IsNullOrEmpty(CacheVersion) || url.Contains('?', StringComparison.Ordinal))
        {
            return url;
        }

        return $"{url}?v={Uri.EscapeDataString(CacheVersion)}";
    }
}
