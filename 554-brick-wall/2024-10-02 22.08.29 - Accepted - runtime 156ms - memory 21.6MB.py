from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        mem = defaultdict(int)
        # Go through each row
        for row in wall:
            endPos = 0
            # Go through each brick ending position
            for brickWidth in row[0:-1]:
                endPos += brickWidth
                # Keep count of number of occurences of a brick ending position.
                mem[endPos] += 1
        print(mem)
        # Ans is no rows - no (most common brick ending position)
        if mem:
            return len(wall) - max(mem.values()) 
        else:
            return len(wall)