class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p = 0
        res = ""
        for c in word1:
            res += c
            if p < len(word2):
                res += word2[p]
                p += 1
        if p < len(word2):
            res += word2[p:]
        return res
        