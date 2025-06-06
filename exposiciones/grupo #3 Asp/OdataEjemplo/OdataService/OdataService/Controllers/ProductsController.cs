using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.OData.Routing.Controllers;
using Microsoft.AspNetCore.OData.Query;
using ODataService.Models;
using System.Collections.Generic;
using System.Linq;
namespace ODataService.Controllers
{
    public class ProductsController : ODataController
    {
        private static List<Product> _products = new List<Product>
        {
            new Product { Id = 1, Name = "Laptop", Price = 1500 },
            new Product { Id = 2, Name = "Mouse", Price = 25 }
        };
        [EnableQuery]
            public ActionResult<IQueryable<Product>> Get()
        {
            return Ok(_products.AsQueryable());
        }
    }
}