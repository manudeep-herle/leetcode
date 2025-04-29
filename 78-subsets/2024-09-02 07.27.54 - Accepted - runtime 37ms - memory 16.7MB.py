class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def recurse(subArr, i):
            if i == len(nums):
                res.append(subArr)
                return
            recurse(subArr + [nums[i]], i + 1) #add a number to subarray    
            recurse(subArr, i + 1)  #skip to the next number
        
        recurse([], 0)
        return res
        