class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        mem = [([0] * 3) for _ in obstacles]
        
        for i in range(len(obstacles)-2, -1, -1):
            obstacleInd = obstacles[i] - 1
            for j in range(3):
                # if obstruction in this cell only
                if j == obstacleInd:
                    mem[i][j] = float('inf')
                # if no obstruction ahead
                elif(mem[i+1][j] != float('inf')):
                    mem[i][j] = mem[i+1][j]
                # if there's an obstruction ahead
                else:
                    if obstacleInd == -1:
                        mem[i][j] = min(mem[i+1][0], mem[i+1][1], mem[i+1][2]) + 1
                    elif obstacleInd == 0:
                        mem[i][j] = min(mem[i+1][1], mem[i+1][2]) + 1
                    elif obstacleInd == 1:
                        mem[i][j] = min(mem[i+1][0], mem[i+1][2]) + 1
                    else:
                        mem[i][j] = min(mem[i+1][0], mem[i+1][1]) + 1
        
        return (mem[0][1])
        