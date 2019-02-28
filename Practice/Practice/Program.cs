using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice
{
    /// <summary>
    /// A program to study C# based on Derek Banas YouTube Video.
    /// </summary>
    class Program
    {
        static void Main(string[] args)
        {
            #region Variables

            bool canVote = true;
            char grade = 'A';

            int maxInt = int.MaxValue;
            long maxLong = long.MaxValue;
            decimal maxDecimal = decimal.MaxValue;
            float maxFloat = float.MaxValue;
            double maxDouble = double.MaxValue;

            Console.WriteLine("Max int: " + maxInt);
            Console.WriteLine("Can vote = " + canVote.ToString());

            var anotherName = "Tom";

            Console.WriteLine("anotherName is a {0}", anotherName.GetTypeCode());

            double pi = 3.14;
            int intPi = (int)pi;

            Random rand = new Random();
            Console.WriteLine("Random Number between 1 and 10" + (rand.Next(1,11)));

            #endregion

            #region Conditonal Statements
            int age = 17;

            if((age >= 5 ) && (age <= 7))
            {
                Console.WriteLine("Go to elementary school");
            }else if((age > 7) && (age < 13))
            {
                Console.WriteLine("Go to middle school");
            }else if((age > 13) && (age < 18))
            {
                Console.WriteLine("Go to high school");
            }
            else
            {
                Console.WriteLine("Go to college");
            }

            if((age < 14) || (age > 67))
            {
                Console.WriteLine("You shouldn't work");
            }

            bool canDrive = age >= 16 ? true : false;

            switch (age)
            {
                case 0:
                    Console.WriteLine("Infant");
                    break;
                case 1:
                case 2:
                    Console.WriteLine("Toddler");
                    break;
                default:
                    Console.WriteLine("Child");
                    break;
            }

            int i = 0;

            while(i < 10)
            {
                if(i == 7)
                {
                    i++;
                    continue;
                }

                if(i == 9)
                {
                    break;
                }

                if ((i % 2) > 0)
                {
                    Console.WriteLine(i);
                }
                i++;

            }

            string guess;

            while (true)
            {

                int randNum = rand.Next(1, 11);

                do
                {
                    Console.WriteLine("Guess a number");
                    guess = Console.ReadLine();


                } while (!guess.Equals(randNum.ToString()));

                Console.WriteLine("Good job! The number was: {0}", randNum.ToString());
            }

            #endregion

            #region foreach
            string randStr = "Here are some random characters that have no significance";

            foreach (var c in randStr)
            {
                Console.WriteLine(c);
            }
            #endregion

            #region Strings
            string sampString = "A bunch of random words";
            string sampString2 = "More random words";

            Console.WriteLine("Is empty" + String.IsNullOrEmpty(sampString));

            Console.WriteLine("Is empty" + String.IsNullOrWhiteSpace(sampString));

            Console.WriteLine("String Length" + sampString.Length);

            Console.WriteLine("Index of bunch" + sampString.IndexOf("bunch"));

            Console.WriteLine("2nd Word" + sampString.Substring(2, 6));

            Console.WriteLine("Starts with \"A bunch\"" + sampString.StartsWith("A bunch"));
            Console.WriteLine("Ends with \"words\"" + sampString.EndsWith("words"));

            sampString = sampString.Trim();
            sampString = sampString.Replace("words", "characters");

            sampString = sampString.Remove(0, 2);

            //Array of strings
            string[] names = new string[3] {"Matt", "Kevin", "Steve"};

            //Changing that array into a string
            Console.WriteLine("Names List" + String.Join("," , names));

            string frmtStr = String.Format("{0:c}{1:00.00}{2:#.00}", 1.56, 15.567, .56, 1000);

            Console.WriteLine(frmtStr);

            #endregion

            #region StringBuilder

            StringBuilder sb = new StringBuilder();

            sb.Append("This is the first sentence");
            sb.AppendFormat("My name is {0} and I live in {1}", "Bryon", "Illinois");

            sb.Replace("a", "e");

            sb.Remove(5, 7);

            Console.WriteLine(sb.ToString());

            #endregion

            #region Arrays

            int[] randNumArray;

            int[] randArray = new int[5];

            int[] randArray2 = { 1, 2, 3, 4, 5 };

            Console.WriteLine("Array Length: " + randArray2.Length);

            Console.WriteLine("Item 0: " + randArray2[0]);

            Console.WriteLine("Where is 1" + Array.IndexOf(randArray2, 1));

            //String Array
            string[] name = { "Tom", "Paul", "Sally" };

            //Join array with commas
            string nameStr = string.Join(",", name);

            //Put string back to into an array with commas
            string[] nameArray = nameStr.Split(",");

            //Multidimensional Arrays
            int[,] multArray = new int[5, 3];

            int[,] multArray2 = { { 0, 1 }, { 2, 3 }, { 4, 5 } };

            //Loop through multidimensional arrays and print all values
            foreach (var num in multArray2)
            {
                Console.WriteLine(num);
            }

            //Loop through multidimensional arrays and print all values based on their indexes
            for (int x = 0; x < multArray2.GetLength(0); x++)
            {
                for (int y = 0; y < multArray2.GetLength(1); y++)
                {
                    Console.WriteLine("{0}|{1} : {2}", x, y, multArray2[x,y]);
                }
            }

            for (int count = 0; count < randArray.Length; count++)
            {
                Console.WriteLine("{0}:{1}", count, randArray2[count]);
            }

            foreach (int num in randArray2)
            {
                Console.WriteLine(num);
            }

            #endregion

            #region Lists

            //Create list, Automatically is sized based on what is stored
            List<int> numList = new List<int>();

            //Add to list
            numList.Add(5);
            numList.Add(15);
            numList.Add(25);

            //Add array to list
            int[] randomArray = { 1, 2, 3, 4, 5 };
            numList.AddRange(randomArray);

            //Copy array to list
            List<int> numList2 = new List<int>(randomArray);

            //Create list with array
            List<int> numList3 = new List<int>(new int[]{ 1, 2, 3, 4 });

            //Insert into list 
            numList.Insert(1, 10);

            //Remove from list based on name
            numList.Remove(5);

            //Remove from list based on index
            numList.RemoveAt(2);

            //Cycle through list
            for (int j = 0; j < numList.Count; j++)
            {
                Console.WriteLine(numList[j]);
            }

            //Find what number is in given index, Returns -1 if nothing is found in that index
            Console.WriteLine("4 is in index" + numList3.IndexOf(4));

            //Check if int is in the list
            Console.WriteLine("5 in list", numList.Contains(5));

            List<string> strList = new List<string>(new string[] { "Tom", "Paul" });

            //Check if string is in list
            Console.WriteLine("Tom in list" + strList.Contains("tom",
             StringComparer.OrdinalIgnoreCase));


            //Sort list
            strList.Sort();
            #endregion

            #region Exception Handling

            try
            {
                Console.WriteLine("Divide by 10");
                int num = int.Parse(Console.ReadLine());
                Console.WriteLine("10 / {0} = {1}", num, (10/num));
            }

            catch(DivideByZeroException ex)
            {
                System.Console.WriteLine("Can't divide by zero");
                System.Console.WriteLine(ex.GetType().Name);
                System.Console.WriteLine(ex.Message);
            }

            catch(Exception ex)
            {
                System.Console.WriteLine(ex.GetType().Name);
                System.Console.WriteLine(ex.Message);
            }

            #endregion

        }
    }
}
