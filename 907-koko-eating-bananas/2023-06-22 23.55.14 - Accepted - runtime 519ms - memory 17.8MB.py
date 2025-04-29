import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 0, 0
        ans = float("inf")

        if len(piles) == 1:
            return math.ceil(piles[0]/h)

        for num in piles:
            if num > r:
                r = num

        def check(mid):
            hours = 0
            for num in piles:
                if num <= mid:
                    hours += 1
                else:
                    hours += math.ceil(num/mid)
            return hours
                    

        while l <= r:
            mid = int((l+r)/2)
            if mid == 0:
                break
            hours = check(mid)

            if hours <= h:
            # Try to eat slower 
                if mid < ans:
                    ans = mid
                r = mid - 1

            else:
            # Eat faster
                l = mid + 1
        
        return ans


        





