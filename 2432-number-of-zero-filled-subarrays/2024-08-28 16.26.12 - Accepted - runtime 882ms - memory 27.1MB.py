class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        cur = [0] * len(nums)
        cur[0] = 1 if nums[0] == 0 else 0
        # setup
        if len(nums) > 1:
            if nums[1] == 0:
                if cur[0] == 1:
                    cur[1] = 3
                else:
                    cur[1] = 1
            else:
                res = cur[0]
        else:
            res = cur[0]

        if len(nums) > 1:
            for i in range(2, len(nums)):
                if nums[i] == 0:
                    cur[i] = cur[i-1] + max(cur[i-1] - cur[i-2], 0) + 1
                else:
                    res += cur[i-1]
            res += cur[-1]
        return res



        