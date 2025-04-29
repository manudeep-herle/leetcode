class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = {}
        for c in s:
            count[c] = count.get(c, 0) + 1
        afterCount = {}
        
        inc = 0
        active = set()
        res = []
        for c in s:
            inc += 1
            active.add(c)

            afterCount[c] = afterCount.get(c, 0) + 1
            if afterCount[c] == count[c]:
                active.remove(c)
            
            if len(active) == 0:
                res.append(inc)
                inc = 0


        return res