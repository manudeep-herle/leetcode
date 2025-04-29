class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hmap = {}
        for c in magazine:
            hmap[c] = hmap.get(c, 0) + 1
        
        for c in ransomNote:
            if c in hmap and hmap[c] > 0:
                hmap[c] -= 1
            else:
                return False
        
        return True