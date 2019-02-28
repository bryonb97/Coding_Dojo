using System;
using System.Collections.Generic;
using System.Xml.Linq;

namespace Grades
{

    public class GradeStatistics
    {
        public GradeStatistics()
        {
            HighestGrade = 0;
            LowestGrade = float.MaxValue;
        }

        public float AverageGrade;
        public float LowestGrade;
        public float HighestGrade;
    }
}
