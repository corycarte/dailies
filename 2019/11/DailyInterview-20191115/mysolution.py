class Solution:
    def minSubArrayLen(self, nums, s): # Fill this in
        cont = []
        sums = []

        prev = 0

        for i in range(1, (len(nums) - 1)):
            if (nums[prev] + nums[i]) >= s:
                if not sums:
                    sums.append(nums[prev])
                    cont.append(prev)
                if cont and cont[-1] == prev:
                    sums.append(nums[i])
                    cont.append(i)
            prev = i

        return len(sums)

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7)) # 2
print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 8)) # 0
print(Solution().minSubArrayLen([2, 0, 1, 2, 4, 3], 4)) # 3