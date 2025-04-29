import math

class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i*i for i in range(1, 101)]
        mem = {}

        def recurse(target):
            if target == 0:
                return 0
            ret = float('inf')
            if target not in mem: 
                for sq in squares:
                    if sq > target:
                        break
                    ret = min(recurse(target- sq) + 1, ret)
                mem[target] = ret
            return mem[target]



        return recurse(n)