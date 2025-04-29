from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rs = deque()
        ds = deque()
        for i, s in enumerate(senate):
            if s == "R":
                rs.append(i)
            else:
                ds.append(i)

        while len(rs) and len(ds):
            r,d = rs.popleft(), ds.popleft()
            if r < d:
                rs.append(r + len(senate))
            else:
                ds.append(d + len(senate))


        return "Radiant" if len(rs) else "Dire"
        