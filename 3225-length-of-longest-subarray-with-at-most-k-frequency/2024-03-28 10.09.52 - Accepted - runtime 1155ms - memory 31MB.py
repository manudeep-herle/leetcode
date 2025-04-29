class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l = 0
        res = 0
        counts = {}
        for r, num in enumerate(nums):
            if num not in counts:
                counts[num] = 0
            counts[num] += 1
            while counts[num] > k:
                counts[nums[l]] -= 1
                l += 1
            res = max(res, r-l+1) 
        
        return res