class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        ap, wp = 0, 0
        A, W = len(abbr), len(word)
        
        while ap < A:
            # Check if wp has surpassed word
            if wp >= W:
                return False
            # Check if abbr character is number or alpha
            if abbr[ap].isalpha():
                if abbr[ap] != word[wp]:
                    return False
                # Move to next character in both strings
                ap += 1
                wp += 1
            else:
                if abbr[ap] == "0":
                    return False
                anc = ap
                while ap < A and not abbr[ap].isalpha():
                    ap += 1
                # Number of spaces to skip in the word
                skip = int(abbr[anc: ap])
                wp += skip
        if ap - A != wp - W:
            return False
        return True
        