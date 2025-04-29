class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        # Just move around 0s and 2s 
        l,r = 0, len(nums) - 1
        i = 0
        for i in range(0, len(nums)):
            while nums[i] == 0 and l < i:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
            i += 1
        for i in range(len(nums)):
            while nums[i] == 2 and i <= r:
                nums[r], nums[i] = nums[i], nums[r]
                r -= 1
            i += 1

        return 
