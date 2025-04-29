# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy 

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse list
        def reverse(head):
            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        curr = reverse(head)

        # Remove nth node
        head, tail = curr, curr.next
        if n == 1:
            head = tail
        elif n == 2:
            head.next = tail.next
        else:
            i = 2
            while tail and tail.next:
                if i+1 == n:
                    tail.next = tail.next.next
                tail = tail.next
                i += 1

        return reverse(head)



        # Reverse list