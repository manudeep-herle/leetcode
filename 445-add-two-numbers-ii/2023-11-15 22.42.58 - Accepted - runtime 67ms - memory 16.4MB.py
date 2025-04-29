# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the two lists
        def reverse(head):
            curr, prev = head, None
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        l1, l2 = reverse(l1), reverse(l2)
        carry  = 0
        root = res = ListNode()
        while l1 or l2:
            val = 0
            if l1 and l2:
                total = l1.val + l2.val + carry
                l1, l2 = l1.next, l2.next
            elif l1:
                total = l1.val + carry
                l1 = l1.next
            else:
                total = l2.val + carry
                l2 = l2.next
            carry = total // 10
            val = total % 10
            root.next = ListNode(val)
            root = root.next
        if carry:
            root.next = ListNode(carry)
            root = root.next
        return reverse(res.next)



        


            
        
        