# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            if not node:
                return (0, level-1)
            (ld, left) = dfs(node.left, level + 1)
            (rd, right) = dfs(node.right, level + 1)
            diameter = max(ld, rd, (left - level + right - level))
            return (diameter, max(left, right))

        return dfs(root, 0)[0]
