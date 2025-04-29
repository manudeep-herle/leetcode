class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        res = 0
        for g in gain:
            cur += g
            res = max(res, cur)
        return res
        