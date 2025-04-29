class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nz = 0
        s = 0

        while s < len(nums):
            if nums[s] == 0:
                nz += 1
            elif nz:
                nums[s - nz] = nums[s]
                nums[s] = 0
            s += 1


        