from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        
        # Check if there are equal numbers for each character
        c1, c2 = Counter(word1), Counter(word2)
        c1, c2 = sorted(c1.values()), sorted(c2.values())
        return(c1 == c2)
        return False 
        