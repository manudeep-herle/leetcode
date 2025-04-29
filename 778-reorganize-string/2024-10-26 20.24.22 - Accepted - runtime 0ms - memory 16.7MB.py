from heapq import heappush
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = collections.Counter(s)
        maxHeap = []

        for key in counts:
            heappush(maxHeap, (-counts[key], key))
        
        prev = None
        res = ""

        while maxHeap or prev:
            # check if we can push back an item from q
            if not maxHeap and prev:
                return ""

            count, char = heappop(maxHeap)
            count += 1 # decrement count by 1
            res += char

            if prev:
                heappush(maxHeap, prev)
                prev = None
            if count != 0:
                prev = (count, char)

        return res
        
            

        