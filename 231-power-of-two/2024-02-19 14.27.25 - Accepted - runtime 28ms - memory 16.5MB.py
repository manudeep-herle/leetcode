class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        mul = 1
        while mul < n:
            mul = mul * 2
            if mul == n:
                return True
        return False

        