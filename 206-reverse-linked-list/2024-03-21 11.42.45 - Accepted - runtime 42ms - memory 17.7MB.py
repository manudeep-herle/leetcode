# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head:
            res = [None]
            def recurse(parent, node):
                if node.next:
                    recurse(node, node.next)
                else:
                    res[0] = node
                node.next = parent
            
            recurse(None, head)

            return res[0]
        