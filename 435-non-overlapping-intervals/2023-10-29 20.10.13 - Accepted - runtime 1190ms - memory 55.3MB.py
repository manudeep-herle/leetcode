class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals) == 0:
            return 0
        intervals = sorted(intervals, key = lambda interval: -interval[1])
        res = 1
        curr = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][1] <= curr[0]:
                curr = intervals[i]
                res += 1
            elif intervals[i][0] > curr[0]:
                curr = intervals[i] 
        

        return len(intervals) - res
         

        
        