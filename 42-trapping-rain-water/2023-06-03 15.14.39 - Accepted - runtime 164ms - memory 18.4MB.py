class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointers one stops when we find a concave region
        ML = [0 for _ in height]
        MR = [0 for _ in height]
        i = -1
        res = 0
        for i in range(len(height)):
            if i > 0:
                ML[i] = max(ML[i-1], height[i-1])
                MR[-i - 1] = max(MR[-i], height[-i])
        i = -1
        for h in height:
            i += 1
            a = min(ML[i], MR[i]) - h
            if a > 0:
                res += a
            
        return res

                   
