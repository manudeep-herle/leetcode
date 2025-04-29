"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        hmap = {}

        while curr:
            new = Node(curr.val)
            hmap[curr] = new
            curr = curr.next
        
        curr = head
        
        while curr:
            if curr.next:
                hmap[curr].next = hmap[curr.next] 
            if curr.random:
                hmap[curr].random = hmap[curr.random]
            curr = curr.next
        
        if head in hmap: return hmap[head]
        else: return None

