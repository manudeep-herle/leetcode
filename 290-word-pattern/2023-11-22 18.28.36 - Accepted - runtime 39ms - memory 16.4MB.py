class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        hmap1, hmap2 = {}, {}
        if len(s) != len(pattern):
            return False

        for i,c in enumerate(pattern):
            if c not in hmap1 and s[i] not in hmap2:
                hmap1[c] = s[i]
                hmap2[s[i]] = c
            elif c in hmap1 and s[i] in hmap2:
                if hmap1[c] == s[i] and hmap2[s[i]] == c:
                    continue
                else:
                    return False
            else:
                return False

        return True 


        
        