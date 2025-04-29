from functools import lru_cache

class Solution:
    def __init__(self):
        self.nums = None

    def rob(self, nums: List[int]) -> int:
        self.nums = nums
        return max(self.recurse(0), self.recurse(1))

    @lru_cache
    def recurse(self, i):
        if i >= len(self.nums):
            return 0
        return self.nums[i] + max(self.recurse(i+2), self.recurse(i+3))


        