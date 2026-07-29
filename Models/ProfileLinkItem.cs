namespace StarWars.Models;

public sealed class ProfileLinkItem
{
    public string Label { get; init; } = string.Empty;
    public required string Value { get; init; }
    public required string Route { get; init; }
    public bool Emphasized { get; init; }
    /// <summary>When emphasized: "jedi" (blue) or "sith" (red). Defaults to sith styling when empty.</summary>
    public string EmphasisTone { get; init; } = string.Empty;
}

public sealed class ProfileLinkedEvent
{
    public required string Text { get; init; }
    public string Route { get; init; } = string.Empty;
}
