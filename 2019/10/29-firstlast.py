class Solution:
    def getRange(self, arr, target):
        # Fill this in.
        first = self.binSearchFirst(arr, target)
        last = self.binSearchLast(arr, target)
        return [first, last]

        # My answer (not optimal)
        #pair = [-1, -1]

        #for i in range(len(arr)):
        #    if arr[i] == target and pair[0] == -1:
        #        pair[0] = i
        #        pair[1] = i
        #    elif arr[i] == target and arr[i + 1] != target:
        #        pair[1] = i
        #return pair

    def binSearchFirst(self, arr, target):
        L = 0
        R = len(arr) - 1
        while L < R:
            m = (L + R) // 2  # floor division
            if arr[m] < target:
                L = m + 1
            else:
                R = m

        if L == (len(arr) - 1):
            return -1
        else:
            return L

    def binSearchLast(self, arr, target):
        L = 0
        R = len(arr) - 1
        while L < R:
            m = (L + R) // 2
            if arr[m] > target:
                R = m
            else:
                L = m + 1

        if L == (len(arr) - 1):
            return -1
        else:
            return (L - 1)



# Test program
test = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8]
x = 2
y = 4
z = 9
print(Solution().getRange(test, x))
# [1, 4]
print(Solution().getRange(test, y))
# [6, 6]
print(Solution().getRange(test, z))
# [-1, -1]
