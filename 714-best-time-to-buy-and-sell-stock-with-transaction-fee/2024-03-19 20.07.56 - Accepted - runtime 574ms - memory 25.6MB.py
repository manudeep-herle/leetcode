class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        mem = [[-prices[0],0]]
        for price in prices[1:]:
            curStep = [0,0]
            prevStep = mem[-1]
            curStep[0] = max(prevStep[0], prevStep[1]-price)
            curStep[1] = max(prevStep[1], prevStep[0]+price - fee)
            mem.append(curStep)

        return mem[-1][1]
        