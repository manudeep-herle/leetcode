class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ("a", "e", "i", "o", "u")
        l,r = 0, 0
        curVowels = 1 if s[0] in vowels else 0
        maxVowels = curVowels

        while r < len(s) - 1:

            if r - l == k - 1:
                if s[l] in vowels:
                    curVowels -= 1
                l += 1

            r += 1
            if s[r] in vowels:
                curVowels += 1
            
            maxVowels = max(curVowels, maxVowels)
        
        return maxVowels


            


        