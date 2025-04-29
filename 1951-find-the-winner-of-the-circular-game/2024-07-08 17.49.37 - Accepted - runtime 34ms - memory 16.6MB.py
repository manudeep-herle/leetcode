class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        mem = [i for i in range(1, n+1)]
        i = 0

        while len(mem) > 1:
            i += (k-1)
            i %= len(mem)
            mem.pop(i)
        
        return mem[0]
        