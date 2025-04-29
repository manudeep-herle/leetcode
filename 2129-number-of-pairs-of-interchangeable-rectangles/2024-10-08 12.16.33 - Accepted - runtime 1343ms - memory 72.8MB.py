class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        mem = collections.defaultdict(int)
        # group interchangable rectangles together
        for [w,h] in rectangles:
            mem[w/h] += 1
        
        res = 0
        for ratio in mem:
            if mem[ratio] > 1:
                res += mem[ratio] * (mem[ratio] - 1) / 2
        
        return int(res)