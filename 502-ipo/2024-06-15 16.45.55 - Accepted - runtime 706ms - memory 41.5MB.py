from heapq import heappush

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        possibleProfits = []
        projIndex = 0
        curCap = w
        projects = list(zip(capital, profits))
        projects.sort()

        for i in range(k):
            while projIndex < len(capital) and projects[projIndex][0] <= curCap:
                heappush(possibleProfits, -projects[projIndex][1])
                projIndex += 1
          
            if not possibleProfits:
                break
           
            curProfit = -heappop(possibleProfits)
            curCap += curProfit
        
        return curCap