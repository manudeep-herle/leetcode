class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows = len(board[0]), len(board)
        visited = set()

        def rec(word, i, j):

                if not word:
                    return True
                
                if ((i,j) in visited or
                    i < 0 or i >= rows or j < 0 or j >= cols or
                    board[i][j] != word[0]):
                    return False
                
                visited.add((i,j))

                res = (rec(word[1:], i + 1, j ) or
                rec(word[1:], i - 1, j ) or
                rec(word[1:], i, j + 1 ) or
                rec(word[1:], i, j - 1 ))
                
                visited.remove((i,j))
        
                return res

        for i in range(rows):
            for j in range(cols):
                if rec(word, i, j):
                    return True
        
        return False
       