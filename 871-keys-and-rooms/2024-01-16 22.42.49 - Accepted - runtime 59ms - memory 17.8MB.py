class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = set([0])
        visited = set()
        while len(keys):
            room = keys.pop()
            if room in visited:
                continue

            visited.add(room)
            for r in rooms[room]:
                keys.add(r)
        
        if len(visited) == len(rooms):
            return True
        return False




        