from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.rootToStart = self.rootToDest = None
        self.startValue, self.destValue = None, None

    def dfs(self, node, path):
        if not self.rootToStart or not self.rootToDest:
            if node.val == self.startValue:
                self.rootToStart = path.copy()
            elif node.val == self.destValue:
                self.rootToDest = path.copy()

            if node.left:
                path.append('L')
                self.dfs(node.left, path)
                path.pop()

            if node.right:
                path.append('R')
                self.dfs(node.right, path)
                path.pop()

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.startValue, self.destValue = startValue, destValue
        self.dfs(root, deque())

        # Delete common path
        for e1, e2 in zip(list(self.rootToStart), list(self.rootToDest)):
            if e1 != e2:
                break
            else:
                self.rootToStart.popleft()
                self.rootToDest.popleft()
        
        # Delete root to start
        for i in range(len(self.rootToStart)):
            self.rootToStart[i] = 'U'

        return "".join(list(self.rootToStart + self.rootToDest))