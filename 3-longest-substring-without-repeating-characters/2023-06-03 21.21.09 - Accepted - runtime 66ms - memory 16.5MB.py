class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0 
        curr = ""
        maxx = ""
        l = 0
        for c in s:
            if c in curr:
                if len(curr) > len(maxx):
                    maxx = curr
                curr = curr[curr.index(c)+1:] + c
            else:
                curr += c
        
        if len(curr) > len(maxx):
            maxx = curr


        return len(maxx)