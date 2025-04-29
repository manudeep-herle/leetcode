class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        mem = {0: -1}
        modPrefix = 0
        for i, num in enumerate(nums):
            modPrefix += num
            modPrefix %= k
            if modPrefix in mem:
                if i - mem[modPrefix] >= 2:
                    return True
            else:
                mem[modPrefix] = i
        return False