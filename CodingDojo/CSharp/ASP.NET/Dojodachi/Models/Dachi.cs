using System;

namespace Dojodachi.Models
{
    public class Dachi
    {
        public int Fullness { get; set; }
        public int Happiness { get; set; }
        public int Meals { get; set; }
        public int Energy { get; set; }
        public string Status { get; set; }

        public Dachi()
        {
            Happiness = 20;
            Fullness = 20;
            Meals = 3;
            Energy = 50;
            Status = "Welcome, Please use the buttons below to interact with your Dojodachi!";
        }

        public Dachi Feed()
        {            
            Random rand = new Random();
            int chance = rand.Next(1, 6);
            if(chance == 0)
            {
                this.Meals--;
                int amount = rand.Next(5, 11);
                this.Fullness += amount;
                this.Status = $"Your Dojodachi did not like what you fed them but still gained {amount} of Fullness!";
                return this;
            }
            else
            {
                this.Meals--;
                int amount = rand.Next(5, 11);
                this.Fullness += amount;
                this.Status = $"Your Dojodachi just ate and is {amount} fuller!";
                return this;
            }            
        }
        

        public Dachi Play()
        {
            Random rand = new Random();
            int chance = rand.Next(1, 6);
            if(chance == 0)
            {
                this.Energy -= 5;
                int amount = rand.Next(5, 11);
                this.Happiness += amount;
                this.Status = $"Your Dojodachi did not like playing but still gained {amount} Happiness";
                return this;
            }
            else
            {
                this.Energy -= 5;
                int amount = rand.Next(5, 11);
                this.Happiness += amount;
                this.Status = $"Your Dojodachi enjoyed playing with you and gained {amount} Happiness";
                return this;
            }
        }

        public Dachi Work()
        {
            Random rand = new Random();
            int amount = rand.Next(1, 4);
            this.Meals += amount;
            this.Status = $"Your Dojodachi worked and gained {amount} Meals";
            return this;
        }

        public Dachi Sleep()
        {
            this.Energy += 15;
            this.Fullness -= 5;
            this.Happiness -= 5;
            this.Status = $"ZZZZZZZZZ. Shhhh You Dojodachi is sleeping.";
            return this;
        }
    }

    
}