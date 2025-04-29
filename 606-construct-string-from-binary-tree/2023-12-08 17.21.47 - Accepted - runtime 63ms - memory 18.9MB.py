# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res = [""]
        def dfs(node):
            if not node:
                return

            res[0] += str(node.val)
            if node.left or node.right:
                res[0] += "("
                dfs(node.left)
                res[0] += ")"
            if node.right:
                res[0] += "("
                dfs(node.right)
                res[0] += ")"
            return
        dfs(root)
        return res[0]
        