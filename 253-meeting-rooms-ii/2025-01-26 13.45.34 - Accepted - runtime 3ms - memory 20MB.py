from heapq import heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # sort the intervals by end time
        # for each interval check if start time overlaps with first interval in dq
        # if no overlap, pop from dq
        # push curr interval into dq

        intervals = sorted(intervals, key = lambda interval: interval[0])
        res = 1

        meetRooms = []

        for [st, et] in intervals:
            while meetRooms:
                prevEt = heappop(meetRooms) 
                if prevEt > st:
                    heappush(meetRooms, prevEt)
                    break

            heappush(meetRooms, et)
            res = max(res, len(meetRooms))        
        return res

            
        