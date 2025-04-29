class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sm, lg, ws = "", "", 0
        if len(s1) <= len(s2):
            sm = ''.join(sorted(s1))
            ws = len(s1)
            lg = s2
        else: 
            return False

        # iterate through lg, with a window size of sm
        r = ws

        while r < len(lg) + 1:
            if ''.join(sorted(lg[r-ws:r])) == sm:
                return True
            r += 1

        return False

        