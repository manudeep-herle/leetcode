class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        small, big = float('inf'), -float('inf')
        for num in nums:
            small = min(num, small)
            big = max(num, big)

        if big < 1:
            return 1
        
        nums = set(nums)
        for i in range(1, big + 2):
            if i not in nums and i > 0:
                return i