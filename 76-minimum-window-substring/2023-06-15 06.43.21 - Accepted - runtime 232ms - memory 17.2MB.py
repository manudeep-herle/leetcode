class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""
        l,r = 0,0
        res_l, res = float("inf"), ""
        missing = {}
        need = 0

        for i in range(len(t)):
            missing[t[i]] = missing.get(t[i], 0) + 1
            need += 1

        while r + l < 2 * len(s):
            if need > 0 and r < len(s):
                if s[r] in missing:
                    if missing[s[r]] > 0: need -= 1
                    missing[s[r]] -= 1
                    
                r += 1
            
            if not need > 0 or r >= len(s):
                if not need and r - l - 1 < res_l: 
                    res_l = r - l - 1
                    res = s[l:r] 

                if s[l] in t:
                    if missing[s[l]] >= 0: need += 1
                    missing[s[l]] = missing.get(s[l], 0) + 1
                    

                l += 1
            
        return res

            
            