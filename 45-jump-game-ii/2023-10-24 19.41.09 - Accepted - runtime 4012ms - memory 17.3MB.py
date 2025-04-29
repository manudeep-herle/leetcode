class Solution:
    def jump(self, nums: List[int]) -> int:
        minDist = [float('inf')] * len(nums)
        minDist[0] = 0

        for i in range(len(nums)-1):
            for j in range(i+1, min((i+1+nums[i]), len(nums))):
                minDist[j] = min(minDist[j], minDist[i]+1)
        print(minDist)
        return minDist[-1]

            

        