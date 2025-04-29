import numpy as np

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        res = 0

        def bfs(i,j):
            q = deque()

            q.append((i,j))
            visited.add((i,j))

            directions= [[1,0],[-1,0],[0,1],[0,-1]]

            while q:
                i,j = q.popleft()

                for dr,dc in directions:
                    r,c = i + dr, j + dc
                    if (r) in range(ROWS) and (c) in range(COLS) and grid[r][c] == '1' and (r ,c) not in visited:
                        q.append((r , c ))
                        visited.add((r, c ))
                


        
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j] == "1":
                    bfs(i,j)
                    res += 1
        return res


        