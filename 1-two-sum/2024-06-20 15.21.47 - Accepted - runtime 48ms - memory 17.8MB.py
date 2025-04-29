class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mem = {}
        for i, num in enumerate(nums):
            if target - num in mem:
                return [mem[target - num], i]
            mem[num] = i
        
        