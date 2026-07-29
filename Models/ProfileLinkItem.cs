namespace StarWars.Models;

public sealed class ProfileLinkItem
{
    public string Label { get; init; } = string.Empty;
    public required string Value { get; init; }
    public required string Route { get; init; }
}

public sealed class ProfileLinkedEvent
{
    public required string Text { get; init; }
    public string Route { get; init; } = string.Empty;
}
