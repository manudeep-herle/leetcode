class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        minDiff = float('inf')

        if len(nums) <= 3:
            return 0

        for i in range(4):
            minDiff = min(minDiff, nums[n - 4 + i] - nums[i])
        return minDiff
