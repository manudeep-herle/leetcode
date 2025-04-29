# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # find length of the ll
        node = head
        leng = 0
        while node:
            leng += 1
            node = node.next
        if leng == 1:
            return None
        toRemove = leng - n
        if toRemove == 0:
            return head.next
        node = head
        prev = None
        i = -1
        while node:
            i += 1
            if i == toRemove:
                prev.next = node.next
                break
            prev = node
            node = node.next
        return head
            

        