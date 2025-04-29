class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res = 0
        minp = maxp = None
        start = 0
        # Sliding window, 4 pointers - start, minp, maxp, end
        for end, num in enumerate(nums):
            if num < minK or num > maxK:
                start = end + 1
                minp = maxp = None
            if num == minK:
                minp = end
            if num == maxK:
                maxp = end
            if minp != None and maxp != None:
                # Count the number of subarrays possible with this window
                res += min(minp, maxp) - start + 1

        return res
                


        
        