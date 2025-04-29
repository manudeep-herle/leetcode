"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def recurse(r,c, size):
            # Actual leaf node
            if size == 1:
                return Node(grid[r][c], True)
            size = size // 2
            tl, tr = recurse(r, c, size), recurse(r, c+ size, size)
            bl, br = recurse(r +size, c, size), recurse(r+size, c+size, size)
            # Merge if all children have same val and all are leaf nodes
            if tl.val == tr.val == br.val == bl.val and tl.isLeaf and tr.isLeaf and br.isLeaf and bl.isLeaf:
                return Node(tl.val, True)
            return Node(tl.val, False, tl, tr, bl, br)
        
        return recurse(0,0,len(grid))
        