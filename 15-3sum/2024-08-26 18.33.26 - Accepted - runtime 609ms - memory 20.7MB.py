class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i, num in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l,r = i+1, len(nums) - 1
            if nums[i] > 0:
                break

            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1
                    print(nums[l-1], nums[l])
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif sum < 0:
                    l += 1
                else:
                    r -= 1                   
        return res