class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        curr = None
        intervals = sorted(intervals, key = lambda x: x[0])
        for interval in intervals:
            if not curr:
                curr = interval
            else:
                # Check for an overlap
                if min(curr[1], interval[1])-max(curr[0], interval[0]) >= 0:
                    curr = [min(curr[0], interval[0]), max(curr[1], interval[1])]
                # If no overlap, add curr to res, new curr is interval
                else:
                    res += [curr]
                    curr = interval
        res += [curr]
        return res