using System;

class Wizard : Human 
{
    public Wizard (string name) : base (name) 
    {
        Name = name;
        health = 50;
        Intelligence = 25;
    }

    public override int Attack (Human target) 
    {
        int dmg = Intelligence * 5;
        target.Health -= dmg;
        Console.WriteLine ($"{Name} attacked {target.Name} for {dmg} damage!");
        health += dmg;
        return target.Health;
    }

    public int Heal (Human target) 
    {
        int cure = Intelligence * 10;
        target.Health += cure;
        Console.WriteLine ($"{Name} has healed {target.Name} and restored {cure.ToString()} hp!");
        return target.Health;
    }

}