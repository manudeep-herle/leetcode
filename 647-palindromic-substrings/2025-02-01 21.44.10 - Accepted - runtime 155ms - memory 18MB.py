class Solution:
    def countSubstrings(self, s: str) -> int:
        res = [0]
        def expand(l,r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res[0] += 1
                l -= 1
                r += 1
            
        for i in range(len(s)):
            expand(i, i)
            expand(i-1, i)
        
        return res[0]




            