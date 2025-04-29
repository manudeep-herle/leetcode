class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums.count(target) < 1:
            return [-1,-1]
        start = i = nums.index(target)
        while i<len(nums) and nums[i] == target:
            i += 1
        return(start,i-1)