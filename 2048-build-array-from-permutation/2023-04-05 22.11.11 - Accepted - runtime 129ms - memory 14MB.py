class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        i = 0
        for (num) in nums:
            ans.append(nums[num])
        return ans