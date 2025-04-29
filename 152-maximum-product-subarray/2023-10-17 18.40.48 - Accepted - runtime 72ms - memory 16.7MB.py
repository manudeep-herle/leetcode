class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minSoFar = 0
        maxSoFar = 0
        res = -float('inf')
        for num in nums:
            if num >= 0:
                maxSoFar = max(num, maxSoFar * num)
                minSoFar = min(num, minSoFar * num)
            else:
                maxSoFar_ = maxSoFar
                maxSoFar = max(num, minSoFar * num)
                minSoFar = min(num, maxSoFar_ * num)

            if maxSoFar > res:
                res = maxSoFar
        
        return res if len(nums) > 1 else nums[0]



        