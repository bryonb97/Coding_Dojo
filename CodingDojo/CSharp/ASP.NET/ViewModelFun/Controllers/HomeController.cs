using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using ViewModelFun.Models;

namespace ViewModelFun.Controllers
{
    public class HomeController : Controller
    {
        public IActionResult Index()
        {
            ViewData["Title"] = "This is my message";
            Message msg = new Message()
            {
                content = "This is a message for the message route"
            };
            return View("Index", msg);
        }

        [HttpGet("numbers")]
        public IActionResult Numbers()
        {
            ViewData["Title"] = "These are my numbers";
            Numbers num = new Numbers()
            {
                numList = new List<int> {1,2,3,4,5,6,7,8,9,0}
            };
            return View(num);
        }
        [HttpGet("users")]
        public IActionResult Users()
        {
            ViewData["Title"] = "Here are some Users!";
            Users user = new Users()
            {
                users = new List<string> {"Bob Joe", "Joe Bob", "Jane Smith", "Smith Jane"}
            };
            return View(user);
        }

        [HttpGet("user")]
        public IActionResult SingleUser()
        {
            ViewData["Title"] = "Here is a User!";
            User user = new User()
            {
                user = "Kevin Stradtman"
            };
            return View(user);
        }
    }
}
