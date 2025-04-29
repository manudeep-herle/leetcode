from heapq import heapify, heappop, heappush

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = 1
        intervals.sort(key = lambda inte: inte[0])
        minheap = [intervals[0][1]]

        for inte in intervals[1:]:
            if minheap and inte[0] < minheap[0]:
                rooms += 1
            elif minheap:
                heappop(minheap)
            heappush(minheap, inte[1])

        return rooms