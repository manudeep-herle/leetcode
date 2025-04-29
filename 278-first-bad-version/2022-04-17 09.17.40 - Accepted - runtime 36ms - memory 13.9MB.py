# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        f=1
        l=n
        m=int((f+l)/2)
        curr_b = -1
        while f<=l:
            # if f == l or f > l:
            #     if isBadVersion(f):
            #         curr_b = f
            #     break
            if isBadVersion(m):
                curr_b = m
                l=m-1
                m=int((f+l)/2)
            else:
                f=m+1
                m=int((f+l)/2)
        return(curr_b)