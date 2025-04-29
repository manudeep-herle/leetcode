class Solution:
    def placeBalls(self, mid, position, m):
        prev = -float('inf')
        for i in position:
            if i >= prev + mid:
                m -= 1
                prev = i
        return False if m > 0 else True

    def maxDistance(self, position: List[int], m: int) -> int:
        # Binary search to determine the max min distance between two balls.
        mid = res = 0
        position.sort()
        l, h = 1, position[-1]
        while l <= h:
            mid = (l+h) // 2
            if self.placeBalls(mid, position, m):
                l = mid + 1
                res = mid
            else:
                h = mid - 1
            
        return res