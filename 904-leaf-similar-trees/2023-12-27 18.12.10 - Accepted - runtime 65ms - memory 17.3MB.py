# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1, leaves2 = [""], [""]
        def dfs(node, leaves):
            if not node.left and not node.right:
                leaves[0] += str(node.val) + ","
                print(leaves)
                
            if node.left:
                dfs(node.left, leaves)
            if node.right:
                dfs(node.right, leaves)
        dfs(root1, leaves1)
        dfs(root2, leaves2)
        return leaves1[0] == leaves2[0]


            
        