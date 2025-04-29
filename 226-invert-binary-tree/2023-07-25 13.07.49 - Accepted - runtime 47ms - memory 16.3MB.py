# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.exchangeChildren(root)
        return root

    def exchangeChildren(self, head):
        if not head:
            return
        head.left and self.exchangeChildren(head.left)
        head.right and self.exchangeChildren(head.right)

        head.left, head.right = head.right, head.left