from collections import deque
class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 1:
            return int(s[0])
        stack1, i = deque(), 0
        s = s.replace(" ", "")
        while i < len(s):
            num = ""
            while i < len(s) and s[i].isnumeric():
                num += s[i]
                i += 1
            stack1.append(int(num))
            if i < len(s):
                stack1.append(s[i])
            i += 1
        stack2 = deque()

        # Multiplicaiton and division from the left
        while len(stack1) > 1:
            op1, operator = stack1.popleft(), stack1.popleft()
            if operator == "*":
                op2 = stack1.popleft()
                stack1.appendleft(op1 * op2)
            elif operator == "/":
                op2 = stack1.popleft()
                stack1.appendleft(math.floor(op1 / op2))
            else:
                stack2.append(op1)
                stack2.append(operator)
        stack2.append(stack1[0])
        del stack1
        while len(stack2) > 1:
            op1, operator, op2 = stack2.popleft(), stack2.popleft(), stack2.popleft()
            if operator == "+":
                stack2.appendleft(op1 + op2)
            elif operator == "-":
                stack2.appendleft(op1 - op2)
        return stack2[0]

        
