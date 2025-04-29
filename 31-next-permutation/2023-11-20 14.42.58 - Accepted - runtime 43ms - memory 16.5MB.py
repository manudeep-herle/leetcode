import heapq
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nextPermExists = False
        # Check if number is not in descending order
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1]:
                nextPermExists = True
                break
        if not nextPermExists:
            nums.sort()
            return

        i = j = len(nums)-1
        for i in range(len(nums) - 1, 0, -1):
            print(i)
            if nums[i] > nums[i-1]:
                # i-1 needs to be replaced with the number just bigger than in in the right half
                for j in range(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        break
                break   
        print(i, j)
        # Replace i-1 with item at j
        nums[i-1], nums[j] = nums[j], nums[i-1]
        # Reverse numbers to the right of i-1
        l,r = i, len(nums)-1
        while l<r:
            nums[l], nums[r] = nums[r], nums[l]
            l+=1 
            r -= 1
        
        return nums
 


            