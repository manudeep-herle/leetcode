from heapq import heapify, heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        mem = [0] * n
        mem[0] = 1
        next2, next3, next5 = 2, 3, 5
        index2, index3, index5 = 0, 0, 0
        for i in range(1, n):
            next = min([next2, next3, next5])
            mem[i] = next
            if next == next2:
                index2 += 1
                next2 = mem[index2] * 2
            if next == next3:
                index3 += 1
                next3 = mem[index3] * 3          
            if next == next5:
                index5 += 1
                next5 = mem[index5] * 5
        print(mem)
        return mem[-1]
        # # Track the cur ugly numbers in a minheap and a set
        # uglyNumbersHeap = [1]
        # uglyNumbersSet = set(uglyNumbersHeap)
        # # To multiple the current smallest ugly number by 2,3 and 5 till we process the nth ugliest number
        # for i in range(1, n + 1):
        #     curSmall = heappop(uglyNumbersHeap)
        #     uglyNumbersSet.discard(curSmall)

        #     for j in [2,3,5]:
        #         if curSmall * j not in uglyNumbersSet:
        #             heappush(uglyNumbersHeap, curSmall * j)
        #             uglyNumbersSet.add(curSmall * j)

        # return curSmall