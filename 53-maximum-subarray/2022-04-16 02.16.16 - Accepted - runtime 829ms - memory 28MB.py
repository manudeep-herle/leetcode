class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        max_so_far, curr_max = float('-inf'), float('-inf') 
        for num in nums:
            curr_max = max(curr_max+num, num)
            max_so_far = max(max_so_far,curr_max) 
        return max_so_far

            
        