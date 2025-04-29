class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        p = -1
        op = {")": "(", "]":"[", "}": "{"}
        for c in s:
            if c == "(" or c == "{" or c == "[":
                st.append(c)
                p += 1
            elif c in op:
                if p < len(st) and p >= 0 and st[p] == op[c]:
                    st.pop()
                    p -= 1
                else:
                    return False
            
        return len(st) == 0
            