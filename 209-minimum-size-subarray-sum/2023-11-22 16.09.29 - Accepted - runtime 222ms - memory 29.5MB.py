class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        currSum = nums[0]
        if currSum >= target:
            return 1
        res = float('inf')
        while r < len(nums)-1:
            r += 1
            currSum += nums[r]
            while currSum >= target:
                res = min(res, r-l+1)
                currSum -= nums[l]
                l += 1
        return res if res < float('inf') else 0
                


        