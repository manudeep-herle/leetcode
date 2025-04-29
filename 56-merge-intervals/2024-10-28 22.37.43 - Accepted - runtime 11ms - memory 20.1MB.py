class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        cur = 0
        next = 1
        res = []
        n = len(intervals)
        while cur < n and next < n:
            if intervals[cur][1] < intervals[next][0]:
                res.append(intervals[cur])
                cur = next
                next += 1
            else:
                intervals[cur][1] = max(intervals[cur][1], intervals[next][1])
                next += 1
        if cur < len(intervals):
            res.append(intervals[cur])
        return res

