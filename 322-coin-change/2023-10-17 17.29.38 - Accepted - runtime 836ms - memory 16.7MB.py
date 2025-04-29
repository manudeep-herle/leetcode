class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf')] * (amount + 1)
        mem[0] = 0

        for coin in coins:
            for amt in range(coin, amount + 1):
                mem[amt] = min(mem[amt], mem[amt - coin] + 1)

        return mem[-1] if mem[-1] < float('inf') else -1