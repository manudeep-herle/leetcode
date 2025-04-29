class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        i = -1
        A = []
        for num in nums:
            i += 1
            l = i+1
            r = len(nums) - 1
            if i > 0 and num == nums[i - 1]:
                continue

            while l < r:
                if l > i+1 and nums[l] == nums[l-1]:
                    l += 1
                    continue
                
                summ = nums[l] + nums[r]
                if summ == -num:
                    A.append([num, nums[l], nums[r]])
                    l += 1
                elif summ < -num:
                    l += 1
                else:
                    r -= 1


        return A

                
            
