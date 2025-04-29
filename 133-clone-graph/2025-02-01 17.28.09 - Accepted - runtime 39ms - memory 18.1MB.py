"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Traverse the graph through a recursive function visit()
        # Create new nodes for children of a node and store it in cloneMap
        # Keep track of nodes which have already been visited in a visited set
        cloneMap = {}
        visited = set()



        def visit(node):
            if node in visited:
                return
            for neighbor in node.neighbors:
                if neighbor.val not in cloneMap:
                    cloneMap[neighbor.val] = Node(neighbor.val)
                cloneMap[node.val].neighbors.append(cloneMap[neighbor.val])
            visited.add(node)
            for neighbor in node.neighbors:
                visit(neighbor)
        if not node:
            return
        cloneMap[node.val] = Node(node.val)
        visit(node)
        
        return cloneMap[1]