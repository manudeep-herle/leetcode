class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        if len(grid[0]) == 1:
            return 0
        pre1, pre2 = grid[0].copy(), grid[1].copy()
        for i in range(1, len(pre1)):
            pre1[i] += pre1[i-1]
            pre2[i] += pre2[i-1]
        
        res = min(pre1[-1] - pre1[0], pre2[-2])
        for i in range(1, len(pre1) - 1):
            res = min(res, max(pre1[-1] - pre1[i], pre2[i-1]))
        
        return res

        