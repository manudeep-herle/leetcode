import numpy as np

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.res = 0
        self.ROWS, self.COLS = len(grid), len(grid[0])
        self.visited = np.zeros((self.ROWS,self.COLS))
        self.grid = grid
        
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.grid[i][j] == "1" and not self.visited[i][j]:
                    isIsland = self.backtrack(i,j)
                    if isIsland:
                        self.res += 1
        
        return self.res
        

    
    def backtrack(self,i,j):
        # If this box is out of bounds or if has been visited we good.
        if i < 0 or j < 0 or i >= self.ROWS or j >= self.COLS or self.visited[i][j] or self.grid[i][j] != "1":
            return True
        else:
            self.visited[i][j] = 1
        # Check left and right and top and bottom
        return self.backtrack(i-1, j) and self.backtrack(i+1, j) and self.backtrack(i, j-1) and self.backtrack(i, j+1)
      

        