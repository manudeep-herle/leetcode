from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counts = Counter(arr)
        arr.sort()
        def foo(n):
            return counts[n]
        arr.sort(key = foo)

        removed = 0
        for i in range(k):
            if i + 1 == len(arr):
                return 0
            if arr[i] != arr[i+1]:
                removed += 1

        return len(counts.keys()) - removed

