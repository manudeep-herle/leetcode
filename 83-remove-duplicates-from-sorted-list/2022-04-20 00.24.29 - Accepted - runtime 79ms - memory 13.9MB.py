# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        node = head
        c_v = head.val
        
        def getNext(node, c_v):
            if node == None:
                return None
            if node.val != c_v:
                return node
            else:
                return getNext(node.next, c_v)
        
        while node.next:
            node.next = getNext(node.next,c_v)
            if node.next == None:
                return head
            node = node.next 
            c_v = node.val 
        return head
        