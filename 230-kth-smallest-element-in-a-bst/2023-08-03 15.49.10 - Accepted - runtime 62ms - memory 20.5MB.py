# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.list = []
        self.addToList(root)
        print(self.list)
        return self.list[k-1]
 
    def addToList(self, head):
        if not head:
            return
        
        if head.left:
            self.addToList(head.left)
        
        self.list.append(head.val)
        
        if head.right:
            self.addToList(head.right)