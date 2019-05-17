
using System;

namespace IronNinja {
    public class SpiceHound : Ninja {
        public override bool IsFull {
            get {
                bool full = false;
                if (calorieIntake > 1200) {
                    full = true;
                }
                return full;
            }
        }
        public override void Consume (IConsumable item) {
            if (item.IsSpicy) {
                calorieIntake += (item.Calories - 5);
            } else {
                calorieIntake += item.Calories;
            }
            ConsumptionHistory.Add (item);
            Console.WriteLine (item.GetInfo ());
        }
    }
}