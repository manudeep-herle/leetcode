class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        r,c, i = 0,0, 0
        res = 0
        for r in range(len(grid)):
            for c in  range(len(grid)):
                flag = True
                for i in range(len(grid)):
                    if grid[r][i] == grid[i][c]:
                        i += 1
                    else:
                        flag = False
                        break
                if flag:
                    res += 1
        return res
        