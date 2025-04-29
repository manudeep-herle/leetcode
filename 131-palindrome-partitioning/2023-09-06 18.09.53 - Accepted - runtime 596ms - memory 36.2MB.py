class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []

        def checkPalin(s):
            if s == s[::-1]:
                return True

        def backtrack(p, np):
            if not np:
                for word in p:
                    if not checkPalin(word):
                        return
                ans.append(p)

            for i in range(1, len(np) + 1):
                temp = p.copy()
                temp.append(np[0:i])
                backtrack(temp, np[i:])

        backtrack([], s)
        return ans

