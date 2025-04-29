class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        leftTotal = 0
        for i in range(len(nums)):
            if (total - nums[i]) / 2 == leftTotal:
                return i
            leftTotal += nums[i]

        return -1
        