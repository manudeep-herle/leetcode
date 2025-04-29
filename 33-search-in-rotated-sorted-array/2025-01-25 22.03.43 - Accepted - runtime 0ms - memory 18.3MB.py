class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # At least one side of m is strictly increasing.

        l, r = 0, len(nums) - 1

        while l <= r:
            print(l , r)
            m = (l + r) // 2
            if target == nums[m]:
                return m
            if nums[l] > nums[m]:
                # right side of m is sorted
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[r] < nums[m]:
                # left side of m is sorted
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target > nums[m] :
                    l = m + 1
                else:
                    r = m - 1
        return -1

                

        # find strictly increasing side first
        