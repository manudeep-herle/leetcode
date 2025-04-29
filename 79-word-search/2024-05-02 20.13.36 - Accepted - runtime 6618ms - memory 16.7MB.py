class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R,C = len(board), len(board[0])
        def backtrack(r, c, i, visited):
            if (r,c) in visited or board[r][c] != word[i]:
                return False
            if i == len(word) - 1:
                return True
            res = False
            visited.append((r, c))

            for [r_, c_] in [[r+1,c], [r, c+1], [r-1,c], [r,c-1]]:
                if r_ >= 0 and r_ < R and c_ >= 0 and c_ < C:
                    res = res or backtrack(r_, c_, i+1, visited)
            visited.pop()
            return res

        for r in range(R):
            for c in range(C):
                res = backtrack(r,c, 0, [])      
                if res:
                    return True
        return False


        