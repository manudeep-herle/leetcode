class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res = -1
        diff = [(gas[i] - cost[i]) for i in range(len(gas))]

        if sum(diff) < 0:
            return -1
        
        cumu = 0
        lastNeg = -1

        for i in range(len(diff)):
            cumu += diff[i]
            if cumu < 0:
                cumu = 0
                lastNeg = i
        return lastNeg+1 if lastNeg>-1 else 0