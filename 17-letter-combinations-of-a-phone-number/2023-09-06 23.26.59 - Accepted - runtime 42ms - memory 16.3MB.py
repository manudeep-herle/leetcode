class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # How do the digits map to letters?
        # Call backtrack for each successive letter
        word = []
        res = []

        def get_letters(digit):
            digit = int(digit)
            if digit == 7:
                return 'pqrs'
            elif digit == 8:
                return 'tuv'
            elif digit == 9:
                return 'wxyz'
            elif digit == 0 or digit == 1:
                return ''
            else:
                return chr((digit - 2) * 3 + 97) + chr((digit - 2) * 3 + 98)  + chr((digit - 2) * 3 + 99) 

        def backtrack(i):
            if i >= len(digits):
                if word:
                    res.append("".join(word))
                return

            for letter in get_letters(digits[i]):
                word.append(letter)
                backtrack(i+1)
                word.pop()

        backtrack(0)
        return res



