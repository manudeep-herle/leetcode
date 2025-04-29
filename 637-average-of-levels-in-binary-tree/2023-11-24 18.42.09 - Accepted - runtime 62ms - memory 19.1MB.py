# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q = deque()
        q.append(root)
        processed, total = 0, 1
        curSum = 0
        res = []
        while q:
            if total == processed:
                print(curSum, total)
                res.append(curSum/ total)
                curSum = 0
                total = len(q)
                processed = 0

            node = q.popleft()
            
            if node:  
                processed += 1
                curSum += node.val 
                q.append(node.left)
                q.append(node.right) 
            else:
                total -= 1

        return res