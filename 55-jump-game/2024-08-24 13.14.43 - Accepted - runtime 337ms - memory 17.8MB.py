class Solution:
    def canJump(self, nums: List[int]) -> bool:
        lastGood = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            j = nums[i] + i
            if j >= lastGood:
                lastGood = i
        return lastGood == 0
        