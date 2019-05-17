using System;
namespace WizardNinjaSamurai {
    class Ninja : Human 
    {
        public Ninja (string name) : base (name) 
        {
            Name = name;
            Dexterity = 15;
        }

        public override int Attack (Human target) 
        {
            Random rand = new Random ();
            int critChance = rand.Next (0, 100);
            int dmg = 0;
            if (critChance <= 20) 
            {
                dmg = 10 + (Dexterity * 5);
            } else 
            {
                dmg = Dexterity * 5;
            }
            target.Health -= dmg;
            Console.WriteLine ($"{Name} attacked {target.Name} for {dmg} damage!");
            return target.Health;
        }

        public int Steal (Human target) 
        {
            target.Health -= 5;
            Health += 5;
            Console.WriteLine ($"{Name} has stolen 5 hp from {target.Name}!");
            return target.Health;
}
    }
}