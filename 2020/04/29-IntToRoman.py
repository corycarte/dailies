// Question given with Daily Interview Pro 28 Apr 2020
// Solution ran through leetcode
// Runtime: 24 ms
// Memory Usage: 12.8 MB

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = ["", "M", "MM", "MMM"]
        hundreds  = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        tens      = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        ones      = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        return (thousands[num // 1000 % 10] + hundreds[num // 100 % 10] + tens[num // 10 % 10] + ones[num % 10])
