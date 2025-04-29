class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        text1 = "1" + text1
        text2 = "0" + text2
        mem = [([0]*(len(text2))) for _ in range(len(text1))]
        for r in range(1, len(text1)):
            for c in range(1, len(text2)):
                if text1[r] == text2[c]:
                    mem[r][c] = (mem[r-1][c-1]) + 1
                else:
                    mem[r][c] = max(mem[r-1][c], mem[r][c-1])
        print(mem)
        return mem[-1][-1]


