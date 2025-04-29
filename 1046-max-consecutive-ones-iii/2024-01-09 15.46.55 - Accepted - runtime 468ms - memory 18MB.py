class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, r = 0, -1
        flipsLeft = k
        cur = res = 0
        while r < len(nums)- 1:
     
            r += 1
            if nums[r] == 0 and flipsLeft > 0:
                cur += 1
                flipsLeft -= 1
            elif nums[r] == 1:
                cur += 1
            elif nums[r] == 0 and flipsLeft == 0:
                while l < r and nums[l] == 1:
                    l += 1
                    cur -= 1
                if l < r:
                    l += 1
            if cur == 0:
                    l += 1
            res = max(cur, res)
        return res


        