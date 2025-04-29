# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(-float('inf'), root, float('inf'))

    def validate(self, left, node, right):
        if not node:
            return True
        if left < node.val < right:
            return self.validate(left, node.left, node.val) and self.validate(node.val, node.right, right)
        else:
            return False
