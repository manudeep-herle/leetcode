class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        mem = []
        for r in range(m):
            mem.append([])
            for c in range(n):
                if c == n-1 or r == m-1:
                    mem[r].append(1)
                else:
                    mem[r].append(0)
        
        for r in range(m-2, -1, -1):
            for c in range(n-2, -1, -1):            
                mem[r][c] = mem[r+1][c] + mem[r][c+1]
        return mem[0][0] 