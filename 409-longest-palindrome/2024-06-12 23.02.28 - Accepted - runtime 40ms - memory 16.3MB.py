from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        vals = counts.values()
        res, odd = 0, 0
        for val in vals:
            if val % 2 == 0:
                res += val
            else:
                if (val - 1) > 0:
                    res += (val - 1)
                odd = 1
        return res + odd