class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c, prevHeight, visited):
            if r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prevHeight or (r,c) in visited:
                return
            visited.add((r,c))
            dfs(r+1,c,heights[r][c], visited)
            dfs(r-1,c,heights[r][c], visited)
            dfs(r,c+1,heights[r][c], visited)
            dfs(r,c-1,heights[r][c], visited)


        for c in range(COLS):
            dfs(0, c, heights[0][c], pac)
            dfs(ROWS-1, c, heights[ROWS-1][c], atl)

        for r in range(ROWS):
            dfs(r, 0, heights[r][0], pac)
            dfs(r, COLS-1, heights[r][COLS-1], atl)

        return list(pac.intersection(atl))
