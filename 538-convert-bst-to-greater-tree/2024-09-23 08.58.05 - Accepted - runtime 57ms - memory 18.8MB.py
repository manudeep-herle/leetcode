# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.curSum = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        def dfs(node):
            if node.right:
                dfs(node.right)
            self.curSum += node.val
            node.val = self.curSum
            if node.left:
                dfs(node.left)
    
        dfs(root)
        return root

            
        