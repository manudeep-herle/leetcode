class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        indices = [i for i in range(0, len(nums))]
        indices = sorted(indices, key = lambda ind: nums[ind])
        small, res = float('inf'), -float('inf')
        for ind in indices:
            small = min(ind, small)
            res = max(res, ind - small)
        return res
