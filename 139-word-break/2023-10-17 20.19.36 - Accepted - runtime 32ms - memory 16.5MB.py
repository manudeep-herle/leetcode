class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        mem = [False] * len(s)
        
        for i in range(len(s)):
            for word in wordDict:
                if len(word) - 1 > i:
                    continue
                if s[i-len(word)+1:i+1] == word and (i-len(word) < 0 or mem[i-len(word)]):
                    mem[i] = True
        print(mem)
        return mem[-1]


                      
        