using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static Practice.Triangle;

namespace Practice
{
    ///<summary>
    ///Working with classes.
    ///</summary>

    //Enumerates.
    public enum Temperature
    {
        Freeze,
        Low,
        Warm,
        Boil
    }
    class Animal
    {
        #region Animal
        public double height {get; set;}
        public double weight {get; set;}
        public string sound {get; set;}

        public string name;
        public string Name
        {
            get {return name;}
            set {name = value;}
        }

        #endregion

        #region Structs
        struct Customers
        {
            private string name;
            private double balance;
            private int id;

            public void createCust(string n, double b, int i)
            {
                name = n;
                balance = b;
                id = i;
            }

            public void showCust()
            {
                System.Console.WriteLine("Name " + name);
                System.Console.WriteLine("Balance " + balance);
                System.Console.WriteLine("Id " + id);
            }
            #endregion
            
        }
        static void Main(String[] args)
        {
            #region Animal
            //Create a new animal using the parameterized constructor.
            Animal spot = new Animal(15, 10, "Spot", "Woof");
            System.Console.WriteLine("{0} says {1}", spot.name, spot.sound);
            System.Console.WriteLine("Number of Animals" + Animal.getNumOfAnimals());
            System.Console.WriteLine(spot.toString());
            System.Console.WriteLine(spot.getSum(1, 2));

            //Object Initializer
            Animal grover = new Animal
            {
                name = "grover",
                height = 16,
                weight = 18,
                sound = "Grrrrr",
            };


            Dog spike = new Dog();

            System.Console.WriteLine(spike.toString());

            spike = new Dog(20, 15, "Spike", "Grrr", "Chicken");
            #endregion

            #region Shape
            Shape rect = new Rectangle(5, 5);
            Shape tri = new Triangle(5, 5);

            System.Console.WriteLine("Rect Area" + rect.area());
            System.Console.WriteLine("Tri Area" + tri.area());

            Rectangle combRect = new Rectangle(5, 5) + new Rectangle(5, 5);

            System.Console.WriteLine("combRect Area" + combRect.area());
            #endregion

            #region Generics

            KeyValue<string, string> superman = new KeyValue<string, string>("", "");

            superman.key = "Superman";
            superman.value = "Clark Kent";

            KeyValue<int, string> samsungTV = new KeyValue<int, string>(0, "");

            samsungTV.key = 12345;
            samsungTV.value = "a 50 imch Samsung TV";

            superman.showData();
            samsungTV.showData();


            #endregion

            #region Enums

            Temperature micTemp = Temperature.Warm;

            switch(micTemp)
            {
                case Temperature.Freeze:
                    System.Console.WriteLine("Temp on Freezing");
                    break;
                
                case Temperature.Low:
                    System.Console.WriteLine("Temp on Low");
                    break;
                
                case Temperature.Warm:
                    System.Console.WriteLine("Temp on Warm");
                    break;
                
                case Temperature.Boil:
                    System.Console.WriteLine("Temp on Boil");
                    break;
            }
            #endregion

            #region Structs

            Customers bob = new Customers();

            bob.createCust("Bob", 15.50, 12345);

            #endregion

            #region Delegate



            #endregion

        }

        //Default constructor.
        public Animal()
        {
            this.height = 0;
            this.weight = 0;
            this.sound = "No Sound";
            this.name = "No Name";
            numOfAnimals++;
        }

        //Paramaterized constructor.
        public Animal(double height, double weight, string sound, string name)
        {
            this.height = height;
            this.weight = weight;
            this.sound = sound;
            this.name = name;
            numOfAnimals++;
        }
        //Keeps track of the number of animals.
        static int numOfAnimals = 0;

        //Ability to get the number of animals.
        public static int getNumOfAnimals()
        {
            return numOfAnimals;
        }

        public string toString()
        {
            return String.Format("{0} is {1} inches tall, weighs {2} lbs and likes to say {3}", name, height, weight, sound);
        }

        //Method overloading

        public int getSum(int num1 = 1, int num2 = 1)
        {
            return num1 + num2;
        }

        public double getSum(double num1 = 1, double num2 = 1)
        {
            return num1 + num2;
        }
        
    }

    class Dog : Animal
    {
        public string favFood {get; set;}

        public Dog() : base()
        {
            this.favFood = "No Favorite";
        }

        public Dog(double height, double weight, string name, string sound, string favFood) : base(height, weight, name, sound)
        {
            this.favFood = favFood;
        }

        new public string toString()
        {
            return String.Format("{0} is {1} inches tall, weighs {2} lbs and likes to say {3} and eats {4}", name, height, weight, sound, favFood);
        }

    }
    
    abstract class Shape
    {
        public abstract double area();

        public void sayHi()
        {
            System.Console.WriteLine("Hi!");
        }
    }

    //Interface
    public interface ShapeItem
    {
        double area();
    }

    class Rectangle : Shape
    {

        private double length, width;

        public Rectangle(double num1, double num2)
        {
            length = num1;
            width = num2;
        }
        
        public override double area()
        {
            return length * width;
        }

        //Operator overloading. Add two Rectangles together.
        public static Rectangle operator+ (Rectangle rect1, Rectangle rect2)
        {
            double rectLength = rect1.length + rect2.length;
            double rectWidth = rect1.width + rect2.width;

            return new Rectangle(rectLength, rectWidth);
        }
            
    }

    class Triangle : Shape
    {

        private double theBase, height;

        public Triangle(double num1, double num2)
        {
            theBase = num1;
            height = num2;
        }
        
        public override double area()
        {
            return .5 * (theBase * height);
        }


        //Generics.
        public class KeyValue<TKey, TValue>
        {
            public TKey key {get; set;}
            public TValue value {get; set;}

            public KeyValue(TKey k, TValue v)
            {
                key = k;
                value = v;
            }

            public void showData()
            {
                System.Console.WriteLine("{0} is {1}", this.key, this.value);
            }

        }
            
    }
}