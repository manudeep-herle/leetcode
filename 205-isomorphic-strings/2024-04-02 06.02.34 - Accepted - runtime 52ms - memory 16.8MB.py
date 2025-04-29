class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hmap = {}
        rhmap = {}
        for i in range(len(s)):
            if s[i] not in hmap and t[i] not in rhmap:
                hmap[s[i]] = t[i]
                rhmap[t[i]] = s[i]
            elif (s[i] in hmap) and (t[i] in rhmap) and hmap[s[i]] == t[i] and rhmap[t[i]] == s[i]:
                continue
            else:
                return False
        
        return True
        