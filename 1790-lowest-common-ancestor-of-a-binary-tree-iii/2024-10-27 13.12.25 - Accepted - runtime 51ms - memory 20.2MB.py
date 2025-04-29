"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        pPath, qPath = set(), []
        
        while p:
            pPath.add(p.val)
            p = p.parent
        while q:
            qPath.append(q)
            q = q.parent


        for q in qPath:
            if q.val in pPath:
                return q
        
        