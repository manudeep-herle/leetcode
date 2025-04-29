class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            if nums[0] > nums[1]:
                return nums[1]
            else:
                return nums[0]

        # Find point at which the list peaks
        l, r = 0, len(nums) - 1
        ans = float("inf")

        while l <= r:
            mid = int((l+r) / 2)
            ans = min(ans, nums[mid])

            # if mid is the highest
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1 

        return ans




















































        



