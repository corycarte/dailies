using System;
using System.Collections.Generic;

namespace problem
{
    class MaxStack
    {
        private Stack<int> maxVals;
        private Stack<int> data;

        public MaxStack()
        {
            maxVals = new Stack<int>();
            data = new Stack<int>();
        }

        public void Push(int val)
        {
            if (maxVals.Count == 0 || val >= maxVals.Peek()) maxVals.Push(val);
            data.Push(val);
        }

        public int Pop()
        {
            if(data.Count > 0)
            {
                int top = data.Pop();
                if (top == maxVals.Peek()) maxVals.Pop();
                return top;
            }
            throw new Exception();
        }

        public int Max()
        {
            if (maxVals.Count > 0) return maxVals.Peek();
            else return 0;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            MaxStack s = new MaxStack();
            s.Push(1);
            s.Push(2);
            s.Push(3);
            s.Push(2);

            Console.WriteLine(s.Max().ToString()); // 3
            s.Pop();
            s.Pop();
            Console.WriteLine(s.Max().ToString()); // 2
        }
    }
}
