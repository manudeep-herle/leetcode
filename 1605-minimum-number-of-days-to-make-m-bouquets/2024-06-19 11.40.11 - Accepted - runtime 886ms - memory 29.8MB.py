class Solution:
    def check(self, mid, bloomDay, m, k):
        bouquets = count = 0
        for day in bloomDay:
            if day <= mid:
                count += 1
                if count == k:
                    count = 0
                    bouquets += 1
                    if bouquets == m:
                        return True
            else:
                count = 0
        return False

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Binary search by number of days
        # Find the minimum number of days where we can have m windows of k flowers
        l, h = 1, 10**9
        res = -1
        while l <= h:
            mid = (l+h)//2
            if self.check(mid,  bloomDay, m, k):
                h = mid - 1
                res = mid
            else: 
                l = mid + 1
        return res