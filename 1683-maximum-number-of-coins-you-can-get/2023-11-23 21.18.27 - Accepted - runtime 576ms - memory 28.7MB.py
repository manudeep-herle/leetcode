from heapq import heapify, heappop 
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort(key = lambda x: -x)
        l,r = 0, len(piles)
        while l < r:
            l += 1
            res += piles[l]
            l += 1
            r -= 1
        return res

        