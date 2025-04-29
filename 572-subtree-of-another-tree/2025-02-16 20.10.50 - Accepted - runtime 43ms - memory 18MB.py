# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def treesMatch(node, subnode):
            if node and subnode and node.val == subnode.val:
                return treesMatch(node.left, subnode.left) and treesMatch(node.right, subnode.right)
            elif not node and not subnode:
                return True
            return False
                

        def dfs(node):
            if not node:
                return False
            if treesMatch(node, subRoot):
                return True
            else:
                return dfs(node.left) or dfs(node.right)
        
        return dfs(root)

        