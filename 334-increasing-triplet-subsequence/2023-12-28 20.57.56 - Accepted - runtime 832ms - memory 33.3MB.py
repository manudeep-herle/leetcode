class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        small1, small2 = float('inf'), float('inf')
        for num in nums:
            if num < small1:
                small1 = num
            elif num < small2 and num > small1:
                small2 = num
            elif num > small1 and num > small2:
                return True
        