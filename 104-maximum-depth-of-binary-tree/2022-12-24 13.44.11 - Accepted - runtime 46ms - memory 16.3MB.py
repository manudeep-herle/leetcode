# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def goDeep(n, depth = 0):
            if n == None:
                return depth
            else: return max(goDeep(n.left, depth+1), goDeep(n.right, depth+1))
        
        return goDeep(root)
            
            
            
