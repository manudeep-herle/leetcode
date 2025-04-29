class Solution:
    def maxDepth(self, s: str) -> int:
        res = count = 0
        for c in s:
            if c == "(":
                count += 1
                res = max(count, res)
            elif c == ")":
                count -= 1

        return res
                     