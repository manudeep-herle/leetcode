class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        bestSum = float('inf')
        for i in range(len(nums)-1):
            l,r = i + 1, len(nums)-1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if abs(target - sum) < abs(target - bestSum):
                    bestSum = sum
                if sum == target:
                    return target
                elif sum < target:
                    l += 1
                else:
                    r -= 1
        return bestSum



        