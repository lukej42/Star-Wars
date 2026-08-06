namespace StarWars.Models;

public sealed class MilitaryUnitFaction
{
    public required string Name { get; init; }
    public required string Slug { get; init; }
    public required string Route { get; init; }
    public required string Color { get; init; }

    public string ArmyRoute => $"{Route}/army";

    public string NavyRoute => $"{Route}/navy";

    public string ArmyHeroPath => $"/images/military-units/{Slug}-army-hero.webp";

    public string NavyHeroPath => $"/images/military-units/{Slug}-navy-hero.webp";

    public string FactionHeroPath => $"/images/military-units/{Slug}-faction-hero.webp";
}
