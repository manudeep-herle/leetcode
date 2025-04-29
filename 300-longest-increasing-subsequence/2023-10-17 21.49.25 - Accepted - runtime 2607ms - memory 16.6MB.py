class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if j < mem[i] - 1:
                    break
                if nums[j] < nums[i]:
                    mem[i] = max(mem[j]+1, mem[i])
        print(mem)
        return max(mem)


        