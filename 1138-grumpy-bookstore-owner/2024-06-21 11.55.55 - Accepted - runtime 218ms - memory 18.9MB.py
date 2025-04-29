class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # Find total customers satisfied without using minutes, also initialize res and curWindow
        total, curWindow = 0, 0
        for i in range(len(customers)):
            if grumpy[i] == 0:
                total += customers[i]
            if i < minutes and grumpy[i]:
                curWindow += customers[i]
        res = curWindow 
        # Slide window of size minutes to check which is the most optimal window
        for i in range(minutes, len(customers)):
            if grumpy[i-minutes]:
                curWindow -= customers[i-minutes] # Shorten window on left
            if grumpy[i]:
                curWindow += customers[i] # Lengthen window on right
                res = max(res, curWindow)

        return total + res