class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 0
        curCount = 1
        num = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == nums[i - 1]:
                curCount += 1
                if curCount > count:
                    count = curCount
                    num = nums[i]
            else:
                curCount = 1
        return num

