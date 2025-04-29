class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for row in range(1, numRows):
            curRow = [1]
            for col in range(1, row):
                curRow.append(res[row-1][col-1] + res[row-1][col])
            curRow.append(1)
            res.append(curRow)
        return res



        