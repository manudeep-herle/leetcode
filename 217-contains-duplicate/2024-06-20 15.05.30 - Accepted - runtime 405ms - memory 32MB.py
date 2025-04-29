class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return True if len(setNums) < len(nums) else False
        