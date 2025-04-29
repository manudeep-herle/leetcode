from collections import deque
import copy
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Find p and q
        plevel, qlevel = None, None
        pnode,qnode = None, None

        # BFS Traversal
        qu = deque([root])
        nodesleftinlevel = 1
        curlevel = 0
         
        while qu and not (qlevel and plevel):
            node = qu.popleft()
            nodesleftinlevel -= 1
            
            if node.val == p.val:
                plevel = curlevel
                pnode = copy.deepcopy(node)
            if node.val == q.val:
                qlevel = curlevel
                qnode = copy.deepcopy(node)
            if node.left:
                node.left.par = node
                qu.append(node.left)
            if node.right:
                node.right.par = node
                qu.append(node.right)    

            if nodesleftinlevel == 0:
                curlevel += 1
                nodesleftinlevel = len(qu)
        
        # Travel upwards
        while pnode.val != qnode.val:
            if plevel == qlevel:

                pnode = pnode.par
                qnode = qnode.par
            elif plevel > qlevel:
                pnode = pnode.par
                plevel -= 1
            elif qlevel > plevel:
                qnode = qnode.par
                qlevel -= 1      

        return pnode  
        
