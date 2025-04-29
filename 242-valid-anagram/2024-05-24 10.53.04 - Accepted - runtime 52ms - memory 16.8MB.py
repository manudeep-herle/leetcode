from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(t) != len(s):
            return False
            
        countS = Counter(s)
        for c in t:
            if c not in countS or countS[c] == 0:
                return False
            else:
                countS[c] -= 1

        return True
        
        