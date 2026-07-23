namespace StarWars.Models;

public sealed class DirectoryProfile
{
    public string Overview { get; init; } = string.Empty;
    public string History { get; init; } = string.Empty;
    public string Significance { get; init; } = string.Empty;
    public IReadOnlyList<string> NotableEvents { get; init; } = [];
    public IReadOnlyList<string> Affiliations { get; init; } = [];
    public IReadOnlyList<ProfileTimelineEntry> Timeline { get; init; } = [];
    public IReadOnlyList<ProfileImage> Gallery { get; init; } = [];
}

public sealed class ProfileTimelineEntry
{
    public required string Era { get; init; }
    public required string Event { get; init; }
}

public sealed class ProfileImage
{
    public required string Path { get; init; }
    public required string Caption { get; init; }
}
