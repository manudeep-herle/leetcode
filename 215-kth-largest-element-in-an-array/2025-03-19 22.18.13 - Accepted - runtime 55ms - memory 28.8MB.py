class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        counts = collections.Counter(nums)
        keys = list(counts.keys())
        heapq.heapify(keys)
        count = 0 # track how many numbers we've already counted
        k = len(nums) - k + 1
        
        while keys:
            key = heappop(keys) # return the minimum key first
            count += counts[key]
            if count >= k:
                return key
        
        return -1
        