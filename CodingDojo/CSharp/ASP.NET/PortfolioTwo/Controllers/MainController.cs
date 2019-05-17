using Microsoft.AspNetCore.Mvc;
namespace PortfolioOne.Controllers //be sure to use your own project's namespace!
{
    public class MainController : Controller //remember inheritance??
    {
        [Route ("")]
        public ViewResult Index() => View();

        [Route ("{projects}")]
        public ViewResult Projects() => View();

        [Route ("contact")]
        public ViewResult Contact() => View();
    }
}