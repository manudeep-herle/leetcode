class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @cache
        def countWaysToTarget(i, curSum):
            res = 0
            if i == len(nums):
                if curSum == target:
                    return 1
                else:
                    return 0
            
            res += countWaysToTarget(i+1, curSum + nums[i])
            res += countWaysToTarget(i+1, curSum - nums[i])
        
            return res
                
        return countWaysToTarget(0, 0)

        