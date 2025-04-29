from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        print(stones)
        while len(stones) > 1:
            fheavy, sheavy = heappop(stones), heappop(stones)
            if fheavy - sheavy:
                heappush(stones, fheavy - sheavy)
        if stones:
            return -stones[0]
        else:
            return 0