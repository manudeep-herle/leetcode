class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda time: time[0])

        prev = -1
        for inte in intervals:
            if inte[0] < prev:
                return False
            prev = inte[1]

        return True
        