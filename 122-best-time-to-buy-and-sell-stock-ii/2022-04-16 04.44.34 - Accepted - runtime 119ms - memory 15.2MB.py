class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r<len(prices):
            if prices[r]<prices[l]:
                l = r
                r += 1
            elif r == len(prices) - 1 and prices[r] >= prices[l]:
                profit += prices[r] - prices[l]
                r += 1
            elif prices[r+1] < prices[r]:
                profit += prices[r] - prices[l]
                l = r + 1
                r += 2
            else: r += 1
        print(profit)
        return profit
