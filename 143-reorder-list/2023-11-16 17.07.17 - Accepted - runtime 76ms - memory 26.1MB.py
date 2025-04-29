# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Split the lists into two.
        def getSecondHead(head):
            sp, fp = head, head
            while fp and fp.next and fp.next.next:
                fp = fp.next.next
                sp = sp.next
            return sp

        def reverse(head):
            l,r = None, head
            while r:
                t = r.next
                r.next = l
                l = r
                r= t
            return l
        firstEnd = getSecondHead(head)
        secondHead = firstEnd.next
        firstEnd.next = None
        # Reverse second half of the list
        h2 = reverse(secondHead)
        h1 = head
        while h1:
            t1 = h1.next
            h1.next = h2
            h1 = t1
            if h2:
                t2 = h2.next
                h2.next = h1
                h2 = t2
        

        