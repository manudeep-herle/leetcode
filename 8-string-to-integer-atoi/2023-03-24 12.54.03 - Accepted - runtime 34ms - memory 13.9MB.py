import re

class Solution:
    def myAtoi(self, s: str) -> int:
        ul = 2**31 - 1
        ll = -2 ** 31 
        # Remove leading white spaces
        s = s.strip()
        m = re.match("\+[0-9]+|-[0-9]+|[0-9]+", s)
        if m:
            print(m[0])
            a = int(m[0]) 
            if a > ul:
                return ul
            elif a < ll:
                return ll
            return a
        else: 
            return 0