# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        # BFS, last node in each level is a part of the output.
        q = collections.deque() # need to maintain fifo order
        q.append(1)
        q.append(root)
        out = []
        while q:
            node = q.popleft()
            if node == 1:
                if q:
                    out.append(q[-1].val)
                    q.append(1)
                continue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return out

