namespace StarWars.Models;

public sealed class LightsaberForm
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Style { get; init; }
    public required string Color { get; init; }
}

public sealed class FamousBattle
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string WarSlug { get; init; }
    public required string Route { get; init; }
    public required string Era { get; init; }
    public required string Color { get; init; }
}

public sealed class EntityCrossLink
{
    public required string Label { get; init; }
    public required string Value { get; init; }
    public required string Route { get; init; }
}

public sealed class ProfileCrossLinkEntry
{
    public required string Category { get; init; }
    public required string Slug { get; init; }
    public IReadOnlyList<EntityCrossLink> Links { get; init; } = [];
}
