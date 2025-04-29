class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort the intervals in ascending order by start time
        # interate through intervals, track st, en & cst, cen.
        # Overlap exists if cst <= en, else no overlap
        # if overlap, en = max(en, cen)
        # if no overlap append (st, en) to output list
        # time = O(nlogn) space = O(n)
        intervals = sorted(intervals, key = lambda int: int[0])
        st, en = -1, -1
        output = []
        for [cst, cen] in intervals:
            
            if cst > en:
                # no overlap
                output.append([st, en])
                st, en = cst, cen
            else:
                en = max(cen, en)
        output.append([st, en])
        return output[1:]

