class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = [defaultdict(int) for _ in range(len(board))], [defaultdict(int) for _ in range(len(board[0]))] 
        boxes = [[defaultdict(int) for _ in range(len(cols)//3)] for _ in range(len(rows)//3)]
        for r in range(len(board)):
            for c in range(len(board[0])):
                val = board[r][c]
                if val != ".":
                    if rows[r][val] + cols[c][val] + boxes[r//3][c//3][val] > 0:
                        return False
                    else:
                        rows[r][val] = 1 
                        cols[c][val] = 1 
                        boxes[r//3][c//3][val] = 1
        return True
                    

        