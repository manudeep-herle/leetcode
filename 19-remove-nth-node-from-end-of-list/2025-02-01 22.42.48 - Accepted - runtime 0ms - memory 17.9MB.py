# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return 
        # convert nth from last to nth from first
        np = head
        count = 1
        while np.next:
            count += 1
            np = np.next
        
        # count + 1 nodes in the list -> from first it'll be counts - n + 1
        n = count - n + 1
        node = head
        counter = 0
        node = ListNode(-1, head)
        head = node
        while node.next:
            counter += 1
            if counter == n:
                # time to remove node.next
                node.next = node.next.next
                break
            node = node.next
        return head.next


        