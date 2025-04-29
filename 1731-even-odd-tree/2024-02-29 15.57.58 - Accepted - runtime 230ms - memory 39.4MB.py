from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque()
        arr = []
        q.append(root)
        levellen = 1
        while q:
            node = q.popleft()
            arr.append(node.val)
            levellen -= 1
            if levellen == 0:
                arr.append(None)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            if levellen == 0:
                levellen = len(q)
        even = False
        prev = -float('inf')
        for i in range(0, len(arr)):
            if arr[i] == None:
                if even:
                    even = False
                    prev = -float('inf')
                else:
                    even = True
                    prev = float('inf')
                continue
            if even:
                if arr[i] % 2 or arr[i] >= prev:
                    return False
            else:
                if arr[i] % 2 == 0 or arr[i] <= prev:
                    return False
            prev = arr[i]
        return True
        