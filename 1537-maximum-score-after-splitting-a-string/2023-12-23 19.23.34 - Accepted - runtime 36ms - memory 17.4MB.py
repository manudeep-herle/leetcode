class Solution:
    def maxScore(self, s: str) -> int:
        if len(s) == 2:
            if s[0] == "0" and s[1] == "1":
                return 2
            elif s[0] == "0" and s[1] == "0":
                return 1
            elif s[0] == "1" and s[1] == "1":
                return 1
            else:
                return 0

        l, r = 1, len(s)-2
        tracker = [[0]*2 for _ in range(len(s))]

        if s[0] == "0":
            tracker[0][0] = 1
        if s[-1] == "1":
            tracker[-1][1] = 1

        for _ in range(0, len(s) - 1):
            if s[l] == "0":
                tracker[l][0] = tracker[l-1][0] + 1
            else:
                tracker[l][0] = tracker[l-1][0]            
            
            if s[r] == "1":
                tracker[r][1] = tracker[r+1][1]+1
            else:
                tracker[r][1] = tracker[r+1][1]
            
            l += 1
            r -= 1

        res = 0

        for rec in tracker[1:len(tracker)-1]:
            res = max(rec[0]+rec[1], res)

        return res
        