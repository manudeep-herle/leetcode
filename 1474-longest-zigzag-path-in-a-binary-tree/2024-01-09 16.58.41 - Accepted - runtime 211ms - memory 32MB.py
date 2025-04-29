# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        def dfs(node, curLen, nextDir):
            lLen = rLen = curLen
            if node.right:
                newLen = curLen + 1 if nextDir == "r" else 1
                rLen = dfs(node.right, newLen, "l")
            if node.left:
                newLen = curLen + 1 if nextDir == "l" else 1
                lLen = dfs(node.left, newLen, "r")
            res = max(lLen, rLen)
            return res
        return max(dfs(root, 0, "r"), dfs(root, 0, "l"))


        