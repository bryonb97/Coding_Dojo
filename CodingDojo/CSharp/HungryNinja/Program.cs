using System;

namespace HungryNinja
{
    class Program
    {
        static void Main(string[] args)
        {
            Buffet myBuffet = new Buffet();
            Ninja myNinja = new Ninja();
            myNinja.Eat(myBuffet.Serve());
        }
    }
}
