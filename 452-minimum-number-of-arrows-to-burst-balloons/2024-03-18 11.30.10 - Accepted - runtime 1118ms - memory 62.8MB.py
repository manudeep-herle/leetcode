class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = 1
        points.sort()
        curInt = points[0]
        for point in points[1:]:
            if curInt[1] >= point[0]:
                curInt = [min(curInt[0], point[0]), min(curInt[1], point[1])]
            else:
                curInt = point
                res += 1
        
        return res
        