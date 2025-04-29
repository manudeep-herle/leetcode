from collections import defaultdict, deque
from heapq import heapify, heappush, heappop
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        minPrices = [float('inf')] * n
        minPrices[src] = 0
        # Build graph
        for [s, d, price] in flights:
            graph[s].append((d, price))

        # BFS
        level = 0
        nodesInLevel = 1
        q = deque()
        q.append([src, 0])
        while q and level <= k:
            [node, curPrice] = q.popleft()
            nodesInLevel -= 1
            print(node, curPrice, level) 
            for [neigh, price] in graph[node]:
                if curPrice + price < minPrices[neigh]:
                    minPrices[neigh] = curPrice + price
                    q.append([neigh, minPrices[neigh]])
            
            if nodesInLevel == 0:
                nodesInLevel = len(q)
                level += 1

        return minPrices[dst] if minPrices[dst] < float('inf') else -1




        