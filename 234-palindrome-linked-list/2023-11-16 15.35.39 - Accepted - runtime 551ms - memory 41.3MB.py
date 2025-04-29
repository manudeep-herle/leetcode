# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Reverse second half of the LL
        # Find the start of second half
        def startOfSecondList(head):
            sp = head
            fp = head.next
            while fp and fp.next and fp.next.next:
                sp = sp.next
                fp = fp.next.next
            return sp.next

        secondHalf = startOfSecondList(head)
        # Reverse it
        def reverse(head):
            fn, sn = None, head
            while sn:
                temp = sn.next
                sn.next = fn
                fn = sn
                sn = temp
            return fn

        secondHalf = reverse(secondHalf)
        while secondHalf and head:
            if head.val == secondHalf.val:
                head = head.next
                secondHalf = secondHalf.next
            else:
                return False
        return True
