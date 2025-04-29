class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        merged = False
        if not intervals:
            return [newInterval]
        for [st, end] in intervals:
            if st > newInterval[1]:
                if not merged:
                    res.append(newInterval)
                    merged = True
                res.append([st,end])
            elif end < newInterval[0]:
                res.append([st,end])
            
            # Needs merging
            elif st <= newInterval[0] and end >= newInterval[0]:
                newInterval[1] = max(newInterval[1], end)
                newInterval[0] = st
            elif st >= newInterval[0] and st <= newInterval[1]:
                newInterval[1] = max(newInterval[1], end)

        if not merged:
            res.append(newInterval)
        return res

        