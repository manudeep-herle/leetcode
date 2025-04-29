class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if(digits[-1] != 9):
            digits[-1] = digits[-1]+1
            return digits
        else:
            i = 0
            first = len(digits) * -1
            while i > first:
                i = i-1
                if(digits[i] == 9):
                    digits[i] = 0
                else:
                    digits[i] = digits[i] + 1
                    return digits
            digits.insert(0,1)
            return digits
            
                
