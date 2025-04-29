class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        backSteps = 0

        for i in range(len(nums)-2, -1, -1):
            backSteps -= 1
            # Can jump from number source to the destination, make this number the new destination
            if backSteps + nums[i] >= 0:
                backSteps = 0
        
        return backSteps >= 0



        