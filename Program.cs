using Microsoft.AspNetCore.Components.Web;
using Microsoft.AspNetCore.Components.WebAssembly.Hosting;
using StarWars;
using StarWars.Data;
using StarWars.Services;

var builder = WebAssemblyHostBuilder.CreateDefault(args);
builder.RootComponents.Add<App>("#app");
builder.RootComponents.Add<HeadOutlet>("head::after");

ImageUrls.Configure(builder.Configuration["ImageBaseUrl"], builder.Configuration["ImageCacheVersion"]);

builder.Services.AddScoped(sp => new HttpClient { BaseAddress = new Uri(builder.HostEnvironment.BaseAddress) });
builder.Services.AddScoped<DirectoryProfileService>();
builder.Services.AddScoped<EntityCrossLinkService>();
builder.Services.AddScoped<EntityLocationService>();

await builder.Build().RunAsync();
