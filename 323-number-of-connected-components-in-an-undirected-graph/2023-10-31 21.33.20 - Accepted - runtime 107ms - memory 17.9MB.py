class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for edge in edges:
            adjList[edge[0]].append(edge[1])
            adjList[edge[1]].append(edge[0])
        print(adjList)
        visited = set()
        q = []
        res = 0

        for node in range(n):
            if node in visited:
                continue
            else:
                q.append(node)
                res += 1
            while q:
                n = q.pop()
                visited.add(n)
                for neigh in adjList[n]:
                    if neigh not in visited:
                        q.append(neigh)
        
        return res
