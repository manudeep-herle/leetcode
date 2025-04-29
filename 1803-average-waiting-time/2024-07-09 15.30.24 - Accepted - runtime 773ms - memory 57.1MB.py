class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        curTime = customers[0][0]
        totalWait = 0

        for [at, wt] in customers:
            curTime = max(curTime + wt, at + wt)
            totalWait += (curTime - at)

        return totalWait/ len(customers)
        