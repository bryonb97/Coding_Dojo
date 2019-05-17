using System;

namespace IronNinja {
    public class SweetTooth : Ninja {

        // Make a child class of Ninja, for a SweetTooth. A SweetTooth should be "full" at 1500 calories.
        public override bool IsFull {
            get {
                bool full = false;
                if (calorieIntake > 1500) {
                    full = true;
                }
                return full;
            }
        }

        // When a SweetTooth "Consumes":
        // If NOT Full
        // - adds calorie value to SweetTooth's total calorieIntake (+10 additional calories if the consumable item is "Sweet")
        // - adds the randomly selected IConsumable object to SweetTooth's ConsumptionHistory list
        // - calls the IConsumable object's GetInfo() method
        public override void Consume (IConsumable item) {
            if (item.IsSweet) {
                calorieIntake += (item.Calories + 10);
            }
            else {
                calorieIntake += item.Calories;
            }
            ConsumptionHistory.Add(item);
            Console.WriteLine(item.GetInfo());
        }
    }
}