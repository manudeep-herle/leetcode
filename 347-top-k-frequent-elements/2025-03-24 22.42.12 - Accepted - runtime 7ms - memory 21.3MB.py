class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the freq of each number
        freqs = collections.Counter(nums)
        # Add (freq, num) to a max heap
        maxHeap = []
        for num in freqs.keys():
            maxHeap.append((-freqs[num], num))
        heapq.heapify(maxHeap)
        # pop the max heap k times to get the k most freq numbers
        out = []
        for i in range(k):
            num = heapq.heappop(maxHeap)
            out.append(num[1])
        return out