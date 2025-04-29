class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        f,l = 0, len(nums)-1
        while f <= l:
            mid = (f+l) //2
            # Check if nums[mid] is the peak
            if mid == len(nums) - 1:
                if nums[mid - 1] < nums[mid]:
                    return mid
                else:
                    l = mid - 1
            elif mid == 0:
                if nums[mid + 1] < nums[mid]:
                    return mid
                else:
                    f = mid + 1
            else:
                if nums[mid - 1] < nums[mid] > nums[mid+1]:
                    return mid
                elif nums[mid - 1] > nums[mid]:
                    l = mid-1
                else:
                    f = mid + 1

        return -1