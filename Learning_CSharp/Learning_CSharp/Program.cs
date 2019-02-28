using System;
using System.Collections.Generic;
using System.Xml.Linq;

namespace Grades
{
    class Program
    {
     
        static void Main(string[] args)
        {
            GradeBook book = new GradeBook();
            book.Name = "Bryon's Grade Book";
            book.AddGrade(91);
            book.AddGrade(89.5f);
            book.AddGrade(75);

            GradeStatistics stats = book.ComputeStatistics();
            Console.WriteLine(book.Name);
            WriteResult("Average Grade", stats.AverageGrade);
            WriteResult("Highest Grade", (int)stats.HighestGrade);
            WriteResult("Lowest Grade", stats.LowestGrade);
        }

        static void WriteResult(string description, float result)
        {
            Console.WriteLine("{0}:  {1:F2}",description, result);
        }
    }
}
