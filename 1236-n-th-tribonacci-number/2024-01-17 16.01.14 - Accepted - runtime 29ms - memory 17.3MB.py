class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache
        def recurse(num):
            if num <= 1:
                return num
            if num == 2:
                return 1
            return recurse(num-3) + recurse(num - 2) + recurse(num - 1) 
        return recurse(n)
        