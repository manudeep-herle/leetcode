class Solution:
    def findMin(self, nums: List[int]) -> int:
        def checkSmallest(m):
            if m > 0 and m < len(nums) - 1:
                if nums[m] < nums[m+1] and nums[m] < nums[m-1]:
                    return True
            elif m == len(nums) - 1:
                if nums[m] < nums[m-1] and nums[m] < nums[0]:
                    return True
            elif m == 0:
                if nums[m] < nums[1] and nums[m] < nums[-1]:
                    return True
            return False
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l+r) // 2
            if checkSmallest(m):
                return nums[m]
            if nums[l] > nums[m]:
                r = m - 1
            elif nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1

