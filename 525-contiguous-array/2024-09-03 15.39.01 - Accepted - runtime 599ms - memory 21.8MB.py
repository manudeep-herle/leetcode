class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hmap = {0:-1}
        curSum = 0
        res = 0
        for i,num in enumerate(nums):
            if num:
                curSum += 1
            else:
                curSum -= 1
            if curSum in hmap:
                res = max(res, i-hmap[curSum])
            else:
                hmap[curSum] = i
        return res

        