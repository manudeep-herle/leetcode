class Solution:
    def maximumSwap(self, num: int) -> int:
        num = str(num)
        num = list(num)

        largeToRight = [None] * len(num)
        large = -float('inf')

        for i in range(len(num) - 1, -1, -1):
            if int(num[i]) > large:
                large = int(num[i])
                largeInd = i
            largeToRight[i] = [large, largeInd]
        
        for i in range(len(num)):
            large, largeInd = largeToRight[i]
            if large > int(num[i]) and largeInd > i:
                num[i], num[largeInd] = num[largeInd], num[i]
                break
        
        return int("".join(num))


            
        