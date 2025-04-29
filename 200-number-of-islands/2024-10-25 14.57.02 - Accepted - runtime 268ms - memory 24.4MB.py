class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # For each unvisited cell that is a 1, mark it as visited, do a dfs
        # explore the whole island
        def dfs(r,c):
            visited.add((r,c))
            # check all neighbors of cell at r,c
            for [r_,c_] in [[r+1,c], [r-1, c], [r, c+1], [r,c-1]]:
                if r_ < 0 or r_ >= ROWS or c_ < 0 or c_ >= COLS:
                    continue
                elif grid[r_][c_] == "1" and (r_, c_) not in visited:
                    dfs(r_,c_)
            return

        # visited grid
        visited = set()
        ROWS, COLS = len(grid), len(grid[0])
        res = 0
        # Go through the grid row by row Col by col
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    res += 1
                    dfs(r,c)
        
        return res
