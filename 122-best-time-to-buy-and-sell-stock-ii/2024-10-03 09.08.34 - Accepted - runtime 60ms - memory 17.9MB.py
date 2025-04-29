class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) > 2:
            buyPrice = prices[0]
            for i in range(1, len(prices)):
                buyPrice = min(buyPrice, prices[i])
                if (i == len(prices) - 1 or prices[i] >= prices[i+1]) and prices[i] > prices[i-1]:
                    profit += prices[i] - buyPrice
                    buyPrice = float('inf')
        elif len(prices) > 1:
            if prices[0] < prices[1]:
                return prices[1] - prices[0]

        return profit
        