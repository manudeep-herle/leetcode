class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total/2 
        
        @cache
        def dfs(sum, i):
            # Base case
            if sum > target:
                return False
            elif sum == target:
                return True
            elif i >= len(nums):
                return False
    
            return dfs(sum+nums[i], i+1) or dfs(sum, i+1)

        return dfs(0,0)