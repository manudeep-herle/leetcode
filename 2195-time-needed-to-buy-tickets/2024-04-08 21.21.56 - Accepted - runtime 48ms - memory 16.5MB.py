class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        res = 0
        j = 0
        while True:
            if j == len(tickets):
                j = 0
            if tickets[j]:
                tickets[j] -= 1
                res += 1
                if j == k and tickets[j] == 0:
                    return res
            j += 1

        return res

        