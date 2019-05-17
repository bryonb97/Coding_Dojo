using System;

namespace IronNinja {
    class Program 
    {
        static void Main (string[] args) 
        {
            Buffet myBuffet = new Buffet ();
            SweetTooth mySweetTooth = new SweetTooth ();
            SpiceHound mySpiceHound = new SpiceHound ();
            while (!mySweetTooth.IsFull) 
            {
                mySweetTooth.Consume (myBuffet.Serve ());
            }
            Console.WriteLine ($"Calorie intake is {mySweetTooth.CalorieAmount}. Ninja is full and cannot consume.");

            Console.WriteLine ("**********");

            while (!mySpiceHound.IsFull) 
            {
                mySpiceHound.Consume (myBuffet.Serve ());
            }
            Console.WriteLine ($"Calorie intake is {mySpiceHound.CalorieAmount}. Ninja is full and cannot consume.");


        }
    }
}