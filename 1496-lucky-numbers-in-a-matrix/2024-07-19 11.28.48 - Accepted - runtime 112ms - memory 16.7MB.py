class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        mins = [float('inf')] * ROWS
        maxs = [-float('inf')] * COLS

        for i in range(ROWS):
            for j in range(COLS):
                mins[i] = min(mins[i], matrix[i][j])
                maxs[j] = max(maxs[j], matrix[i][j])
        res = []
        for num in mins:
            if num in maxs:
                res.append(num)

        return res