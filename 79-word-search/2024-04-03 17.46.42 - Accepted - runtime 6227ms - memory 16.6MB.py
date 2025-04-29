class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = []
        R,C,W = len(board), len(board[0]), len(word)
        def recurse(r, c, i):
            if word[i] == board[r][c]:
                if i == W-1:
                    return True
                visited.append((r,c))
                for [r,c] in [[r+1, c], [r-1, c], [r,c+1], [r, c-1]]:
                    if r < 0 or r >= R or c < 0 or c >= C or (r,c) in visited:
                        continue
                    else:
                        res = recurse(r, c, i+1)
                        if res:
                            return res
                visited.pop()
                return False



        for r in range(R):
            for c in range(C):
                res = recurse(r,c, 0)
                if res:
                    return True
        return False


            