class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols, rows = len(board[0]), len(board)
        dirs = ['u', 'd', 'l', 'r']
        ans = [False]

        def rec(word, visited, i, j):
            if (i,j) not in visited and board[i][j] == word[0]:
                word = word[1:]
                if not word:
                    ans[0] = True
                    return
                
                visited.add((i,j))
                
                for dir in dirs:
                    i_,j_ = i,j
                    if dir == 'u':
                        i_ = i - 1
                    elif dir == 'd':
                        i_ = i + 1
                    elif dir == 'l':
                        j_ = j - 1
                    else:
                        j_ = j + 1
                    
                    if i_ < 0 or i_ >= rows or j_ >= cols or j_ < 0:
                        continue 

                    rec(word, visited.copy(), i_, j_ )
        
        for i in range(rows):
            for j in range(cols):
                rec(word, set(), i, j)
        return ans[0]