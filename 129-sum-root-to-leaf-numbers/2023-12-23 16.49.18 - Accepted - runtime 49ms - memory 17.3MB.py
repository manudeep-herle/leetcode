# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:

        def dfs(node, sum):
            if not node.right and not node.left:
                return sum * 10 + node.val
            sum = sum * 10 + node.val
            l, r = 0, 0
            if node.left:
                l = dfs(node.left, sum)
            if node.right:    
                r = dfs(node.right, sum)
            return l + r
        
        return dfs(root, 0)
        