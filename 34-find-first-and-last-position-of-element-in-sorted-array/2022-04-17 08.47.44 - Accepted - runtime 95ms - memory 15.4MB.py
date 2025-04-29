class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l = len(nums)
        if nums.count(target) < 1:
            return [-1,-1]
        start = i = nums.index(target)
        while i+1 < l and nums[i+1] == target:
            i += 1
        return(start,i)