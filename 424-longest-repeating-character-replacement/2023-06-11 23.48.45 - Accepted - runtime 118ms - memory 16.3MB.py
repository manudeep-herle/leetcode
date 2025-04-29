class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        b,f = 0,0
        hmap = {}
        maj = s[f]
        hmap[s[b]] = 1
        ws = 1
        maxws = ws

        while f < len(s) - 1 and b <= f:
            f += 1
            ws +=1

            hmap[s[f]] = hmap.get(s[f],0) + 1
            if hmap[s[f]] > hmap[maj]:
                maj = s[f]
            
            # Check if this window is valid
            if ws - hmap[maj] > k:
                ws -= 1
                hmap[s[b]] -= 1
                b += 1
            
            if ws > maxws:
                maxws = ws


        
        return maxws