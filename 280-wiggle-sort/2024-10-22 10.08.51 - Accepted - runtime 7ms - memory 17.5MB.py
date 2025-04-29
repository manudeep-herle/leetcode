class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mem = sorted(nums)
        odd = math.ceil(len(mem)/2)
        even = 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = mem[even]
                even += 1
            else:
                nums[i] = mem[odd]
                odd += 1
        

