def sortArrayByParityI(self, A):
    """
    Runtime : 68ms
    Memory  : 13.3MB
    :type A: List[int]
    :rtype: List[int]
    """
    odd = []
    even = []
      
    for i in xrange(len(A)):
        if A[i] % 2 == 0:
            even.append(A[i])
        else:
            odd.append(A[i])
                
    return even + odd

def sortArrayByParityII(self, A):
    """
    Runtime : 72ms
    Memory  : 13.1MB
    :type A: List[int]
    :rtype: List[int]
    """
    B = A
    s = 0
    
    for i in xrange(len(B)):
        if B[i] % 2 == 0:
            B[i], B[s] = B[s], B[i]
            s += 1
            
    return B