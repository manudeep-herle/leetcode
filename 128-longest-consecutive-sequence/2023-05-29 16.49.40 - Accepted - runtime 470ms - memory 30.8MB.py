import array

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()

        a = 0
        curr_len = 0
        for i in range(len(nums)):
            curr_len += 1
            if curr_len > a:
                a = curr_len
            if i < len(nums) - 1:
                if nums[i + 1] == nums[i]:
                    curr_len -= 1
                elif nums[i] + 1 != nums[i + 1]:
                    curr_len = 0
 

        return a

