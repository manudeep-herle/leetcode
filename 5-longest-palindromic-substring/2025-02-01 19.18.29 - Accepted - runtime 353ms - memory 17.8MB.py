class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(n2)
        # go through s, assume each char/ ind to be midpoint of a palindrome, 
        # expand on either side till characters on edge match and we don't go out of bound
        # if r-l + 1 > resR - resL + 1, resR = r, resL = l
        resR = resL = 0
        for i in range(len(s)):
            l = r = i
            while (l-1) >= 0 and (r+1) < len(s) and s[l-1] == s[r+1]:
                l -= 1
                r += 1
            if (r-l+1) > (resR - resL + 1):
                resR = r
                resL = l

            if i > 0 and s[i] == s[i-1]:
                l = i - 1
                r = i
                while (l-1) >= 0 and (r+1) < len(s) and s[l-1] == s[r+1]:
                    l -= 1
                    r += 1
                if (r-l+1) > (resR - resL + 1):
                    resR = r
                    resL = l
        
        return s[resL: resR+1]
