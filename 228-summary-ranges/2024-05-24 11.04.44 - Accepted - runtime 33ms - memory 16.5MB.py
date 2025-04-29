class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [str(nums[0])]
            
        res = []
        l = 0
        for r in range(1,len(nums)):
            if nums[r] > nums[r-1]+1:
                if l == r-1:
                    res.append(str(nums[l]))
                else:
                    res.append(str(nums[l])+"->"+str(nums[r-1]))
                l = r

        if l == r:
            res.append(str(nums[l]))
        else:
            res.append(str(nums[l])+"->"+str(nums[r]))
        
        return res
        