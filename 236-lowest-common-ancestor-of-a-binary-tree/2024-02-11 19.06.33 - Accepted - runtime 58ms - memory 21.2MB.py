# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.ans = None

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        def dfs(node):
            if not node:
                return False
            mid = node == p or node == q
            l,r = dfs(node.left), dfs(node.right)

            if mid + l + r >= 2:
                self.ans = node

            return l or r or mid
        
        dfs(root)
        return self.ans    
            
        