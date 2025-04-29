from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        counts = Counter(arr1)
        for num in arr2:
            res += [num] * counts[num]
            del counts[num]
        
        keys = sorted(list(counts.keys()))
        for num in keys:
            res += [num] * counts[num]
        return res
        