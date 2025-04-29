from collections import defaultdict, deque

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        event = defaultdict(int)
        times = set()
        for passengers, start, end in trips:
            event[start] += passengers
            event[end] += -passengers
            times.add(start)
            times.add(end)

        times = deque(sorted(times))
        cur_passengers = 0

        while times:
            time = times.popleft()
            cur_passengers += event[time]

            if cur_passengers > capacity:
                return False
        return True
        

        