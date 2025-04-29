class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # calculate prefix sum
        sum, prefix = 0, []
        for num in nums:
            sum += num
            prefix.append(sum)

        res = [prefix[-1] - nums[0] * len(nums)]   
        for i in range(1, len(nums)):
            ans = (nums[i] * i - prefix[i-1]) +((prefix[-1] - prefix[i]) - nums[i] * (len(nums) -i - 1))  
            res.append(ans)
        return res    