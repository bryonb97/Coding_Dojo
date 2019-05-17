using System;
using System.Collections.Generic;
using System.Linq;

namespace Puzzles
{
    class Program
    {
        static void Main(string[] args)
        {
            // RandomArray();
            // TossCoin();
            // TossMultipleCoins(3);
            Names();
        }

        static int[] RandomArray(){
            Random rand = new Random();
            int[] randArr = new int[10];

            int max = 0;
            int sum = 0;

            // Fill array with random values ranging from 5-25.
            for(var i = 0; i < 10; i++){
                randArr[i] = rand.Next(5, 26);
                // Console.WriteLine(randArr[i]);              
            }

            // Have to initiate min after array is filled otherwise min will always be set to 0.
            int min = randArr[0];

            foreach (var num in randArr)
            {
                sum += num;

                if(num > max){
                    max = num;
                }
                if(num < min){
                    min = num;
                }
            }

            Console.WriteLine($"Min: {min}");
            Console.WriteLine($"Max: {max}");
            Console.WriteLine($"Sum: {sum}");

            return randArr;
        }

        static string TossCoin(){
            Console.WriteLine("Tossing a coin!");

            Random rand = new Random();

            int toss = rand.Next(2);

            string heads = "Heads";
            string tails = "Tails";
            
            if(toss == 0){
                Console.WriteLine("Heads");
                return heads;
            }
            else{
                Console.WriteLine("Tails");
                return tails;
            }          
        }

        static double TossMultipleCoins(int num){
            int headsCount = 0;
            int tailsCount = 0;
            int tosses = 0;
            while (tosses != num){
                TossCoin();
                
                if(TossCoin() == "heads"){
                    headsCount++;
                }
                else tailsCount++;
                tosses++;
            }
            return tosses / headsCount;
        }

        static List<string> Names(){
            List<string> listOfNames = new List<string>();
            listOfNames.Add("Todd");
            listOfNames.Add("Tiffany");
            listOfNames.Add("Charlie");
            listOfNames.Add("Geneva");
            listOfNames.Add("Sydney");            

            // foreach (var item in listOfNames)
            // {
            //     if(item.Length < 5){
            //         listOfNames.Remove(item);
            //         Console.WriteLine($"Removed {item} because it was only {item.Length} character long!");
            //     }
            // }

            ShuffleList(listOfNames);
            
            return listOfNames;
        }

        static List<string> ShuffleList(List<string> list){
            Random rand = new Random();
            var result = list.OrderBy(item => rand.Next()).ToList();
            foreach (var item in result)
            {
                Console.WriteLine(item);
            }
            return result;            
        }

    }
}
