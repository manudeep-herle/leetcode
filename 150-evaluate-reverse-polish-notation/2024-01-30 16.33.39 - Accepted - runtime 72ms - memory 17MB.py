import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ("*", "/", "+", "-")
        st = []

        def operate(op1, op2, op):
            if op == "*":
                return op1 * op2
            elif op == "/":
                return op1 / op2
            elif op == "+":
                return op1 + op2
            else:
                return op1 - op2
        
        for i in range(len(tokens)):
            # if not an operator
            if tokens[i] not in ops:
                st.append(tokens[i])
            else:
                op2 = st.pop()
                op1 = st.pop()
                res = operate(float(op1), float(op2), tokens[i])

                st.append(int(res))

        return int(st[-1]) 