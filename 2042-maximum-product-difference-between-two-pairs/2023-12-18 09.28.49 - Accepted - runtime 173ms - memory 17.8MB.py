class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        b1,b2, s1,s2 = 0,0,10000,10000
        for num in nums:
            if num > b1:
                b1,b2 = num, b1
            elif num > b2:
                b2 = num
            if num < s1:
                s1,s2 = num, s1
            elif num < s2:
                s2 = num
        return b1*b2 - s1*s2