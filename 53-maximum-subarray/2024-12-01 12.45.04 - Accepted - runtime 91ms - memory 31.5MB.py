class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = curSum = -float('inf')
        for num in nums:
            curSum = max(num, curSum + num)
            maxSum = max(curSum, maxSum)

        return maxSum