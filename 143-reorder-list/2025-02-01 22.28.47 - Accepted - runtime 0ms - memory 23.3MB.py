# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of ll, 
        sp, fp = head, head
        while fp and fp.next and fp.next.next:
            fp = fp.next.next
            sp = sp.next
        middle = sp.next
        sp.next = None
        prev = None
        while middle:
            next = middle.next
            middle.next = prev
            prev = middle
            middle = next
        tail = prev
        node = head

        while tail:
            tnext = tail.next
            nnext = node.next

            node.next = tail
            node.next.next = nnext

            node = nnext
            tail = tnext
    
        return head
  

        




            

    


        # reverse ll from middle till end, 
        
        # merge the end with the beginning

    
        