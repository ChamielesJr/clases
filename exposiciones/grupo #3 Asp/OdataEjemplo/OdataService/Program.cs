using Microsoft.AspNetCore.OData;
using Microsoft.OData.ModelBuilder;
using ODataService.Models;
var builder = WebApplication.CreateBuilder(args);
builder.Services.AddControllers().AddOData(opt =>
{
    var builderModel = new ODataConventionModelBuilder();
    builderModel.EntitySet<Product>("Products");
    opt.AddRouteComponents("odata", builderModel.GetEdmModel()).
    EnableQueryFeatures();
});
var app = builder.Build();
app.UseHttpsRedirection();
app.UseAuthorization();
app.MapControllers();
app.Run();