# Star Wars Worlds

An interactive Star Wars encyclopedia built with **Blazor WebAssembly**. Browse factions, characters, Jedi, Sith, planets, and starships across the saga — from the films and series to *Knights of the Old Republic* — with rich detail pages, an explorable galaxy map, and a responsive sidebar navigation.

## Features

| Section | Count | Description |
|---------|------:|-------------|
| **Galaxy Map** | 66 worlds | Pan, zoom, and search an interactive map of the galaxy. Click any marker for a quick preview and jump to the full planet page. |
| **Factions** | 7 | Major galactic powers — Republic, Confederacy, Empire, Rebel Alliance, New Republic, Hutt Cartel, and the ancient Sith Empire. |
| **Characters** | 66 | Heroes, villains, droids, and leaders from across the saga (excluding dedicated Jedi/Sith directories). |
| **Jedi Directory** | 42 | Jedi Masters, Knights, and Padawans with rank, history, and legacy. |
| **Sith Directory** | 34 | Sith Lords and dark-side figures from the Rule of Two through the Old Republic era. |
| **Planets** | 66 | Worlds with region, coordinates, environment, culture, and timeline. |
| **Ships** | 60 | Starships and vehicles with class, era, production counts, blueprints, and scene illustrations. |

Each directory entry includes a summary card in the index view and a full detail page with overview, history, significance, notable events, affiliations, timeline, and image gallery where profile data is available.

### Galaxy Map

The map is built on an 8000 × 5000 coordinate system with:

- **Search** — type-ahead suggestions for all 66 worlds
- **Pan and zoom** — drag to move, toolbar controls from 20% to 600% zoom
- **Planet markers** — colour-coded by world, with click-to-preview panels
- **Deep links** — navigate straight to any planet detail page

### Navigation

The sidebar uses collapsible flyout menus for each directory, with colour-coded dots matching entry accent colours. On mobile, flyouts expand on tap and the menu closes after navigation.

## Tech stack

- [.NET 9](https://dotnet.microsoft.com/) with [Blazor WebAssembly](https://learn.microsoft.com/en-us/aspnet/core/blazor/)
- [Bootstrap 5](https://getbootstrap.com/) for layout and responsive styling
- Static JSON profiles served from `wwwroot/data/profiles/`
- Client-side routing with scoped CSS per component

No backend server is required — the app runs entirely in the browser after the initial load.

## Prerequisites

- [.NET 9 SDK](https://dotnet.microsoft.com/download/dotnet/9.0) or later

Verify your installation:

```bash
dotnet --version
```

## Getting started

### Clone the repository

```bash
git clone https://github.com/lukej42/Star-Wars.git
cd Star-Wars
```

### Run locally

```bash
dotnet run
```

Then open the URL shown in the terminal (typically `https://localhost:5001` or `http://localhost:5000`).

### Build for production

```bash
dotnet publish -c Release
```

Published output is written to `bin/Release/net9.0/publish/wwwroot/` and can be deployed to any static host (Azure Static Web Apps, GitHub Pages, Netlify, etc.).

## Project structure

```
Star-Wars/
├── Components/          # Shared UI shells (detail pages, planet layout)
├── Data/                # Static catalogues (characters, planets, ships, …)
├── Layout/              # MainLayout and NavMenu
├── Models/              # C# record types for entries and profiles
├── Pages/               # Routable Blazor pages
├── Services/            # DirectoryProfileService (JSON profile loader)
├── wwwroot/
│   ├── css/             # Global styles
│   ├── data/profiles/   # Extended JSON content per entry
│   └── images/          # Portraits, planet art, ship blueprints & scenes
├── App.razor            # Router and 404 handling
├── Program.cs           # DI and host configuration
└── Star-Wars.csproj
```

## Routes

| Route | Page | Notes |
|-------|------|-------|
| `/` | Home | Landing page |
| `/galaxy-map` | Galaxy Map | Interactive world map |
| `/factions/{slug}` | Faction detail | e.g. `/factions/empire` |
| `/all-characters` | Character index | |
| `/characters/{slug}` | Character detail | e.g. `/characters/han-solo` |
| `/all-jedi` | Jedi index | |
| `/jedi/{slug}` | Jedi detail | e.g. `/jedi/obi-wan-kenobi` |
| `/all-sith` | Sith index | |
| `/sith/{slug}` | Sith detail | e.g. `/sith/darth-vader` |
| `/all-planets` | Planet index | |
| `/planet/{slug}` | Planet detail | e.g. `/planet/tatooine` |
| `/all-ships` | Ship index | |
| `/ships/{slug}` | Ship detail | e.g. `/ships/millennium-falcon` |

Some iconic worlds also have short alias routes (e.g. `/tatooine`, `/coruscant`, `/bespin`, `/hoth`, `/mustafar`, `/dantooine`, `/naboo`, `/korriban`) that render the same planet detail view.

## Content architecture

Content is split into two layers:

1. **Catalogue data** (`Data/*.cs`) — name, slug, route, summary description, accent colour, and type-specific fields (rank, class, region, map coordinates, etc.). This is compiled into the app and drives navigation and index pages.

2. **Profile JSON** (`wwwroot/data/profiles/{category}/{slug}.json`) — extended content loaded at runtime by `DirectoryProfileService`. Each profile can include:

   ```json
   {
     "overview": "...",
     "history": "...",
     "significance": "...",
     "notableEvents": ["..."],
     "affiliations": ["..."],
     "timeline": [{ "era": "...", "event": "..." }],
     "gallery": [{ "path": "/images/...", "caption": "..." }]
   }
   ```

   Profiles are cached in memory after the first fetch. If a profile file is missing, the detail page falls back to the summary from the catalogue data.

### Profile coverage

| Category | Profiles |
|----------|----------:|
| Characters | 66 |
| Jedi | 42 |
| Sith | 34 |
| Planets | 66 |
| Ships | 60 |

Ship entries include SVG blueprint and scene illustrations under `wwwroot/images/ships/`.

## Adding new content

To add a new entry (e.g. a character):

1. Add a record to the appropriate `Data/*.cs` file with `Name`, `Slug`, `Route`, `Description`, and `Color`.
2. Create a matching JSON profile at `wwwroot/data/profiles/{category}/{slug}.json`.
3. Add any images under `wwwroot/images/`.
4. The sidebar and index pages update automatically from the catalogue data — no route registration is needed beyond the existing `{Slug}` page templates.

For planets, also set `X` and `Y` coordinates in `GalaxyData.cs` so the world appears on the galaxy map (see `GalaxyMapSettings.cs` for the coordinate bounds).

## Disclaimer

This is a fan project for educational and personal use. *Star Wars* and all related names, characters, and imagery are trademarks of Lucasfilm Ltd. This project is not affiliated with, endorsed by, or sponsored by Lucasfilm or The Walt Disney Company.
