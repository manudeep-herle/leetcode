class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.COLS = len(matrix[0])
        self.ROWS = len(matrix)
        self.prefixMatrix = [[0] * self.COLS for _ in range(self.ROWS)]
        # self.prefixMatrix = matrix
        self.fillPrefix()

    def fillPrefix(self):
        colSum = [0] * self.COLS
        for r in range(self.ROWS):
            rowSum = 0
            for c in range(self.COLS):
                self.prefixMatrix[r][c] = self.matrix[r][c] + rowSum + colSum[c]
                rowSum = self.prefixMatrix[r][c]
                colSum[c] += self.matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        left = self.prefixMatrix[row2][col1 - 1] if col1 > 0 else 0
        top = self.prefixMatrix[row1 - 1][col2] if row1 > 0 else 0
        topleft = self.prefixMatrix[row1 - 1][col1 - 1] if (col1 > 0 and row1 > 0 )else 0
        return self.prefixMatrix[row2][col2] - left - top + topleft
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)