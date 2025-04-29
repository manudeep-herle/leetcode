class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mem = collections.defaultdict(int)
        prefixSum = 0
        res = 0
        mem[0] = 1
        for num in nums:
            prefixSum += num
            if prefixSum - k in mem:
                res += mem[prefixSum - k]
            mem[prefixSum] += 1
        
        return res
        