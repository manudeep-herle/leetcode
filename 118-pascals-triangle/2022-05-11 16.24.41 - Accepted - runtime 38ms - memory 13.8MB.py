class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1]]
        for level in range(1, numRows):
            print(level)
            result.append([])
            result[level].append(result[level-1][0])
            for i in range(1, level): #from 2nd to last 2nd element
                result[level].append(result[level - 1][i-1]+result[level - 1][i])
            result[level].append(result[level-1][-1])  
        return result
            
        