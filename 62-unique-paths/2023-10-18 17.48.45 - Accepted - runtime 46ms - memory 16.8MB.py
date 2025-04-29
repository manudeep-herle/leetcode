class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visited = [([False]*n) for _ in range(m)] 
        print(visited)
        
        @cache
        def explore(r,c):
            # Base cases 
            if r == m-1 and c == n-1:
                return 1
            visited[r][c] = True

            dirs = [(r+1,c), (r,c+1)]
            total = 0

            for (i,j) in dirs:
                if i >= m or j >= n:
                    continue
                total += explore(i,j)
            return total

        return explore(0,0) 