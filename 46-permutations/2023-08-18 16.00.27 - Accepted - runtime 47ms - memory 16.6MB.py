class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        
        def dfs(curr, nums):
            if not nums:
                ans.append(curr)
            for i in range(0, len(nums)):
                curr.append(nums[i])
                dfs(curr.copy(), nums[0:i]+nums[i+1:])
                curr.pop()

        dfs([], nums)
        return ans
