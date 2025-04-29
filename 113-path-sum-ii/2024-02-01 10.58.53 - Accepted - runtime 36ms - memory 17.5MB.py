# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if not root:
            return res
        def dfs(node, curSum, path):
            path.append(node.val)
            curSum += node.val
            if curSum == targetSum and not (node.left or node.right):
                res.append(path.copy())
                return
            if node.left:
                dfs(node.left, curSum, path)
                path.pop()
            if node.right:
                dfs(node.right, curSum, path)
                path.pop()
        dfs(root, 0, [])            
        return res

        