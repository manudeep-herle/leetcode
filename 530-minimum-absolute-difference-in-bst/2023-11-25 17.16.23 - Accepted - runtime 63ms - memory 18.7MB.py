# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from heapq import heappush, heapify, heappop 
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        arr = []
        heapify(arr)
        def recurse(node):
            if not node:
                return
            heappush(arr, node.val)
            recurse(node.right)
            recurse(node.left)
        
        recurse(root)
        res = float('inf') 
        curr = heappop(arr)
        while arr:
            prev = curr
            curr = heappop(arr)
            res = min(res, curr-prev)
        
        return res