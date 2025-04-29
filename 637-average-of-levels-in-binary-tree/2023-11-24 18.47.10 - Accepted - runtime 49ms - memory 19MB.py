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
                res.append(curSum/ total)
                curSum = processed = 0
                total = len(q)
            node = q.popleft()
            processed += 1
            curSum += node.val 

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(curSum/ total)


        return res