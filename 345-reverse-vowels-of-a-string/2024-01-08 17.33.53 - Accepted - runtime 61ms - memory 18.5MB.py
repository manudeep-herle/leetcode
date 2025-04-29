class Solution:
    def reverseVowels(self, s: str) -> str:
        l,r = 0 , len(s) - 1
        VOWELS = ("a", "e", "i", "o", "u")
        s = list(s)
        while l < r:
            while l < r and s[l].lower() not in VOWELS:
                l += 1
            while l < r and s[r].lower() not in VOWELS:
                r -= 1
            
            if l < r:
                s[l],s[r] = s[r],s[l]
                l += 1
                r -= 1
        return "".join(s)