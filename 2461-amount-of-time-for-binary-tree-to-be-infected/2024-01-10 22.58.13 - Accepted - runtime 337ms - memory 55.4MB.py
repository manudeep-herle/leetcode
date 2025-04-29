from collections import deque 
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        q = deque()
        q.append(root)
        graph = {root.val: []}
        res = 0
        while q:
            node = q.pop()
            if node:
                if node.right:
                    graph[node.val].append(node.right.val)
                    q.append(node.right)
                    if node.right.val not in graph:
                        graph[node.right.val] = []
                    graph[node.right.val].append(node.val)
                if node.left:
                    graph[node.val].append(node.left.val)
                    q.append(node.left)
                    if node.left.val not in graph:
                        graph[node.left.val] = []
                    graph[node.left.val].append(node.val)
        
        visited = set()
        visited.add(start)
        q.append(start)
        levelSize = 0
        while q:
            if levelSize == 0:
                levelSize = len(q)
                res += 1
            par = q.popleft()
            levelSize -= 1
            for node in graph[par]:
                if node not in visited:
                    visited.add(node)
                    q.append(node)
        
        return res-1


        
            

        