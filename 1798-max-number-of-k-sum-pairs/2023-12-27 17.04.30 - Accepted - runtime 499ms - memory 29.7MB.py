class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0, len(nums) - 1
        res = 0
        while l < r:
            sum = nums[l] + nums[r]
            if sum == k:
                l += 1
                r -= 1
                res += 1
            elif sum < k:
                l += 1
            else:
                r -= 1 
        return res
        