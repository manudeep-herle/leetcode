class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        l,r = 0, len(nums)-1
        while l < r:
            mid = (l+r) //2

            if nums[mid + 1] > nums[mid]:
                l = mid + 1
            else:
                r = mid

        return l