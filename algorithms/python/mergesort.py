
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2   # find midpoint
        L = arr[:mid]        # split on midpoint
        R = arr[mid:]        #

        mergesort(L)         # call mergesort on subarray L
        mergesort(R)         # call mergesort on subarray R

        i = j = k = 0

        # merge arrays
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1

            k += 1
            # end while i < len(L) and j < len(R):

        # collect any remaining elements from L and R

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
            # end while i < len(L):

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
            # end while j < len(R):


arr = [12, 11, 13, 5, 6, 7, 13]
print("Original array: ")
for i in range(len(arr)):
    print("%d " % arr[i])
mergesort(arr)
print("Sorted array: ")
for i in range(len(arr)):
    print("%d " % arr[i])
