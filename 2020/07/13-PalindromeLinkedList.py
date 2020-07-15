# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        listCheck = []
        
        n = head
        
        while n:
            listCheck.append(n.val)
            n = n.next
            
        n = head
        
        while n:
            if n.val == listCheck[-1]:
                listCheck.pop()
                n = n.next
            else:
                return False
                
        return True