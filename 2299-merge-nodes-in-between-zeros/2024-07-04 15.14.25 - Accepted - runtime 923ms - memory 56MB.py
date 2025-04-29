# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node, prev = head, head
        sum = 0
        while node:
            if node.val == 0 and sum:
                prev.next.val = sum
                prev.next.next = node
                prev = node
                sum = 0
            else:
                sum += node.val
            node = node.next

        node = head.next
        prev = node
        while node:
            if node.val == 0:
                prev.next = node.next
                prev = node.next
            node = node.next
        
        return head.next
        