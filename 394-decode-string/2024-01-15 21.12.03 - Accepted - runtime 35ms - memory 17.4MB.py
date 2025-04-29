class Solution:
    def decodeString(self, s: str) -> str:
        exp1 = "3*('a')+2*('b'+'c')"
        exp = ""
        for i in range(len(s)):
            if s[i] == "[":
                exp += "*("
            elif s[i] == "]":
                exp += ")"
            elif s[i].isalpha():
                if exp and s[i-1] != "[":
                    exp += "+"
                exp += "'" + s[i] + "'"
            elif s[i].isnumeric():
                if exp and not s[i-1].isnumeric():
                    exp += "+"
                exp += s[i]
        res = eval(exp)
        return res

        