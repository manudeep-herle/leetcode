class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0
        
        for num in nums:
            if num -1 not in nums:
                curr = num
                streak = 1
                while curr + 1 in nums:
                    curr += 1
                    streak += 1
                res = max(res, streak)
        
        return res
                
        