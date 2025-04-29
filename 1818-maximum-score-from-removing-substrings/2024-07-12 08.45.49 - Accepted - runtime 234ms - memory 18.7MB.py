class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        res = 0
        if x > y:
            big, sm, fir, sec = x, y, "a", "b"
        else:
            big, sm, fir, sec = y, x, "b", "a"
        stack = []
        for c in s:
            if c == sec and stack and stack[-1] == fir:
                stack.pop()
                res += big
            else:
                stack.append(c)
        print(res, stack)
        s = "".join(stack)
        stack = []
        for c in s:
            if c == fir and stack and stack[-1] == sec:
                stack.pop()
                res += sm
            else:
                stack.append(c)
        
        return res

        
