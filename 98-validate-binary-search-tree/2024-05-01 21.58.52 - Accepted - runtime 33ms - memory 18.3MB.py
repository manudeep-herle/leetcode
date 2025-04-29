# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recurse(node, low, high):
            if not node:
                return True
            if node.val < high and node.val > low:
                return recurse(node.left, low, node.val) and recurse(node.right, node.val, high)

        return recurse(root, -float('inf'), float('inf'))