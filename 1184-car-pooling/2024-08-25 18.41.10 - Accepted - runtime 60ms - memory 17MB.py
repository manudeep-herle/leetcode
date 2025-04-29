from collections import defaultdict, deque

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event = defaultdict(int)
        for passengers, start, end in trips:
            event[start] += passengers
            event[end] += -passengers
      

        times = deque(sorted(event.keys()))
        cur_passengers = 0

        while times:
            time = times.popleft()
            cur_passengers += event[time]

            if cur_passengers > capacity:
                return False
        return True
        

        