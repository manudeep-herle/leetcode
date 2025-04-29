class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        res = ""
        LEN = min(len(str1), len(str2))
        for i in range(LEN):
            if str1.count(str1[0:i+1]) * (i+1) == len(str1) and str2.count(str1[0:i+1]) * (i+1) == len(str2):
                res = str1[0:i+1]
        return res
        