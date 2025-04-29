class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1 = " " + word1
        word2 = " " + word2

        mem = [[0]*len(word2) for _ in range(len(word1))]
        
        for i in range(len(word1)):
            for j in range(len(word2)):
                if i == 0:
                    mem[i][j] = j
                elif j == 0:
                    mem[i][j] = i
                elif word1[i] == word2[j]:
                    mem[i][j] = mem[i-1][j-1]
                # elif i == j:
                    # mem[i][j] =  min(mem[i-1][j], mem[i][j-1], mem[i-1][j-1]) + 1
                else:
                    # mem[i][j] = min(mem[i-1][j], mem[i][j-1]) + 1
                    mem[i][j] =  min(mem[i-1][j], mem[i][j-1], mem[i-1][j-1]) + 1
        
        return mem[-1][-1]
