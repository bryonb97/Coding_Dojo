using System;
using System.Collections.Generic;
class Buffet {
    public List<Food> Menu;

    //constructor
    // Expression body for constructor
    public Buffet() => Menu = new List<Food>()
        {
            new Food ("Chicken", 100, false, false),
            new Food ("Sweet BBQ Chicken", 100, false, true),
            new Food ("Spicy Chicken", 100, true, false),
            new Food ("Spicy Sweet BBQ Chicken", 150, true, true),
            new Food ("Burger", 300, false, false),
            new Food ("Lasagna", 500, false, false),
            new Food ("Tomato Soup", 300, false, false),
        };

    // Serves a random item for the Menu.
    public Food Serve() 
    {
        Random rand = new Random();
        int r = rand.Next(Menu.Count);
        Console.WriteLine($"Served: {Menu[r].name}");
        return Menu[r];
    }
}