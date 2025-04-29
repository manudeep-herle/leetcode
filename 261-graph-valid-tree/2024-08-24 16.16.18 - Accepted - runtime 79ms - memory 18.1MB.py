from collections import defaultdict

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        if len(edges) != n-1:
            return False

        # Build adjacency list
        for [start, end] in edges:
            adj_list[start].append(end)
            adj_list[end].append(start)
        
        print(adj_list)
        seen = set()
        q = [0]
        while q:
            node = q.pop()
            seen.add(node)
            for child in adj_list[node]:
                if child in seen:
                    continue
                q.append(child)
        return len(seen) == n
            
        


        