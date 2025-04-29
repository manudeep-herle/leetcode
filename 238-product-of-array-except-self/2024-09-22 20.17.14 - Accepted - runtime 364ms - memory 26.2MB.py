class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            ltor, rtol = [], deque()
            currltor, currrtol = 1, 1
            for i in range(len(nums)):
                currltor *= nums[i] 
                currrtol *= nums[-(i+1)] 
                ltor.append(currltor)
                rtol.appendleft(currrtol)
            
            res = [rtol[1]]
            for i in range(1, len(nums) - 1):
                res.append(ltor[i-1] * rtol[i+1])
            res.append(ltor[-2])
            return res
        return nums