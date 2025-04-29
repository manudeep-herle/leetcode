class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossCounts = {}
        res = [[], []]
        for [winner, loser] in matches:
            if winner not in lossCounts:
                lossCounts[winner] = 0
            if loser not in lossCounts:
                lossCounts[loser] = 0
            lossCounts[loser] += 1
        
        for key in lossCounts:
            if lossCounts[key] == 0:
                res[0].append(key)
            elif lossCounts[key] == 1:
                res[1].append(key)
        res[0].sort()
        res[1].sort()
        return res
        