class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = {}
        
        for x in range(len(nums)):
            if nums[x] in count:
                count[nums[x]] += 1
            else:
                count[nums[x]] = 1
        
        res = 0
        
        for num in count:
            res += ((count[num] * (count[num] - 1)) // 2)
            
        return res