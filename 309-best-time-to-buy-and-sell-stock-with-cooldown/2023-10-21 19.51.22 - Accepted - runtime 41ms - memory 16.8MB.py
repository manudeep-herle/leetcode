class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0 

        mem = [[0]*(len(prices)+1) for _ in range(3)]
        mem[1][0], mem[2][0] = -float('inf'), -float('inf')

        for j in range(1, len(prices)+1):
            mem[0][j] = max(mem[0][j-1], mem[2][j-1])
            mem[1][j] = max(mem[1][j-1], mem[0][j-1]-prices[j-1])
            mem[2][j] = mem[1][j-1] + prices[j-1]
        
        res = (max(mem[:][-1]))
  
        return max(res, 0)

   