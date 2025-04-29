class Solution:
    def jump(self, nums: List[int]) -> int:
        @cache
        def getMinJumps(start):
            if start == len(nums) - 1:
                return 0
            elif start >= len(nums):
                return float('inf')
            minJumps = float('inf')
            for pos in range(start+1, start + nums[start] + 1):
                minJumps = min(minJumps, getMinJumps(pos))
            return 1 + minJumps

        return getMinJumps(0)
    
        