class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]

        def dp(nums):
            mem = [0] * len(nums)
            mem[0] = nums[0]
            if len(nums) > 1: mem[1] = max(mem[0], nums[1])
            
            # go from 1st house to last but one
            # go from 2nd house to last house
            for i in range(2, len(nums)):
                mem[i] = max(mem[i-1], mem[i-2] + nums[i])
            return mem[-1]
        return max(dp(nums[1:]), dp(nums[0:-1]))