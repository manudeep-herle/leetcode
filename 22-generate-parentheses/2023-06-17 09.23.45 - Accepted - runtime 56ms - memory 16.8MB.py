# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
        
#         res = []
#         s = []
#         def gen(s,count):
#             if len(s) == 2*n:
#                 if count == 0:
#                     res.append("".join(s))
#                 return
#             else:
#                 if count < 2*n - len(s):
#                     s.append("(")
#                     count += 1
#                     gen(s, count)
#                     s.pop()
#                 if count > 0:
#                     s.append(")")
#                     count -= 1
#                     gen(s, count)
#                     s.pop()


#         gen(["("], 1)
#         return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(count):
            if len(stack) == 2*n:
                if count == 0:
                    res.append("".join(stack))
                return

            if count < n:
                stack.append("(")
                backtrack(count + 1)
                stack.pop()
            if count > 0:
                stack.append(")")
                backtrack(count - 1)
                stack.pop()

        backtrack(0)
        return res
