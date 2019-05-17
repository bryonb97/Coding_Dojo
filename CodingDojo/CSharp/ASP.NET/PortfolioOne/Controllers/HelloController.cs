    using Microsoft.AspNetCore.Mvc;
    namespace PortfolioOne.Controllers //be sure to use your own project's namespace!
    {
        public class HelloController : Controller //remember inheritance??
        {
        [Route("")]
        public string Index() => "This is my index!";

        [HttpGet]
        [Route("{projects}")]
        public string Projects() => $"These are my projects!";

        [HttpGet]
        [Route("contact")]
        public string Contact() => $"This is my Contact Info!";
    }
    }