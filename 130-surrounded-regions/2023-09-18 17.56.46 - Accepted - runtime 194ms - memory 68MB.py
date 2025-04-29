class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        os = set()
        visited = set()
        ROWS, COLS = len(board), len(board[0])
        
    # DFS when you run into a o
        def dfs(i,j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS: # We've hit a wall oops.
                return False
            if board[i][j] == 'X' or (i,j) in visited:
                return True
            visited.add((i,j))
            os.add((i,j))
            b,t,r,l = dfs(i+1, j), dfs(i-1, j), dfs(i,j+1), dfs(i,j-1)
            return b and t and r and l

        def capture(os):
            for [i,j] in os:
                board[i][j] = 'X'


        # Iterate through the board
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 'O' and (i,j) not in visited:
                    surrounded = dfs(i,j)
                    if surrounded:
                        # Update o's to x's from the os set
                        capture(os)
                    else:
                        # clear os
                        os.clear()



        
        # if you hit a wall return false Else add this index to to_be_changed and return true
        