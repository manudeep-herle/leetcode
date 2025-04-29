class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        res = ""
        LEN = min(len(word1), len(word2))
        while i < LEN:
            res += word1[i]
            res += word2[i]
            i += 1
        if i < len(word1):
            res += word1[i:]
        elif i < len(word2):
            res += word2[i:]
        return res
        