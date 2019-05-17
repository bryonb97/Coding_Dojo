using System;

namespace Phone 
{
    public class Nokia : Phone, IRingable 
    {
        public Nokia (string versionNumber, int batteryPercentage, string carrier, string ringTone) : base (versionNumber, batteryPercentage, carrier, ringTone) { }

        public string Ring() => _ringTone;

        public string Unlock () 
        {
            Console.WriteLine("Unlocked");
            return "Your phone is unlocked you idiot!";
        }
        public override void DisplayInfo () 
        {
            Console.WriteLine("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");
            Console.WriteLine(_versionNumber);
            Console.WriteLine($"Battery Percentage: {_batteryPercentage}");
            Console.WriteLine($"Carrier: {_carrier}");
            Console.WriteLine($"Ring Tone: {_ringTone}");
            Console.WriteLine("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$");        
        }
    }

}