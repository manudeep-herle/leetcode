# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        A = []
        def recSolve(node, A):
            if node == None:
                return
            print(node.val)
            A.append(node.val)
            recSolve(node.left, A)
            recSolve(node.right, A)
        recSolve(root,A)
        return A