class Solution:
    def __init__(self):
        self.nums = None

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Go from right to left
        # When we find a drop in the order i.e. nums[i] > nums[i-1]
        # Swap nums[i-1] with the next biggest element to it's right
        # Swap all numbers from nums[i] to nums[-1]
        self.nums = nums
        if len(nums) == 1:
            return nums

        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        print(i)
        #  if i >= 0, swap i with next biggest number
        if i >= 0:
            j = len(nums) - 1
            while j > i:
                if nums[j] > nums[i]:
                    # swap i and j
                    self.swap(i, j)
                    break
                j -= 1
        self.reverse(i + 1)
        return self.nums

    def swap(self, i, j):
        # swap num at i with num at j
        self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def reverse(self, l):
        # reverse numbers starting from index i
        r = len(self.nums) - 1
        while l< r:
            self.swap(r, l) 
            r -= 1
            l += 1