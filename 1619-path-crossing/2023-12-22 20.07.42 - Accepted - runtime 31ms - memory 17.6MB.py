class Solution:
    def isPathCrossing(self, path: str) -> bool:
        visited = set()
        visited.add((0,0))
        x,y = 0,0
        for dir in path:
            if dir == "N":
                loc = (x,y+1)
            elif dir == "S":
                loc = (x, y - 1)
            elif dir == "E":
                loc = (x+1, y)
            else:
                loc = (x-1, y)

            x, y = loc[0], loc[1]
            print(loc)
            if loc in visited:
                return True
            else:
                visited.add(loc)
        print(visited)
        return False