from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        # demarcate nodes at different levels in the dq
        # add a split in the dq after the root node, from here on, whenever a split is encountered in the dq while popping,
        # add another split at the end after all the current nodes in the dq.
        dq = deque()
        SPLIT = "|"
        dq.append(root)
        dq.append(SPLIT)
        res = []
        curList = []
        while dq:
            node = dq.popleft()
            if node:
                if node == SPLIT:
                    dq.append(SPLIT)
                    if len(dq) == 1:
                        break
                    res.append(curList.copy())
                    curList = []
                    continue
                curList.append(node.val)
                dq.append(node.left)
                dq.append(node.right)
        return res

            
