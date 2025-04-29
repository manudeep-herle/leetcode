class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        def check(arr):
            l, g = min(arr), max(arr)
            diff = (g - l) / (len(arr) - 1)
            arrSet = set(arr)
            curr = l
            while curr < g:
                curr += diff
                if curr not in arrSet:
                    return False
            return True
        
        for l,r in zip(l,r):
            res.append(check(nums[l:r+1]))
        return res