# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def rec_solve(node, A):
            if node == None:
                return
            rec_solve(node.left,A)
            rec_solve(node.right,A)
            A.append(node.val)
        A = []
        rec_solve(root, A)
        return A