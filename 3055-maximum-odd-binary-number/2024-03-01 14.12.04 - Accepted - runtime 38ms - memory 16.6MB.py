from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        counts = Counter(s)
        res = ""
        res = res + "1"*min(1, counts["1"])
        res = "0"*counts["0"] + res
        res = "1" * max(0, counts["1"] - 1) + res
        return res 
        