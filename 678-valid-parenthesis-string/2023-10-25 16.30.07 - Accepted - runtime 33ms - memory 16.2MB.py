class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for c in s:
            if c == ")":
                lo -= 1
                hi -= 1
            elif c == "(":
                lo += 1
                hi += 1
            elif c =="*":
                lo -= 1
                hi += 1
            lo = max(0, lo)
            if hi < 0:
                return False 
        if 0 in range(lo, hi+1):
            return True
        return False