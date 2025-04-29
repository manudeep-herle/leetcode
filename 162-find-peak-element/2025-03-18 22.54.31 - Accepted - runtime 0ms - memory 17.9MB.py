class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n - 1
        # binary search
        while l <= r:
            mid = (l+r) // 2
            left_elem = nums[mid - 1] if mid > 0 else -float('inf')
            right_elem = nums[mid + 1] if mid < n-1 else -float('inf')
            # num[mid] can be 4 things:
            # peak - return
            if left_elem < nums[mid] and nums[mid] > right_elem:
                return mid
            # ascent - go right
            if left_elem < nums[mid] and nums[mid] < right_elem:
                l = mid + 1
            # descent - go left
            # valley - go left
            else:
                r = mid - 1
        
        return -1
