class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        mem = [1] * len(nums)
        res = 1
        for i in range(1, len(nums)):
            for j in range(i-1, -1, -1):
                if nums[j] < nums[i]:
                    mem[i] = max(mem[j]+1, mem[i])

                    if mem[i] > res:
                        res = mem[i]

        print(mem)
        return res


        