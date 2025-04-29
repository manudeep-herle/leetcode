class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mem = {}
        curLen = 0
        res = 0
        for i,c in enumerate(s):
            if c in mem and mem[c] >= i - curLen:
                curLen = i - mem[c]
            else:
                curLen += 1
            mem[c] = i
            res = max(curLen, res)
        return res
