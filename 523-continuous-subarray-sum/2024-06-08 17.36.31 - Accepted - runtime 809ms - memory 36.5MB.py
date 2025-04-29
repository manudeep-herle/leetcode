class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mem = {0:-1}
        prefixMod = 0

        for i, num in enumerate(nums):
            prefixMod = (prefixMod + num) % k
            if prefixMod in mem:
                if i - mem[prefixMod] > 1:
                    return True
            else:
                mem[prefixMod] = i
        return False
        