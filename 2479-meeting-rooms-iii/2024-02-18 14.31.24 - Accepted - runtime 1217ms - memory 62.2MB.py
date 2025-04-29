from heapq import heapify, heappush, heappop

class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        avRooms = [i for i in range(n)]
        res = [0] * n
        occRooms = []
        meetings.sort(key = lambda meeting: meeting[0])
        for meeting in meetings:
            # Put all rooms freed up into avRooms
            while occRooms and occRooms[0][0] <= meeting[0]:
                [_, room] = heappop(occRooms)
                heappush(avRooms, room)
            # If meeting room is available from unused room
            if avRooms:
                room = heappop(avRooms)
                heappush(occRooms, (meeting[1], room))
                res[room] += 1

            # Delay when no rooms are available
            else:
                room = heappop(occRooms)
                meeting[1] = meeting[1] + room[0] - meeting[0]
                heappush(occRooms, (meeting[1], room[1]))
                res[room[1]] += 1

        ret = max(range(len(res)), key = lambda i: res[i])
        return ret

                
