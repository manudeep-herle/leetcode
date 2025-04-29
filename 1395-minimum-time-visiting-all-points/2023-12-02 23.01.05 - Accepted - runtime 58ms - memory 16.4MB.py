class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points) - 1):
            [x,y] = points[i]
            nextX, nextY = points[i+1]
            res += max(abs(x-nextX), abs(y-nextY))

        return res

        