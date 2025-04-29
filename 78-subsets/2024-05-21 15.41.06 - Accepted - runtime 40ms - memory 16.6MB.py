class Solution:
    def __init__(self):
        self.res = []
        self.nums = None

    def recurse(self, i, partialArr):
        if i >= len(self.nums):
            self.res.append(partialArr.copy())
            return
        partialArr.append(self.nums[i])
        self.recurse(i+1, partialArr)
        partialArr.pop()
        self.recurse(i+1, partialArr)        

    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        self.recurse(0, [])
        return self.res

        