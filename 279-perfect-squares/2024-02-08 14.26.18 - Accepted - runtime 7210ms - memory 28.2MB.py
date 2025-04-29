import math

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, 101)]
        mem = {}
        @lru_cache
        def recurse(target):
            if target == 0:
                return 0
            ret = float('inf')
            if target in mem: 
                return mem[target]

            for sq in squares:
                if sq > target:
                    break
                ret = min(recurse(target- sq) + 1, ret)
            
            mem[target] = ret
            return ret



        return recurse(n)