class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        # How do the digits map to letters?
        # Call backtrack for each successive letter
        word = []
        res = []

        get_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i):
            if i >= len(digits):
                if word:
                    res.append("".join(word))
                return

            for letter in get_letters[digits[i]]:
                word.append(letter)
                backtrack(i+1)
                word.pop()

        backtrack(0)
        return res



