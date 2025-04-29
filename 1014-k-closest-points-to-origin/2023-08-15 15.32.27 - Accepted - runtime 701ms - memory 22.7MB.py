import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        hmap = {}
        minHeap = []
        heapq.heapify(minHeap)
        ans = []

        for point in points:
            dist = (point[0])**2 + (point[1])**2
            if dist in hmap:
                hmap[dist].append(point)
            else:
                hmap[dist] = [point]
            
            heapq.heappush(minHeap, dist)
        
        i = 1
        while i <= k:
            dist = heapq.heappop(minHeap)
            
            i += len(hmap[dist])
            ans += hmap[dist]

        return ans