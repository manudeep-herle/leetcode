from heapq import heapify, heappop
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        hmap = Counter(s)
        invHmap = {}
        counts = set()
        print(hmap)
        for key in hmap:
            invHmap[hmap[key]] = invHmap.get(hmap[key], [])
            invHmap[hmap[key]].append(key)
            counts.add(-hmap[key])
        counts = list(counts)
        heapify(counts)
        res = ""
        while counts:
            count = -heappop(counts)
            while invHmap[count]:
                res += (invHmap[count][-1] * count)
                invHmap[count].pop()

        return res