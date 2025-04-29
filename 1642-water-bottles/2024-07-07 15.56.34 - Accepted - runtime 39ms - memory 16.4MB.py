class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = numBottles
        emptyBottles = 0
        while numBottles:
            numBottles += emptyBottles
            emptyBottles = numBottles % numExchange
            numBottles = numBottles // numExchange
            res += numBottles

        return res
        