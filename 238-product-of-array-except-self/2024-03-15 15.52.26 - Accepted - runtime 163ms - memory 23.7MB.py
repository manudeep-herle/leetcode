class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod, zero_flag = 1, False

        for num in nums:
            if num == 0 and not zero_flag:
                zero_flag = True
                continue
                
            prod = prod * num

        if prod == 0:
            return [prod] * len(nums)

        a = []
        for num in nums:
            if zero_flag and num == 0:
                a.append(prod)
            elif zero_flag and num != 0:
                a.append(0)
            else:
                a.append(int(prod/num))

        return a