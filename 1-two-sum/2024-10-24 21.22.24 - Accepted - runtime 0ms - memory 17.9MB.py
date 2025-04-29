class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, curNum in enumerate(nums):
            if target - curNum in mem:
                return [mem[target - curNum], i]
            mem[curNum] = i
        return [-1, -1]
        