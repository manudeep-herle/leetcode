class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) >= len(needle):
            for i,c in enumerate(haystack):
                l, r = i, 0 
                while haystack[l] == needle[r]:
                    r += 1
                    l += 1
                    if r ==len(needle):
                        return i
                    if l ==len(haystack):
                        return -1
        return -1
            
        