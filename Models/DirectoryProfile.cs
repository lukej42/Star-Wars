namespace StarWars.Models;

public sealed class DirectoryProfile
{
    public string DateRange { get; init; } = string.Empty;
    public string Overview { get; init; } = string.Empty;
    public string History { get; init; } = string.Empty;
    public string Significance { get; init; } = string.Empty;
    public IReadOnlyList<string> NotableEvents { get; init; } = [];
    public IReadOnlyList<ProfileLinkedEvent> MajorEvents { get; init; } = [];
    public IReadOnlyList<ProfileLinkItem> KeyFactions { get; init; } = [];
    public IReadOnlyList<ProfileLinkItem> MajorCharacters { get; init; } = [];
    public IReadOnlyList<ProfileLinkItem> Planets { get; init; } = [];
    public IReadOnlyList<ProfileLinkItem> Ships { get; init; } = [];
    public IReadOnlyList<string> Films { get; init; } = [];
    public IReadOnlyList<string> Series { get; init; } = [];
    public IReadOnlyList<string> Games { get; init; } = [];
    public IReadOnlyList<string> Books { get; init; } = [];
    public IReadOnlyList<string> Affiliations { get; init; } = [];
    public IReadOnlyList<ProfileTimelineEntry> Timeline { get; init; } = [];
    public IReadOnlyList<ProfileImage> Gallery { get; init; } = [];
    public ProfileLinkItem? Government { get; init; }
    public ProfileLinkItem? HeadOfGovernment { get; init; }
    public ProfileLinkItem? HeadOfState { get; init; }
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
