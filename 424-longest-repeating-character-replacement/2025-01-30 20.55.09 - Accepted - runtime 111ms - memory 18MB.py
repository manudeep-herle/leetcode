from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window
        # While increasing or decreasing the window, keep track of freq of every character
        # While increasing the window, keep track of the most freq character
        # increase window as long as no of non-most freq characters <= k, largest window throughout is the res
        counts = defaultdict(int)
        maxf = 0
        l = 0
        res = 0

        for r, char in enumerate(s):
            counts[char] += 1
            maxf = max(counts[char], maxf)

            while (r-l+1 - maxf) > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, r-l + 1)

        return res

        