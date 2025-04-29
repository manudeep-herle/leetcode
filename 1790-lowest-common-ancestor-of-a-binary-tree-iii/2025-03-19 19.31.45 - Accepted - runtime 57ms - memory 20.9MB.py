"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # for each input node, traverse to the parent
        # keep track of path to parent in a list
        # compare ancestor_list for both input nodes, first matching node is the lca
        def traverse(node, path):
            while node and node.parent:
                path.append(node)
                node = node.parent
            path.append(node) # the root needs to be added to the path as well
        
        pathp, pathq = [], []
        traverse(p, pathp)
        traverse(q, pathq)

        
        for nodep in pathp:
            for nodeq in pathq:
                if nodep.val == nodeq.val:
                    return nodep

        return -1
