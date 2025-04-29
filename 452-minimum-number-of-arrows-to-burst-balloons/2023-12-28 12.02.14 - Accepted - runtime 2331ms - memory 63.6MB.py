class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 0
        points.sort(key = lambda p: p[0])
        minEnd = -float('inf')

        for point in points:
            if point[0] > minEnd:
                minEnd = point[1]
                res += 1
            else:
                minEnd = min(point[1], minEnd)

        return res
        