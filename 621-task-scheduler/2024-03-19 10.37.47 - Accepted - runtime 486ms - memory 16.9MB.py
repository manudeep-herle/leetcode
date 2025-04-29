from heapq import heapify, heappush, heappop
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        t_c = Counter(tasks)
        counts = [-c for c in t_c.values()]
        heapify(counts)
        time = 0
        q = []

        while counts or q:
            time += 1

            if counts:
                count = heappop(counts) # Get count of the most freq char in counts
                count += 1 # Reduce count by 1
                if count:
                    q.append((count, time + n)) # Wait for n

            if q and q[0][1] == time:
                heappush(counts, q[0][0])
                q = q[1:]

        return time