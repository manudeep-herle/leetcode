class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = {")": "(", "]":"[", "}": "{"}

        for c in s:
            if c not in op:
                st.append(c)
            elif c in op:
                if len(st) > 0 and st[-1] == op[c]:
                    st.pop()
                else:
                    return False
            
        return len(st) == 0
            