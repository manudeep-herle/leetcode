class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            curr = (r - l) * min(height[l],height[r])
            if curr > res:
                res = curr
            
            if min(height[l],height[r]) == height[l]:
                l += 1
            else:
                r -= 1
        
        return res