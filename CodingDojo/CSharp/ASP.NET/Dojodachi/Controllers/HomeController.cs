using Dojodachi.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Newtonsoft.Json;
using System;

namespace Dojodachi.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet("")]            
        public IActionResult Index()
        {
            if(HttpContext.Session.GetObjectFromJson<Dachi>("DachiData") == null)
            {
                HttpContext.Session.SetObjectAsJson("DachiData", new Dachi());
            }            
            ViewBag.DachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
                if(ViewBag.DachiData.Fullness < 1 || ViewBag.DachiData.Happiness < 1 )
                {
                    ViewBag.DachiData.Status = "Your Dachi just died...";
                } 
                else if(ViewBag.DachiData.Fullness > 100 && ViewBag.DachiData.Happiness > 100 && ViewBag.DachiData.Energy > 100)
                {
                    ViewBag.DachiData.Status = "Your Dachi just succeeded in life...";
                }

            return View();
        }

        [HttpGet("feed")]
        public IActionResult FeedDachi()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if(CurrDachiData.Meals > 0){
                CurrDachiData.Feed();
            } else {
                CurrDachiData.Status = "No more meals! Send your Dojodachi to work to earn more meals.";
            }
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }

        [HttpGet("play")]
        public IActionResult PlayDachi()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if(CurrDachiData.Energy > 0){
                CurrDachiData.Play();
            } else {
                CurrDachiData.Status = "No Energy... your Dachi cannot work or play. Dachi needs sleep.";
            }
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }

        [HttpGet("work")]
        public IActionResult WorkDachi()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            if(CurrDachiData.Energy > 0){
                CurrDachiData.Work();
            } else {
                CurrDachiData.Status = "Your Dojodachi has no more energy.";
            }
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }

        [HttpGet("sleep")]
        public IActionResult SleepDachi()
        {
            Dachi CurrDachiData = HttpContext.Session.GetObjectFromJson<Dachi>("DachiData");
            CurrDachiData.Sleep();
            HttpContext.Session.SetObjectAsJson("DachiData",CurrDachiData);
            return RedirectToAction("Index");
        }

        [HttpGet("reset")]
        public IActionResult Reset()
        {
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }

    }

}
