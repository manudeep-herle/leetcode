class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return min(nums)
        mid = n // 2
        if nums[mid] < nums[mid+1] and nums[mid] < nums[mid-1]:
            return nums[mid]
        if nums[mid] >= nums[0] and nums[mid] <= nums[-1]:
            return nums[0]
        elif nums[mid] > nums[-1]:
            return self.findMin(nums[mid+1:])
        else:
            return self.findMin(nums[0: mid])
        


        