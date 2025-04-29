class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        distance = [[float('inf')] * len(matrix[0]) for _ in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i == 0:
                    distance[i][j] = matrix[i][j]
                else:
                    for k in range(max(0, j-1), min(len(matrix[0]), j+2)):
                        # print(i, j, k)
                        if distance[i][j] > matrix[i][j] + distance[i-1][k]:
                            distance[i][j] = matrix[i][j] + distance[i-1][k]
        return min(distance[-1])
                      
        