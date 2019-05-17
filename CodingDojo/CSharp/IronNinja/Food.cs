
namespace IronNinja {
    public class Food : IConsumable {
        public string Name { get; set; }
        public int Calories { get; set; }
        public bool IsSpicy { get; set; }
        public bool IsSweet { get; set; }
        public string GetInfo () {
            return $"Food name: {Name}, Calories: {Calories},  Spicy: {IsSpicy}, Sweet: {IsSweet}";
        }
        public Food (string name, int calories, bool spicy, bool sweet) {
            Name = name;
            Calories = calories;
            IsSpicy = spicy;
            IsSweet = sweet;
        }
    }
}