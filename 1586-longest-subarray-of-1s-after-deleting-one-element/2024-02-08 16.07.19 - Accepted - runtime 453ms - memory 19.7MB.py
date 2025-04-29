class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        l = r = 0
        res = -1
        zeroFlag = False if nums[0] == 1 else True
        prevZero = None if nums[0] == 1 else 0
        while r < len(nums)-1:
            r += 1
            if nums[r] == 0:
                if zeroFlag:
                    res = max(res, r-1-l)
                    l = prevZero + 1
                else:
                    zeroFlag = True
                prevZero = r
        
        return max(res, r-l)
            
            
        