class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        sq = 0
        l,r = 0, len(nums) - 1
        for i in range(len(nums) -1, -1, -1):
            if abs(nums[r]) > abs(nums[l]):
                sq = nums[r]
                r -= 1
            else:
                sq = nums[l]
                l += 1
            res[i] = sq * sq
        return res

        
        