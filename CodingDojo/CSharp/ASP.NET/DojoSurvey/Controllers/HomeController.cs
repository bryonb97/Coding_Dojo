using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using DojoSurvey.Models;

namespace DojoSurvey.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index() => View();

        [HttpPost("result")]
        public ActionResult Result(string name, string location, string language, string textarea)
        {
            ViewBag.name = name;
            ViewBag.location = location;
            ViewBag.language = language;
            ViewBag.textarea = textarea;

            return View();
}

        [HttpGet("result")]
        public RedirectToActionResult Redirect() => RedirectToAction("Index");
    }
}
