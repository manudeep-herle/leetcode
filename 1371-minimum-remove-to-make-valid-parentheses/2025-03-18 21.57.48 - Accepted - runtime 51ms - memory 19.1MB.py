class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        index_to_remove, stack = [], []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            elif c == "(":
                stack.append(i)
            elif not stack:
                index_to_remove.append(i)
            else:
                stack.pop()
        
        index_to_remove += stack
        index_to_remove = set(index_to_remove)
        out = ""
        for i,c in enumerate(s):
            if i not in index_to_remove:
                out += c
        
        return out