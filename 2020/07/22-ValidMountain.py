DOWN = -1
NONE =  0
UP   =  1

'''
Leetcode 941 - Valid Mountain Array

Runtime => 268ms
Memory => 15MB
'''
class Solution:
    # my submission
    def validMountainArray(self, A: List[int]) -> bool:
        # states = -1 -> DOWN
        #        =  0 -> NONE
        #        =  1 -> UP
        state = NONE
        
        for i in range(1, len(A)):
            if state == NONE:
                if A[i] > A[i-1]:
                    state = UP
                    continue
            
            if state == UP:
                if A[i] < A[i-1]:
                    state = DOWN
                    continue
                if A[i] > A[i-1]:
                    continue
                    
            if state == DOWN:
                if A[i] < A[i-1]:
                    continue
                    
            return False
        
        return state == DOWN

    # 220ms submission
    def validMountainArray_220ms(self, A: List[int]) -> bool:
        if len(A) < 3 or A[0] >= A[1]:
            return False
        
        uphill = True
        
        for i in range(1, len(A)):
            if uphill:
                if A[i-1] >= A[i]:
                    uphill = False
            if not uphill:
                if A[i-1]<=A[i]:
                    return False
        return not uphill