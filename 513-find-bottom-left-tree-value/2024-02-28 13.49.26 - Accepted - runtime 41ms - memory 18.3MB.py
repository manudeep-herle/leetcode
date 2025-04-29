# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.res = 0
        self.maxLevel = -1

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def dfs(node, level):
            if not node:
                return
            if level > self.maxLevel:
                self.res = node.val
                self.maxLevel = level
            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return self.res

        