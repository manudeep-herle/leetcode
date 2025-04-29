# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.findDepth(root)

    def findDepth(self, head):
        if not head:
            return 0
        count = 1 + max(self.findDepth(head.left), self.findDepth(head.right))
        return count
            
            
