"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        duplicate = {}
        if not node:
            return None

        # Create a node clone with all it's neigbors
        def clone(node):

            if node in duplicate:
                return duplicate[node]

            copy = Node(node.val)
            duplicate[node] = copy

            for neigh in node.neighbors:
                copy.neighbors.append(clone(neigh))

            return copy

        
        return clone(node)
            



        