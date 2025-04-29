class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        minimum = float('inf')
        for price in prices:
            minimum = min(price, minimum)
            profit = max(profit, price - minimum)
        
        return profit
