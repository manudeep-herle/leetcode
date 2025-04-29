class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        i = 0

        while i < len(nums):
            anchor = nums[i]
            while i+1 < len(nums) and nums[i]+1 == nums[i+1]:
                i += 1
            if nums[i] == anchor:
                res.append(str(nums[i]))
            else:
                res.append(str(anchor)+"->"+str(nums[i]))
            
            i += 1
        
        return res
        