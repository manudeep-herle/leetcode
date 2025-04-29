class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        i = 0
        for n in nums:
            if target - n in hashmap:
                return (hashmap[target - n], i)
            hashmap[n] = nums.index(n)
            i += 1