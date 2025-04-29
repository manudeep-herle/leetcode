class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        mem = [([1] + [0]*(amount)) for _ in range(len(coins)+1)]

        for i in range(1, len(coins)+1):
            for j in range(1, amount+1):
                mem[i][j] = mem[i-1][j]
            for j in range(coins[i-1], amount+1):
                mem[i][j] = mem[i-1][j] + mem[i][j - coins[i-1]]

        return mem[-1][-1]
        