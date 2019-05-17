using System;
using System.Collections.Generic;

namespace CollectionsPractice
{
    class Program
    {
        static void Main(string[] args)
        {
            int[] nums = {1, 2, 3, 4, 5, 6, 7, 8, 9};
            string[] names = {"Tim", "Martin", "Nikki", "Sara"};
            bool[] altVals = {true, false, true, false, true, false, true, false, true, false};

            List<string> icecreamFlavors = new List<string>();
            icecreamFlavors.Add("Vanilla");
            icecreamFlavors.Add("Chocolate");
            icecreamFlavors.Add("Strawberry");
            icecreamFlavors.Add("Cookie Dough");
            icecreamFlavors.Add("Cookies 'n Cream");

            Console.WriteLine($"There are {icecreamFlavors.Count} different icecream flavors!");
            Console.WriteLine($"The third flavor is {icecreamFlavors[4]}");
            icecreamFlavors.RemoveAt(4);
            Console.WriteLine($"There are {icecreamFlavors.Count} different icecream flavors!");

            Dictionary<string, string> users = new Dictionary<string, string>();
            users.Add(names[0], icecreamFlavors[0]);
            users.Add(names[1], icecreamFlavors[1]);
            users.Add(names[2], icecreamFlavors[2]);
            users.Add(names[3], icecreamFlavors[3]);

            foreach (var user in users)
            {
                Console.WriteLine($"Key: {user.Key} Value: {user.Value}");
            }
        }   
    }
}
