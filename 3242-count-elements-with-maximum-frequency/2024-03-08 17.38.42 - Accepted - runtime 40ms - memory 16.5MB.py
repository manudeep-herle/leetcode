class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums.sort()
        freq, maxFreq, noMaxFreq = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                freq += 1
            else:
                freq = 1
            if freq == maxFreq:
                noMaxFreq += 1
            elif freq > maxFreq:
                noMaxFreq = 1
                maxFreq = freq
        
        return noMaxFreq * maxFreq
        