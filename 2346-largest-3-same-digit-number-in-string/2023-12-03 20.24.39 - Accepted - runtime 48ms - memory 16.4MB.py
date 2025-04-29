class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -float('inf')
        count = 1
        for i in range(1, len(num)):
            if num[i] == num[i-1]:
                count += 1
                if count == 3:
                    res = max(res, int(num[i]))
            else:
                count = 1

        if res == -float('inf'):
            return ""
        else:
            return str(res)*3

        