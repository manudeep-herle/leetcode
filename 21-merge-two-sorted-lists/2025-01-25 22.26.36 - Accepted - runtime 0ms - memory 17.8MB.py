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
        root = None
        if list1 and list2:
            if list1.val <= list2.val:
                head = list1
                root = list1
                p2 = list2
            else:
                head = list2
                root = list2
                p2 = list1
            p1 = head.next
            # compare p1 and p2 at each iteration, smaller of two becomes head.next,
            while p1 and p2:
                if p1.val < p2.val:
                    head.next = p1
                    p1 = p1.next
                else:
                    head.next = p2
                    p2 = p2.next
                head = head.next

            if p1:
                head.next = p1
            elif p2:
                head.next = p2
            return root
        elif list1:
            return list1
        elif list2:
            return list2
        else:
            return None

        # we also increment min(p1, p2) to next and then head to head.next
        # if p1 or p2 is left, we do head.next = p1 or p2.