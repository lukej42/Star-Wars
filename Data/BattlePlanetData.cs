using StarWars.Models;
using StarWars.Services;

namespace StarWars.Data;

public static class BattlePlanetData
{
    private static readonly Dictionary<string, string> BattlePlanets = new(StringComparer.OrdinalIgnoreCase)
    {
        ["first-battle-of-geonosis"] = "Geonosis",
        ["battle-of-coruscant"] = "Coruscant",
        ["battle-of-utapau"] = "Utapau",
        ["battle-of-kashyyyk"] = "Kashyyyk",
        ["siege-of-mandalore"] = "Mandalore",
        ["battle-of-mon-cala"] = "Mon Cala",
        ["battle-of-yavin"] = "Yavin 4",
        ["battle-of-hoth"] = "Hoth",
        ["battle-of-endor"] = "Endor",
        ["battle-of-scarif"] = "Scarif",
        ["battle-of-jakku"] = "Jakku",
        ["assault-on-cloud-city"] = "Bespin",
        ["battle-of-malachor-v"] = "Malachor V",
        ["battle-of-dxun"] = "Dxun",
        ["devastation-of-cathar"] = "Cathar",
        ["battle-of-telos-iv"] = "Telos IV",
        ["siege-of-tar-is"] = "Taris",
        ["battle-of-althir"] = "Althir",
        ["battle-of-ossus"] = "Ossus",
        ["battle-of-coruscant-great-sith-war"] = "Coruscant",
        ["battle-of-yavin-4-exar-kun"] = "Yavin 4",
        ["battle-of-kemplex-nine"] = "Kemplex IX",
        ["duel-on-ossus"] = "Ossus",
        ["sith-invasion-of-ossus"] = "Ossus",
        ["sacking-of-coruscant"] = "Coruscant",
        ["battle-of-alderaan-great-galactic-war"] = "Alderaan",
        ["recapture-of-korriban"] = "Korriban",
        ["battle-of-ilum-great-galactic-war"] = "Ilum",
        ["siege-of-balmorra"] = "Balmorra",
        ["invasion-of-ord-mantell"] = "Ord Mantell",
        ["battle-of-troiken"] = "Troiken",
        ["battle-of-qika"] = "Qika",
        ["battle-of-primus-goluud"] = "Primus Goluud",
        ["coruscant-financial-crisis"] = "Coruscant",
        ["battle-of-corbos"] = "Corbos",
        ["battle-of-tython"] = "Tython",
        ["battle-of-ruusan"] = "Ruusan",
        ["seventh-battle-of-ruusan"] = "Ruusan",
        ["thought-bomb-detonation"] = "Ruusan",
        ["battle-of-jabiim-new-sith-wars"] = "Jabiim",
        ["destruction-of-hosnian-prime"] = "Hosnian Prime",
        ["battle-of-starkiller-base"] = "Starkiller Base",
        ["battle-of-crait"] = "Crait",
        ["battle-of-exegol"] = "Exegol",
        ["battle-of-takodana"] = "Takodana",
        ["battle-of-d-qar"] = "D'Qar",
        ["battle-of-corellia"] = "Corellia",
        ["battle-of-alderaan-great-war"] = "Alderaan",
        ["battle-of-ilum-great-war"] = "Ilum",
        ["battle-of-makeb"] = "Makeb",
        ["siege-of-kaon"] = "Kaon",
        ["fall-of-balmorra-great-war"] = "Balmorra",
    };

    public static ProfileLinkItem? GetLink(string battleSlug) =>
        BattlePlanets.TryGetValue(battleSlug, out var planetName)
            ? PlanetLinks.FromName(planetName)
            : null;
}
