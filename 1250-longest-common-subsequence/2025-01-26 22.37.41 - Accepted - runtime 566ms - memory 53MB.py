class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem = [[0] * len(text1) for _ in range(len(text2))]
        # r --> text2, c --> text1
        for r in range(len(text2)):
            for c in range(len(text1)):
                if r == 0 and c == 0: mem[0][0] = 1 if text1[0] == text2[0] else 0
                elif r == 0:
                    mem[r][c] = 1 if mem[r][c-1] == 1 or text1[c] == text2[r] else 0
                elif c == 0:
                    mem[r][c] = 1 if mem[r-1][c] == 1 or text1[c] == text2[r] else 0 
                
                else:
                    if text1[c] == text2[r]:
                        mem[r][c] = mem[r-1][c-1] + 1
                    else:
                        mem[r][c] = max(mem[r-1][c], mem[r][c-1])
        print(mem)
        
        return mem[-1][-1]


    #    [[0, 0, 0, 0, 0, 0, 0, 0], 
    #     [0, 0, 0, 0, 0, 0, 0, 1], 
    #     [0, 0, 0, 0, 0, 0, 0, 1], 
    #     [0, 0, 0, 0, 0, 0, 0, 1], 
    #     [2, 2, 1, 1, 1, 1, 1, 1], 
    #     [2, 2, 2, 2, 2, 2, 2, 2], 
    #     [2, 2, 2, 2, 2, 2, 2, 2], 
    #     [2, 2, 2, 2, 2, 2, 2, 2], 
    #     [2, 2, 2, 2, 2, 2, 2, 2]]

