using StarWars.Models;

namespace StarWars.Data;

public static class LightsaberFormData
{
    public static IReadOnlyList<LightsaberForm> Forms { get; } =
    [
        new()
        {
            Name = "Shii-Cho (Form I)",
            Slug = "shii-cho",
            Route = "the-force/lightsaber-forms/shii-cho",
            Style = "The oldest and most basic form, emphasizing wide, sweeping strikes and disarming techniques against multiple opponents.",
            Color = "#94a3b8"
        },
        new()
        {
            Name = "Makashi (Form II)",
            Slug = "makashi",
            Route = "the-force/lightsaber-forms/makashi",
            Style = "An elegant dueling form built on precision, footwork, and economy of motion against a single blade-wielding foe.",
            Color = "#c084fc"
        },
        new()
        {
            Name = "Soresu (Form III)",
            Slug = "soresu",
            Route = "the-force/lightsaber-forms/soresu",
            Style = "The ultimate defensive form, using tight guard positions and patient counter-strokes to outlast blaster fire and relentless assault.",
            Color = "#3b82f6"
        },
        new()
        {
            Name = "Ataru (Form IV)",
            Slug = "ataru",
            Route = "the-force/lightsaber-forms/ataru",
            Style = "An acrobatic, Force-enhanced form favoring leaps, spins, and aggressive momentum to overwhelm opponents.",
            Color = "#22c55e"
        },
        new()
        {
            Name = "Shien / Djem So (Form V)",
            Slug = "shien-djem-so",
            Route = "the-force/lightsaber-forms/shien-djem-so",
            Style = "A counter-offensive form that redirects blaster bolts (Shien) and absorbs an opponent's power before answering with crushing strikes (Djem So).",
            Color = "#f97316"
        },
        new()
        {
            Name = "Niman (Form VI)",
            Slug = "niman",
            Route = "the-force/lightsaber-forms/niman",
            Style = "The balanced \"Way of the Rancor,\" blending elements of earlier forms with Force powers for versatile, diplomatic combatants.",
            Color = "#eab308"
        },
        new()
        {
            Name = "Juyo / Vaapad (Form VII)",
            Slug = "juyo-vaapad",
            Route = "the-force/lightsaber-forms/juyo-vaapad",
            Style = "The most aggressive forms—Juyo's ferocious offense and Mace Windu's Vaapad, which channels dark-side energy through the wielder without surrendering to it.",
            Color = "#dc2626"
        }
    ];

    public static LightsaberForm? GetBySlug(string slug) =>
        Forms.FirstOrDefault(form => form.Slug.Equals(slug, StringComparison.OrdinalIgnoreCase));
}
