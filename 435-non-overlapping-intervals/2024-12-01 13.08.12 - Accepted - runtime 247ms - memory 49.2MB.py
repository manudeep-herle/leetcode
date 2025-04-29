class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda int: int[1])
        largestEt = -float('inf')
        overlap = 0 
        print(intervals)
        for [st, et] in intervals:
            if st < largestEt:
                print(st, largestEt)
                overlap += 1
            else:
                largestEt = et
        return overlap
        