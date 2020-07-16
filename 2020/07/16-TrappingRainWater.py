class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Step 1: find max to left of index
        # Step 2: find max to right of index
        # Step 3: compute water trapped at index
        # Step 4: sum trapped water
        
        
        n = len(height)
        
        if n == 0:
            return 0
        
        max_left = [0 for i in range(n)]
        max_right = [0 for i in range(n)]
        
        max_left[0] = height[0]
        max_right[-1] = height[-1]
        
        
        # forward iteration for max_left
        for i in range(1, n):
            max_left[i] = max(max_left[i-1], height[i])
        
        # reverse iteration for max_right
        i = n - 2
        
        while i > -1:
            max_right[i] = max(max_right[i + 1], height[i])
            i -= 1
        
        # compute water trapped per index and add to result        
        res = 0
        
        for i in range(n):
            res += min(max_left[i], max_right[i]) - height[i]
        
        return res


    def capacity(self, arr: List[int]) -> int:
        n = len(arr)
        left_maxes = [0 for _ in range(n)]
        right_maxes = [0 for _ in range(n)]

        current_left_max = 0
        for i in range(n):
            current_left_max = max(current_left_max, arr[i])
            left_maxes[i] = current_left_max

        current_right_max = 0
        for i in range(n - 1, -1, -1):
            current_right_max = max(current_right_max, arr[i])
            right_maxes[i] = current_right_max

        total = 0
        for i in range(n):
            total += min(left_maxes[i], right_maxes[i]) - arr[i]
        
        return total