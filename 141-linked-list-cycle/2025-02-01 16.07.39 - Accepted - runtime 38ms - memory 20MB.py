# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # sp, fp. 
        # sp moves 1 node, fp moves 2 nodes, if they meet, cycle present
        # sp and fp moves after n iters where n is the number of nodes in the cycle.
        fp = head
        while fp and fp.next and fp.next.next:
            fp = fp.next.next
            head = head.next
            if fp == head:
                return True
        return False
        