# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, curSum):
            curSum += node.val
            if not (node.left or node.right):
                if curSum == targetSum:
                    return True
                return False
            l,r = False, False
            if node.left:
                l = dfs(node.left, curSum)
            if node.right:
                r = dfs(node.right, curSum)
            return l or r

        return dfs(root, 0)            
            
        