class Solution:
    def isHappy(self, n: int) -> bool:
        def getSum(n):
            sum = 0
            for digit in str(n):
                sum += int(digit)**2
            return sum
        
        sum = getSum(n)
        seen = []
        while sum not in seen:  
            seen.append(sum)
            if sum == 1:
                return True
            sum = getSum(sum)
        return False

            

        