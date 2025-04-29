from heapq import heapify, heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # Track the cur ugly numbers in a minheap and a set
        uglyNumbersHeap = [1]
        uglyNumbersSet = set(uglyNumbersHeap)
        # To multiple the current smallest ugly number by 2,3 and 5 till we process the nth ugliest number
        for i in range(1, n + 1):
            curSmall = heappop(uglyNumbersHeap)
            uglyNumbersSet.discard(curSmall)

            for j in [2,3,5]:
                if curSmall * j not in uglyNumbersSet:
                    heappush(uglyNumbersHeap, curSmall * j)
                    uglyNumbersSet.add(curSmall * j)

        return curSmall