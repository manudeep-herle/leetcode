class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        charsCounter = Counter(chars)
        res = 0
        for word in words:
            wordCounter = Counter(word)
            addFlag = True
            for key in wordCounter:
                if key not in charsCounter or wordCounter[key] > charsCounter[key]:
                    addFlag = False
                    break
            if addFlag:
                res += len(word)
        return res
        