namespace StarWars.Models;

public sealed class Faction
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Era { get; init; }
    public required string YearsActive { get; init; }
    public required string Capital { get; init; }
    public required string Government { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    public string ImagePath => $"/images/factions/{Slug}.svg";
}
