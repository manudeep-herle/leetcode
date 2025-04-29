class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
            
        s1 = " " + s1
        s2 = " " + s2
        s3 = " " + s3

        mem = [[0]*(len(s2)) for _ in range(len(s1))]

        for i in range(len(s1)):
            for j in range(len(s2)):

                left = mem[i][j-1]
                top = mem[i-1][j]

                if i > 0 and j > 0:
           
                    if left > top and s3[left + 1] == s2[j]:
                        mem[i][j] = left + 1   
                    elif s3[top + 1] == s1[i]:
                        mem[i][j] = top + 1               
           
                elif i > 0:
                    if s3[top + 1] == s1[i]:
                        mem[i][j] = top + 1
                elif j > 0:
                    if s3[left + 1] == s2[j]:
                        mem[i][j] = left + 1
                else:
                    continue

        if mem[-1][-1] == len(s3) - 1:
            return True
        else:
            return False


        return False 
        