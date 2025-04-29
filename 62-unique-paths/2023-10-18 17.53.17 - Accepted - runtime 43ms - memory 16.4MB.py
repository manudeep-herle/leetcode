class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = [([None]*n) for _ in range(m)]

        def explore(i,j):
            # Base cases 
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            if mem[i][j] == None:
                mem[i][j] = explore(i+1, j) + explore(i,j+1)
            return mem[i][j]

        return explore(0,0) 