class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False

        s1 = " " + s1
        s2 = " " + s2
        s3 = " " + s3

        mem = [[False]*(len(s2)) for _ in range(len(s1))]

        for i in range(len(s1)):
            for j in range(len(s2)):

                left = mem[i][j-1]
                top = mem[i-1][j]

                if i > 0 and j > 0:
                    mem[i][j] = (left and s3[i + j] == s2[j]) or (top and s3[i + j] == s1[i])
                elif i > 0:
                        mem[i][j] = (top and s3[i] == s1[i])
                elif j > 0:
                        mem[i][j] = (left and s3[j] == s2[j])
                else:
                    mem[i][j] = True


        return mem[-1][-1]


        return False 
        