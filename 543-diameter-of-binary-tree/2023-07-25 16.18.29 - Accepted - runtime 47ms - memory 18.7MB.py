# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0
        # For every node determine length of left and right branches
        self.findDiameter(root)
        return self.best
    
    def findDiameter(self, head):
        if not head:
            return 0
       
        leftLen, rightLen = self.findDiameter(head.left), self.findDiameter(head.right)
        
        if leftLen + rightLen > self.best:
            self.best = leftLen + rightLen
        
        return 1 + max(leftLen, rightLen)
    
