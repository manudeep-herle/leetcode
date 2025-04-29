class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastPos = {}
        for i, char in enumerate(s):
            lastPos[char] = i
        
        curCount = biggestLastPos = 0
        res = []

        for i in range(len(s)):
            biggestLastPos = max(biggestLastPos, lastPos[s[i]])
            curCount += 1
            if i == biggestLastPos:
                res.append(curCount)
                curCount = 0
        return res
            