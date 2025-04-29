from heapq import heapify, heappush, heappop

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        maxHeap = []
        heapify(maxHeap)
       
        intervals = sorted(intervals, key = lambda interval: interval[0])
        currRooms, maxRooms = 1, 1
        heappush(maxHeap, intervals[0][1])
        for i in range(1, len(intervals)):
            prevMeetingEnd = heappop(maxHeap)
            if prevMeetingEnd > intervals[i][0]:
                heappush(maxHeap, prevMeetingEnd)
                currRooms += 1
                maxRooms = max(currRooms, maxRooms)

            heappush(maxHeap, intervals[i][1])

        return maxRooms

        