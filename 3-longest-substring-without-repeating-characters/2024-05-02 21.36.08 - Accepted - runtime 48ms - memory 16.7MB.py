class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        present = {}
        res = 0
        for r, c in enumerate(s):
            if c in present and present[c]:
                while s[l] != c:
                    present[s[l]] -= 1
                    l += 1
                present[c] -= 1
                l += 1
            present[c] = 1
            res = max(res, r-l+1)
        
        return res
        