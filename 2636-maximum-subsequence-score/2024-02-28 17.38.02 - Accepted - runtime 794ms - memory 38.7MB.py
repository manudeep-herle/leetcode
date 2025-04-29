from heapq import heapify, heappush, heappop

class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        pairs = [(a,b) for a,b in zip(nums1, nums2)]
        pairs.sort(key = lambda x: -x[1])
        
        top_k_heap = [x[0] for x in pairs[:k]]
        heapify(top_k_heap)
        top_k_sum = sum(top_k_heap)
        res = top_k_sum * pairs[k-1][1]

        for i in range(k, len(pairs)):
            top_k_sum -= heappop(top_k_heap)
            top_k_sum += pairs[i][0]
            heappush(top_k_heap, pairs[i][0])
            res = max(res, top_k_sum * pairs[i][1])

        return res