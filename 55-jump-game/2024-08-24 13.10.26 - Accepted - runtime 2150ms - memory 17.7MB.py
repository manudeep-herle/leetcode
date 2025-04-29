class Solution:
    def canJump(self, nums: List[int]) -> bool:
        mem = [0] * len(nums)
        mem[-1] = 1

        for i in range(len(nums) - 2, -1, -1):
            j = nums[i] + i
            for k in range(i+1, min(j+1, len(nums))):
                if mem[k]:
                    mem[i] = 1
                    break
        return mem[0]