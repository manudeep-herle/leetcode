class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0
        visited = set()


        def bfs(i,j):
            q = deque()
            q.append([i,j])
            area = 0

            while len(q):
                [r,c] = q.popleft()
                if (r,c) in visited:
                    continue
                visited.add((r,c))
                area += 1

                dirs = [[r+1, c], [r-1, c], [r, c+1], [r, c-1]]
                
                for [r,c] in dirs:
                    if r >= 0 and c >= 0 and r < ROWS and c < COLS and grid[r][c] == 1:
                        q.append([r,c])

            return area
                

        
        # Iterate through the grid
        for i in range(ROWS):
            for j in range(COLS):
                if (i,j) not in visited and grid[i][j]: 
                    # Do BFS on encountering a 1
                    area = bfs(i,j) 
                    if area > max_area:
                        max_area = area

        
        return max_area