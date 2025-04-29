class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        l = r = None
        res = ""
        for l in range(len(word)):
            if word[l] == ch:
                r = l + 1
                break

        if r:
            while l > -1:
                res += word[l]
                l -= 1
            if r < len(word):
                res += word[r:]

        else:
            res = word

        return res