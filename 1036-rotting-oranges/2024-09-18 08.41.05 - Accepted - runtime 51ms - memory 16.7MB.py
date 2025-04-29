from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rottenQ = deque()
        visited = set()
        rottenCount = freshCount = 0
        # Add all rotten oranges to the deque
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    visited.add((r,c))
                    rottenQ.append((r,c))
                    rottenCount += 1
                elif grid[r][c] == 1:
                    freshCount += 1

        time, levelLen = 0, len(rottenQ)
        while rottenQ:
            [r,c] = rottenQ.popleft()
            levelLen -= 1
            for [r_, c_] in [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]:
                if r_ < 0 or r_ == ROWS or c_ < 0 or c_ == COLS or (r_ , c_) in visited:
                    continue
                if grid[r_][c_] == 1:
                    grid[r_][c_] = 2
                    visited.add((r_, c_))
                    rottenQ.append((r_, c_))
            if levelLen == 0:
                time += 1
                levelLen = len(rottenQ)
        
        orangeCount = (rottenCount + freshCount)
        if not orangeCount:
            return 0
        elif len(visited) == orangeCount:
            return time - 1
        return -1
            

                
                
