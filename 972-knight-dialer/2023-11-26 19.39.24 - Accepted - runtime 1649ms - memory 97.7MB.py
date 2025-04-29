import functools
class Solution:
    def knightDialer(self, n: int) -> int:
        validMoves = {
            0:[4,6],
            1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4]
        }
        
        @cache
        def recurse(pos, n):
            if n == 0:
                return 1
            possibleMoves = 0
            for nextPos in validMoves[pos]:
                possibleMoves += recurse(nextPos, n-1)
            return possibleMoves
        
        res = 0
        for startPos in validMoves:
            res += recurse(startPos, n-1)

        return res%(10 ** 9 + 7)