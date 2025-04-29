# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        curr = n = head 
        
        while curr and n:
            n = n.next
            while n and n.val == curr.val:
                n = n.next    
            
            curr.next = n
            
            curr = n


        return head        
