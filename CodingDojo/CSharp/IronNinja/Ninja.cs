using System;
using System.Collections.Generic;

namespace IronNinja {
    public abstract class Ninja {

        protected int calorieIntake;
        public List<IConsumable> ConsumptionHistory;
        public Ninja () {
            calorieIntake = 0;
            ConsumptionHistory = new List<IConsumable> ();
        }

        public int CalorieAmount {
            get {
                return calorieIntake;
            }
        }
        public abstract bool IsFull {get;}
        public abstract void Consume(IConsumable item);
    }
}