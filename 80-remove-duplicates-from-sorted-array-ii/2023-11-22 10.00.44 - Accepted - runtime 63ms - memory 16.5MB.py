class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = dict(Counter(nums))
        keys = list(count.keys())
        index = 0
        for key in keys:
            r = min(count[key], 2)
            for i in range(r):
                nums[index] = key
                index += 1
        for i in range(index, len(nums)):
            nums.pop()
        print(nums)


        