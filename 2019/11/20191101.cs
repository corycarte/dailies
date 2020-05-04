using System;
using System.Collections.Generic;

namespace DailyProblem_20191101
{
    class Program
    {

        static public bool TwoSum(int [] nums, int k)
        {
            List<int> comps = new List<int>();

            for (int i = 0; i < nums.Length; i++)
            {
                if (comps.Contains(nums[i])) return true;

                comps.Add(k - nums[i]);
            }

            return false;
        }

        static void Main(string[] args)
        {
            int[] test1 = { 4, 7, 1, -3, 2 };

            int[] test2 = { 8, 7, 1, -3, 2 };

            int[] test3 = { 8, 7, 1, 8, 2 };

            Console.WriteLine(TwoSum(test1, 5));
            Console.WriteLine(TwoSum(test2, 5));
            Console.WriteLine(TwoSum(test3, 5));
        }
    }
}
