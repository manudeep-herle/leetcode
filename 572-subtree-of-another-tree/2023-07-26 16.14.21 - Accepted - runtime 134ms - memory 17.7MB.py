# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.check(root, subRoot)
    
    def check(self, r, sr):
        if self.match(r, sr):
            return True
        else:
            left = right = False
            if r.left:
                left = self.check(r.left, sr)
            if not left and r.right:
                right = self.check(r.right, sr)
        
        return left or right
        
        
    def match(self, r, sr):
        if (not r and not sr):
            return True
        
        if not r or not sr:
            return False
        
        if r.val != sr.val:
            return False
        
        left, right = self.match(r.left, sr.left), self.match(r.right, sr.right) 
        return left and right

