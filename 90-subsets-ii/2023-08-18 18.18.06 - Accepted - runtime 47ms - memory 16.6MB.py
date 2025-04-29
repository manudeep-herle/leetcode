class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(curr, nums):
            if not nums:
                return [sorted(curr)]
            return solve(curr, nums[1:]) + solve(curr + [nums[0]], nums[1:]) 

        ans =  solve([], nums)
        res = []
        for li in ans:
            temp = tuple(li)
            if temp not in res:
                res.append(temp)
        return res