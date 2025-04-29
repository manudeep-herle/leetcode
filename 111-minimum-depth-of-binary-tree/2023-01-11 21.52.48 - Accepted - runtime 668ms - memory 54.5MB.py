# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def rec_solve(node):
            if node == None:
                return 0
            l = rec_solve(node.left)
            r = rec_solve(node.right)
            if l * r == 0 and l+r != 0:
                l = r = max(l,r)
            return 1 + min(l, r)
        return rec_solve(root)     