# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # do a dfs
        # each node gets passed 2 parents, left parent (parent before turning left), right parent (parent before turning right) -> (inf, -inf)
        # each node should be smaller than left parent and greater than right parent
        def dfs(node, lp, rp):
            if not node:
                return True
            if node.val >= lp or node.val <= rp:
                return False
            
            # visite children
            leftRes = dfs(node.left, node.val, rp)
            rightRes = dfs(node.right, lp, node.val)

            return leftRes and rightRes
        
        return dfs(root, float('inf'), -float('inf'))


        