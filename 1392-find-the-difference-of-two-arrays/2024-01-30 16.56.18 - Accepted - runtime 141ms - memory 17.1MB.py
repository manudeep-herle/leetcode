from collections import Counter
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res = [[],[]]
        h1, h2 = Counter(nums1), Counter(nums2)
        for key in h1:
            if key not in h2:
                res[0].append(key)
        for key in h2:
            if key not in h1:
                res[1].append(key)    
        return res


        