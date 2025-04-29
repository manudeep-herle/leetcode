class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        l = 0
        curProd = 1
        res = 0
        for r in range(len(nums)):
            curProd *= nums[r]
            while curProd >= k and l < r:
                curProd = curProd / nums[l]
                l += 1
            if curProd < k:
                res += r-l+1
        
        return res


            
        