class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        def traverse(r,c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or grid[r][c] == "0" or (r,c) in visited:
                return
            visited.add((r,c))
            traverse(r+1, c)
            traverse(r, c+1)
            traverse(r-1, c)
            traverse(r, c-1)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    traverse(r,c)

        return islands



        