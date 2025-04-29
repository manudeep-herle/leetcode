# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # do dfs, left -> root -> right (preorder)
        # add values to a list -> vals 
        # return vals[i+1]
        vals = []
        def dfs(node):
            if node.left:
                dfs(node.left)
            vals.append(node.val)
            if node.right:
                dfs(node.right)
        
        dfs(root)
        return vals[k-1]