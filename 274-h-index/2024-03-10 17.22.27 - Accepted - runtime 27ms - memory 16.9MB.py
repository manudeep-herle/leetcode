class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        res = 0
        n = len(citations)
        for i in range(len(citations)):
            if n - i <= citations[i]:
                res = max(n-i, res)
        return res 
        