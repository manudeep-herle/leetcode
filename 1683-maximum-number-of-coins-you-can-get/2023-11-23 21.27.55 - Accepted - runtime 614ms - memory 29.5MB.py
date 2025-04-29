from heapq import heapify, heappop 
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles = [-p for p in piles]
        heapify(piles)
        for i in range(len(piles)//3):
            heappop(piles)
            res += -1 * heappop(piles)
        return res
        