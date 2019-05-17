using System;
using System.Collections.Generic;

namespace ScramblerAlgo {
    public class Words 
    {
        // Function will take in a Category and that Categorie's list.
        public void GetRandomWord(List<string> Words) 
        {

            // Declare lists of strings that will be all of the words for that category.
            List<string> FoodList = new List<string>();
            FoodList.Add("Burger");
            FoodList.Add("Pizza");

            Random rand = new Random ();
            int wordId = rand.Next(Words.Count);
            Console.WriteLine(Words[wordId]);

        }
    }
}