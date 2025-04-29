class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Non dp solution
        maxLen = 0
        maxStr = ""
        # Start from every point and extend both ways
        for start in range(len(s)):
            # Odd length
            l, r = start, start
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ssLen = r - l + 1
                if ssLen > maxLen:
                    maxLen = ssLen
                    maxStr = s[l:r+1]
                l -= 1
                r += 1
            # Even length
            l, r = start, start + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                ssLen = r - l + 1
                if ssLen > maxLen:
                    maxLen = ssLen
                    maxStr = s[l:r+1]
                l -= 1
                r += 1

        
        return maxStr
            
                