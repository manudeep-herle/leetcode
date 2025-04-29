from heapq import heappush, heappop
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        maxHeap = []
        for val in counts.values():
            heappush(maxHeap, -val)
        q = collections.deque()
        time = 0
        while maxHeap or q:
            time += 1
            if maxHeap:
                count = heappop(maxHeap)
                count += 1
                if count != 0:
                    idleTime = time + n
                    q.append([idleTime, count])
            if q and q[0][0] == time:
                count = q.popleft()[1]
                heappush(maxHeap, count)
        
        return time