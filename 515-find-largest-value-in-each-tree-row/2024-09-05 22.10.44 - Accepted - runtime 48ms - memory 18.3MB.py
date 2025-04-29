from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root:
            q = deque([root])
            nodesInLevel = 1
            largestInLevel = -float('inf')
            res = []
            while(q):
                node = q.popleft()
                if largestInLevel < node.val:
                    largestInLevel = node.val
                nodesInLevel -= 1 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if nodesInLevel == 0:
                    nodesInLevel = len(q)
                    res.append(largestInLevel)
                    largestInLevel = -float('inf')
            
            return res
            





        