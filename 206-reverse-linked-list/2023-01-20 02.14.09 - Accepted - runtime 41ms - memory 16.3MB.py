# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        curr = ListNode(head.val, None)
        head = head.next
        while head != None:
            prev = ListNode(curr.val, curr.next)
            curr.val = head.val
            curr.next = prev
            head = head.next
        return curr