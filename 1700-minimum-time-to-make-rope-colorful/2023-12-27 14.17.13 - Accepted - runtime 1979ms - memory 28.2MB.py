class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        # Left to right, when there's consecutive same colors, remove one with smallest time
        i = 0
        while i < len(colors) - 1:
            if colors[i] == colors[i+1]:
                res += min(neededTime[i], neededTime[i+1])
                cur = max(neededTime[i], neededTime[i+1])
                i += 1
                while i < len(colors) - 1 and colors[i] == colors[i+1]:
                    res += min(cur, neededTime[i+1])
                    cur = max(cur, neededTime[i+1])
                    i += 1
            i += 1
        return res



        