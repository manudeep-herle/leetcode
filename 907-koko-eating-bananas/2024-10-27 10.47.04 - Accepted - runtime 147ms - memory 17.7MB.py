class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatBananas(bananasPerHour):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / bananasPerHour)
            return hours <= h
        # Binary search to find the ideal number for bananas-per-hour (k)
        l, r = 1, 10**9
        leastBananasPerHour = -1

        while l <= r:
            bananasPerHour = (l+r) // 2
            if canEatBananas(bananasPerHour):
                leastBananasPerHour = bananasPerHour
                r = bananasPerHour-1
            else:
                l = bananasPerHour + 1
        
        return leastBananasPerHour
        
