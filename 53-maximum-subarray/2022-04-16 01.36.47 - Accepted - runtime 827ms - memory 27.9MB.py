class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        a, b = float('-inf'), float('-inf') 
        for num in nums:
            a, b = max(a,b), max(b+num, num)
        return max(a,b) 

            
        