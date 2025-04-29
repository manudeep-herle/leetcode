from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        # Each item in the q has the node, the row and the column it's at
        q = deque()
        q.append((root, 0, 0))
        mem = defaultdict(lambda: [])
        res = []
        if root:
            while q:
                (node, row, col) = q.popleft()
                mem[col].append(node.val)
                if node.left:
                    q.append((node.left, row + 1, col - 1))
                if node.right:
                    q.append((node.right, row + 1, col + 1))
            
            cols = mem.keys()
            small, big = min(mem.keys()), max(mem.keys())

            for col in range(small, big+1):
                res.append(mem[col])
        return res
            