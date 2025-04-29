# class Solution:
#     def partition(self, s: str) -> List[List[str]]:
#         res = []
#         parts = []

#         def checkPalin(s):
#             if s and s == s[::-1]:
#                 return True

#         def backtrack(i):
#             if i > len(s):
#                 res.append(parts.copy())
#                 return

#             for j in range(i, len(s)):
#                 if checkPalin(s[i:j]):
#                     parts.append(s[i:j])
#                     backtrack(j+1)
#                     parts.pop()



#         backtrack(0)
#         return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True