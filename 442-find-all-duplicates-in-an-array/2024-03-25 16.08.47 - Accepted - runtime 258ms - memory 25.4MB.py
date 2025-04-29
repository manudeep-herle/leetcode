from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        res = []
        for k in counts.keys():
            if counts[k] > 1:
                res.append(k)
        
        return res