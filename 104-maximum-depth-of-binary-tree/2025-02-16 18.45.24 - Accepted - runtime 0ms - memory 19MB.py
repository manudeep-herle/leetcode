# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node, level):
            if not node:
                return level
            level += 1
            return max(level, dfs(node.left, level), dfs(node.right, level))
        return dfs(root, 0)