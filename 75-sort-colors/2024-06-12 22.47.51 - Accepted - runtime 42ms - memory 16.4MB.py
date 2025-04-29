class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        c = 0

        while c <= r:
            if nums[c] == 0:
                nums[c], nums[l] = nums[l], nums[c]
                l += 1
                c += 1
            elif nums[c] == 2:
                nums[r], nums[c] = nums[c], nums[r] 
                r -= 1
            else:
                c += 1
        
        return nums
