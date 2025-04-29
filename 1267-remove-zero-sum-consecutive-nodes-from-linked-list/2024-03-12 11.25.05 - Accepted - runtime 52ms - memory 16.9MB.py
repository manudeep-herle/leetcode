# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while head and head.val == 0:
            head = head.next
        if not head:
            return
        arr = [head.val]
        node = head.next
        while node:
            prev = arr[-1] if arr else 0
            if prev + node.val == 0:
                arr = []
            elif prev + node.val in arr:
                ind = arr.index(prev + node.val)
                arr = arr[0:ind+1]
            else:
                arr.append(prev + node.val)
            node = node.next
        if not arr:
            return None
        head = ListNode(arr[0])
        pointer = head
        prev = arr[0]
        for num in arr[1:]:
            if num == 0:
                continue
            pointer.next = ListNode(num - prev)
            prev = num
            pointer = pointer.next
        return head




        