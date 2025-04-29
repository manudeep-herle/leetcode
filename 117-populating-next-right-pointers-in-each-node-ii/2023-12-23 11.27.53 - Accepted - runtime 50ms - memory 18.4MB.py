from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return 
        q, q2 = deque(), deque()
        root.next = None
        q.append(root)

        while q:
            curr = q.popleft()
            q2.append(curr)
            while q:
                next = None
                if q:
                    next = q.popleft()
                curr.next = next
                curr = next
                q2.append(curr)

            while q2:
                node = q2.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return root        