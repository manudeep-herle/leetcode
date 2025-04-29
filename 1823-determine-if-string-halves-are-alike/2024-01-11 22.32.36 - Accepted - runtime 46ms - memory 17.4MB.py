class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        l, r = 0 , len(s)//2
        L,R = 0,0
        VOWELS = ("a", "e", "i", "o", "u")
        while r < len(s):
            if s[l].lower() in VOWELS:
                L += 1
            if s[r].lower() in VOWELS:
                R += 1
            l += 1
            r += 1
        return L == R
        