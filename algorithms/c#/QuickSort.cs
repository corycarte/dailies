using System;

namespace Algorithms
{
    class Quicksort
    {
        /// <summary>
        /// Takes the last element as pivot and places that element into its correct location in sorted array.
        /// Places all smaller (than pivot) values to left of pivot and greater (than pivot) values to the right of pivot
        /// </summary>
        /// <param name="arr"></param>
        /// <param name="low"></param>
        /// <param name="high"></param>
        /// <returns></returns>
        static int partition(int[] arr, int low, int high)
        {
            int piv = arr[high];

            // index of smaller element
            int i = (low - 1);
            for (int j = low; j < high; j++)
            {
                // if the current element is smaller than the pivot
                if (arr[j] < piv)
                {
                    i++;

                    // swap arr[i] and arr[j]
                    int loopTemp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = loopTemp;
                }
            }

            // swap arr[i+1] and arr[high] (or pivot)
            int temp = arr[i + 1];
            arr[i + 1] = arr[high];
            arr[high] = temp;

            return (i + 1);
        }

        static void quickSort(int[] arr, int low, int high)
        {
            if (low < high)
            {
                // pi is partitioning index, arr[pi] is now at right place
                int pi = partition(arr, low, high);

                // recursively sort elements before and after partition
                quickSort(arr, low, pi - 1);
                quickSort(arr, pi + 1, high);
            }
        }

        static void printArray(int[] arr)
        {
            for (int i = 0; i < arr.Length; i++)
                Console.WriteLine(arr[i] + " ");
        }

        static void Main(string[] args)
        {
            int[] arr = { 10, 7, 8, 9, 1, 5 };

            Console.WriteLine("Original array: ");
            printArray(arr);

            quickSort(arr, 0, (arr.Length - 1));
            
            Console.WriteLine("\nSorted array: ");
            printArray(arr);
        }
    }
}
