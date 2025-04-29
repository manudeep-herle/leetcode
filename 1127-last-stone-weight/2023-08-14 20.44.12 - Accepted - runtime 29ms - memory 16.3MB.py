import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-1 * s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            s1, s2 = -1 * heapq.heappop(stones),  -1 * heapq.heappop(stones)
            if s1 > s2:
                heapq.heappush(stones, -1 * (s1 - s2))
        
        if len(stones) == 1:
            return -1 * stones[0]
        
        return 0
            

