from functools import lru_cache

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        @cache
        def recurse(dice_index, rem_target):
            if dice_index == n-1:
                if rem_target > 0 and rem_target <= k:
                    return 1
                return 0
            if rem_target < n - dice_index - 1:
                return 0

            sum = 0
            for roll in range(1, k+1):
                sum += recurse(dice_index+1, rem_target - roll)
            
            return sum
        
        res =  recurse(0, target)

        return res % (10**9 + 7)