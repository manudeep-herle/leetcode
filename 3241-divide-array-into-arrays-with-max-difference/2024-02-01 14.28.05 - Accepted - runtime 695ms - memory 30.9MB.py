class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            if nums[i+2] - nums[i] > k:
                return [] 
            res.append(nums[i:i+3])
            i += 3
        return res