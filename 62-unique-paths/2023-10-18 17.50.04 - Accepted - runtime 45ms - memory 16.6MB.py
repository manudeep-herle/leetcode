class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def explore(i,j):
            # Base cases 
            if i >= m or j >= n:
                return 0
            if i == m-1 and j == n-1:
                return 1
            return explore(i+1, j) + explore(i,j+1)

        return explore(0,0) 