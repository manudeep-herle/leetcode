from heapq import heapify, heappush, heappop
class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        first, last = [float('inf')], [float('inf')]
        i = 0
        costs = deque(costs)
        for i in range(min(candidates, len(costs))):
            cost = costs.popleft()
            heappush(first, cost)
        
        for i in range(min(candidates, len(costs))):
            cost = costs.pop()
            heappush(last, cost)

        res = 0
        cost = None
        for round in range(k):
            if first[0] <= last[0]:
                c = heappop(first)
                res += c
                if costs:
                    cost = costs.popleft()
                else:
                    cost = float('inf')  
                heappush(first, cost)
            else:
                c = heappop(last)
                res += c
                if costs:
                    cost = costs.pop()
                else:
                    cost = float('inf')
                heappush(last, cost)
        return res
    