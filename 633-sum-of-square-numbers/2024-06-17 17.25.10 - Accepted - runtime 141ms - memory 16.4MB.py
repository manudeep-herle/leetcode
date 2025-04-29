class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for a in range(0, int(sqrt(c)) + 1):
            b = c - a*a
            if(sqrt(b) % 1 == 0):
                return True
        return False
        