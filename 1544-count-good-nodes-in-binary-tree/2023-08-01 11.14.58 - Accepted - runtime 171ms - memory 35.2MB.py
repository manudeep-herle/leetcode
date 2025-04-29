# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        self.count(root, -float("inf"))
        return self.ans
    
    def count(self, head, prev):
        if not head:
            return 
        p = prev
        if head.val >= p:
            self.ans += 1
            p = head.val
        self.count(head.left, p)
        self.count(head.right, p)
