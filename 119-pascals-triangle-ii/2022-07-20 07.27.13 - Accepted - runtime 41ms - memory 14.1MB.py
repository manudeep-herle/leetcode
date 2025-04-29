class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1],[1,1]]
        if rowIndex == 0:
            return res[0]
        elif rowIndex == 1:
            return res[1]
        for i in range (2, rowIndex+1):
            temp = [1]
            for j in range (0, i-1):
                print(i,j)
                temp.append(res[i-1][j] + res[i-1][j+1])
            temp.append(1)
            print("temp",temp)
            res.append(temp)
        return(res[-1])
                
                
        