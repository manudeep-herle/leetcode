class Solution:
    def minSwaps(self, s: str) -> int:
        imbalance = 0
        curSum = 0
        for c in s:
            if c == "]":
                curSum -= 1
                if curSum == -1:
                    imbalance += 1
                    curSum = 0
            elif c == "[":
                curSum += 1
        res = imbalance // 2
        if imbalance % 2:
            res += 1
        return res

