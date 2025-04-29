# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import wraps

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def rec_solve(node):
            if node == None:
                 return 0 
            lh = rec_solve(node.left)
            rh = rec_solve(node.right)
            if lh< 0 or rh < 0 or abs(lh-rh) > 1:
                return -1
            else: return max(lh,rh) + 1

        return rec_solve(root) > -1
                

                