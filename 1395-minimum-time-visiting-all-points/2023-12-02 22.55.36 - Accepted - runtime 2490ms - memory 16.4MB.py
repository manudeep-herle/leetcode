class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        currPoint = 0
        res = 0
        while currPoint < len(points)-1:
            if points[currPoint][0] == points[currPoint+1][0] and points[currPoint][1] == points[currPoint+1][1]:
                currPoint += 1
                continue
            if points[currPoint][0] < points[currPoint+1][0]:
                points[currPoint][0] += 1
            elif points[currPoint][0] > points[currPoint+1][0]:
                points[currPoint][0] -= 1
            if points[currPoint][1] < points[currPoint+1][1]:
                points[currPoint][1] += 1
            elif points[currPoint][1] > points[currPoint+1][1]:
                points[currPoint][1] -= 1
            res += 1
        return res

        