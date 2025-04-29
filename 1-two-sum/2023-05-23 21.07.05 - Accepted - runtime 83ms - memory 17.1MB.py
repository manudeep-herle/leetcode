class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sorted_nums = sorted(nums)
        l,r = 0, len(nums) - 1
        while l < r:
            if sorted_nums[l] + sorted_nums[r] == target:
                fi = nums.index(sorted_nums[l])
                nums[fi] = None
                return (fi, nums.index(sorted_nums[r]))
            elif sorted_nums[l] + sorted_nums[r] < target:
                l += 1
            else:
                r -= 1
        