using System;
using System.Collections.Generic;

class Food
{
    public string name;
    public int calories;
    public bool isSpicy;
    public bool isSweet;

    public Food(string name, int calories, bool isSpicy, bool isSweet)
    {
        this.name = name;
        this.calories = calories;
        this.isSpicy = isSpicy;
        this.isSweet = isSweet;
    }
}