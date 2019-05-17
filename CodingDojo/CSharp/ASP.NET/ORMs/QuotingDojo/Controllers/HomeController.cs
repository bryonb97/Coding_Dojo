using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using QuotingDojo.Models;
using DbConn;

namespace QuotingDojo.Controllers
{
    public class HomeController : Controller
    {
        // Get all Quotes
        [HttpGet("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpPost("create")]
        public IActionResult Create(Quote newQuote)
        {
            string query = $"INSERT INTO quotes (content, author) VALUES ('{newQuote.content}', '{newQuote.author}')";
            System.Console.WriteLine("Inserted into db!");
            DbConnector.Execute(query);
            return RedirectToAction("Show");
        }


        [HttpGet("quotes")]
        public IActionResult Show()
        {
            List<Dictionary<string, object>> AllQuotes = DbConnector.Query("SELECT * FROM quotes");
            ViewBag.Quotes = AllQuotes;
            System.Console.WriteLine($"ViewBag.Quotes");
            return View();
        }
    }
}
