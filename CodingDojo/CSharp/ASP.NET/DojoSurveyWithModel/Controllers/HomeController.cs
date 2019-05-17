using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using DojoSurveyWithModel.Models;

namespace DojoSurveyWithModel.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index() => View();

        [HttpPost("result")]
        public IActionResult Index(Survey response)
        {
            if(ModelState.IsValid)
            {
                return View("Result");
            }
            else
            {
                return View();
            }
        }
    }
}
