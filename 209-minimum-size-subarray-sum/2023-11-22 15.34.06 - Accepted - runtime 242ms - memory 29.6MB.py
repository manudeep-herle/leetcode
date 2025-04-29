class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r = 0,0
        currSum = nums[0]
        res = float('inf')
        while r < len(nums):
            if currSum < target and r < len(nums) - 1:
                r += 1
                currSum += nums[r]
            else:
                res = min(res, r-l+1)
                if currSum - nums[l] >= target:
                    while currSum - nums[l] >= target:
                        currSum -= nums[l]
                        l += 1
                elif r < len(nums) - 1:
                    r += 1
                    currSum += nums[r]
                else:
                    break
        return res if res < float('inf') and currSum >= target else 0
                


        