class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left, right = [0] * n, [0] * n
        lp, rp = 1, 1
        for i in range(n):
            right[n-i-1] = nums[n-i-1] * rp
            left[i] = nums[i] * lp
            rp, lp = right[n-i-1], left[i]
        ans = []
        print(left, right)
        for i in range(n):
            lh = rh = 1
            if i-1 >= 0:
                lh = left[i-1]
            if i+1 < n:
                rh = right[i+1]
            print(lh, rh, i)
            ans.append(lh * rh)
        return ans
        