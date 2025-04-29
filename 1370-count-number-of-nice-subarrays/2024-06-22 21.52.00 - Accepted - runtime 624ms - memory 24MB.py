from collections import defaultdict

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [1 if num % 2 else 0 for num in nums]
        mem = defaultdict(int)
        prefixS = res = 0
        for num in nums:
            mem[prefixS] += 1
            prefixS += num
            if prefixS-k in mem:
                res += mem[prefixS-k]
        return res
          