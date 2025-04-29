class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost = [0] + cost
        mem = [0] * len(cost)
        mem[1] = cost[1]

        for i in range(2, len(mem)):
            mem[i] = min(mem[i-1], mem[i-2]) + cost[i]
        return min(mem[-1], mem[-2])
