class Solution:
    def rob(self, nums: List[int]) -> int:

        def decide(nextHouse, nums, cache):
            if nextHouse not in range(len(nums)):
                return 0
            if nextHouse not in cache:
                cache[nextHouse] = max(decide(nextHouse + 1, nums, cache), nums[nextHouse] + decide(nextHouse + 2, nums, cache))
            return cache[nextHouse]

        if len(nums) == 1:
            return nums[0]
        return max(decide(0, nums[:-1], {}), decide(0, nums[1:], {}))
                
        