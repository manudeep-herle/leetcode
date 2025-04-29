class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSoFar = -float('inf')
        total = 0

        for num in nums:
            total += num
            if total > maxSoFar:
                maxSoFar = total
            if total < 0:
                total = 0

        return maxSoFar


        