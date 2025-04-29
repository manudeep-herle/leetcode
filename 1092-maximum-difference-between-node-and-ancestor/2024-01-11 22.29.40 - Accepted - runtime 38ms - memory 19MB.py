# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node, s, b):
            if not node:
                return b-s
            s = min(s, node.val)
            b = max(b, node.val)
            return max(dfs(node.left, s, b), dfs(node.right, s, b))

        
        return dfs(root, float('inf'), -float('inf'))


               
        