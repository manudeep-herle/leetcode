class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l,r = 0, k-1
        maxSum = curSum = sum(nums[l:r+1])
        while r < len(nums) - 1:
            r += 1
            curSum = curSum + nums[r] - nums[l]
            l += 1
            maxSum = max(curSum, maxSum)
        
        return maxSum / k

        