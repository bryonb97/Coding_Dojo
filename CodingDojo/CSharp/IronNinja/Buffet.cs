using System;
using System.Collections.Generic;

namespace IronNinja {
    public class Buffet {
        public List<IConsumable> Menu; 
        // add a constructor and set Menu to a hard coded list of 7 or more Food objects you instantiate manually
        public Buffet () {
            Menu = new List<IConsumable> () {
                new Food ("Slice of Cheese Pizza", 277, false, false),
                new Food ("Tiramisu", 240, false, true),
                new Food ("Steak Taco", 250, true, false),
                new Food ("Egg Salad Sandwich", 600, false, false),
                new Food ("Pad Thai", 940, true, false),
                new Food ("Snickers Bar", 215, false, true),
                new Food ("Mac and Cheese", 310, false, false),
                new Drink ("Bloody Mary", 120, true, false),
                new Drink ("Michelada", 190, true, false),
                new Drink ("Yoohoo", 180, false, true),
                new Drink ("Piña Colada", 55, false, true),
            };
        }
        
        // build out a Serve method that randomly selects a Food object from the Menu list and returns the Food object
        Random rand = new Random ();
        public IConsumable Serve () {
            return Menu[rand.Next(Menu.Count)];
        }
    }
}