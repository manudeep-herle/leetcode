from heapq import heapify, heappush, heappop 
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        heapify(nums)
        i = len(nums) - k

        for j in range(0,i):
            heappop(nums)
        
        return heappop(nums)