class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        COLS = len(grid[0])
        ROWS = len(grid)
        @cache
        def dp(r,c1,c2):
            if c1<0 or c2<0 or c1>=COLS or c2>= COLS:
                return -float('inf')
            if  r >= ROWS:
                return 0
            res = 0
            if c1 != c2:
                res = grid[r][c1] + grid[r][c2]
                print(res)
            else:
                res = grid[r][c1]
            
            m = res + max(dp(r+1, c1, c2), dp(r+1, c1-1, c2-1), dp(r+1,c1+1, c2+1), dp(r+1, c1, c2-1), dp(r+1, c1, c2+1), dp(r+1, c1-1, c2), dp(r+1, c1+1, c2), dp(r+1, c1+1, c2-1), dp(r+1, c1-1, c2+1))
     
            return m
        

        res = dp(0, 0, COLS-1)
        return res



        