class Solution:
    def trap(self, height: List[int]) -> int:
        l,r = 0, len(height) - 1
        ML, MR = height[l],height[r]

        res = 0

        for i in range(1, len(height) - 1):
            if ML < MR:
                l += 1
                a = ML - height[l]
                if a > 0:
                    res += a
                ML = max(ML, height[l])
                
            else:
                r -= 1
                a = MR - height[r]
                if a > 0:
                    res += a
                MR = max(MR, height[r])

        return res
                        

                   
