class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # minimums until that point
        mins, low = [], float('inf')
        for price in prices:
            low = min(low, price)
            mins.append(low)
        res = 0
        for i in range(len(prices) - 1, -1, -1):
            res = max(res, prices[i] - mins[i])

        return res

        