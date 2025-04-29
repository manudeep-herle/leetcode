from collections import deque
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        s,f = head, head.next
        while f and f.next:
            s = s.next
            f = f.next.next
        l,r = head, s.next
        left, right = [], deque()
        res = 0
        while l and r:
            left.append(l.val)
            right.appendleft(r.val)
            l, r = l.next, r.next
        for i in range(len(left)):
            res = max(res, left[i] + right[i])
        
        return res

        