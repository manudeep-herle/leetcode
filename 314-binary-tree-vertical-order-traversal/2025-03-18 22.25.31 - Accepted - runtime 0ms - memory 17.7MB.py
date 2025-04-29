from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        data = defaultdict(list)
        q = deque()
        q.append((root, 0))
        while q:
            [node, col] = q.popleft()
            if not node: 
                continue
            data[col].append(node.val)
            q.append((node.left, col-1))
            q.append((node.right, col+1))
        res = []
        cols = data.keys()
        for col in range(min(cols), max(cols)+1):
            res.append(data[col])
        
        return res