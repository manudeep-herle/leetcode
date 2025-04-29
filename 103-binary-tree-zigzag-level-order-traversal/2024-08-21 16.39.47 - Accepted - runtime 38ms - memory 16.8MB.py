from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque() # active nodes
        q.append(root)
        levelLen = 1 # the number of nodes in each level
        ltor = True # Determines the direction in which node values are added to temp array
        temp = deque() # temp array to store node values at each level
        res = [] 
        while q:
            node = q.popleft()
            if ltor:
                temp.append(node.val)
            else:
                temp.appendleft(node.val)
            levelLen -= 1
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
            if levelLen == 0:
                ltor = not ltor # change direction
                levelLen = len(q)
                res.append(temp.copy()) # add temp to res
                temp = deque() # clear temp
        return res
            



        