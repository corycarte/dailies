# This function takes the last element as pivot, places the
# pivot element into the correct position in the sorted array,
# then places all smaller (than pivot) elements to the left of
#  pivot and all larger (than pivot) elements to the right of pivot


def partition(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):
        # if the current element is smaller than the pivot
        if arr[j] < pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# the main function that implements quickSort
# arr[] --> Array to be sorted
# low   --> Start index
# high  --> End index


def quicksort(arr, low, high):
    if low < high:
        # pi is partitioning index, arr[pi] is now
        # at the right place
        pi = partition(arr, low, high)

        # Separately sort elements before
        # partition and after partition
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


# Driver code for test
arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
print("Original array: ")
for i in range(n):
    print("%d " % arr[i])
quicksort(arr, 0, n-1)
print("Sorted array: ")
for i in range(n):
    print("%d " % arr[i])
