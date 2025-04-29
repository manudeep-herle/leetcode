class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def dfs(s, curr, nums):
            if s > target:
                return
            if s == target:
                ans.append(curr)
                return
            if nums:
                dfs(s + nums[0], curr.copy() + [nums[0]], nums[1:])
                i = 1
                c = len(nums)
                while i < c and nums[i] == nums[i - 1]:
                    i += 1
                dfs(s, curr.copy(), nums[i:])

        dfs(0, [], candidates)
        return ans
