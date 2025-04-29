class Solution:
    def mySqrt(self, x: int) -> int:
        if(x==0):
            return 0
        if(x == 1):
            return 1
        if(x==2):
            return 1
        for i in range(1, int(x/2) + 2):
            if i * i == x:
                return i
            if i * i > x:
                return i - 1
        