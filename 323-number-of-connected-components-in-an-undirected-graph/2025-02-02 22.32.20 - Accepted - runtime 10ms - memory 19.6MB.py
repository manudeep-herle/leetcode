from collections import defaultdict

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        for st, en in edges:
            adjList[st].append(en)
            adjList[en].append(st)
        
        visited = set()
        
        def dfs(node):
            if node in visited:
                return 0
            visited.add(node)
            for neigh in adjList[node]:
                dfs(neigh)
            return 1
        res = 0
        for node in range(n):
            res += dfs(node)
        
        return res
