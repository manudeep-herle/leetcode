class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        # Left to right, when there's consecutive same colors, remove one with smallest time
        curMax = 0
        for i in range(len(colors)):
            if i > 0 and colors[i] != colors[i-1]:
                curMax = 0
            res += min(curMax, neededTime[i])
            curMax = max(curMax, neededTime[i])
        return res



        