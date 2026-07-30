namespace StarWars.Services;

/// <summary>
/// Resolves app-relative /images/... paths to Azure Blob URLs when ImageBaseUrl is configured.
/// </summary>
public static class ImageUrls
{
    private const string ImagesPrefix = "/images/";

    public static string BaseUrl { get; private set; } = string.Empty;

    public static void Configure(string? baseUrl) =>
        BaseUrl = baseUrl?.Trim().TrimEnd('/') ?? string.Empty;

    public static string Resolve(string? path)
    {
        if (string.IsNullOrWhiteSpace(path))
        {
            return string.Empty;
        }

        if (path.StartsWith("http://", StringComparison.OrdinalIgnoreCase)
            || path.StartsWith("https://", StringComparison.OrdinalIgnoreCase))
        {
            return path;
        }

        if (string.IsNullOrEmpty(BaseUrl))
        {
            return path.StartsWith('/') ? path : $"/{path}";
        }

        if (path.StartsWith(ImagesPrefix, StringComparison.OrdinalIgnoreCase))
        {
            return $"{BaseUrl}/{path[ImagesPrefix.Length..].TrimStart('/')}";
        }

        if (path.StartsWith("images/", StringComparison.OrdinalIgnoreCase))
        {
            return $"{BaseUrl}/{path["images/".Length..]}";
        }

        return path.StartsWith('/') ? $"{BaseUrl}{path}" : $"{BaseUrl}/{path}";
    }
}
