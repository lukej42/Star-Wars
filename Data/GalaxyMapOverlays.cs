namespace StarWars.Data;

public sealed record GalaxySector(
    string Name,
    string Slug,
    double CenterX,
    double CenterY,
    double RadiusX,
    double RadiusY,
    string FillColor,
    string Label,
    double LabelX,
    double LabelY,
    string Description);

public sealed record GalaxyHyperlane(
    string Name,
    string Slug,
    IReadOnlyList<(double X, double Y)> Points,
    string Color);

public static class GalaxyMapOverlays
{
    public static IReadOnlyList<GalaxySector> Sectors { get; } =
    [
        new("Deep Core", "deep-core", 4000, 2500, 720, 520, "rgba(255, 247, 214, 0.22)", "Deep Core", 4000, 1680, "Ancient stellar cradle orbiting the galactic core black hole."),
        new("Core Worlds", "core-worlds", 4000, 2500, 1400, 900, "rgba(126, 184, 255, 0.24)", "Core Worlds", 4000, 1180, "Wealthy founding systems and dense trade hubs at the heart of the Republic."),
        new("Inner Rim", "inner-rim", 4000, 2500, 2100, 1300, "rgba(96, 165, 250, 0.18)", "Inner Rim", 6200, 1480, "Established colonies linking the Core to the Mid Rim trade lanes."),
        new("Mid Rim", "mid-rim", 4000, 2500, 2800, 1700, "rgba(74, 222, 128, 0.16)", "Mid Rim", 4000, 620, "Diverse industrial and agricultural worlds between the Core and Outer Rim."),
        new("Outer Rim", "outer-rim", 4000, 2500, 3500, 2200, "rgba(251, 191, 36, 0.18)", "Outer Rim", 4000, 4480, "Frontier systems, Hutt influence, and remote battlefields far from Coruscant."),
        new("Wild Space", "wild-space", 4000, 4300, 3200, 900, "rgba(248, 113, 113, 0.16)", "Wild Space", 1400, 4300, "Uncharted fringes beyond standard hyperspace charts and patrol routes."),
        new("Unknown Regions", "unknown-regions", 6400, 2500, 1400, 2100, "rgba(167, 139, 250, 0.22)", "Unknown Regions", 7200, 980, "Mysterious space beyond the eastern galactic disc; home to the Chiss and First Order redoubts."),
        new("Western Reaches", "western-reaches", 1600, 2500, 1100, 1800, "rgba(148, 163, 184, 0.16)", "Western Reaches", 900, 980, "Sparse western frontier systems trailing the Perlemian Trade Route."),
    ];

    public static IReadOnlyList<GalaxyHyperlane> Hyperlanes { get; } =
    [
        new(
            "Corellian Run",
            "corellian-run",
            [(3200, 2100), (3600, 2300), (4000, 2500), (4400, 2800), (4800, 3200), (5200, 3600)],
            "#fbbf24"),
        new(
            "Hydian Way",
            "hydian-way",
            [(2800, 1200), (3200, 1600), (3600, 2100), (4000, 2500), (4200, 3100), (4300, 3800), (4200, 4400)],
            "#38bdf8"),
        new(
            "Perlemian Trade Route",
            "perlemian-trade-route",
            [(5200, 1800), (4800, 2100), (4400, 2300), (4000, 2500), (3600, 2700), (3200, 2900), (2800, 3100)],
            "#a78bfa"),
        new(
            "Rimma Trade Route",
            "rimma-trade-route",
            [(3600, 3400), (4000, 3600), (4400, 3800), (4800, 4000), (5200, 4100)],
            "#34d399"),
        new(
            "Corellian Trade Spine",
            "corellian-trade-spine",
            [(4000, 2500), (4000, 3000), (3950, 3500), (3900, 4000)],
            "#fb7185"),
    ];
}
