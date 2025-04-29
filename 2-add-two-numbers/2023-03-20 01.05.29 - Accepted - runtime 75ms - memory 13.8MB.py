# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        h1 = l1
        h2 = l2
        sum = ListNode()
        sum_head = sum
        carry  = 0
        # Iterate through both the lists until end of the shorter list
        while True:
            # print(h1, h2, "\n")
            if h1 and h2:
                s = h1.val + h2.val + carry
                h1 = h1.next
                h2 = h2.next
            elif h1:
                s = h1.val + carry
                h1 = h1.next
            elif h2:
                s = h2.val + carry
                h2 = h2.next
            elif carry:
                s = carry
            else: 
                return(sum_head)
                break

            sum.val = s % 10
            carry = int(s/10)

            if h1 or h2 or carry:
                sum.next = ListNode()
                sum = sum.next

        # Add carrys