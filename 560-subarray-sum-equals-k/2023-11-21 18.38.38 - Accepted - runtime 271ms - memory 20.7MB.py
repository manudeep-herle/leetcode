class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum = 0
        allSums = defaultdict(int)
        allSums[0] = 1
        res = 0
        for num in nums:
            sum += num
            res += allSums[sum - k]
            allSums[sum] += 1
        return res