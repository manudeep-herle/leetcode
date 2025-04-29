# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res = [0]
        hmap = {}

        def dfs(node, curSum):
            if not node:
                return
            curSum += node.val
            
            if curSum == targetSum:
                print(curSum, targetSum)
                res[0] += 1
            if curSum - targetSum in hmap:
                print(curSum, targetSum)
                res[0] += hmap[curSum - targetSum]

            hmap[curSum] = hmap.get(curSum, 0) + 1
            
            dfs(node.left, curSum)
            dfs(node.right, curSum)

            hmap[curSum] -= 1
        
        dfs(root, 0)

        return res[0]
        