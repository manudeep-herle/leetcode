class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for start in range(len(s)):
            # Odd palindrome
            l,r = start,start
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1
            # Even palindrome
            l,r = start, start+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res


        