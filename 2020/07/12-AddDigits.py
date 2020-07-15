class Solution:
    def addDigits(self, num: int) -> int:
        n = num
        
        while n > 9:
            res = 0
            while n > 0:
                res = res + (n % 10)
                n //= 10
            n = res
        
        return n