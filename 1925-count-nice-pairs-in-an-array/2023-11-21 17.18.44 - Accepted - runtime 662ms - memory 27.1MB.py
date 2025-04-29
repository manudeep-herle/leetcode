class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            res = 0
            while num:
                r = num % 10
                num = num // 10
                res = res * 10 + r
            return res
        
        res = 0
        hmap = {}
        for num in nums:
            diff = num - rev(num)
            if diff in hmap:
                res += hmap[diff]
                hmap[diff] += 1
            else:
                hmap[diff] = 1

        return res % (10**9 + 7)