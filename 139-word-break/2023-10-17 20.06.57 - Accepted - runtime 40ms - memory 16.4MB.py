class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            for word in wordDict:
                # If there aren't enough characters in s[:i+1] to form the word
                if i < 0:
                    return True

                if i < len(word)-1:
                    continue

                if s[i-len(word)+1: i+1] == word:
                    if not dp(i-len(word)):
                        print("Cont", i-len(word), word)
                        continue
                    return True

        return dp(len(s) - 1)
        