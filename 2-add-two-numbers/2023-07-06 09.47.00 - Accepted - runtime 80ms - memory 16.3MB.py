# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans_head = ListNode()
        ans = ans_head
        carry = 0
        
        while l1 and l2:
            ans.next = ListNode()
            ans = ans.next
            sum_ = l1.val + l2.val + carry
            carry, s = int(sum_/10), sum_ % 10
            ans.val  = s
            l1, l2 = l1.next, l2.next

        rem = None
        if l1:
            rem = l1
        elif l2:
            rem = l2
        while rem:
            ans.next = ListNode()
            ans = ans.next
            
            sum_ = rem.val + carry
            carry, s = int(sum_/10), sum_ % 10

            ans.val = s
            rem = rem.next
        
        # Clean up
        if carry:
            ans.next = ListNode()
            ans = ans.next
            ans.val = carry
        
        return ans_head.next


        

            
        