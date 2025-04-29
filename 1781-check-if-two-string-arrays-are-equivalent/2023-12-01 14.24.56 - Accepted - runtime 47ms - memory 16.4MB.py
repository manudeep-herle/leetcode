class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        l,r = 0, 0
        outl, outr = 0, 0
        while outl < len(word1) and outr < len(word2):
            while l < len(word1[outl]) and r < len(word2[outr]):
                if word1[outl][l] != word2[outr][r]:
                    return False
                l += 1
                r += 1
            if l >= len(word1[outl]):
                outl += 1
                l = 0
            if r >= len(word2[outr]):
                outr += 1
                r = 0
        return outl == len(word1) and outr == len(word2)
            
            

            
        