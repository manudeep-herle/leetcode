class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        i = 1
        while i < len(nums):
            if nums[i] == nums[i-1]:
                count += 1
                if count > 2:
                    while i < len(nums) and nums[i] == nums[i-1]:
                        nums.pop(i)
                else:
                    i += 1
            else:
                count = 1
                i += 1

        return