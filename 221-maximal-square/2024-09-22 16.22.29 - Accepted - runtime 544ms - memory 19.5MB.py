class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[0] * COLS for _ in range(ROWS)]
        res = 0
        # Base case
        r = ROWS - 1
        for c in range(COLS-1, -1, -1):
            if matrix[r][c] == '1':
                cache[r][c] = 1 
                res = 1
            else: cache[r][c] = 0
        c = COLS - 1
        for r in range(ROWS-1, -1, -1):
            if matrix[r][c] == '1':
                cache[r][c] = 1 
                res = 1
            else: cache[r][c] = 0        
        if ROWS > 1 and COLS > 1:
            for r in range(ROWS-2, -1, -1):
                for c in range(COLS-2, -1, -1):
                    if matrix[r][c] == "1":
                        cache[r][c] = min(cache[r+1][c], cache[r+1][c+1], cache[r][c+1]) + 1
                        res = max(cache[r][c], res)
        return res*res

        

        

