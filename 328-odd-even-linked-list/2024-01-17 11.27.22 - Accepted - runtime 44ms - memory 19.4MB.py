# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        rh, l, r = head.next, head, head.next
        while r and r.next:
            r.next, l.next = r.next.next, r.next
            r = r.next
            l = l.next
        l.next = rh
        return head
        

        