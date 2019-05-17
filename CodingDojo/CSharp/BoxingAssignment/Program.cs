using System;
using System.Collections.Generic;

namespace BoxingAssignment
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> myObject = new List<object>();
            myObject.Add(7);
            myObject.Add(28);
            myObject.Add(-1);
            myObject.Add(true);
            myObject.Add("chair");

            int sum = 0;
            foreach (var item in myObject)    
            {
                Console.WriteLine(item);

                if(item is int){
                    sum += (int)item;
                }
            }
            Console.WriteLine(sum);
        }
    }
}
