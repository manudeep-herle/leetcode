
class Solution:
    def arrange(self, t: int, o: int) -> int:
        return factorial(t+o)/ (factorial(o) * factorial(t))
    def climbStairs(self, n: int) -> int:
        ways = 0
        t = int(n/2)
        o = n - t * 2
        while t >= 0:
            ways = ways + self.arrange(t,o)
            t = t-1
            o = o+2
        return int(ways)