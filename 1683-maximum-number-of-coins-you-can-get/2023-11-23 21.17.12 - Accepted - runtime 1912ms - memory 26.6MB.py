from heapq import heapify, heappop 
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        res = 0
        piles.sort(key = lambda x: -x)
        while piles:
            piles.pop(0)
            res += piles.pop(0)
            piles.pop()
        return res

        