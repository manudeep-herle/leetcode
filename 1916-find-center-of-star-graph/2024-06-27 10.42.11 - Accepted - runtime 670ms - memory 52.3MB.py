class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        [n1, n2] = edges[0]
        return n1 if n1 in edges[1] else n2
        