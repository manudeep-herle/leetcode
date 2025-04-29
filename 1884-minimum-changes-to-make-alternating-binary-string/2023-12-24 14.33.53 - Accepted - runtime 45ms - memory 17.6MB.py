class Solution:
    def minOperations(self, s: str) -> int:
        invert = {"1": "0", "0": "1"}
        # Starts with 0
        curChar0, res0 = "0", 0
        # Starts with 1
        curChar1, res1 = "1", 0
        for c in s:
            if c != curChar0:
                res0 += 1
            curChar0 = invert[curChar0]

            if c != curChar1:
                res1 += 1
            curChar1 = invert[curChar1]

        return min(res0, res1)       