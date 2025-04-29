class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort intervals by end times
        # for each interval, check if it starts after prev int end time
        intervals = sorted(intervals, key = lambda interval: interval[1])
        prevEt = -1
        
        for [st, et] in intervals:
            if st < prevEt:
                return False
            prevEt = et
        
        return True

