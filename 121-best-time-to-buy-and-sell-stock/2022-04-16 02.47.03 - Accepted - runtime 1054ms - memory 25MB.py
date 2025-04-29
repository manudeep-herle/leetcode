class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit > 0:
                right += 1
                if profit > max_profit: max_profit = profit
            else:
                left = right
                right += 1
        return max_profit
                
        