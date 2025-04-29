class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        @cache
        def bottomUp(target, i):
            # Base case
            if i == 0 and (target == -nums[0] or target == nums[0]):
                return 1
            elif i == 0 or target > total or target < -total:
                return 0

            return bottomUp(target - nums[i], i-1) + bottomUp(target + nums[i], i-1)
        
        res = bottomUp(target, len(nums)-1)
        return res if nums[0] > 0 else res * 2
        