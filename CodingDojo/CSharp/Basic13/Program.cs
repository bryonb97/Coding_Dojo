using System;

namespace Basic13 {
    class Program {
        static void Main (string[] args) {
            Console.WriteLine ("Hello World!");
        }

        public static void PrintNumbers () {
            // Print all of the integers from 1 to 255.
            for (int i = 1; i < 256; i++) {
                Console.WriteLine (i);
            }
        }

        public static void PrintOdds () {
            // Print all of the odd integers from 1 to 255.
            for (int i = 1; i < 256; i++) {
                if (i % 2 != 0) {
                    Console.WriteLine (i);
                }
            }
        }

        public static void PrintSum () {
            // Print all of the numbers from 0 to 255, 
            // but this time, also print the sum as you go. 
            // For example, your output should be something like this:

            // New number: 0 Sum: 0
            // New number: 1 Sum: 1
            // New Number: 2 Sum: 3
            int sum = 0;
            for (int i = 0; i < 256; i++) {
                sum += i;
                Console.WriteLine ($"New number: {i} Sum: {sum}");
            }
        }

        public static void LoopArray (int[] numbers) {
            // Write a function that would iterate through each item of the given integer array and 
            // print each value to the console. 
            foreach (var i in numbers) {
                Console.WriteLine (i);
            }
        }

        public static int FindMax (int[] numbers) {
            // Write a function that takes an integer array and prints and returns the maximum value in the array. 
            // Your program should also work with a given array that has all negative numbers (e.g. [-3, -5, -7]), 
            // or even a mix of positive numbers, negative numbers and zero.
            int max = 0;
            foreach (var num in numbers) {
                if (num > max) {
                    max = num;
                }
            }
            return max;
        }

        public static GetAverage (int[] numbers) {
            // Write a function that takes an integer array and prints the AVERAGE of the values in the array.
            // For example, with an array [2, 10, 3], your program should write 5 to the console.
            int sum = 0;
            foreach (var num in numbers) {
                sum += num;
            }
            return sum / numbers.Length;
        }

        public static int[] OddArray () {
            // Write a function that creates, and then returns, an array that contains all the odd numbers between 1 to 255. 
            // When the program is done, this array should have the values of [1, 3, 5, 7, ... 255].cop
            int[] oddNums = new int[256];
            for (int i = 0; i < oddNums.Length; i++) {
                oddNums[i] = i;
            }
            return oddNums;
        }

        public static int GreaterThanY (int[] numbers, int y) {
            // Write a function that takes an integer array, and a integer "y" and returns the number of array values 
            // That are greater than the "y" value. 
            // For example, if array = [1, 3, 5, 7] and y = 3. Your function should return 2 
            // (since there are two values in the array that are greater than 3).
            int count = 0;
            foreach (var num in numbers) {
                if (num > y) {
                    count++;
                }
            }
            return count;
        }

        public static SquareArrayValues (int[] numbers) {
            // Write a function that takes an integer array "numbers", and then multiplies each value by itself.
            // For example, [1,5,10,-10] should become [1,25,100,100]
            foreach (var num in numbers) {
                num *= num;
            }
        }

        public static EliminateNegatives (int[] numbers) {
            // Given an integer array "numbers", say [1, 5, 10, -2], create a function that replaces any negative number with the value of 0. copy
            // When the program is done, "numbers" should have no negative values, say [1, 5, 10, 0]
            foreach (var num in numbers) {
                if (num < 0) {
                    num = 0;
                }
            }
            return numbers;
        }
        public static void MinMaxAverage (int[] numbers) {
            // Given an integer array, say [1, 5, 10, -2], create a function that prints the maximum number in the array, 
            // the minimum value in the array, and the average of the values in the array.
            int min = numbers[0];
            int max = 0;
            int sum = 0;
            foreach (var num in numbers) {
                if (num > max) {
                    max = num;
                } else if (num < min) {
                    min = num;
                }

                sum += num;
            }
            Console.WriteLine ($"Min: {min} Max: {max} Avg: {sum / numbers.Length}");
        }

        public static void ShiftValues (int[] numbers) {
            // Given an integer array, say [1, 5, 10, 7, -2], 
            // Write a function that shifts each number by one to the front and adds '0' to the end. 
            // For example, when the program is done, if the array [1, 5, 10, 7, -2] is passed to the function, copy
            // it should become [5, 10, 7, -2, 0]
            int[] newArr = new int[numbers.Length];
            int count = 0;
            for (int i = 1; i < numbers.Length; i++) {
                newArr[count] = numbers[i];
                count++;
            }
            newArr[newArr.Length - 1] = 0;
            for (int j = 0; j < newarr.Length; j++) {
                Console.WriteLine (newArr[j]);
            }
        }

        public static object[] NumToString (int[] numbers) {
            // Write a function that takes an integer array and returns an object array 
            // that replaces any negative number with the string 'Dojo'.
            // For example, if array "numbers" is initially [-1, -3, 2] 
            // your function should return an array with values ['Dojo', 'Dojo', 2].
            foreach (var num in numbers) {
                if (num < 0) {
                    num = "Dojo";
                }
            }
            return numbers as object;
        }

    }
}