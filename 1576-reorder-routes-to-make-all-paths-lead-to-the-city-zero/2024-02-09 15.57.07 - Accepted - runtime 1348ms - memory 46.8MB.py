from collections import defaultdict, deque
class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        graph, revGraph = defaultdict(list), defaultdict(list)
        for con in connections:
            graph[con[0]].append(con[1])
            revGraph[con[1]].append(con[0])
        print(graph, revGraph)
        visited = set([0])
        q = deque()
        res = 0
        q.append(0)

        while q:
            node = q.popleft()
            for neigh in revGraph[node]:
                q.append(neigh)
                visited.add(neigh)    
            for neigh in graph[node]:
                if neigh not in visited:
                    q.append(neigh)
                    res += 1
                    visited.add(neigh)
                
        return res