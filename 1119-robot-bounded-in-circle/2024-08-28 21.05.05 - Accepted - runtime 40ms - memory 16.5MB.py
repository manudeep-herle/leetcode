class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # if there's a skew in the path, the robot is going to go in a circle. i.e. L > R or R > L
        pos = [0,0]
        dir = 'n'
        dirMap = {'n':{'r':'e', 'l':'w'}, 's':{'r':'w', 'l':'e'}, 'e':{'r':'s', 'l':'n'}, 'w':{'r':'n', 'l':'s'}}
        disp = {'n':(0,1), 's':(0,-1), 'e':(+1, 0), 'w':(-1, 0)}
        for instr in instructions:
            if instr == 'G':
                pos[0] += disp[dir][0]  
                pos[1] += disp[dir][1]   
            elif instr == "L":
                dir = dirMap[dir]['l']
            else:
                dir = dirMap[dir]['r']

        return (pos[0] == 0 and pos[1] == 0) or dir != 'n'
        