class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        fresh_count = [0]
        rotten = set() # Contains all rotten oranges for this iteration
        newly_rotten = set()
        minutes = [0]
        # spread()
        def spread():
            # In every iteration, spread the rot to all adjacent oranges of the already rotten oranges
            for [i,j] in rotten:
                dirs = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]
                for [i,j] in dirs:
                    if i >= ROWS or i< 0 or j >= COLS or j< 0 or grid[i][j] != 1:
                        continue
                    else:
                        grid[i][j] = 2
                        newly_rotten.add((i,j))
                        fresh_count[0] -= 1
            
            if not newly_rotten:
                return 
            # Clean up - replace rotten with newly rotten oranges, clear newly rotten oranges, update minutes 
            rotten.clear()
            rotten.update(newly_rotten)
            newly_rotten.clear()
            minutes[0] += 1        
            spread()

        
        # Find positions of rotting oranges
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotten.add((i,j))
                elif grid[i][j] == 1:
                    fresh_count[0] += 1
        # Pass initial positions to spread()
        spread()

        if fresh_count[0] == 0:
            return minutes[0]
        else:
            return -1