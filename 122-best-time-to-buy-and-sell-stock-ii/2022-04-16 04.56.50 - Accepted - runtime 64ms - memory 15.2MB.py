class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        profit = 0
        while r<len(prices):
            if prices[r]>prices[l]:
                profit += prices[r]-prices[l]
            r +=1
            l +=1

                
        print(profit)
        return profit
