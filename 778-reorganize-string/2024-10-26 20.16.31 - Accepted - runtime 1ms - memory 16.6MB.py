from heapq import heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        maxHeap = []

        for key in counts:
            heappush(maxHeap, (-counts[key], key))
        
        q = collections.deque()
        res = ""

        while maxHeap or q:
            # check if we can push back an item from q
            if res and q and res[-1] != q[0][1]:
                    tup = q.popleft()
                    heappush(maxHeap, tup)

            # if not maxHeap and only q
            if not maxHeap and q:
                if res[-1] != q[0][1]:
                    # push first element from q to maxHeap
                    tup = q.popleft()
                    heappush(maxHeap, tup)
                else:
                    print(maxHeap, q, res)
                    return ""

            count, char = heappop(maxHeap)
            count += 1 # decrement count by 1
            res += char

            if count != 0:
                q.append((count, char))

        return res
        
            

        