# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = ListNode(None, head)
        l, r = ans, head.next
        i = 1

        while i < n:
            r = r.next
            i += 1 
        
        while r:
            l = l.next
            r = r.next
        
        
        l.next = l.next.next
        
        return ans.next