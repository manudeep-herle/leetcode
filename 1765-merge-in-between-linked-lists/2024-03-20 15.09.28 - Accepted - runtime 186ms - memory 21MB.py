# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        aminus, pointer = None, list1
        i = 0
        while pointer:
            i += 1
            if i == a:
                aminus = pointer
            elif i == b + 2:
                bplus = pointer
                break
            pointer = pointer.next
        aminus.next = list2
        while aminus.next:
            aminus = aminus.next
        aminus.next = bplus
        
        return list1
                

            
        