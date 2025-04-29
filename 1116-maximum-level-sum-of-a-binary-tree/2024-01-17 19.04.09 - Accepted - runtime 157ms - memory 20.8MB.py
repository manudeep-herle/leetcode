from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Do a BFS with level seperation
        q = deque()
        q.append(root)
        levelSize = len(q)
        level = 0
        levelSum = 0
        res = -float('inf')
        resLevel = -1
        while q:
            node = q.popleft()
            levelSize -= 1

            if node:
                levelSum += node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if levelSize == 0:
                levelSize = len(q)
                if levelSum > res:
                    resLevel = level
                    res = levelSum
                levelSum = 0
                level += 1
        return resLevel + 1


        