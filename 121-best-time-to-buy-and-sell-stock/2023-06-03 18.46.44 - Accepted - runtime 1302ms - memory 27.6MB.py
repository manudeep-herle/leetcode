class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = [x for x in prices]
        h = [x for x in prices]

        for i in range(1, len(prices)):
            l[i] = min(l[i], l[i-1])
            h[-i -1] = max(h[-i -1], h[-i])
        maxx = 0
        for i in range(0, len(prices)):
            if h[i] - l[i] > maxx:
                maxx = h[i] - l[i]
        return maxx
        