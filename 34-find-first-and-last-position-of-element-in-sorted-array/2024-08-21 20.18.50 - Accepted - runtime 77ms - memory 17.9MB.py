class Solution:
    def __init__(self):
        self.start = -1
        self.end = -1
        self.target = None
        self.nums = None

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.target = target
        self.nums = nums
        self.binarySearch(0, len(nums) - 1)
        return [self.start, self.end]
    def binarySearch(self, l, r):
        if l > r:
            return
        m = (l+r) // 2
        if (self.nums[m] == self.target):
            # Check if m is the start or end
            if m == 0 or self.nums[m-1] != self.nums[m]:
                self.start = m
                self.binarySearch(m+1, r)
            if m == len(self.nums) -1 or self.nums[m+1] != self.nums[m]:
                self.end = m
                self.binarySearch(l, m-1)
            # Binary search in both directions of this mid point to find start and end
            else:
                self.binarySearch(l, m-1)
                self.binarySearch(m+1, r)
            
        elif self.nums[m] < self.target:
            self.binarySearch(m+1, r)
        elif self.nums[m] > self.target:
            self.binarySearch(l, m-1)
          