# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:

        def dfs(node, psum):
            # Go right
            if node.right:
                psum = dfs(node.right, psum)
            # Modify val
            psum += node.val
            node.val = psum
            # Go left
            if node.left:
                psum = dfs(node.left, psum)
            return psum

        dfs(root, 0)
    
        return root