'''
Solution not complete as of 0650 18Jun2020

TODO - Logic to determine position within res for the index returned from findNextSmaller
'''

class Solution:
    # return the index of the target's next smaller int
    def findNextSmaller(self, nums: List[int], start: int, tgt: int) -> List[int]:
        for i in range(start, len(nums)):
            if nums[start] > nums[i]:
                return i
        
        return -1
    
    
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        
        curr = len(nums) - 2 # start at next to last value in nums
        
        res = []
        
        res.insert(0, 0) # last index of nums will always have no elements to the right
        
        while curr > -1:
            if nums[curr] > nums[curr + 1]: # greater than val to the right
                res.insert(0, res[0] + 1)
            else:
                nextSmaller = Solution().findNextSmaller(nums, curr, nums[curr])
                if nextSmaller > -1:
                    print("Found next smaller")
                    res.insert(0, 0)
                else:
                    res.insert(0, 0)
            curr -= 1
            
        return res
