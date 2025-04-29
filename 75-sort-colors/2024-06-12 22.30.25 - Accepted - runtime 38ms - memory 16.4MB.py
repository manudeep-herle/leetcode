from collections import Counter
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = Counter(nums)
        for i in range(len(nums)):
            if counts[0]:
                nums[i] = 0 
                counts[0] -= 1
            elif counts[1]:
                nums[i] = 1
                counts[1] -= 1
            else:
                nums[i] = 2
        return nums