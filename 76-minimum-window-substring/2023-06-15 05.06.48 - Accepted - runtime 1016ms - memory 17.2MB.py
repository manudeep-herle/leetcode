class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l,r = 0,0
        
        if len(t) > len(s): return ""
        
        res_l, res = float("inf"), ""
        missing = {}

        for i in range(len(t)):
            missing[t[i]] = missing.get(t[i], 0) + 1
        
        def checkMissing(m):
            for key in m:
                if m[key] > 0:
                    return True
            return False

        while r < len(s) or l < len(s):
            if checkMissing(missing) and r < len(s):
                if s[r] in missing:
                    missing[s[r]] -= 1
                r += 1
            
            if not checkMissing(missing) or r >= len(s):
                if not checkMissing(missing) and r - l - 1 < res_l: 
                    res_l = r - l - 1
                    res = s[l:r] 

                if s[l] in t:
                    missing[s[l]] = missing.get(s[l], 0) + 1

                l += 1
            
        return res

            
            