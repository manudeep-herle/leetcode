class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        op = {")": "(", "]":"[", "}": "{"}

        for c in s:
            if c == "(" or c == "{" or c == "[":
                st.append(c)
            elif c in op:
                if len(st) > 0 and st[-1] == op[c]:
                    st.pop()
                else:
                    return False
            
        return len(st) == 0
            