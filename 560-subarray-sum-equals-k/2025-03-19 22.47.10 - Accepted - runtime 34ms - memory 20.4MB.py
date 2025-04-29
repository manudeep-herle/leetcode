class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # go through nums
        # at each point, check if we can form a valid sub array by excluding some previously encountered nums
        # for this we keep track of cumulative sum (csum)
        # if we can get k by subtracting a previous csum with current csum, then we have a valid subarray that sums up to k
        hist = collections.defaultdict(int)
        hist[0] = 1
        out = csum = 0
        for num in nums:
            csum += num
            if csum - k in hist:
                out += hist[csum - k]
            hist[csum] += 1
        return out


