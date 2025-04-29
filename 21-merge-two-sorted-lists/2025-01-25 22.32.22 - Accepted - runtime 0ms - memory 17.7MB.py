# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # check which of the 2 lists starts with smaller number.
        # That'll be head
        # head.next = p1 and the head of other ll is p2.
        nodeHead = ListNode(-1)
        node = nodeHead
        # compare p1 and p2 at each iteration, smaller of two becomes head.next,
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 if list1 is not None else list2

        return nodeHead.next
        # we also increment min(p1, p2) to next and then head to head.next
        # if p1 or p2 is left, we do head.next = p1 or p2.