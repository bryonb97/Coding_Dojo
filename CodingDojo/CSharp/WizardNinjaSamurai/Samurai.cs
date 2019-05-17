using System;

class Samurai : Human 
{
    public Samurai (string name) : base (name) 
    {
        Name = name;
        health = 200;
    }

    public override int Attack (Human target) 
    {
        base.Attack (target);
        if (target.Health < 50) 
        {
            target.Health = 0;
        }
        return target.Health;
    }

    public int Meditate () 
    {
        Health = 200;
        Console.WriteLine ($"{Name} has recovered 200 hp!");
        return Health;
    }

}