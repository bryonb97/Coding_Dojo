using System;
using System.Collections.Generic;

class Ninja {
    private int calorieIntake;
    public List<Food> FoodHistory;

    // add a constructor
    public Ninja () 
    {
        calorieIntake = 0;
        FoodHistory = new List<Food> ();
    }
    // add a public "getter" property called "IsFull"
    public bool IsFull
    {
        get
        {
            if(calorieIntake > 1200)
            {
                return true;
            }
            else
            {
                return false;
            }            
        }
    }

    // build out the Eat method
    public void Eat (Food item)
    {
        if(IsFull)
        {
            Console.WriteLine("Ninja is full and can't eat more!");            
        }
        else
        {
            calorieIntake += item.calories; 
            FoodHistory.Add(item);
            if(item.isSpicy)
            {
                Console.WriteLine($"{item.name} is Spicy!");
            }
            else
            {
                Console.WriteLine($"{item.name} is Sweet!");
            }            
        }
    }
}