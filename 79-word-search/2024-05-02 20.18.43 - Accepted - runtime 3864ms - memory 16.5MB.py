class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])
        def backtrack(r, c, i):
            if board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            res = False
            board[r][c] = "#"
            for [r_, c_] in [[r+1,c], [r, c+1], [r-1,c], [r,c-1]]:
                if r_ >= 0 and r_ < R and c_ >= 0 and c_ < C:
                    res = res or backtrack(r_, c_, i+1)
            board[r][c] = word[i]
            return res

        for r in range(R):
            for c in range(C):
                if backtrack(r,c, 0):
                    return True
        return False



