using System;

namespace fundamentals1 {
    class Program {
        static void Main (string[] args) {
            for (int i = 1; i < 101; i++) {
                if (i % 3 == 0 || i % 5 == 0) {
                    Console.WriteLine (i);
                }
            }

            for (int i = 1; i < 101; i++) {
                if (i % 3 == 0) {
                    Console.WriteLine (i + " " + "Fizz");
                }
                if (i % 5 == 0) {
                    Console.WriteLine (i + " " + "Buzz");
                }
                if (i % 3 == 0 && i % 5 == 0) {
                    Console.WriteLine (i + " " + "FizzBuzz");
                }
            }

            int i = 1;
            while (i < 101) {
                if (i % 3 == 0) {
                    Console.WriteLine (i + " " + "Fizz");
                }
                if (i % 5 == 0) {
                    Console.WriteLine (i + " " + "Buzz");
                }
                if (i % 3 == 0 && i % 5 == 0) {
                    Console.WriteLine (i + " " + "FizzBuzz");
                }
                i++;
            }

        }
    }
}
