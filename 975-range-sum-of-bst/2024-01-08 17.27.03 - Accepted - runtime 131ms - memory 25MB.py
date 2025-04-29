from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        q = deque()
        q.append(root)
        res = 0
        while q:
            node = q.popleft()
            if node:
                if node.val >= low and node.val <= high:
                    res += node.val
                q.append(node.left)
                q.append(node.right)
        
        return res

            
        