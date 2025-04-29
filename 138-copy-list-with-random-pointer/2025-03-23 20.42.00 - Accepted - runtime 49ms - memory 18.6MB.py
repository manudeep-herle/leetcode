"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mem = {}
        def copyNode(node):
            if not node:
                return None
            if node in mem:
                return mem[node]
            copy = Node(node.val, None, None)
            mem[node] = copy
            copy.next = copyNode(node.next)
            copy.random = copyNode(node.random)
            return copy
        
        return copyNode(head)