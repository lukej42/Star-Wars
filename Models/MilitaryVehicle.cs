namespace StarWars.Models;

public enum MilitaryVehicleType
{
    Ground,
    Air
}

public sealed class MilitaryVehicle
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string FactionSlug { get; init; }
    public required MilitaryVehicleType Type { get; init; }
    public required string VehicleClass { get; init; }
    public required string Description { get; init; }
    public required string Color { get; init; }

    public string TypeSlug => Type == MilitaryVehicleType.Ground ? "ground" : "air";

    public string Route => $"military-units/{FactionSlug}/{TypeSlug}/{Slug}";

    public string HeroImagePath => $"/images/military-vehicles/{FactionSlug}-{TypeSlug}-{Slug}-hero.webp";
}
