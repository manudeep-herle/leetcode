class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(matrix), len(matrix[0])
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                if j not in range(len(res)):
                    res.append([])
                
                res[j].append(matrix[i][j])
                        
        return res
        