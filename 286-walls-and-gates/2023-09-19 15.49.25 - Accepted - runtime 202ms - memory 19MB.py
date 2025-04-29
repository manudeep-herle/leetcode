from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        ROWS, COLS = len(rooms), len(rooms[0])
        INF = 2147483647
        dist = 1
        q = deque()

        # Find indices of gates
        for i in range(ROWS):
            for j in range(COLS):
                if rooms[i][j] == 0:
                    q.append((i,j))

        while len(q):
            for k in range(len(q)):
                [i,j] = q.popleft()

                neighbors = [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]

                for [i, j] in neighbors:
                    if i >= ROWS or j >= COLS or i < 0 or j < 0:
                        continue
                    if rooms[i][j] > dist:
                        rooms[i][j] = dist
                        q.append((i,j))
                        
            dist += 1
            

            
        
        # From each gate do a BFS simultaneously.

        # Every empty room gets a distance to nearest gate