class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = [float('inf') for _ in range(amount + 1)]
        mem[0] = 0

        for amt in range(amount+1):
            for coin in coins:
                if amt-coin >= 0:
                    mem[amt] = min(mem[amt], mem[amt-coin] + 1)

        if mem[-1] < float('inf'):
            return mem[-1]
        else:
            return -1
















        # mem = [float('inf') for _ in range(amount + 1)]
        # res = -1

        # def dp(noCoins, i, amt):
        #     if amt > amount or i >= len(coins):
        #         return
        #     # If we have already have a smaller number of coins to reach this amount, break.
        #     if noCoins > mem[amt]:
        #         return
        #     # We have a new minimum
        #     mem[amt] = noCoins
        #     # Use coin at i
        #     dp(noCoins + 1, i, amt+coins[i])
        #     # Skip coin at i
        #     dp(noCoins, i + 1, amt)

        # dp(0, 0, 0)
        # res = mem[amount]
        # if res < float('inf'):
        #     return res
        # else:
        #     return -1