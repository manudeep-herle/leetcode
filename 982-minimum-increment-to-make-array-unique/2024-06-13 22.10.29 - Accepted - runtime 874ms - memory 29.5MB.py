from heapq import heappush
class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        maxheap = [1]

        for num in nums:
            prev = - heappop(maxheap)
            if num <= prev:
                diff = (1 + (prev - num))
                num += diff
                res += diff
            heappush(maxheap, -num)
            heappush(maxheap, -prev)
            
        return res

                
