class Solution:
    def rob(self, nums: List[int]) -> int:
        cache = {}
        def decide(nextHouse):
            if nextHouse not in range(len(nums)):
                return 0
            if nextHouse not in cache:
                cache[nextHouse] = max(nums[nextHouse] + decide(nextHouse + 2), decide(nextHouse + 1))
            return cache[nextHouse]

        return decide(0)