class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        toRemove = []
        stack = []

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if stack:
                    stack.pop()
                else:
                    toRemove.append(i)
        
        toRemove += stack
        res, p = "", 0
        for i in toRemove:
            res += s[p:i]
            p = i + 1
        
        if p < len(s):
            res += s[p:]

        return res

            
        