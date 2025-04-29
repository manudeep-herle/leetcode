class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {c:i for (i,c) in enumerate(s)}
        res = []

        anchor = end = 0
        for (i,c) in enumerate(s):
            end = max(end,lastIndex[c])

            if i == end:
                res.append(end-anchor+1)
                anchor = i+1

        return res