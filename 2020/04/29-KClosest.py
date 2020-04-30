    def findCrossOver(arr, low, high, x):
        # base case
        if arr[high] <= x:
            return high;

        if arr[low] > x:
            return low

        m = (low + high) // 2

        if arr[m] = x:
            return m

        if arr[m] < x:
            return findCrossOver(arr, m+1, high, x)

        return findCrossOver(arr, low, mid-1, x)


    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l = findCrossOver(arr, 0, len(arr)-1, x)

        while arr[l] == x:
            l -= 1

        while arr[r] == x:
            r += 1
