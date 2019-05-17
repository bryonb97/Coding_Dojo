using System;

namespace HumanProject
{


    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("start");
            Human george = new Human("George");
            Console.WriteLine("created george");
            Human bob = new Human("Bob");
            Console.WriteLine("created bob");

            george.Attack(bob);
        }
    }
}
