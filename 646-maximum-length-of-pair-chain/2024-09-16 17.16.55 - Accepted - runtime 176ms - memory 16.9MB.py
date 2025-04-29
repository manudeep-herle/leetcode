class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs = sorted(pairs, key = lambda pair: pair[1])
        curEndTime = -float('inf')
        res = 0
        for pair in pairs:
            if pair[0] > curEndTime:
                res += 1
                curEndTime = pair[1]
            
        return res