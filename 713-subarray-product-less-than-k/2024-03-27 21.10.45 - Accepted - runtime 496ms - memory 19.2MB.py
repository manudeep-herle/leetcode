class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        l = r = 0
        n = len(nums)
        curProd = 1
        res = 0
        while r < n:
            curProd *= nums[r]
            while curProd >= k:
                curProd //= nums[l]
                l += 1
            res += r - l + 1
            r += 1
        return res