# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = curr = ListNode()

        while list1 and list2:
            curr.next = ListNode()
            curr = curr.next

            print(list1.val, list2.val)
            if list1.val < list2.val:
                curr.val = list1.val
                list1 = list1.next
            else:
                curr.val = list2.val
                list2 = list2.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        

        return ans.next