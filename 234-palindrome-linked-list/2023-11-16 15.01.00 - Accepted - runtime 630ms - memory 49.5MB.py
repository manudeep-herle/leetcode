# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        # Traverse the linked list and copy the values to a string/ list
        while head:
            vals.append(head.val)
            head = head.next
        
        for i in range(len(vals)//2):
            if vals[i] != vals[-(i+1)]:
                return False
        
        return True
        
        