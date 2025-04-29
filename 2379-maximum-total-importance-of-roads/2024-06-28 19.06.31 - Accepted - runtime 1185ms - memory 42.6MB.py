from collections import defaultdict

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = defaultdict(int)
        for [c1, c2] in roads:
            degrees[c1] += 1
            degrees[c2] += 1
        
        roadEnds = list(degrees.values())
        roadEnds.sort(reverse = True)
        res = 0
        for roadEnd in roadEnds:
            res += n * roadEnd
            n -= 1
        return res