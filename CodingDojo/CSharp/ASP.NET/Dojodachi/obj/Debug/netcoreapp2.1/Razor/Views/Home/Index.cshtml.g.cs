#pragma checksum "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml" "{ff1816ec-aa5e-4d10-87f7-6f4963833460}" "610b630e5d0f230f218bd9f853a49217628d70ca"
// <auto-generated/>
#pragma warning disable 1591
[assembly: global::Microsoft.AspNetCore.Razor.Hosting.RazorCompiledItemAttribute(typeof(AspNetCore.Views_Home_Index), @"mvc.1.0.view", @"/Views/Home/Index.cshtml")]
[assembly:global::Microsoft.AspNetCore.Mvc.Razor.Compilation.RazorViewAttribute(@"/Views/Home/Index.cshtml", typeof(AspNetCore.Views_Home_Index))]
namespace AspNetCore
{
    #line hidden
    using System;
    using System.Collections.Generic;
    using System.Linq;
    using System.Threading.Tasks;
    using Microsoft.AspNetCore.Mvc;
    using Microsoft.AspNetCore.Mvc.Rendering;
    using Microsoft.AspNetCore.Mvc.ViewFeatures;
#line 1 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/_ViewImports.cshtml"
using Dojodachi;

#line default
#line hidden
#line 2 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/_ViewImports.cshtml"
using Dojodachi.Models;

#line default
#line hidden
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"610b630e5d0f230f218bd9f853a49217628d70ca", @"/Views/Home/Index.cshtml")]
    [global::Microsoft.AspNetCore.Razor.Hosting.RazorSourceChecksumAttribute(@"SHA1", @"9f823666e3659d58cebeb316cce4284db07d26c9", @"/Views/_ViewImports.cshtml")]
    public class Views_Home_Index : global::Microsoft.AspNetCore.Mvc.Razor.RazorPage<dynamic>
    {
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_0 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("src", new global::Microsoft.AspNetCore.Html.HtmlString("~/images/dachiimage.png"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        private static readonly global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute __tagHelperAttribute_1 = new global::Microsoft.AspNetCore.Razor.TagHelpers.TagHelperAttribute("alt", new global::Microsoft.AspNetCore.Html.HtmlString("Dachi Image"), global::Microsoft.AspNetCore.Razor.TagHelpers.HtmlAttributeValueStyle.DoubleQuotes);
        #line hidden
        #pragma warning disable 0169
        private string __tagHelperStringValueBuffer;
        #pragma warning restore 0169
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperExecutionContext __tagHelperExecutionContext;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner __tagHelperRunner = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperRunner();
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __backed__tagHelperScopeManager = null;
        private global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager __tagHelperScopeManager
        {
            get
            {
                if (__backed__tagHelperScopeManager == null)
                {
                    __backed__tagHelperScopeManager = new global::Microsoft.AspNetCore.Razor.Runtime.TagHelpers.TagHelperScopeManager(StartTagHelperWritingScope, EndTagHelperWritingScope);
                }
                return __backed__tagHelperScopeManager;
            }
        }
        private global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper;
        #pragma warning disable 1998
        public async override global::System.Threading.Tasks.Task ExecuteAsync()
        {
            BeginContext(0, 441, true);
            WriteLiteral(@"    <div class=""container""id='wrapper'>
        <div id=""dachiheader"">
            <h3>Welcome to Dojo Dachi</h3><br>
            <!-- <p>To play: enter your Dachi's name and click Play</p>
            <input type=text id=""dachinameinput"" placeholder=""Enter your Dachi's name here""> -->
        </div>
        <div id=""scores"">
            <div id=""fullnessscore"" class=""score"">
                Fullness: <span class=""currdachidata"">");
            EndContext();
            BeginContext(442, 26, false);
#line 9 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
                                                 Write(ViewBag.DachiData.Fullness);

#line default
#line hidden
            EndContext();
            BeginContext(468, 137, true);
            WriteLiteral("</span>\r\n            </div>\r\n            <div id=\"happinessscore\" class=\"score\">\r\n                Happiness: <span class=\"currdachidata\">");
            EndContext();
            BeginContext(606, 27, false);
#line 12 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
                                                  Write(ViewBag.DachiData.Happiness);

#line default
#line hidden
            EndContext();
            BeginContext(633, 128, true);
            WriteLiteral("</span>\r\n            </div>\r\n            <div id=\"mealscore\" class=\"score\">\r\n                Meals:<span class=\"currdachidata\"> ");
            EndContext();
            BeginContext(762, 23, false);
#line 15 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
                                              Write(ViewBag.DachiData.Meals);

#line default
#line hidden
            EndContext();
            BeginContext(785, 131, true);
            WriteLiteral("</span>\r\n            </div>\r\n            <div id=\"energyscore\" class=\"score\">\r\n                Energy: <span class=\"currdachidata\">");
            EndContext();
            BeginContext(917, 24, false);
#line 18 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
                                               Write(ViewBag.DachiData.Energy);

#line default
#line hidden
            EndContext();
            BeginContext(941, 122, true);
            WriteLiteral("</span>\r\n            </div>\r\n        </div>\r\n        <div id=\"dachi\">\r\n            <div id=\"dachiimage\">\r\n                ");
            EndContext();
            BeginContext(1063, 53, false);
            __tagHelperExecutionContext = __tagHelperScopeManager.Begin("img", global::Microsoft.AspNetCore.Razor.TagHelpers.TagMode.StartTagOnly, "a6cbe17133084a6795aa25d6f2f5b5fc", async() => {
            }
            );
            __Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper = CreateTagHelper<global::Microsoft.AspNetCore.Mvc.Razor.TagHelpers.UrlResolutionTagHelper>();
            __tagHelperExecutionContext.Add(__Microsoft_AspNetCore_Mvc_Razor_TagHelpers_UrlResolutionTagHelper);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_0);
            __tagHelperExecutionContext.AddHtmlAttribute(__tagHelperAttribute_1);
            await __tagHelperRunner.RunAsync(__tagHelperExecutionContext);
            if (!__tagHelperExecutionContext.Output.IsContentModified)
            {
                await __tagHelperExecutionContext.SetOutputContentAsync();
            }
            Write(__tagHelperExecutionContext.Output);
            __tagHelperExecutionContext = __tagHelperScopeManager.End();
            EndContext();
            BeginContext(1116, 79, true);
            WriteLiteral("\r\n            </div>\r\n            <div id=\"dachifeedback\">\r\n                <p>");
            EndContext();
            BeginContext(1196, 24, false);
#line 26 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
              Write(ViewBag.DachiData.Status);

#line default
#line hidden
            EndContext();
            BeginContext(1220, 42, true);
            WriteLiteral("</p>\r\n            </div>\r\n        </div>\r\n");
            EndContext();
#line 29 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
          if(ViewBag.DachiData.Status != "Your Dachi just died..." && ViewBag.DachiData.Status != "Your Dachi just succeeded in life..." ){

#line default
#line hidden
            BeginContext(1403, 475, true);
            WriteLiteral(@"        <div id=""dachiactions"">
            <button id='feed' onclick=""window.location.href='/feed'"">Feed</button>
            <button id='play' onclick=""window.location.href='/play'"">Play</button>
            <button id='work' onclick=""window.location.href='/work'"">Work</button>
            <button id='sleep' onclick=""window.location.href='/sleep'"">Sleep</button>
            <button id='sleep' onclick=""window.location.href='/reset'"">Reset</button>
        </div>
");
            EndContext();
#line 37 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
        } else {

#line default
#line hidden
            BeginContext(1896, 141, true);
            WriteLiteral("        <div id=\"dachideathactions\">\r\n            <button id=\'reset\' onclick=\"window.location.href=\'/reset\'\">Reset</button>\r\n        </div>\r\n");
            EndContext();
#line 41 "/Users/bryonbauer/Projects/CodingDojo/CSharp/ASP.NET/Dojodachi/Views/Home/Index.cshtml"
        }

#line default
#line hidden
            BeginContext(2049, 719, true);
            WriteLiteral(@"        <div id=""instruction"">
            <h4>Instructions:</h4>
            <p>Feeding costs 1 meal and yields between 5 and 10 fullness.</p>
            <p>Playing costs 5 energy and yields between 5 and 10 happiness.</p>
            <p>Work costs 5 energy and yields between 1 and 3 meals.</p>
            <p>Sleep costs 5 fullness and 5 happuness and yields 15 energy.</p>
            <br>
            <p>You cannot work or play if you have no energy.</p>
            <p>You cannot eat if you have no meals.</p>
            <p>If you get to 0 Fullness or 0 Happiness, you Dachi will die.</p>
            <p>To Win: Fullness, Happiness, and Energy must be greater than 100.</p>
        </div>
    </div>");
            EndContext();
        }
        #pragma warning restore 1998
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.ViewFeatures.IModelExpressionProvider ModelExpressionProvider { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IUrlHelper Url { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.IViewComponentHelper Component { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IJsonHelper Json { get; private set; }
        [global::Microsoft.AspNetCore.Mvc.Razor.Internal.RazorInjectAttribute]
        public global::Microsoft.AspNetCore.Mvc.Rendering.IHtmlHelper<dynamic> Html { get; private set; }
    }
}
#pragma warning restore 1591
