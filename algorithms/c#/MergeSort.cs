using System;

namespace Algorithms
{
    class MergeSort
    {
        static void Merge(int[] arr, int l, int m, int r)
        {
            // Find sizes of the two subarrays to be merged
            int n1 = m - l + 1;
            int n2 = r - m;

            // Create temp arrays
            int[] L = new int[n1];
            int[] R = new int[n2];

            // Copy data to temp arrays
            for (int li = 0; li < n1; li++)
                L[li] = arr[l + li];
            for (int rj = 0; rj < n2; rj++)
                R[rj] = arr[m + 1 + rj];

            // Merge the temp arrays
            // initial index of the first and second arrays
            int i = 0, j = 0;

            // initial index of merged subarray array
            int k = l;

            while( i < n1 && j < n2)
            {
                if (L[i] <= R[j])
                    arr[k++] = L[i++];
                else
                    arr[k++] = R[j++];
            }

            // Copy remaining elements of L into arr
            while (i < n1)
            {
                arr[k++] = L[i++];
            }

            // Copy remaining elements of R into arr
            while (j < n2)
            {
                arr[k++] = R[j++];
            }
        }

        static void Sort(int[] arr, int l, int r)
        {
            if (l < r)
            {
                // Find the middle
                int m = l + (r - l) / 2;

                // Call Sort recursively
                Sort(arr, l, m);        // first half
                Sort(arr, m + 1, r);    // second half

                // run merge on result
                Merge(arr, l, m, r);
            }
        }

        static void PrintArray(int[] arr)
        {
            foreach (int j in arr)
                Console.WriteLine(j + " ");
        }

        static void Main(string[] args)
        {
            int[] tosort = { 12, 11, 13, 5, 6, 7 };

            Console.WriteLine("Given Array: ");
            PrintArray(tosort);

            Sort(tosort, 0, (tosort.Length - 1));

            Console.WriteLine("Sorted Array: ");
            PrintArray(tosort);
        }
    }
}
