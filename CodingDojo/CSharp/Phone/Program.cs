using System;

namespace Phone
{
    class Program
    {
        static void Main(string[] args)
        {
            Galaxy s10 = new Galaxy("s10", 100, "T-Mobile", "Ring ring");
            Nokia elevenHundred = new Nokia("1100", 60, "Metro PCS", "Ring Ring Mother Trucker!");

            s10.DisplayInfo();
            Console.WriteLine(s10.Ring());
            Console.WriteLine(s10.Unlock());
            Console.WriteLine("");

            elevenHundred.DisplayInfo();
            Console.WriteLine(elevenHundred.Ring());
            Console.WriteLine(elevenHundred.Unlock());
            Console.WriteLine("");

        }
    }
}
