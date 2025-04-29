# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from functools import wraps

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def memoize(func):
            cache = {}

            @wraps(func)
            def wrapper(*args, **kwargs):
                if args not in cache:
                    cache[args] = func(*args, **kwargs)
                return cache[args]
            return wrapper
            
        def rec_solve(n1, n2):
            @memoize    
            def depth(node):
                if node == None:
                    return 0
                else:
                    return (1 + max(depth(node.left), depth(node.right)))

            if abs(depth(n1) - depth(n2)) <= 1:
                if n1 != None and n2 != None:
                    return rec_solve(n1.left, n1.right) and rec_solve(n2.left, n2.right)
                else:
                    return True
            else:
                return False 
            
        if root == None:
            return True
        return rec_solve(root.left, root.right)
                

                