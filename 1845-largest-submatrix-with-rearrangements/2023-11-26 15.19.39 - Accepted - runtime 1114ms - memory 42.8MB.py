class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        for c in range(len(matrix[0])):
            prev = 0
            for r in range(len(matrix)):
                if matrix[r][c]: matrix[r][c] += prev
                prev = matrix[r][c]
        
        res = 0
        for row in matrix:
            row.sort(key = lambda x: -x)
            for c,val in enumerate(row):
                res = max(res, (c+1) * val)

        return res
        