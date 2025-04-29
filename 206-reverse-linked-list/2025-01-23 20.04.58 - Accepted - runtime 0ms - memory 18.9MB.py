# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = head
        node = head
        res = [None]
        if not node:
            return node
        def recurse(node, prev):
            if node.next:
                recurse(node.next, node)
                node.next = prev
            else:
                res[0] = node
                node.next = prev

        recurse(head, None)
        return res[0]

