namespace StarWars.Models;

public sealed class SiteSearchEntry
{
    public required string Name { get; init; }
    public required string Route { get; init; }
    public required string Category { get; init; }
}
