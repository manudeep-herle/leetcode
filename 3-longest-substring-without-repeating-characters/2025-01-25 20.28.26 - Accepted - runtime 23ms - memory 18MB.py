class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxStringSize = 0
        currWindowChars = set()

        for r in range(len(s)):
            if s[r] in currWindowChars:
                while s[l] != s[r]:
                    currWindowChars.remove(s[l])
                    l += 1
                currWindowChars.remove(s[l])
                l += 1
            currWindowChars.add(s[r])
            maxStringSize = max(maxStringSize, r-l + 1)
        
        return maxStringSize
        