from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rsCounter = Counter(ransomNote)
        mCounter = Counter(magazine)

        for key in rsCounter.keys():
            if mCounter[key] < rsCounter[key]:
                return False

        return True


        