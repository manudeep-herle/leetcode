class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # traverse through abbr, pointer for word
        wordp = 0
        abbrp = 0

        while abbrp < len(abbr):
            if wordp >= len(word):
                return False
            # if num, extract full number.
            if (abbr[abbrp]).isnumeric():
                # Check for trailing zero
                if abbr[abbrp] == "0":
                    return False
                num = ""
                while abbrp < len(abbr) and (abbr[abbrp]).isnumeric():
                    num += abbr[abbrp]
                    abbrp += 1
                wordp += int(num)
                if wordp > len(word):
                    return False
            #  If string match with word
            else:
                if word[wordp] != abbr[abbrp]:
                    return False
                else:
                    abbrp += 1
                    wordp += 1
        if wordp < len(word):
            return False
        return True
            